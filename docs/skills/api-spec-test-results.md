# API spec lookup skill: test results

Results of the [test prompts](api-spec-test-prompts.md) (FR-REL-1, FR-REL-2).

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

## Not yet done

- **GitHub Copilot** (FR-REL-1): the same prompts, with the skill installed in `.github/skills/` or
  `.agents/skills/`.
