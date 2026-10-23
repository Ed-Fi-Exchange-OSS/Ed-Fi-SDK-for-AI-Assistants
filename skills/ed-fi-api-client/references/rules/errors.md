# Rules: Errors and reliability

Part of the [Ed-Fi API client rules](../rules.md). See that file for what each level means for
building and reviewing code.

## ERR-1: Branch on the problem-details `type`, not on the `detail` text

- **Level:** Preferred
- **Why:** `type` is a stable URN (e.g. `urn:ed-fi:api:data-conflict:unresolved-reference`); `detail`
  text can change.
- **Detect:** string matching on `detail` or `title` to decide how to handle an error; status code alone
  used to tell apart different `409` or `403` causes.
- **Details:** [errors.md](../errors.md)

## ERR-2: Retry only `5xx`, `429` and network errors, with backoff; never retry a `4xx` unchanged

- **Level:** Required
- **Why:** `4xx` errors are data or configuration problems and fail again unchanged; retrying them adds
  load and hides the cause. Unbounded or immediate retries overload the host.
- **Detect:** retries on every error; no backoff or jitter; no attempt limit; `Retry-After` ignored on
  `429`.
- **Details:** [errors.md](../errors.md#retry-policy)

## ERR-3: Log failures with natural key, status, `type` and `correlationId`; never log sensitive data

- **Level:** Required
- **Why:** the `correlationId` lets the API host find the request in its logs, and the natural key lets
  the source data be fixed. Full records expose student data.
- **Detect:** errors swallowed or logged without the response body; full request or response bodies
  with student data in logs; no `correlationId` captured.
- **Details:** [errors.md](../errors.md#logging-a-failed-record)

## ERR-4: Continue past individual record failures and report them at the end

- **Level:** Preferred
- **Why:** one bad record should not stop a load of thousands; a summary at the end lets the source data
  be fixed in one pass.
- **Detect:** the first failed record aborts the whole run; failures not collected or reported.
- **Details:** [push.md](../push.md#8-throughput-and-reliability)
