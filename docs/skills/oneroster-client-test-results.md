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
  come from the service source (`edfi-oneroster` `main`, 2026-10-16) and the Ed-Fi documentation.

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

## Still to run

- A check of T1, T3 and T6 against a running Ed-Fi OneRoster service, if a test environment is available.
