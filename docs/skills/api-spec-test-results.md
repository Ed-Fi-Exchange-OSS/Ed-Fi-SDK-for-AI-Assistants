# API spec lookup skill: test results

Results of the [test prompts](api-spec-test-prompts.md) (FR-REL-1, FR-REL-2).

> **Runs 1 and 2 used an earlier version of the generated content** that derived natural keys from the request
> schemas (identity fields plus required references), which the specification can't support. Runs 3 and 4 used
> content without natural keys. **Run 5** adds natural keys again, now from the GET query parameters marked
> `x-Ed-Fi-isIdentity`, and re-runs the prompts about keys.

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

## Run 5 · Claude Code, natural keys from the GET query parameters · 2026-10-27

The request schemas mark identity on scalar fields only, but the collection GET's query parameters flatten
references into their fields and mark every identity field with `x-Ed-Fi-isIdentity` (all 138 collections in
Data Standard 5.2). Each resource file now has a **Natural key** section built from them; for `localAccounts`
it is `accountIdentifier`, `fiscalYear`, `educationOrganizationId`, without `chartOfAccountReference`.

Re-run of the prompts about keys (T1, T8, T11) and a new one (T13), same harness as Run 3:

| Test | With skill | Without skill |
|---|---|---|
| T1 · Required fields and references | ✅ Pass | ✅ Pass |
| T8 · Key changes | ✅ Pass (cites `x-Ed-Fi-isUpdatable`; gives the section's natural key) | ❌ Fail (hedged: "depends on your version"; key right, from memory) |
| T11 · `localAccounts` natural key | ✅ Pass (key from the spec; `chartOfAccountReference` not in it) | ✅ Pass (from Data Standard knowledge, with a caveat) |
| T13 · `studentSectionAssociations` natural key | ✅ Pass (seven fields, with the reference each comes from) | ✅ Pass |

T8's expected outcomes were updated for this run: the index now shows the natural key and whether it can
change, so the answer should give both from the specification. Both runs were scored against the updated
outcomes; without the skill, the answer gives the key from memory but doesn't say whether it can change.

With the skill, the answers about keys now come from the specification and say so; without it, the model
answers these well-known resources from memory and hedges.

## Run 6 · Claude Code, upgrade prompts T12–T14 · 2026-11-11

- **Harness:** Claude Code, headless, default model (`claude-sonnet-5-5`), fresh session per prompt.
- **Conditions:** *with skill* (`ed-fi-api-spec` installed, including the version change lists
  `references/whats-new-v50.md`, `v51.md` and `v52.md`) and *without skill* (empty project).
- **Restrictions:** the *without skill* runs were not limited to the model alone. The usage records show web
  searches by a `claude-haiku-5-5` helper model (1 in T12, 2 in T13, 3 in T14), although the top-level
  `server_tool_use` counters read 0. In T14 the answer also says it could not read the local spec files. The
  *with skill* runs made no searches.
- **Prompts:** the upgrade prompts T12 (Data Standard 4.0 to 5.0), T13 (5.0 to 5.1) and T14 (5.1 to 5.2) from
  [api-client-test-prompts.md](api-client-test-prompts.md). The prompts with the same numbers in this
  file's [test prompts](api-spec-test-prompts.md) (nested collections, natural key) were not run.
- **Skill invocation:** the skill was invoked automatically in all three prompts. In an earlier run of T13
  it was not; the `SKILL.md` description change fixed that.

### Summary

| Test | Topic | With skill | Without skill |
|---|---|---|---|
| T12 | Upgrade: Data Standard 4.0 to 5.0 | ✅ Pass | ❌ Fail (grading period key change missing) |
| T13 | Upgrade: Data Standard 5.0 to 5.1 | ✅ Pass | ✅ Pass (key outcomes only; see below) |
| T14 | Upgrade: Data Standard 5.1 to 5.2 | ✅ Pass | ❌ Fail (one of five registration resources, no load order) |
| **Total** | | **3 / 3** | **1 / 3** |

### Outcomes by test

| Test | Key outcomes | With skill | Without skill |
|---|---|---|---|
| T12 | Parent becomes Contact | ✅ `parents` to `contacts`, `studentParentAssociations` to `studentContactAssociations`, `parentReference` to `contactReference` (does not name `contactUniqueId`) | ⚠️ "StudentParentAssociation equivalents"; asks to confirm `/ed-fi/contacts`; no exact names |
| T12 | `gradingPeriods` natural key changed | ✅ Old and new key, `periodSequence` optional, every `gradingPeriodReference` changes, affected resources listed | ❌ Says `GradingPeriodName` was added as required and `PeriodSequence` is optional; never says the key or its references changed |
| T12 | `beginDate` in the key of `staffSectionAssociations` | ✅ Only `staffSectionAssociations` | ✅ |
| T13 | No breaking changes | ✅ Includes the namespace caveat | ✅ For the data model, but then lists ODS/API 7.2 breakages it did not confirm as 5.1 changes |
| T13 | New resources `crisisEvents`, `studentHealths`, `studentTransportations` | ✅ With keys and required fields | ✅ Named as entities (`CrisisEvent`, etc.) |
| T14 | Dual credit on `studentSectionAssociations`, all five properties | ✅ Five properties, and says not on `sections` | ⚠️ Right resource, three of five properties; misses `dualCreditTypeDescriptor` and `dualCreditEducationOrganizationReference` |
| T14 | Five new assessment registration resources | ✅ All five, plus `studentEducationOrganizationAssessmentAccommodations` | ❌ Only `studentAssessmentRegistrations`; "other resources may exist, I did not enumerate them" |
| T14 | 5.2 is non-breaking | ✅ Cites the change list | ⚠️ "Minor release, intended to be non-breaking", hedged |

Other outcomes:

| Test | Outcome | With skill | Without skill |
|---|---|---|---|
| T12 | Deprecated elements removed, `schoolChoiceTransfer` deprecated, none invented | ✅ | ✅ |
| T12 | New optional fields and `studentSpecialEducationProgramEligibilityAssociations` | ✅ | ✅ |
| T12 | Treats 5.0 as breaking, no claim of a complete list | ✅ | ✅ |
| T13 | `displacedStudents` references `crisisEvent` by `crisisEventName` | ✅ | ⚠️ Collection found, no `crisisEventName`; unsure of the field name |
| T13 | `hispanicLatinoEthnicity` deprecated, not removed | ✅ | ✅ |
| T13 | New descriptor types; values come from the target API | ✅ Nine types, "values must be loaded by the host" | ❌ Only the Race sample values |
| T13 | No other changes claimed | ✅ | ⚠️ Adds ODS/API 7.2 changes (labeled as platform) |
| T14 | `assessment` created before `assessmentAdministrations` | ✅ | ❌ |
| T14 | `studentSection504ProgramAssociations` and deprecated descriptor values | ✅ Both, about 110 values across 19 descriptors | ❌ |
| T14 | No renamed fields claimed | ✅ Says duration properties only state their unit | ✅ |

### What the skill changed

- **T12:** the clearest gain is the grading period key. With the skill the answer gave the old and new key, said
  `periodSequence` is optional and listed the five resources whose references change. Without it, the answer
  mentioned only that `gradingPeriodName` is required. The Run 6 error of adding `beginDate` to the key of
  `studentSectionAssociations` did not recur.
- **T13:** both conditions passed the key outcomes. The skill added the field-level detail (keys, required
  fields, the nine descriptor types, `crisisEventName`) and kept to the data standard. Without it, the answer
  mixed in ODS/API 7.2 changes and said it could not confirm which were new in 7.2.
- **T14:** with the skill the answer was field-level, gave the load order and listed the 504 resource and the
  deprecated descriptor values. Without it, the answer relied on search summaries and got the registration
  resources and dual credit properties only partly.
- **Web search narrowed the gap.** Compared with an offline baseline, the *without skill* answers named the
  Contact rename, the dual credit location and `studentAssessmentRegistrations`. They still missed everything
  that needs the change list itemized.

### Context use

| Test | Without skill (cost · time · turns) | With skill (cost · time · turns) |
|---|---|---|
| T12 | $0.188 · 81 s · 5 | $0.142 · 21 s · 5 |
| T13 | $0.153 · 99 s · 7 | $0.134 · 17 s · 5 |
| T14 | $0.208 · 48 s · 9 | $0.145 · 22 s · 6 |

The *without skill* costs include the Haiku helper's web searches. With the skill, each answer was about 30%
cheaper and 2 to 5 times faster.

> [!NOTE]
> As with all runs, review the answers before relying on them. The with-skill T14 answer says
> `programEducationOrganizationId` is now in the natural key of
> `studentSpecialEducationProgramEligibilityAssociations`; this was not checked against the specification.

## Not yet done

- **Codex** (optional, NFR-PORT-1).
- **GitHub Copilot** for prompts T12-T14
