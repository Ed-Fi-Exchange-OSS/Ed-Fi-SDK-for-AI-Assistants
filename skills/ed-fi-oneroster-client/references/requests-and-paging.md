# Requests, paging and errors

What the Ed-Fi OneRoster API serves and how to read it reliably. Part of the
[ed-fi-oneroster-client](../SKILL.md) skill.

## Endpoints

Read-only GET, relative to `urls.dataManagementApi` (`.../ims/oneroster/rostering/v1p2/`):

| Collection | Single record | Notes |
|---|---|---|
| `orgs` | `orgs/{sourcedId}` | Schools, districts (LEAs) and the state (SEA) |
| `schools` | `schools/{sourcedId}` | `orgs` of type `school` |
| `academicSessions` | `academicSessions/{sourcedId}` | School years, terms and grading periods |
| `terms`, `gradingPeriods` | `terms/{sourcedId}`, `gradingPeriods/{sourcedId}` | Subsets of `academicSessions` |
| `courses` | `courses/{sourcedId}` | |
| `classes` | `classes/{sourcedId}` | One per ODS/API section |
| `users` | `users/{sourcedId}` | Students, staff and contacts |
| `students`, `teachers` | `students/{sourcedId}`, `teachers/{sourcedId}` | Subsets of `users` |
| `enrollments` | `enrollments/{sourcedId}` | Student and staff section associations |
| `demographics` | `demographics/{sourcedId}` | Needs the demographics scope |

- The nested endpoints of the OneRoster specification (such as `schools/{id}/classes` or
  `classes/{id}/students`) are **not** implemented and return `404`. Use the collection with a `filter`
  instead, or join on the client.
- There is no POST, PUT or DELETE, and no Gradebook or Resources service.
- The OpenAPI document is at `urls.openApiMetadata` (`/swagger.json`) when the host enables it.

## Responses

- Collections are wrapped in the plural name: `{ "users": [ ... ] }`. Single records use the singular:
  `{ "user": { ... } }`.
- **Subset endpoints use the parent's wrapper:** `/schools` returns `orgs`, `/terms` and `/gradingPeriods`
  return `academicSessions`, `/students` and `/teachers` return `users` (and `org`, `academicSession`, `user`
  for single records). A pager that reads `page.students` gets nothing.
- **Top-level fields with no value are omitted**, not returned as `null`. Treat every optional field as
  possibly absent. Nested objects (such as `metadata`) can still contain `null` values on some hosts.
- Some text fields come back as an empty string instead of being omitted (for example `username` when there
  is no email).
- Flags such as `enabledUser` and `primary` are the strings `"true"` and `"false"`, not booleans.
- References use `{ "href", "sourcedId", "type" }`. `href` is a path relative to `urls.dataManagementApi`
  (`/orgs/{sourcedId}`); resolve it against that base, not against the host root.

## Query parameters

| Parameter | Behavior in this service |
|---|---|
| `limit` | Default 100. Values above the host's maximum (500 by default) are **clamped silently**, not rejected |
| `offset` | Default 0 |
| `sort`, `orderBy` | Comma-separated fields, `asc` or `desc`. A field that isn't sortable is ignored without an error. `sourcedId` is always added as the last sort key |
| `filter` | OneRoster filter syntax (`field='value'`, `AND`/`OR`). Each resource allows a fixed list of fields; at most 20 clauses and 250 characters per value. An invalid filter returns `400` |
| `fields` | Comma-separated field list. An unknown field returns `400` |

- `limit=0`, a non-numeric `limit` or `offset`, or the same parameter twice returns `400`.
- Single-record requests (`/users/{sourcedId}`) ignore `filter`, `fields` and `sort` and return every field.

## Paging a full sync

The service sends **no total count** (no `X-Total-Count` header) and may return fewer records than the
`limit` you asked for. Page like this:

```text
offset = 0
loop:
    page = GET {dataManagementApi}users?limit=500&offset={offset}
    if page.users is empty: stop
    process(page.users)
    offset = offset + len(page.users)    # records received, not the limit requested
```

- Stopping on "page shorter than `limit`" breaks when the requested `limit` is above the host's maximum: the
  first page comes back with 500 records and the loop stops early. Stopping on an empty page costs one more
  request and always works.
- Offset paging is stable within one refresh (the sort always ends in `sourcedId`), but a refresh in the
  middle of a run can shift records between pages. For a sync that must be complete, deduplicate by
  `sourcedId` and see [data-freshness.md](data-freshness.md).

## Rate limit

The host limits requests per client IP (100 per minute by default). Over the limit the service returns `429`.

- The `429` body is plain text, not an `imsx` body. Branch on the status code.
- Wait for the time in the `Retry-After` header (or the `RateLimit-Reset` header) before retrying. Without
  it, back off exponentially.
- Parallel workers behind the same IP share one limit, and requests rejected with `401` count too. Prefer one
  sequential pager with a large `limit` over many parallel requests.
- Discovery is not rate limited. The OpenAPI document and Swagger UI have their own, lower limit.

## Errors

Except for `429`, errors use the OneRoster status info body:

```json
{
  "imsx_codeMajor": "failure",
  "imsx_severity": "error",
  "imsx_codeMinor": "invalid_data",
  "imsx_description": "Field 'grade' is not allowed for filtering. Allowed fields: ..."
}
```

`imsx_codeMinor` is not always present. The ODS/API problem-details rules of `ed-fi-api-client` (ERR-1) don't
apply.

| Status | Meaning here | Client action |
|---|---|---|
| `400` | Invalid `filter`, `fields`, `limit` or `offset`; a missing school-year segment on a multi-year host | Fix the request; don't retry |
| `401` | Missing, expired or rejected token, or a tenant or school year the token isn't for | Get a new token and retry once; if it fails again, see [authentication.md](authentication.md) |
| `403` | Missing scope, or an internal authorization error (`forbidden`) | Don't retry; see [authentication.md](authentication.md) |
| `404` | Unknown endpoint, unknown `sourcedId`, a record outside the token's education organizations, or no ODS instance for the token | Check the URL; for single records, treat as "not visible to this client" |
| `429` | Rate limit | Wait and retry |
| `500` | Server error (no detail returned), including a timeout while a refresh is running | Retry with backoff a few times, then report to the host with the time and URL |

Discovery errors are different: an unknown tenant or school year on the Discovery URL returns `404` with an
ODS/API-style body (`error`, `title`, `status`), not an `imsx` body.
