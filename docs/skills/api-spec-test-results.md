# API spec lookup skill: test results

Results of the [test prompts](api-spec-test-prompts.md) (FR-REL-1, FR-REL-2).

> **Runs 1 and 2 used an earlier version of the generated content** that stated natural keys derived from the
> OpenAPI metadata. Review showed the specification can't support that (a required reference may or may not be
> part of a record's identity), so the content and the prompts changed. **Run 3 is the current result.**

## Run 1 · Claude Code · 2026-10-22

- **Harness:** Claude Code, headless (`claude -p`), default model, fresh session per prompt.
- **Conditions:** *with skill* (`ed-fi-api-spec` installed in the project's `.claude/skills/`) and *without
  skill* (empty project). The API Client skill was not installed in either condition.
- **Restrictions:** file writes, shell and web access disabled in both conditions, so answers come from the
  model plus, when installed, the skill.
- **Skill invocation:** the skill was invoked automatically in all 10 prompts.

### Summary

| Test | Topic | With skill | Without skill |
|---|---|---|---|
| T1 | Exact resource: natural key and required fields | ✅ Pass | ✅ Pass |
| T2 | Natural language: enrollment | ✅ Pass | ✅ Pass |
| T3 | Synonym: parents and guardians | ✅ Pass | ❌ Fail |
| T4 | Daily attendance vs. section attendance | ✅ Pass | ✅ Pass |
| T5 | Descriptors | ✅ Pass | ✅ Pass |
| T6 | Keys inside a reference | ✅ Pass | ❌ Fail |
| T7 | Synonym: test scores | ✅ Pass | ✅ Pass |
| T8 | Key changes | ✅ Pass | ❌ Fail |
| T9 | Change-query endpoints | ✅ Pass | ✅ Pass |
| T10 | Limits: extensions | ✅ Pass | ✅ Pass |
| **Total** | | **10 / 10** | **7 / 10** |

### What the skill changed

The three failures without the skill come from mixing in older Data Standard versions:

| Test | Without the skill | With the skill |
|---|---|---|
| T3 | `/ed-fi/parents` and `studentParentAssociations` (Data Standard 4 names) | `contacts` and `studentContactAssociations`, with their keys |
| T6 | `gradingPeriodReference` with `periodSequence` (Data Standard 4) | `gradingPeriodName`, as in Data Standard 5.2 |
| T8 | "Usually no": delete and recreate the section, re-pointing its dependents | Yes: `sections` allows key changes with PUT (cascading key updates); notes the host can turn it off |

Passing *without skill* answers still had gaps the skill avoided: T5 listed a `gradeLevelDescriptor` field on
`studentSectionAssociation` that does not exist, T7 listed `namespace` as a separate key field of
`studentAssessments`, and T9 said the natural key of `studentSchoolAssociations` cannot change (it can).
Without the skill the assistant also hedged most answers ("from memory, check against your spec").

With the skill, answers were grounded in the resource file and stated the limits that apply (descriptor values
come from the target API; extensions are not indexed). In T10 it found only the core `busRouteDescriptors` and
did not invent fields for the extension.

### Issue found and fixed

In four prompts (T1, T6, T8, T9) the assistant first tried to open a singular file name (`grade.md`,
`section.md`), failed, and then searched the index. `SKILL.md` now says files use the plural collection name.
A rerun of those four prompts opened the right file on the first try: 2 tool calls instead of 4, and about 40%
fewer input tokens (about 104 K instead of 177 K), with the same passing answers.

### Context use

| Condition | Input tokens per prompt (average) | Cost per prompt (average) |
|---|---|---|
| Without skill | ~45 K | $0.045 |
| With skill (run 1) | ~152 K | $0.079 |
| With skill (rerun of T1, T6, T8, T9 after the fix) | ~104 K | $0.075 |

Input tokens are cumulative over the session's turns and mostly cached; about 30 K is the harness's own context
on every turn. The skill adds the cost of reading `SKILL.md`, a search of the index and one resource file. The
alternative, loading the Resources specification itself (about 2.7 million tokens), does not fit in the
context window.

## Run 2 · GitHub Copilot smoke test · 2026-10-22

- **Harness:** GitHub Copilot in VS Code, agent mode, `chat.useAgentSkills` enabled, skill installed in the
  project's `.github/skills/`. The model was not recorded.
- **Scope:** a smoke test with the three prompts that fail without the skill in Claude Code (T3, T6, T8).
  With skill only.
- **Skill invocation:** Copilot loaded the skill automatically in all three prompts ("Read skill
  `ed-fi-api-spec`") and opened the matching resource files.

| Test | Topic | Result | Notes |
|---|---|---|---|
| T3 | Synonym: parents and guardians | ✅ Pass | Read `contacts.md` and `studentContactAssociations.md`; "There isn't a separate parent resource"; correct keys |
| T6 | Keys inside a reference | ✅ Pass | Read `grades.md` and `studentSectionAssociations.md`; all seven reference fields and `gradingPeriodName` |
| T8 | Key changes | ✅ Pass | Read `sections.md`; key change with PUT and cascading key updates; pointed to `/keyChanges` |

Observation: Copilot searched the index before opening a file in each prompt, so it did not hit the
singular-file-name issue seen in Claude Code's first run.

## Run 3 · Claude Code, after the review changes · 2026-10-23

Same harness as Run 1, on the regenerated content: no natural keys, required flags only, the fields to supply
in each reference, nested collections expanded one level. The prompts that depended on keys were rewritten
(T1, T3, T4, T6, T7, T8), and two were added: T11 (identity is not inferred from required references, using
`localAccounts`) and T12 (nested collections).

| Test | Topic | With skill | Without skill |
|---|---|---|---|
| T1 | Required fields and references | ✅ Pass | ✅ Pass |
| T2 | Natural language: enrollment | ✅ Pass | ✅ Pass |
| T3 | Synonym: parents and guardians | ✅ Pass | ❌ Fail (`/ed-fi/parents`, `studentParentAssociations`) |
| T4 | Daily attendance vs. section attendance | ✅ Pass | ✅ Pass |
| T5 | Descriptors | ✅ Pass | ✅ Pass |
| T6 | Fields inside a reference | ✅ Pass | ❌ Fail (`periodSequence` instead of `gradingPeriodName`) |
| T7 | Synonym: test scores | ✅ Pass | ✅ Pass |
| T8 | Limits: key changes | ✅ Pass | ✅ Pass |
| T9 | Change-query endpoints | ✅ Pass | ✅ Pass |
| T10 | Limits: extensions | ✅ Pass | ✅ Pass |
| T11 | Identity not inferred from required references | ✅ Pass | ✅ Pass |
| T12 | Nested collections | ✅ Pass | ✅ Pass |
| **Total** | | **12 / 12** | **10 / 12** |

- **T8 and T11 with the skill** separated what the index shows from what it doesn't: for `localAccounts`, the
  answer said the specification marks no identity, gave the likely Data Standard key with that caveat, and
  explained why `chartOfAccountReference` is probably not part of it.
- **T12 with the skill** read the expanded `classPeriods` items directly from `sections.md`.
- **Without the skill**, T8 and T11 passed by hedging and answering from Data Standard knowledge; the
  remaining failures are, as in Run 1, Data Standard 4 names.
- **Context use:** about 104 K input tokens for prompts that open one resource file, and about 140 K for those
  that search the index more than once (cumulative over the session's turns, mostly cached).

## Run 4 · GitHub Copilot, after the review changes · 2026-10-23

GitHub Copilot in VS Code, agent mode, skill in `.github/skills/`, regenerated content, fresh chat per prompt.
With skill only. Copilot loaded the skill automatically in every prompt.

| Test | Result | Notes |
|---|---|---|
| T1 | ✅ Pass | Required fields and the fields of each reference |
| T2 | ✅ Pass | `studentSchoolAssociations` with its required fields |
| T3 | ✅ Pass | `contacts` and `studentContactAssociations` |
| T4 | ✅ Pass | `studentSchoolAttendanceEvents` with its required fields |
| T5 | ✅ Pass | Key outcomes met, but it also said grade level is on the Student resource (it is on `studentSchoolAssociations`) |
| T6 | ✅ Pass | All seven reference fields and `gradingPeriodName` |
| T7 | ✅ Pass | `studentAssessments`, `assessments` first, scores in `scoreResults` |
| T8 | ⚠️ Inconsistent | Two runs gave opposite answers: "generally can't change it with PUT" (fail) and "usually you can" (pass) |
| T9 | ⚠️ Partial | Right endpoint (`/deletes`), but no change-version bounds and no `/keyChanges` |
| T10 | ✅ Pass | Asked for the host's metadata; did not invent fields |
| T11 | ✅ Pass | `chartOfAccountReference` not in the key, with a source. To get there it fetched the Data Standard model from GitHub |
| T12 | ✅ Pass | `classPeriodReference` with `classPeriodName` and `schoolId` |
| **Total** | **10 / 12** | |

Observations:

- **Key changes (T8):** the index no longer said anything about changing a record's identifying values, so the
  answer came from the model's own knowledge and varied between runs. Fixed: resources whose PUT carries
  `x-Ed-Fi-isUpdatable` (eight in Data Standard 5.2) now say that `PUT` can change their identifying values,
  without listing the fields. With that line, T8 gave the same correct answer in three Claude Code runs, citing
  the specification, and T11 still said the specification doesn't show which fields identify a record.
- **Harness behavior:** in T10 Copilot asked for the host URL before answering, and in T11 it tried a GitKraken
  tool (cancelled) and fetched a web page. These come from the VS Code setup, not the skill.

## Not yet done

- **Codex** (optional, NFR-PORT-1).
