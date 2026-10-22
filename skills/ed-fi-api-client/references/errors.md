# Diagnosing Ed-Fi API responses

Ed-Fi APIs return errors as RFC 9457 problem details. Read the body before guessing:

```json
{
  "detail": "Data validation failed. See 'validationErrors' for details.",
  "type": "urn:ed-fi:api:bad-request:data-validation-failed",
  "title": "Data Validation Failed",
  "status": 400,
  "correlationId": "3ba4019d-5f0c-437e-b81d-b0b41b440df5",
  "validationErrors": {
    "$.birthDate": ["The supplied value is invalid."]
  }
}
```

- `type` is a stable URN that identifies the error category. Branch on it in code, not on `detail`
  (rule [ERR-1](rules/errors.md)).
- `detail` and `errors` / `validationErrors` explain the specific problem.
- `correlationId` identifies the request in the API's logs. Always log it and give it to the API
  host when asking for help.

## Quick reference

| Status | Meaning in Ed-Fi | Retry? | First thing to check |
|---|---|---|---|
| `200` | Read succeeded, or POST updated an existing record | — | — |
| `201` | POST created a new record; `Location` holds its URL | — | — |
| `204` | PUT or DELETE succeeded | — | — |
| `400` | Request body or query is invalid | No | `validationErrors` / `errors` in the body |
| `401` | Token missing, malformed, or expired | Once, after re-authenticating | Token lifecycle |
| `403` | Authenticated, but not allowed for this resource or record | No | Claim set and education organization scope |
| `404` | No resource at that URL | No | URL uses `id`, not a natural key; path spelling |
| `405` | Method not supported for this resource | No | Resource is read-only or the operation is not allowed |
| `409` | The write conflicts with other data | No | Missing reference, or dependents exist |
| `412` | `If-Match` ETag is stale | After re-reading the record | Concurrent update |
| `413` | Request too large | No | Split the payload |
| `429` | Rate limited by the host or a gateway | Yes, honor `Retry-After` | Concurrency level |
| `500` | Unexpected server error | Yes, with backoff | `correlationId` to the host if it persists |
| `502/503/504` | Host or gateway unavailable | Yes, with backoff | Host status |

## 400 Bad Request

The request itself is wrong. Common causes:

- A required field is missing, or a value has the wrong type (a number sent as a string).
- A date is not `YYYY-MM-DD`.
- A string exceeds the schema's maximum length.
- A descriptor value is malformed or does not exist in the target API.
- An unknown property name (often a casing mistake: Ed-Fi uses camelCase).
- A query parameter is not a property of the resource.

Each key in `validationErrors` is a JSON path to the offending field. Fix the data at the source;
resending it unchanged will fail again.

## 401 Unauthorized

The token is missing, expired, or not valid for this API instance. Re-authenticate once and retry.
If the retry also returns 401, stop and check the credentials. See
[authentication.md](authentication.md#token-lifecycle-rules).

If the **token request itself** returns 401 (or 400 `invalid_client`) while using a Basic header,
check the encoding before suspecting the credentials:

1. Were the key and secret each **form-urlencoded** before joining them? Library "basic auth"
   helpers often skip this, which breaks secrets with special characters.
2. Was the joined `key:secret` string **base64-encoded**?
3. Is the token request going to the instance (and tenant) that issued the credentials?

See [authentication.md](authentication.md#requesting-a-token).

## 403 Forbidden

Authentication worked, but the client is not allowed to do this. Branch on the `type`:

| `type` | Cause | Fix |
|---|---|---|
| `urn:ed-fi:api:security:authorization:access-denied:resource` | The claim set has no permission on this resource | API host must change the claim set |
| `urn:ed-fi:api:security:authorization:access-denied:action` | The claim set allows the resource but not this action (e.g. a read-only client POSTing) | API host must change the claim set |
| `urn:ed-fi:api:security:authorization` (and more specific sub-types) | The record is outside the client's education organization scope: no relationship between the student, contact or staff member and the client's education organizations, or a school the client is not authorized for | Check the record's school / education organization; load the relationships authorization depends on (such as the student's enrollment) first |
| `urn:ed-fi:api:security:authorization:namespace:access-denied:namespace-mismatch` | The record's `namespace` (descriptors, assessments…) does not match a prefix assigned to the client | Use the client's namespace, or ask the host to assign it |
| `urn:ed-fi:api:security:data-policy:incorrect-usage` | A Profile content type was used that is not assigned to the client, or a required writable Profile content type was omitted | Use the `Content-Type` / `Accept` the host assigned |

Claim set failures affect every record of a resource; education organization failures affect only
some records. Report the `correlationId` to the API host if the cause is unclear.

## 404 Not Found

- PUT/DELETE/GET by id: the `id` does not exist. The most common mistake is putting a natural key
  (`studentUniqueId`, `schoolId`) in the URL instead of the resource `id`.
- Collection URL: the resource path is misspelled, missing the `ed-fi/` (or extension) prefix, or
  does not exist in this Data Standard version.

## 409 Conflict

A 409 means the write is valid on its own but conflicts with other data in the API. It is **not** a
"duplicate key" error: POST of an existing natural key is an update and returns 200.

| `type` | Situation | Fix |
|---|---|---|
| `urn:ed-fi:api:data-conflict:unresolved-reference` | POST/PUT with a `...Reference` to a record that does not exist (a student, school, school year…) | Load the referenced record first (dependency order), or correct the reference's key values |
| `urn:ed-fi:api:data-conflict:dependent-item-exists` | DELETE of a record that other records still reference | Delete the dependent records first (reverse dependency order) |
| `urn:ed-fi:api:data-conflict:non-unique-identity` | PUT changes the natural key to values another record already has | Correct the source data, or update the other record |

Example: POSTing a `studentSchoolAssociation` whose `studentReference.studentUniqueId` has not been
loaded returns 409 `unresolved-reference`. Load the student, then retry the association.

## 412 Precondition Failed

Type `urn:ed-fi:api:optimistic-lock-failed`; only possible when the host has the ETag feature on.
The `If-Match` header held an ETag that no longer matches the stored record: someone changed it
since you read it. GET the record again, reapply your change to the fresh copy, and PUT again with
the new ETag. See [push.md](push.md#7-optimistic-concurrency-with-etags).

## Retry policy

Rule: [ERR-2](rules/errors.md).

Retry only failures that can succeed unchanged:

| Failure | Action |
|---|---|
| Network error, timeout, `500`, `502`, `503`, `504` | Retry with exponential backoff and jitter (e.g. 0.5 s, 1 s, 2 s, 4 s…), up to a limit (e.g. 5 attempts) |
| `429` | Retry after the `Retry-After` header value if present, otherwise with backoff |
| `401` | Re-authenticate once and retry once; see [authentication.md](authentication.md#designing-the-client) |
| `412` | Re-read the record, reapply the change, then retry |
| Any other 4xx | Do not retry. Log it and fix the data or configuration |

```text
withRetry(send):
    for attempt in 1..maxAttempts:
        response = send()   (network errors count as retryable)
        if success or not retryable(response): return / raise
        wait Retry-After if present, else baseDelay * 2^(attempt-1) * random(0.5..1.5)
    raise last error
```

## Logging a failed record

Rule: [ERR-3](rules/errors.md).

Log enough to fix the record at the source, without exposing data you should not log. For each
failed record, log:

- the resource path (e.g. `/ed-fi/studentSchoolAssociations`)
- the record's natural key (e.g. `studentUniqueId` and `schoolId`)
- the HTTP status
- `type`, `detail`, and `validationErrors` / `errors` from the problem details body
- `correlationId`

Do not log full student records, tokens, or the client secret.
