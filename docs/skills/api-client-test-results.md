# API Client skill: test results

Results of the [test prompts](api-client-test-prompts.md) (FR-REL-1, FR-REL-2).

## Run 1 · Claude Code · 2026-10-21

- **Harness:** Claude Code 2.1.304, headless (`claude -p`), default model, fresh session per prompt.
- **Conditions:** *with skill* (`ed-fi-api-client` installed in the project's `.claude/skills/`) and *without
  skill* (empty project).
- **Restrictions:** file writes, shell and web access disabled in both conditions, so answers come from the
  model plus, when installed, the skill.
- **Skill invocation:** the skill was invoked automatically in all 10 prompts, and the matching reference files
  were read (e.g. `errors.md` for T4, `review.md` for T3 and T10).

### Summary

| Test | Topic | With skill | Without skill |
|---|---|---|---|
| T1 | Push script (dependencies, auth, descriptors) | ✅ Pass | ❌ Fail |
| T2 | Updating a record | ✅ Pass | ✅ Pass |
| T3 | Review: token per call | ✅ Pass | ✅ Pass |
| T4 | Diagnosing a 409 | ✅ Pass | ✅ Pass |
| T5 | 401 on the token request | ✅ Pass | ❌ Fail |
| T6 | Incremental sync | ✅ Pass | ✅ Pass |
| T7 | Large extract (paging) | ✅ Pass (second run) | ❌ Fail |
| T8 | Moving to Ed-Fi API 8 | ✅ Pass | ❌ Fail |
| T9 | Descriptors | ✅ Pass | ✅ Pass |
| T10 | Review: documented exception | ✅ Pass | ❌ Fail |
| **Total** | | **10 / 10** | **5 / 10** |

### What the skill changed

| Test | Without the skill | With the skill |
|---|---|---|
| T1 | Library basic auth (no urlencoding, AUTH-1); bare grade codes expanded with a hard-coded `ed-fi.org` namespace; fallback to hard-coded `/data/v3` and `/oauth/token`; no `correlationId` logging | Basic header urlencoded; order from the `dependencies` endpoint; descriptor mapping in a config file and validated against the API; retry and logging per ERR-2/ERR-3 |
| T5 | Suggested the API probably doesn't decode urlencoded credentials and recommended switching to body credentials | Identified the missing urlencoding (RFC 6749 §2.3.1), showed how to build the header, kept body credentials as a one-time diagnostic only |
| T7 | Invented a `/keyset` endpoint; no `/partitions` | Cursor paging (`pageSize`, `pageToken`, `Next-Page-Token`) with `/partitions`, restrictions and fallback |
| T8 | Vague, generic list; did not mention the `v3` removal, case-sensitive properties or `/connect/token`; claimed API 8 targets a newer Data Standard | The documented breaking changes, each with the client-side action |
| T10 | Treated delete and repost as blocking despite the documented reason | Reported it as a **suggestion** (PUSH-2) and pointed to cascading key updates on `sections` |

Passing *without skill* answers still had gaps the skill avoided: T3's suggested fix kept body credentials and
hard-coded paths, T6 invented a "late commits" overlap re-read and did not give the processing order, and T9
kept the descriptor mapping in code.

### Issues found

- **Test environment (T7, first run):** the read of `references/pull.md` was denied in headless mode, and the
  answer fell back to general knowledge (it failed). A second run read the file and passed. This looks like a
  transient permission issue in headless mode, not a skill problem; watch for it in future runs.
- **Review over-reporting (T10):** the review flagged PUSH-3 as *must fix* on the assumption that `old_id` might
  be a natural key. `review.md` says not to guess intent, so an ambiguous identifier should go under
  *Not checked* or be phrased as a question. **Fixed:** `review.md` now says to list ambiguous identifiers
  under *Not checked* with the question to confirm.

## Run 2 · GitHub Copilot smoke test · 2026-10-22

- **Harness:** GitHub Copilot in VS Code, agent mode, `chat.useAgentSkills` enabled, skill installed in the
  project's `.github/skills/`. The model was not recorded.
- **Scope:** a smoke test with three prompts that exercise the review interface (T3), authentication (T5)
  and platform differences (T8). With skill only.
- **Skill invocation:** Copilot loaded the skill automatically in all three prompts ("Read skill
  `ed-fi-api-client`") and read the relevant references (`review.md` and the rule files for T3,
  `authentication.md` and `rules/auth.md` for T5, `pull.md` and `authentication.md` for T8).

| Test | Topic | Result | Notes |
|---|---|---|---|
| T3 | Review: token per call | ✅ Pass | AUTH-2, ERR-2, AUTH-5 as *must fix*; AUTH-1 as *should fix*; DISC-1 flagged; review format followed |
| T5 | 401 on the token request | ✅ Pass | Identified the missing urlencoding before base64 and showed how to build the header; did not mention checking the instance or tenant (non-key) |
| T8 | Moving to Ed-Fi API 8 | ✅ Pass | `v3` removal, case-sensitive properties, `/connect/token` with the `/oauth/token` proxy, no snapshots; no undocumented claims |

Observation: in T5, one read failed because Copilot built a path with a stray space (`\ .github\`); it
recovered from the files it had already read. This is a harness quirk, not a skill issue.

## Run 3 · GitHub Copilot, remaining prompts · 2026-10-22

Same harness as Run 2, with the skill updated to include the API 8 and review fixes. With skill only. With
Run 2, all ten prompts have now run in Copilot: **10/10 pass**.

| Test | Topic | Result | Notes |
|---|---|---|---|
| T1 | Push script | ✅ Pass | Wrote a loader: order from `dependencies`, URLs from Discovery (trailing slash added), urlencoded Basic header, bounded token renewal margin, retries on 429/5xx with `Retry-After`, `correlationId` logged. Non-key gap: expects full descriptor URIs in the CSV instead of a mapping in configuration |
| T2 | Updating a record | ✅ Pass | GET by `studentUniqueId` for the `id`, then PUT with the full record and `If-Match`; no delete and repost |
| T4 | Diagnosing a 409 | ✅ Pass | Missing referenced student; load it first or fix the reference; don't retry unchanged |
| T6 | Incremental sync | ✅ Pass | Both bounds, `/keyChanges` and `/deletes`, offset paging for those two, checkpoint saved only after success, purge check |
| T7 | Large extract | ✅ Pass | `/partitions` and cursor paging with `Next-Page-Token`, max page size 500, no `limit`/`offset`/`totalCount` mixing |
| T9 | Descriptors | ✅ Pass | Full descriptor URI, values read from the target API, mapping in configuration |
| T10 | Review: documented exception | ✅ Pass | PUSH-2 as a suggestion; cascading key updates on `sections`; ambiguous `old_id` under *Not checked* (the `review.md` fix from Run 1) |

Observations:

- **Agent mode acts instead of answering.** In T2 ("update the last name… show me the HTTP requests") Copilot
  first asked for the API URL and credentials so it could run the update. Told not to run anything, it wrote
  the requests. In T1 it wrote the script to the workspace and ran a syntax check. This is harness behavior,
  not a skill issue; prompts for answer-only tests should say "don't run anything".
- **Workspace files were visible.** The answers were saved inside the test workspace, so in T1, T2 and T6
  Copilot also read other answer files and the T1 script. They hold Copilot's own answers, not the expected
  outcomes, so the results stand; future runs should keep results outside the workspace.

## Ed-Fi API 8.1 pre-release verification · pilot test kit · 2026-10-22

- **Environment:** [Ed-Fi API v8 pilot test kit](https://github.com/Ed-Fi-Exchange-OSS/Ed-Fi-API-v8-pilot-testing-kit),
  populated template. Discovery reports `version 8.0.0`, `informationalVersion 8.1.0-beta1`, Data Standard 5.2.0.
  The kit's smoke test passed 13/13.
- **Method:** direct HTTP checks of the skill's API 8 claims with a SIS-vendor credential and a data-warehouse
  credential created by the kit.
- **Version:** these results are from `8.1.0-beta1`, an 8.1 pre-release. On 2026-10-23 the token check was
  repeated on a later pre-release (`8.1.0-beta.0.1.32`, which reports `version 8.1.0`): it accepts credentials
  in the body, form or JSON, as 8.1 does. The other rows were not repeated on that build.

| Check | Result on API 8 | Skill change |
|---|---|---|
| Token with credentials in the form body | `8.1.0-beta1`: `400` "Malformed Authorization header". `8.1.0-beta.0.1.32`: `200` | AUTH-1 keeps the Basic header as the recommendation (it works on every version); body credentials are *Allowed but discouraged* |
| `pageSize` without `pageToken` | `400` "PageToken is required when pageSize is specified" | First token from `/partitions` (`pull.md`, PULL-2, `SKILL.md`) |
| `/partitions` | `pageTokens`; 13,015 records split into 4 even partitions; small resources return 1 token | None |
| Cursor end | Last data page still has a token; the next returns `[]` with no token | Stop rule clarified |
| `/deletes`, `/keyChanges` | Same fields as 7.x; reject `pageToken`/`pageSize`; need `ReadChanges` | Added to `pull.md` |
| Key change by PUT | StudentSchoolAssociation: `204` and a `/keyChanges` entry; Student: `400` `key-change-not-supported` | "Detect at runtime" removed; `400` type added |
| Wrong-case or unknown property in a POST | Ignored silently (`200`); wrong case on a required property gives `400` "is required" | `SKILL.md` warns about silent data loss |
| `Use-Snapshot: true` | `404` "Snapshot not found" (same as an unconfigured 7.x host) | Noted in `pull.md` |
| ETag / stale `If-Match` | Always on; `412` `optimistic-lock-failed` | Noted in `push.md` and `errors.md` |
| Discovery, `limit` max 500, change queries, 409 / 403 / 400 types | As described in the skill | None |

Not verified: tenant and context route segments (the kit is single-tenant), and a released 8.1 build.

### Generated client, end to end

Claude Code (headless, fresh session, skill installed, no shell or web access) wrote a Python CLI from one
prompt: `load` reads students and enrollments from two CSV files (grade levels as codes such as `09`) and
`sync` copies student school associations to a local file incrementally, including deletions. The code ran
**unchanged** against the pilot kit, with the SIS-vendor credential for `load` and the data-warehouse
credential for `sync`:

| Scenario | Result |
|---|---|
| `load`, first run | ✅ 3 students and 3 enrollments created (`201`) |
| `load` again with the same files | ✅ No duplicates: 3 + 3 replaced (`200`) |
| `sync`, first run | ✅ Full copy (963 enrollments), change version saved |
| `sync` with nothing new | ✅ Skipped the run (no `minChangeVersion > maxChangeVersion` request) |
| Update, key change and delete in the API, then `sync` | ✅ "2 changed, 1 deleted, 1 key change"; the local copy matched the API |

The code followed the rules the skill teaches, including today's API 8 and review fixes: urlencoded Basic
header, bounded token renewal margin, URLs from Discovery with the trailing slash added, grade codes mapped in
a configuration file, first cursor token from `/partitions`, offset paging for `/deletes` and `/keyChanges`,
TLS validation off only through an explicit setting, and `Retry-After` in both formats.

## Skill description and automatic loading · 2026-10-23

In review, the skill did not load on its own for a request like "Review the Ed-Fi API client code" on old ODS/API
3.x-style Python code, in Claude Code or Copilot. The description now names the kinds of code it covers
(scripts, CLIs, SDKs, ETL jobs, integrations), the review verbs (review, audit, fix), older clients
(ODS/API 2.x–6.x) and path cues (`oauth/token`, `/data/v3`).

Claude Code, headless, clean workspace with only the skill and one old client file, 3 runs per description:

| Request | Previous description | New description |
|---|---|---|
| "Review the Ed-Fi API client code" (file under `edfi/`) | Loaded the skill first, 3/3 | Loaded the skill first, 3/3 |
| "Review the API client code in tools/nightly_sync.py" (no "Ed-Fi" in the request, file name or docstring) | Read the file first, then loaded the skill, 3/3 | Loaded the skill first, 3/3 |

The reviewer's miss did not reproduce in a clean workspace with either description, so the difference likely
depends on the session (other skills or project files competing). The new description matches the shape of
the request without needing Ed-Fi words in it.

## Code review on real client code · 2026-10-23

The review interface (`references/review.md`) was run on three public Ed-Fi API clients, as test inputs: a small
Python CLI for ODS/API 2.x–3.x (`Ed-Fi-Exchange-OSS/Python-Minimal-CLI`), a Python client library for ODS/API
7.x (`edanalytics/edfi_api_client`), and a C# parallel-read example for ODS/API 6.1
(`Ed-Fi-Exchange-OSS/ParallelAPIConsumption`).

- **Harness:** Claude Code, headless, fresh session per repository, read-only tools. Request: "Review the Ed-Fi
  API client code in this repository." The skill loaded on its own in all three.
- **Accuracy:** about 15 findings were checked against the code, spread across the three reports; all were
  real. Beyond the rules, the reviews also found ordinary bugs (for example a swallowed exception that
  truncates parallel reads, a method called with an argument it doesn't take, an undefined variable on an
  error path).
- **Platform handling:** each report named the platform it inferred (ODS/API 2.x–3.x, 6.1, 7.x) and noted
  where 7.x/8 rules only partly apply.

Issues found in the reports, and the changes made:

| Issue | Change |
|---|---|
| A finding reported above its rule's level (a *Preferred* rule under *Must fix*, with the text calling it a suggestion) | `review.md`: keep the level from the table; mention unusual impact in the text |
| The same rule listed as *Passed* and as a finding | `review.md`: one place per rule; report each part once at its own level |
| Unsure whether `requests`' `HTTPBasicAuth` counts as a "built-in basic-auth helper" (AUTH-1) | AUTH-1 **Detect** now names helpers in Python, JavaScript and .NET |

A rerun of the library review after the first two changes kept every rule at its table level and no longer
listed the same rule as passed and failed, except for a minor *Suggestion* that was also counted as passed.

## Not yet done

- **GitHub Copilot:** a run without the skill for comparison.
- **Codex** (optional, NFR-PORT-1).
