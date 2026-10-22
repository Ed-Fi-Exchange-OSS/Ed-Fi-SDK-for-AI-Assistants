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

## Ed-Fi API 8 verification · pilot test kit · 2026-10-22

- **Environment:** [Ed-Fi API v8 pilot test kit](https://github.com/Ed-Fi-Exchange-OSS/Ed-Fi-API-v8-pilot-testing-kit),
  populated template. Discovery reports `version 8.0.0`, `informationalVersion 8.1.0-beta1`, Data Standard 5.2.0.
  The kit's smoke test passed 13/13.
- **Method:** direct HTTP checks of the skill's API 8 claims with a SIS-vendor credential and a data-warehouse
  credential created by the kit.

| Check | Result on API 8 | Skill change |
|---|---|---|
| Token with credentials in the form body | `400` "Malformed Authorization header" | Body credentials marked ODS/API 7.x only (AUTH-1, `authentication.md`, `SKILL.md`) |
| `pageSize` without `pageToken` | `400` "PageToken is required when pageSize is specified" | First token from `/partitions` (`pull.md`, PULL-2, `SKILL.md`) |
| `/partitions` | `pageTokens`; 13,015 records split into 4 even partitions; small resources return 1 token | None |
| Cursor end | Last data page still has a token; the next returns `[]` with no token | Stop rule clarified |
| `/deletes`, `/keyChanges` | Same fields as 7.x; reject `pageToken`/`pageSize`; need `ReadChanges` | Added to `pull.md` |
| Key change by PUT | StudentSchoolAssociation: `204` and a `/keyChanges` entry; Student: `400` `key-change-not-supported` | "Detect at runtime" removed; `400` type added |
| Wrong-case or unknown property in a POST | Ignored silently (`200`); wrong case on a required property gives `400` "is required" | `SKILL.md` warns about silent data loss |
| `Use-Snapshot: true` | `404` "Snapshot not found" (same as an unconfigured 7.x host) | Noted in `pull.md` |
| ETag / stale `If-Match` | Always on; `412` `optimistic-lock-failed` | Noted in `push.md` and `errors.md` |
| Discovery, `limit` max 500, change queries, 409 / 403 / 400 types | As described in the skill | None |

Not verified: tenant and context route segments (the kit is single-tenant) and generated client code end to end.

## Not yet done

- **GitHub Copilot:** the remaining seven prompts, and a run without the skill for comparison.
- **Codex** (optional, NFR-PORT-1).
- Running assistant-generated client code end to end against the pilot test kit.
