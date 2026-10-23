# Rules: Push (writing data)

Part of the [Ed-Fi API client rules](../rules.md). See that file for what each level means for
building and reviewing code.

## PUSH-1: Load resources in the order given by the `dependencies` endpoint; delete in reverse order

- **Level:** Required
- **Why:** a resource can only be written after the resources it references exist; otherwise the API
  returns `409` `unresolved-reference`. Inferring the order from the OpenAPI spec is brittle.
- **Detect:** resources loaded in an arbitrary or hard-coded order not derived from `urls.dependencies`;
  deletes in forward order.
- **Details:** [push.md](../push.md#1-load-resources-in-dependency-order)

## PUSH-2: Update existing records with POST (upsert) or PUT by `id`, rather than deleting and reposting

- **Level:** Preferred. Deleting and reposting to apply an update is **Allowed but discouraged**.
- **Why:** POST of an existing natural key replaces the record (`200`), so delete-and-repost is usually
  unnecessary. It fails when other records reference the target (`409` `dependent-item-exists`), changes
  the resource `id`, and floods change queries with deletes. There are legitimate cases, such as changing
  the natural key of a resource that does not support cascading key updates.
- **Build:** update with POST or PUT. Use delete-and-repost only when an update cannot work (e.g. a key
  change without cascading key updates), and handle dependent records first.
- **Detect:** a DELETE followed by a POST of the same natural key as the routine way to apply a change;
  "clear and reload" loops over existing data. Accept it when the code explains a legitimate reason.
- **Details:** [push.md](../push.md#2-post-is-an-upsert),
  [push.md](../push.md#changing-a-natural-key)

## PUSH-3: Use the resource `id` in item URLs, never a natural key

- **Level:** Required
- **Why:** item URLs (`/ed-fi/students/{id}`) take the server-generated `id`. A natural key in the URL
  returns `404`.
- **Detect:** URLs built from `studentUniqueId`, `schoolId` or other key fields, e.g.
  `/students/{studentUniqueId}`; PUT or DELETE without first obtaining the `id` from `Location` or a GET.
- **Details:** [push.md](../push.md#3-put-and-delete-use-the-resource-id-never-the-natural-key)

## PUSH-4: Send the complete record on POST and PUT

- **Level:** Required
- **Why:** POST and PUT replace the stored record; omitted fields are cleared.
- **Detect:** partial bodies used to "update one field"; PATCH-style logic; bodies built from only the
  changed columns.
- **Details:** [push.md](../push.md#2-post-is-an-upsert)

## PUSH-5: Send descriptors as full URIs that exist in the target API, with the mapping in configuration

- **Level:** Required
- **Why:** descriptor values (`uri://ed-fi.org/GradeLevelDescriptor#Fifth grade`) vary by state and
  district namespace. Unknown values are rejected.
- **Detect:** bare code values (`"Fifth grade"`, `"05"`) in descriptor fields; hard-coded allow-lists
  copied from documentation; source-to-descriptor mappings embedded in code.
- **Details:** [push.md](../push.md#5-descriptors)

## PUSH-6: Send dates as `YYYY-MM-DD` and datetimes in ISO-8601 with a time zone

- **Level:** Required
- **Why:** a date element with a time part is rejected; a datetime without a zone is treated as UTC,
  silently shifting local times.
- **Detect:** date fields serialized with a time; datetimes formatted without `Z` or an offset; local
  time values sent as-is.
- **Details:** [push.md](../push.md#6-dates-and-datetimes)

## PUSH-7: Use `If-Match` with the record's ETag on PUT and DELETE when the host enables ETags

- **Level:** Preferred
- **Why:** prevents overwriting another client's change; a stale ETag returns `412`.
- **Detect:** PUT or DELETE of records that other systems also edit, without `If-Match`, on a host that
  returns `ETag` headers; `412` treated as a fatal error instead of re-read and retry.
- **Details:** [push.md](../push.md#7-optimistic-concurrency-with-etags)
