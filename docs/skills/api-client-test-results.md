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

## Not yet done

- **GitHub Copilot:** the remaining seven prompts, and a run without the skill for comparison.
- **Codex** (optional, NFR-PORT-1).
- Running generated code against a live Ed-Fi API 8 instance (pilot test kit).
