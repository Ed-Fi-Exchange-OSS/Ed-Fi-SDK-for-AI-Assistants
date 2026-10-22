# Rules: Pull (reading data)

Part of the [Ed-Fi API client rules](../rules.md). See that file for what each level means for
building and reviewing code.

## PULL-1: Always page through collections; stop on an empty or short page

- **Level:** Required
- **Why:** every collection GET is paged (default 25 records). Records can be added or removed during the
  read, so a computed total is not a reliable stop condition.
- **Detect:** a single GET expected to return all records; no `limit`/`offset` or `pageToken` handling;
  a loop that stops at `Total-Count`; `totalCount=true` on every page.
- **Details:** [pull.md](../pull.md#1-paging)

## PULL-2: Use cursor paging (and `/partitions` for parallel reads) on large resources where supported

- **Level:** Preferred
- **Why:** offset paging slows down as `offset` grows; cursor paging keeps deep pages fast.
- **Detect:** large extracts using deep `offset` values; parallel workers splitting work by offset
  ranges.
- **Detect (API 8):** `pageSize` sent without a `pageToken` on the first request; Ed-Fi API 8 answers
  `400`. Get the first token from `/partitions`.
- **Versions:** cursor paging requires ODS/API 7.3 or later and works on Ed-Fi API 8; fall back to offset
  paging if the API rejects `pageToken`/`pageSize` as unknown parameters.
- **Details:** [pull.md](../pull.md#cursor-paging-odsapi-73-and-later)

## PULL-3: Sync incrementally with change queries, processing key changes, changes and deletes

- **Level:** Required (for incremental sync)
- **Why:** re-reading everything is slow; reading only changed records misses deletes and key changes,
  so the target drifts from Ed-Fi.
- **Detect:** full re-reads on every run; filtering by a timestamp field instead of `changeVersion`; only
  `minChangeVersion` without `maxChangeVersion`; no use of `/deletes` or `/keyChanges`; the saved version
  updated before the run succeeds; wrong order (process key changes, then changes, then deletes in reverse
  dependency order).
- **Versions:** the ODS/API 7.x host can disable change queries; Ed-Fi API 8 always enables them.
- **Details:** [pull.md](../pull.md#3-change-queries), [pull.md](../pull.md#4-recommended-sync-algorithm)

## PULL-4: Read with a snapshot when the host provides one

- **Level:** Preferred
- **Why:** records keep changing during a long extract; a snapshot gives a consistent point in time.
- **Detect:** long multi-page extracts on an ODS/API 7.x host with snapshots configured, without the
  `Use-Snapshot: true` header on every request.
- **Versions:** ODS/API 7.x only; Ed-Fi API 8.0 has no snapshot support.
- **Details:** [pull.md](../pull.md#snapshots-consistent-reads)
