# Push integrations: writing data into Ed-Fi

A push integration sends records from a source system (SIS, assessment platform, HR system…) into
an Ed-Fi API. Authenticate first: [authentication.md](authentication.md).

## 1. Load resources in dependency order

Rule: [PUSH-1](rules/push.md).

A resource can only be written after the resources it references exist. A
`studentSchoolAssociation` needs its `student` and `school`; a `section` needs its `courseOffering`,
which needs a `course` and a `session`.

Do not infer this order from the OpenAPI spec. Read it from the `urls.dependencies` endpoint:

```json
[
  { "resource": "/ed-fi/sourceSystemDescriptors", "order": 1, "operations": ["Create", "Update"] },
  { "resource": "/ed-fi/people",                  "order": 2, "operations": ["Create", "Update"] },
  { "resource": "/ed-fi/contacts",                "order": 3, "operations": ["Create"] }
]
```

- Resources with `order: 1` have no prerequisites. Load all of order 1, then order 2, and so on.
- Resources within the same order can be loaded in parallel.
- Only load the resources the integration actually needs, but keep their relative order.
- For deletes, use the reverse order: delete dependents before what they reference.

## 2. POST is an upsert

Rules: [PUSH-2](rules/push.md), [PUSH-4](rules/push.md).

Ed-Fi identifies records by their **natural key** (e.g. `studentUniqueId` for a student;
`studentReference` + `schoolReference` + `entryDate` for a studentSchoolAssociation). POST to the
collection URL:

```http
POST {dataManagementApi}ed-fi/students
Content-Type: application/json

{
  "studentUniqueId": "604822",
  "firstName": "Jane",
  "lastSurname": "Smith",
  "birthDate": "2010-03-15"
}
```

| Response | Meaning |
|---|---|
| `201 Created` | No record with that natural key existed; one was created |
| `200 OK` | A record with that natural key already existed; it was **replaced** with this body |

Consequences:

- Re-sending the same POST is safe, which makes POST the simplest choice for idempotent sync jobs.
- The body **replaces** the stored record. Fields omitted from the body are cleared. Always send the
  complete record, never a partial update.
- The `Location` response header holds the record's URL, ending in its server-generated `id`.
  Store that `id` if you will PUT or DELETE the record later.

### Don't delete and repost to update

To change an existing record, POST it again (upsert) or PUT it by `id`. Deleting it and posting it again is
**discouraged**:

- It fails when other records reference it (`409` `dependent-item-exists`).
- It gives the record a new `id`, breaking stored references in other systems.
- It shows up in change queries as a delete plus an insert, so pull integrations do extra work.

There are legitimate cases, such as changing the natural key of a resource that does not support cascading
key updates (see [Changing a natural key](#changing-a-natural-key)). In those cases, handle dependent records
first and document why in the code.

## 3. PUT and DELETE use the resource `id`, never the natural key

Rule: [PUSH-3](rules/push.md).

```http
PUT    {dataManagementApi}ed-fi/students/{id}
DELETE {dataManagementApi}ed-fi/students/{id}
```

`{id}` is the opaque identifier from the `Location` header or from the `id` field returned by a GET.
`/ed-fi/students/604822` (a `studentUniqueId`) is **wrong** and returns 404.

To find the `id` for a known natural key, query by the key fields:

```http
GET {dataManagementApi}ed-fi/students?studentUniqueId=604822
```

- PUT also replaces the whole record. The body must contain the full resource.

### Changing a natural key

On most resources the natural key cannot be changed. To change it, delete the record and POST a
new one, after deleting or re-pointing the records that reference it.

A few resources allow a PUT that changes the natural key. The API then cascades the new key to
every record that references it ("cascading key updates"). As shipped in ODS/API 7.x these are:

- Class Period
- Grade
- GradebookEntry
- Location
- Section
- Session
- Student School Association
- Student Section Association

A host can enable this on other resources, so a PUT that changes a key may work on one host and
not on another. If the new key values already belong to another record, the API returns `409`
with type `urn:ed-fi:api:data-conflict:non-unique-identity`.

Pull integrations see these changes through the `/keyChanges` endpoint; see
[pull.md](pull.md#deletes-and-key-changes).

## 4. References

A reference to another resource is an object holding that resource's natural key, not its `id`:

```json
{
  "studentReference": { "studentUniqueId": "604822" },
  "schoolReference": { "schoolId": 255901001 },
  "entryDate": "2026-08-15",
  "entryGradeLevelDescriptor": "uri://ed-fi.org/GradeLevelDescriptor#Fifth grade"
}
```

If the referenced record does not exist, the API returns **`409 Conflict`**. See
[errors.md](errors.md#409-conflict).

## 5. Descriptors

Rule: [PUSH-5](rules/push.md).

Descriptors are Ed-Fi's controlled vocabularies (grade levels, sexes, attendance events…). A
descriptor value is a URI made of a **namespace** and a **code value**:

```text
uri://ed-fi.org/GradeLevelDescriptor#Fifth grade
└────── namespace ──────────────┘ └ codeValue ┘
```

- Use the exact namespace and code value that exist in the target API. Values are not standardized
  across states and districts: many use their own namespace (e.g. `uri://somestate.edu/...`).
- Do not hard-code allow-lists copied from documentation. Read the available values from the
  descriptor endpoints and build the source-to-Ed-Fi mapping from them:

  ```http
  GET {dataManagementApi}ed-fi/gradeLevelDescriptors?limit=500
  ```

- Mapping source codes (e.g. a SIS grade `"05"`) to descriptor URIs is the integrator's
  responsibility. Keep the mapping in configuration, not code.
- An unknown descriptor value is rejected; the error names the descriptor property.
- Creating new descriptor values usually requires a claim set with descriptor write access and
  authority over that namespace.

## 6. Dates and datetimes

Rule: [PUSH-6](rules/push.md).

| Element type | Send | The API returns |
|---|---|---|
| Date (e.g. `birthDate`, `entryDate`) | `YYYY-MM-DD` only. A value with a time part is rejected | The date only |
| Datetime | ISO-8601 with a time zone: `2026-08-15T13:45:00Z` or `2026-08-15T08:45:00-05:00` | ISO-8601 in UTC |

- A datetime without a time zone designator is treated as UTC. A local time sent without an offset
  is silently shifted. Always include the zone.
- Stored and returned values are UTC; convert to local time only for display.

## 7. Optimistic concurrency with ETags

Rule: [PUSH-7](rules/push.md).

When the host has the ETag feature enabled, responses include an `ETag` header (and `_etag` in GET
bodies). To avoid overwriting someone else's change, send it back in `If-Match`:

```http
PUT {dataManagementApi}ed-fi/students/{id}
If-Match: "5250549902005221347"
```

If the record changed since you read it, the API returns **`412 Precondition Failed`** with type
`urn:ed-fi:api:optimistic-lock-failed`. Re-read the record, reapply your change, and try again.
`If-Match` also works on DELETE. If responses carry no `ETag`, the feature is off and the last
write wins.

## 8. Throughput and reliability

Rules: [ERR-2, ERR-3, ERR-4](rules/errors.md).

- Group work by dependency order; within an order, send requests in parallel with a bounded
  concurrency (start around 4–8 and tune against the host).
- Retry only 5xx, 429 and network failures, with exponential backoff. Never retry a 4xx unchanged.
- Log every failed record with its natural key, the status code, and the response `correlationId`
  so it can be traced in the API logs and fixed at the source.
- Continue past individual record failures; report them at the end instead of stopping the run.
- To load very large volumes, check whether the host recommends a bulk tool (e.g. the Ed-Fi Bulk
  Load Client) instead of a custom loop.

## Checklist before sending a record

- [ ] Every required field is present (check the resource schema)
- [ ] Dates are `YYYY-MM-DD`; datetimes carry a time zone; numbers are JSON numbers, not strings
- [ ] Every descriptor is a full URI that exists in the target API
- [ ] Every referenced record has already been loaded (dependency order)
- [ ] The body is the complete record, not a partial update
- [ ] Updates use POST or PUT by `id`, not delete and repost
- [ ] String lengths are within the schema limits
