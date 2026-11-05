# OneRoster client skill: test results

Results of the [test prompts](oneroster-client-test-prompts.md) (FR-REL-1, FR-REL-2).

## Run 1 · Claude Code · 2026-10-30

- **Harness:** Claude Code 2.1.312, headless (`claude -p`), default model, fresh session per prompt.
- **Conditions:** *with skill* (`ed-fi-oneroster-client` installed in the project's `.claude/skills/`) and
  *without skill* (empty project).
- **Restrictions:** only `Read`, `Glob`, `Grep` and `Skill` allowed; file writes, shell and web access
  disabled in both conditions, so answers come from the model plus, when installed, the skill.
- **Skill invocation:** the skill was invoked automatically in all 8 prompts, followed by one to three
  reference file reads. The run log didn't record which files; the answers use details that appear only in the
  matching reference files.
- **Not checked against a running service:** no OneRoster test instance was available, so the expected outcomes
  come from the service source (`edfi-oneroster` `main`, 2026-10-16) and the Ed-Fi documentation. Run 3
  checks them against a running service.

### Summary

| Test | Topic | With skill | Without skill |
|---|---|---|---|
| T1 | First request (token from the ODS/API) | ✅ Pass | ✅ Pass |
| T2 | Demographics returns 403 | ✅ Pass | ❌ Fail |
| T3 | Paging a full sync | ✅ Pass | ❌ Fail |
| T4 | Writing grades (not supported) | ✅ Pass | ❌ Fail |
| T5 | Data freshness and deletions | ✅ Pass | ❌ Fail |
| T6 | Empty results with a valid token | ✅ Pass | ✅ Pass |
| T7 | Duplicate students | ✅ Pass | ❌ Fail |
| T8 | Missing fields in classes | ✅ Pass | ❌ Fail |
| **Total** | | **8 / 8** | **2 / 8** |

Output tokens across the 8 prompts: 16,637 with the skill, 22,770 without.

### What the skill changed

| Test | Without the skill | With the skill |
|---|---|---|
| T1 | Passed, but used the library's basic-auth helper (no urlencoding), hard-coded the OneRoster path, and didn't mention that the host must issue JWT tokens | Discovery on the OneRoster root, urlencoded Basic header, token from `urls.oauth`, one retry on `401`, `imsx` error parsing |
| T2 | Said some providers treat `roster.readonly` as including demographics, and suggested requesting the scope in the client first | `roster.readonly` excludes demographics by design; a host-side permission, not a code change; retrying doesn't help |
| T3 | Credentials in the form body; stopped on a page shorter than `limit`, which breaks when the `limit` is above the host maximum; read an `X-Total-Count` header the service doesn't send | Pages to an empty page, advances by records received, `limit` 500, backoff on `429` with `Retry-After`, dedup by `sourcedId` |
| T4 | Wrote a full script against `PUT /lineItems` and `PUT /results`, which the service doesn't have | Read-only Rostering, no Gradebook; grades go through the ODS/API `grades` resource |
| T5 | Hedged on the refresh ("if it reads from a snapshot"), and told the client to rely on `status=tobedeleted`, which this service never sends | 15-minute refresh, resources refresh separately, no refresh-status endpoint; the reasons a record goes missing and the safeguards before deleting |
| T7 | Blamed duplicate Ed-Fi records first; listed school-scoped users only as a guess | Users are school-scoped by design; group by `identifier` |
| T8 | Told the developer to fill `academicSubjectDescriptor` and grade levels in Ed-Fi, which doesn't change the output | The service never fills these fields; workaround in the client |

### Issues found and fixed

- **Joining back to Ed-Fi (T4, T8):** with the skill, the answers suggested matching OneRoster records to Ed-Fi
  through the `sourcedId` or the section's natural key, without saying where that key is. **Fixed:**
  `mapping-to-ed-fi.md` now describes `metadata.edfi` (the Ed-Fi resource and natural key on every record) and
  which fields hold Ed-Fi IDs.
- **JWT host setting (T1, outcome 5):** not mentioned with or without the skill. **Fixed:** `SKILL.md` now says
  the host must set the ODS/API to issue JWT tokens for the OneRoster service.
- T1, T4 and T8 were run again with the skill after these fixes; see below.

### Rerun after the fixes (T1, T4, T8)

Same harness and restrictions, with the updated skill.

| Test | With skill | Notes |
|---|---|---|
| T1 | ✅ Pass, all 5 outcomes | Now says a `401` from OneRoster with a token that works on the ODS/API is a host setting (JWT tokens with the OneRoster audience) |
| T4 | ✅ Pass | No change in substance; matches LMS records to Ed-Fi through the roster instead of `sourcedId` |
| T8 | ✅ Pass | Joins classes to Ed-Fi sections through `metadata.edfi.naturalKey`, matching case-insensitively and taking `schoolYear` from the term |

### Fact-check against the service code, and rerun (T3, T5, T6, T8)

After Run 1, every claim in the skill was checked against the `edfi-oneroster` source by a separate reviewer
that hadn't written it. About 70 claims were confirmed and 10 were wrong. The most important:

- **Refresh schedule:** "every 15 minutes by default" holds only for PostgreSQL, through the shipped
  `PGBOSS_CRON` example. The shipped SQL Server Agent job runs **once a day at 02:00**, although
  `README_mssql.md` says every 15 minutes. The skill and T5 now say the host sets the schedule.
- **Courses** don't fill `grades`, `subjects` or `subjectCodes` either, so the T8 workaround now reads them from
  the ODS/API.
- A tenant or school year the token isn't for returns `401`, not `404`; the `401` messages and causes were
  corrected.
- On Data Standard 4.0, contacts are parents (`parentUniqueId`); a contact's `sourcedId` follows the school of
  the linked students' latest enrollment.

The reviewer also found behavior the skill didn't cover; it now does: subset endpoints use the parent's
wrapper (`/schools` returns `orgs`), `href` is relative to `dataManagementApi`, single-record requests ignore
`filter`/`fields`/`sort`, flags are strings, reads can fail with `500` during a refresh, and the `/oauth/token`
redirect drops the tenant and school-year segments.

The prompts most affected were run again with the skill (same harness):

| Test | With skill | Notes |
|---|---|---|
| T3 | ✅ Pass | Also retries `500` (refresh in progress) and suggests scheduling after the host's refresh |
| T5 | ✅ Pass | Gives both schedules (PostgreSQL cron, SQL Server daily at 02:00) and says to ask the host |
| T6 | ✅ Pass | Unchanged diagnosis; mentions the school-level token hiding parent orgs |
| T8 | ✅ Pass | Reads subjects and grade levels from the ODS/API through `metadata.edfi`, not from the OneRoster course |

## Run 2 · GitHub Copilot · 2026-11-03

- **Harness:** GitHub Copilot CLI 1.0.105, headless (`copilot -p`), model `claude-sonnet-5.5`, fresh session per
  prompt, with the skill as it stood after the fact-check above.
- **Conditions:** *with skill* (`ed-fi-oneroster-client` installed in the project's `.github/skills/`) and
  *without skill* (empty project).
- **Restrictions:** file writes and shell denied; web fetch, web search and GitHub code search excluded, so
  answers come from the model plus, when installed, the skill. A first pass still allowed GitHub code search,
  which the runs without the skill used in T4 and T8; those two prompts were run again with it excluded, and
  those are the results below.
- **Skill invocation:** the skill was invoked automatically in all 8 prompts, followed by one to three reference
  file reads or searches.

### Summary

| Test | Topic | With skill | Without skill |
|---|---|---|---|
| T1 | First request (token from the ODS/API) | ✅ Pass | ✅ Pass |
| T2 | Demographics returns 403 | ✅ Pass | ✅ Pass |
| T3 | Paging a full sync | ✅ Pass | ❌ Fail |
| T4 | Writing grades (not supported) | ✅ Pass | ❌ Fail |
| T5 | Data freshness and deletions | ✅ Pass | ❌ Fail |
| T6 | Empty results with a valid token | ✅ Pass | ✅ Pass |
| T7 | Duplicate students | ✅ Pass | ❌ Fail |
| T8 | Missing fields in classes | ✅ Pass | ❌ Fail |
| **Total** | | **8 / 8** | **3 / 8** |

The CLI doesn't report tokens.

### What the skill changed

| Test | Without the skill | With the skill |
|---|---|---|
| T1 | Passed; Basic auth without urlencoding, hard-coded OneRoster path, a new token on every call, no JWT note | Discovery on both roots, urlencoded Basic header, token from ODS/API `urls.oauth`, one retry on `401`, `imsx` errors, JWT and edorg notes |
| T2 | Passed: a separate demographics scope granted by the admin. Also guessed the client's `roster.readonly` might be the core-only scope, and suggested requesting the scope in the token request | `roster.readonly` excludes demographics by design; a host-side permission; retrying won't help |
| T3 | Built around `X-Total-Count` and `Link` headers the service doesn't send; stops on a page shorter than `limit` and suggests raising `limit` to the server maximum, which breaks when the host clamps it; credentials in the form body | `limit` 500, pages to an empty page, advances by records received, backoff on `429`/`500` with `Retry-After`, group by `identifier` |
| T4 | Planned `PUT lineItems` and `PUT results` against a Gradebook the service doesn't have | Read-only Rostering, no Gradebook; grades go to the ODS/API `grades` resource |
| T5 | Told the client to delete only records marked `tobedeleted`, which this service never sends | Both refresh schedules, resources refresh separately, the reasons a record goes missing, safeguards before deleting |
| T7 | Blamed duplicate Ed-Fi records first; school-scoped users only as a guess | Users are school-scoped by design; group by `identifier` |
| T8 | Told the developer to fill `academicSubjectDescriptor` and `offeredGradeLevels` on the course | The service never fills these fields; read them from the ODS/API through `metadata.edfi` |

Partial outcomes with the skill: T1 gets a new token per call instead of reusing it (outcome 3), T3 logs the
raw error body instead of parsing `imsx` fields (outcome 5), and T7 doesn't mention `demographics` (outcome 3).
No change to the skill was needed.

The first pass of T4 without the skill, with GitHub code search available, searched Ed-Fi repositories,
found nothing, and still answered that the service is read-only. A smoke run before it, and the rerun above,
both planned Gradebook calls. Without the skill the answer to T4 depends on the run; with the skill it was
correct in all three.

## Run 3 · Check against a running service · 2026-11-04

- **Service:** the Docker demo stack in the `edfi-oneroster` repository (`stack/`, `main` at `c0b9bb0`), single
  tenant on PostgreSQL: ODS/API 7.3.2 with the populated template (Data Standard 5.2), the
  `one-roster-api:pre` image and NGINX on `https://localhost`. The refresh cron was set to every 5 minutes.
- **Method:** HTTP calls with the stack's LEA and school test API clients, then the T1 code from the rerun
  below executed against the stack. Test data and permission changes were made only in the local stack.

### What the service did

| # | Check | Result |
|---|---|---|
| 1 | Discovery on the OneRoster root, no token | ✅ `version`, `urls.oauth` (the ODS/API token URL), `urls.dataManagementApi`, plus `openApiMetadata` and `swaggerUI` |
| 2 | Token from `urls.oauth` with a Basic header | ✅ A JWT valid for 30 minutes, accepted by the OneRoster service |
| 3 | `POST /oauth/token` on the OneRoster host | ✅ `307` to the ODS/API token URL |
| 4 | Token requested **without** `scope` | ❌ The skill said to ask the host. The token has no `scope` claim and every endpoint returns `403`. **Fixed** (below) |
| 5 | Token with `roster-core.readonly` only | ✅ `403` "Insufficient scope" on `demographics`, `200` on `users` |
| 6 | No token, an invalid token, a token with another audience | ✅ `401` "Missing or invalid Authorization header." and "Invalid or expired token." |
| 7 | `users?limit=10000` | ✅ 500 records, no error, no total-count header (only `RateLimit-*`); 100 records without `limit` |
| 8 | Page `users` to an empty page | ✅ 2,888 records in 7 pages, no duplicate `sourcedId` |
| 9 | More than 100 requests in a minute | ✅ `429` with a plain-text body, `Retry-After: 30` and `RateLimit-*` headers; Discovery still `200` |
| 10 | `limit=0`, `limit=abc`, `offset=-1`, `limit` twice, a field not allowed in `filter` or `fields` | ✅ `400` with an `imsx` body (`invalid_data`); `schools/{id}/classes` returns `404` |
| 11 | API client with no education organizations | ✅ `200` with empty collections, `404` for a single record. New tokens reflected the change after about 3 minutes |
| 12 | School-level API client | ✅ Only its school in `orgs`; the parent district returns `404` |
| 13 | A student associated with a second school | ✅ Two `users` records with the same `identifier` and different `sourcedId`s; `dateLastModified` didn't change |
| 14 | A student written through the ODS/API | ✅ Not in OneRoster until the next scheduled refresh, then present; the service also refreshes right after it starts |

No endpoint reports the last refresh. Upstream commit `c0b9bb0` records refresh history in a SQL Server
table, not in the API.

### Corrections to the skill

- **Scopes (check 4):** the ODS/API puts in the token only the OneRoster scopes that the client **requests**
  in the token request's `scope` parameter **and** the API client's claim set allows; the rest are dropped
  without an error. `authentication.md` and `SKILL.md` now tell the client to request the scopes, to check the
  token's `scope` claim, and to go to the host only when a requested scope is missing.
- **Token limit:** the ODS/API allows 15 unexpired tokens per client by default and answers `429`
  (`too-many-tokens`) over it. `authentication.md` now says so next to "reuse the token".
- **Education organization changes** take a few minutes to reach new tokens (check 11); added to
  `authentication.md`.
- **Test prompts:** T1 has a new key outcome (request a OneRoster scope in the token request), and T2
  outcome 2 now expects the client to request `roster-demographics.readonly` before going to the host.
  Under the earlier criteria, "request the scope" counted against the answers without the skill in T2.

### Rerun of T1 and T2

Same harnesses and restrictions as Runs 1 and 2, with the corrected skill. The other prompts weren't run
again; the corrections only touch the token request.

| Test | Claude Code with skill | Claude Code without | Copilot with skill | Copilot without |
|---|---|---|---|---|
| T1 | ✅ Pass: requests `roster.readonly` | ❌ Fail: no `scope` (outcome 3) | ✅ Pass: requests `roster.readonly` | ❌ Fail: no `scope` (outcome 3) |
| T2 | ✅ Pass | ✅ Pass | ✅ Pass | ✅ Pass |

With these results, the totals are 8/8 with the skill in both harnesses, and 2/8 without it in both (Copilot's
T1 without the skill moves from pass to fail, Claude Code's T2 from fail to pass).

Both Claude Code answers to T1 were then run against the stack, unchanged except for the environment
variables: the code written with the skill listed the first 100 classes; the code written without it failed
with `403` on its first OneRoster request.

## Run 4 · Review changes · 2026-11-05

After the second review of PR #70, `data-freshness.md` no longer describes the backend databases (only the
refresh cycle and what it means for a client), `SKILL.md` has a rule to request the OneRoster scopes, and
`authentication.md` no longer names specific claim sets. A new prompt, T9, covers an API client whose claim set
has no OneRoster claims.

Same harnesses and restrictions as Runs 1 and 2, with the final skill. T1, T2 and T5 cover the changed text;
the other prompts don't depend on it and weren't run again.

| Test | Claude Code with skill | Claude Code without | Copilot with skill | Copilot without |
|---|---|---|---|---|
| T1 | ✅ Pass | ❌ Fail: no `scope` (outcome 3) | ✅ Pass | ❌ Fail: no `scope` (outcome 3) |
| T2 | ✅ Pass | ✅ Pass | ✅ Pass | ✅ Pass |
| T5 | ✅ Pass: refresh cycle, no database details | ❌ Fail: relies on `tobedeleted` | ✅ Pass | ❌ Fail: relies on `tobedeleted` |
| T9 | ✅ Pass | ✅ Pass | ✅ Pass | ❌ Fail: says the claim set has no bearing on OneRoster scopes |

- **T9 with the skill:** both answers say the claim set has no OneRoster claims, the ODS/API drops the
  requested scope without an error, and the host has to add the claims or change the claim set. Claude Code
  also suggests sending the full scope URI, because the prompt writes the short name; that's a reasonable side
  check, not the fix it leads with (outcome 3 ⚠️).
- **T9 without the skill:** Claude Code reaches the claim set from the general Ed-Fi security model, with
  hedging; Copilot says the claim set is unrelated and points to an identity provider.

With T9, the totals are 9/9 with the skill in both harnesses, and 3/9 (Claude Code) and 2/9 (Copilot) without
it.
