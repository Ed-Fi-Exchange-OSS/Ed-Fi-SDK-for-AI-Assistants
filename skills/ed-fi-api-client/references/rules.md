# Ed-Fi API client rules

The single source of truth for how a client should interact with an Ed-Fi API. Both interfaces use these
rules:

- **Build:** when writing new code, apply every *Required* and *Preferred* rule, and never generate an
  *Allowed but discouraged* pattern.
- **Review:** when reviewing existing code, check each rule using its **Detect** notes and report findings
  by level, following [review.md](review.md).

| Level | Build | Review finding |
|---|---|---|
| **Required** | Always do this | *Must fix* |
| **Preferred** | Do this | *Should fix* |
| **Allowed but discouraged** | Never generate it | Accept, and suggest the preferred alternative |

Rules apply to ODS/API 7.x and Ed-Fi API 8 unless a **Versions** note says otherwise. Each rule links to the
guide with the details. A rule can add a **Build** note when building and reviewing apply it differently.

Rules are grouped in one file per category; open only the categories the task needs:
[discovery](rules/discovery.md) · [auth](rules/auth.md) · [push](rules/push.md) · [pull](rules/pull.md) ·
[errors](rules/errors.md).

## All rules

| Rule | Level | Statement |
|---|---|---|
| [DISC-1](rules/discovery.md#disc-1-configure-only-the-api-root-url-take-every-other-url-from-the-discovery-api) | Required | Configure only the API root URL; take every other URL from the Discovery API |
| [AUTH-1](rules/auth.md#auth-1-send-client-credentials-in-a-basic-authorization-header-urlencoded-then-base64-encoded) | Preferred | Send client credentials in a Basic `Authorization` header, urlencoded then base64-encoded |
| [AUTH-2](rules/auth.md#auth-2-reuse-the-access-token-until-it-is-about-to-expire) | Required | Reuse the access token until it is about to expire |
| [AUTH-3](rules/auth.md#auth-3-on-401-re-authenticate-once-and-retry-once-then-stop) | Required | On `401`, re-authenticate once and retry once, then stop |
| [AUTH-4](rules/auth.md#auth-4-never-hard-code-or-log-the-client-secret-or-access-tokens) | Required | Never hard-code or log the client secret or access tokens |
| [AUTH-5](rules/auth.md#auth-5-use-https-and-never-permanently-disable-certificate-validation) | Required | Use HTTPS, and never permanently disable certificate validation |
| [PUSH-1](rules/push.md#push-1-load-resources-in-the-order-given-by-the-dependencies-endpoint-delete-in-reverse-order) | Required | Load resources in the order given by the `dependencies` endpoint; delete in reverse order |
| [PUSH-2](rules/push.md#push-2-update-existing-records-with-post-upsert-or-put-by-id-rather-than-deleting-and-reposting) | Preferred | Update existing records with POST (upsert) or PUT by `id`, rather than deleting and reposting |
| [PUSH-3](rules/push.md#push-3-use-the-resource-id-in-item-urls-never-a-natural-key) | Required | Use the resource `id` in item URLs, never a natural key |
| [PUSH-4](rules/push.md#push-4-send-the-complete-record-on-post-and-put) | Required | Send the complete record on POST and PUT |
| [PUSH-5](rules/push.md#push-5-send-descriptors-as-full-uris-that-exist-in-the-target-api-with-the-mapping-in-configuration) | Required | Send descriptors as full URIs that exist in the target API, with the mapping in configuration |
| [PUSH-6](rules/push.md#push-6-send-dates-as-yyyy-mm-dd-and-datetimes-in-iso-8601-with-a-time-zone) | Required | Send dates as `YYYY-MM-DD` and datetimes in ISO-8601 with a time zone |
| [PUSH-7](rules/push.md#push-7-use-if-match-with-the-records-etag-on-put-and-delete-when-the-host-enables-etags) | Preferred | Use `If-Match` with the record's ETag on PUT and DELETE when the host enables ETags |
| [PULL-1](rules/pull.md#pull-1-always-page-through-collections-stop-on-an-empty-or-short-page) | Required | Always page through collections; stop on an empty or short page |
| [PULL-2](rules/pull.md#pull-2-use-cursor-paging-and-partitions-for-parallel-reads-on-large-resources-where-supported) | Preferred | Use cursor paging (and `/partitions` for parallel reads) on large resources where supported |
| [PULL-3](rules/pull.md#pull-3-sync-incrementally-with-change-queries-processing-key-changes-changes-and-deletes) | Required | Sync incrementally with change queries, processing key changes, changes and deletes |
| [PULL-4](rules/pull.md#pull-4-read-with-a-snapshot-when-the-host-provides-one) | Preferred | Read with a snapshot when the host provides one |
| [ERR-1](rules/errors.md#err-1-branch-on-the-problem-details-type-not-on-the-detail-text) | Preferred | Branch on the problem-details `type`, not on the `detail` text |
| [ERR-2](rules/errors.md#err-2-retry-only-5xx-429-and-network-errors-with-backoff-never-retry-a-4xx-unchanged) | Required | Retry only `5xx`, `429` and network errors, with backoff; never retry a `4xx` unchanged |
| [ERR-3](rules/errors.md#err-3-log-failures-with-natural-key-status-type-and-correlationid-never-log-sensitive-data) | Required | Log failures with natural key, status, `type` and `correlationId`; never log sensitive data |
| [ERR-4](rules/errors.md#err-4-continue-past-individual-record-failures-and-report-them-at-the-end) | Preferred | Continue past individual record failures and report them at the end |
