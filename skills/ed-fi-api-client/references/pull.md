# Pull integrations: reading data out of Ed-Fi

A pull integration reads Ed-Fi data into another system (a data warehouse, an analytics platform,
a vendor application). Authenticate first: [authentication.md](authentication.md).

## 1. Paging

Rules: [PULL-1, PULL-2](rules/pull.md).

Every collection GET is paged. Never assume one request returns everything. Ed-Fi APIs offer two
paging strategies; they cannot be mixed in the same request.

### Offset paging (default, all versions)

```http
GET {dataManagementApi}ed-fi/students?limit=500&offset=0&totalCount=true
```

| Parameter | Meaning |
|---|---|
| `limit` | Page size. Default 25. The maximum is set by the host, commonly 500 |
| `offset` | Number of records to skip |
| `totalCount=true` | Adds a `Total-Count` response header with the full record count |

- Request `totalCount=true` on the first page only; it adds cost to every request that asks for it.
- Stop when a page returns fewer records than `limit` (or an empty array), not when you reach a
  computed total; records can be added or removed during the read.
- Offset paging gets slower as `offset` grows. For large resources, prefer cursor paging.

### Cursor paging (ODS/API 7.3 and later)

Cursor paging seeks directly to the next page, so deep pages stay fast. Use it for large
resources and full extracts.

```http
GET {dataManagementApi}ed-fi/studentSectionAttendanceEvents/partitions?number=1
GET {dataManagementApi}ed-fi/studentSectionAttendanceEvents?pageToken={token}&pageSize=500
```

1. Get the first page token from `/partitions` (one token covers the whole resource; see below for
   more). Ed-Fi API 8 requires a `pageToken` whenever `pageSize` is sent: `pageSize` alone gets `400`
   "PageToken is required when pageSize is specified".
2. Send `pageToken` and `pageSize` (and no `limit`/`offset`). The maximum `pageSize` is 500; a default
   applies if omitted.
3. Read the `Next-Page-Token` response header and send it back as `pageToken` on the next request,
   with the same `pageSize` and filters.
4. Stop when a page returns no records or the response has no `Next-Page-Token`. The last page with
   data usually still carries a token; the request after it returns an empty array.

Rules:

- `pageToken`/`pageSize` cannot be combined with `limit`/`offset`.
- `totalCount` is not supported with cursor paging. To get a count, make a separate request with
  `limit=0&totalCount=true`.
- `/deletes` and `/keyChanges` do not accept `pageToken`/`pageSize`; page them with `limit`/`offset`.
- If the API rejects `pageToken`/`pageSize` as unknown parameters, the host runs an older version: fall
  back to offset paging.

### Parallel extraction with `/partitions`

Each resource has a `/partitions` child endpoint that splits its records into roughly even
partitions, one page token per partition:

```http
GET {dataManagementApi}ed-fi/studentSectionAttendanceEvents/partitions?number=4
```

```json
{ "pageTokens": ["MA==", "NDk5OQ==", "OTk5OQ==", "MTQ5OTk="] }
```

- `number` is optional; without it the API returns up to 10 partitions. It may return fewer when
  there is not enough data.
- Page through each partition in its own worker, starting from its token, until a page returns
  no records.
- `/partitions` accepts the same filters as the resource, including `minChangeVersion` and
  `maxChangeVersion`. Use exactly the same filters on the `/partitions` request and on every page
  request, or the partitions will be uneven.

## 2. Filtering

Query parameters filter on a resource's properties, including key fields of references:

```http
GET {dataManagementApi}ed-fi/studentSchoolAssociations?schoolId=255901001&limit=500&offset=0
```

- Filters are exact matches. There are no ranges, wildcards, or OR conditions.
- Descriptor filters take the full URI (URL-encoded).
- The client's authorization scope already limits results to the records it may see. An empty
  result can mean "no data" or "not authorized for that data".

## 3. Change queries

Rule: [PULL-3](rules/pull.md).

Change queries let a pull integration read only what changed since its last run, instead of
re-reading everything. They are available in ODS/API 7.x (the host can disable them, so confirm
with the host) and always enabled in Ed-Fi API 8.

Every write gets a `changeVersion`, an increasing number. The workflow:

1. Get the current range:

   ```http
   GET {urls.changeQueries}availableChangeVersions
   ```

   ```json
   { "oldestChangeVersion": 0, "newestChangeVersion": 104598 }
   ```

2. On the **first run**, record `newestChangeVersion`, then read every resource with no change
   filters. Save that version only after the whole load succeeds.
3. On **each later run**, read the new range for every resource:

   ```http
   GET {dataManagementApi}ed-fi/students?minChangeVersion=104599&maxChangeVersion=110230&limit=500&offset=0
   ```

   where `minChangeVersion` is the last saved value + 1 and `maxChangeVersion` is the current
   `newestChangeVersion`. Save the new `maxChangeVersion` only after the run succeeds.
4. Always pass **both** bounds, so writes landing during the run are picked up next time instead
   of half-read now.

### Deletes and key changes

Changed and new records come from the normal resource endpoint. Two more endpoints per resource
cover what a normal GET cannot show:

| Endpoint | Returns (each item) |
|---|---|
| `GET …/ed-fi/students/deletes?minChangeVersion=…&maxChangeVersion=…` | `id`, `changeVersion`, `keyValues` (the natural key of the deleted record) |
| `GET …/ed-fi/students/keyChanges?minChangeVersion=…&maxChangeVersion=…` | `id`, `changeVersion`, `oldKeyValues`, `newKeyValues` |

- Page both endpoints with `limit`/`offset`; they reject cursor paging parameters.
- Both need the `ReadChanges` permission in the client's claim set; without it they return `403`
  `urn:ed-fi:api:security:authorization:access-denied:action`.
- `/keyChanges` always returns an empty array for resources whose natural key cannot change. See
  [push.md](push.md#3-put-and-delete-use-the-resource-id-never-the-natural-key) for which
  resources allow key changes.
- An incremental sync must process all three (changes, deletes, key changes) or the target drifts
  from Ed-Fi over time.

### Snapshots (consistent reads)

Rule: [PULL-4](rules/pull.md).

Records keep changing while a long extract runs. A snapshot is a read-only, point-in-time copy
the host can provide so a run reads consistent data.

| Platform | Snapshot support |
|---|---|
| ODS/API 7.x | Optional, configured by the host. Send `Use-Snapshot: true` on **every** request of the run. A `404` with "Snapshot Not Found" means the host has not set up snapshots |
| Ed-Fi API 8 | Not available (planned for a future release). `Use-Snapshot: true` returns the same `404` "Snapshot not found", so the same detection works on both platforms |

Without snapshots, records can change between pages of the same run. Bound every request with
`maxChangeVersion` as above, make the target writes idempotent, and plan a periodic full
re-initialization to correct any drift.

## 4. Recommended sync algorithm

This follows the Ed-Fi Client Developers' Guide:

```text
order    = GET urls.dependencies                       # resource processing order
range    = GET availableChangeVersions
snapshot = try GET with "Use-Snapshot: true"; use it on every call if available (ODS/API 7.x only)

if no saved version:                                   # initial load (one time)
    v = range.newestChangeVersion
    for each resource in order: page through GET resource   -> insert
    save v (only after everything succeeded)
else:                                                  # scheduled change processing
    min = saved + 1; max = range.newestChangeVersion
    for each resource in order:          page through GET resource/keyChanges?min..max -> update keys
    for each resource in order:          page through GET resource?min..max            -> upsert by id
    for each resource in reverse order:  page through GET resource/deletes?min..max    -> delete by id
    save max (only after every step succeeded)
```

- Process **key changes first**, then changes, then deletes.
- Key target records by the Ed-Fi `id` as well as the natural key, so deletes and key changes can
  be matched.
- If `oldestChangeVersion` is greater than the saved version, the host has purged change history.
  Do a full re-initialization.
- Get the dependency order from `urls.dependencies`; see
  [push.md](push.md#1-load-resources-in-dependency-order).

## 5. Reading dates and datetimes

Datetime values are returned in ISO-8601 UTC; convert to local time only when displaying them.
Date-only elements are returned without a time part.

## 6. Reading descriptors

Responses contain descriptor URIs (`uri://ed-fi.org/GradeLevelDescriptor#Fifth grade`). To show
human-readable labels, read the descriptor resource once and cache it:

```http
GET {dataManagementApi}ed-fi/gradeLevelDescriptors?limit=500
```

Each value has `namespace`, `codeValue`, `shortDescription` and `description`.

## 7. Reliability

Rules: [ERR-2, ERR-3, ERR-4](rules/errors.md).

- Retry 5xx, 429 and network failures with exponential backoff; see [errors.md](errors.md#retry-policy).
- Persist progress (resource, page or page token, change version) so a failed run can resume.
- Respect host limits: bounded parallelism, and back off on 429 using `Retry-After` when present.
