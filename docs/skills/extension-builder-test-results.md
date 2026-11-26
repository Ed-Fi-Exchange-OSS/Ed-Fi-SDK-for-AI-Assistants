# Extension Builder skill: test results

Results of the [test prompts](extension-builder-test-prompts.md) (FR-REL-1, FR-REL-2), run on 2026-11-25 with
[`eng/extension-test-prompts`](../../eng/extension-test-prompts/README.md).

## Setup

- **Harnesses:** Claude Code 2.1.319 (`claude -p`, default model, which reported `claude-sonnet-5-5`) and GitHub
  Copilot CLI 1.0.105 (`copilot -p`, model `claude-sonnet-5.5`). One fresh session per prompt and condition.
- **Conditions:** *with skill* (`ed-fi-extension-builder` from `main` at `ac5e73e`, installed in the project's
  `.claude/skills/` or `.github/skills/`) and *without skill*. Both work folders held the `BusRoutes` fixture
  for T11.
- **Restrictions:** read-only. Claude Code denied file writes, shell and web tools; Copilot denied shell and
  write and excluded web fetch, web search and code search. Answers come from the model plus, when installed,
  the skill. No MetaEd build or Ed-Fi API was available to the assistants.
- **Scoring:** by hand, against the expected outcomes. A prompt passes when every **(key)** outcome is met.
  Each condition ran once.

## Summary

| Test | Topic | Claude Code with | Claude Code without | Copilot with | Copilot without |
|---|---|---|---|---|---|
| T1 | The core model already has it | ❌ | ❌ | ❌ | ❌ |
| T2 | New program association and descriptor | ✅ | ✅ | ✅ | ❌ |
| T3 | Required field on a core resource | ✅ | ❌ | ✅ | ❌ |
| T4 | A build that fails | ❌ | ❌ | ❌ | ❌ |
| T5 | Building from the command line | ✅ | ❌ | ✅ | ❌ |
| T6 | Deploying to a local Ed-Fi API 8.1 | ✅ | ❌ | ✅ | ❌ |
| T7 | Provisioning error at start | ✅ | ❌ | ✅ | ❌ |
| T8 | New resource returns 403 | ✅ | ❌ | ✅ | ❌ |
| T9 | Descriptor write returns 403 | ✅ | ✅ | ✅ | ✅ |
| T10 | Checking a deployment | ✅ | ❌ | ✅ | ❌ |
| T11 | Reviewing an extension (13 defects) | ✅ 12/13 | ❌ 9/13 | ✅ 13/13 | ❌ 9/13 |
| T12 | An ODS/API 7.3 host | ✅ | ✅ | ✅ | ✅ |
| **Total** | | **10 / 12** | **3 / 12** | **10 / 12** | **2 / 12** |

The skill was used in every *with* run except two in Claude Code: T4 (answered without reading anything) and
T12 (it looked at the skill's scope and chose not to use it, which is the expected result).

## What the skill changed

| Test | Without the skill | With the skill |
|---|---|---|
| T2 | Claude Code: right design, but files with a `Namespace` header and multi-line documentation, which MetaEd 4.9 doesn't accept. Copilot: a new association with its own student and dates instead of `based on EdFi.GeneralStudentProgramAssociation`, and a `Descriptor` suffix | `based on EdFi.GeneralStudentProgramAssociation`, descriptor without suffix, values as data, `package.json`, claims as the next step |
| T3 | Both said `is required` makes the API reject writes without the value (Ed-Fi API 8.1 doesn't); Claude Code also used `Domain Entity Extension Staff`, which isn't MetaEd syntax | `EdFi.Staff additions`, optional, with the reason and where to validate |
| T5 | Invented config files and commands (`metaed.json`, cloning MetaEd-js); Copilot treated `-a` as something CI just needs | The `@edfi` feed, the two packages, the real config, `-a` left to the developer, exit codes, output path |
| T6 | Old or invented DMS scripts (`start-local-dms.ps1`, `USE_API_SCHEMA_PATH`), no claims fragment, no warning that the reset deletes data | Schema staging, claims fragment, reset with a warning, start, success signs |
| T7 | Blamed the `BusRoutes` fixture in the folder; no `ddl emit`, no known issue | `ddl emit` to see the cause, the `ClassRanking` known issue, the workaround and the redeploy |
| T8 | ODS/API 7.x claim names (`/ods/` segment, security database tables) | Ed-Fi API 8 claim name, fragment with `claimSets`, redeploy, how to read the `403` |
| T10 | ODS/API 7.x URLs (`/data/v3/...`, `/metadata/data/v3/...`); no Discovery `dataModels` | Discovery, `/data/sample-student-transcript/...`, `_ext` written and read back, new client after the reset |
| T11 | Both said `Domain Entity EdFi.Student additions` is invalid and asked for a `Namespace` block; missed the `Student`-first and `is queryable field` defects | All build errors and core duplicates found; see below |

T9 and T12 passed in every condition: the namespace prefix rule and the ODS/API 7.x path are general Ed-Fi
knowledge.

## Failures with the skill

- **T1 (both harnesses):** neither found the core `StudentTransportation` (Data Standard 5.1 and later). Claude
  Code said Data Standard 5.2 has no transportation entity "that I know of", suggested checking, and wrote the
  extension anyway; Copilot reworked the `BusRoutes` fixture into a transportation extension. The skill told
  the assistant to check the core model, but not how, and the `ed-fi-api-spec` skill wasn't installed.
- **T4, Claude Code:** the skill wasn't loaded for MetaEd source pasted into the chat. The answer found the
  missing `max length`, but said `School` needs no prefix and added a `Begin Namespace` block, which MetaEd 4.x
  doesn't use.
- **T4, Copilot:** the skill was loaded, but no reference was read. The answer found the missing `EdFi.`
  prefix and missed the missing `max length`; it also mentioned a `Namespace` block.
- **T11, both harnesses:** one false positive: both said the association's two references need `is part of
  identity` and the build fails without it. The same extension builds without it (see the
  [review test](extension-builder-review-test.md)); an association's references are its identity. Claude Code
  also missed defect 12 (`Student` not first).

## Changes from this test

- `SKILL.md`: check the core model before writing any `.metaed` file, with `ed-fi-api-spec` or by searching the
  core model package, and ask the developer when neither is possible. The description now names MetaEd source
  pasted into the chat and MetaEd build errors. Two rules added: `string` needs `max length` (and `decimal` its
  digits), and MetaEd 4.x files have no `Namespace` block; an association's references are its identity.
- `rules.md` KEY-1: don't report an association's references as missing `is part of identity`.

## Rerun after the fixes (T1, T4, T11)

Same harnesses and restrictions, with the skill at `4946600`. T1 also ran with `ed-fi-api-spec` installed
next to the extension builder, as [Installing and using the Ed-Fi SDK for AI](using-the-skills.md)
recommends.

| Test | Claude Code | Copilot | Notes |
|---|---|---|---|
| T1, extension builder only | ❌ | ❌ | Both stopped before writing anything and asked the developer to check the core model; both named `StudentTransportation` from memory but couldn't confirm it (key outcome 1 partly met) |
| T1, with `ed-fi-api-spec` | ✅ | ✅ | Both looked up `studentTransportations` and mapped every need to a core field; no extension written |
| T4 | ✅ | ✅ | Both found the missing `max length` and the missing `EdFi.` prefix; Claude Code loaded the skill and read `build.md` |
| T11 | ✅ 13/13 | ✅ 13/13 | No false positive on the association's identity; both said its references are correct as written |

With the fixes, the *with skill* runs pass 11 of 12 prompts in each harness, and 12 counting T1 with
`ed-fi-api-spec` installed (the other prompts weren't run with it). The *without skill* runs weren't
repeated, since nothing changed for them.

## Review as a separate skill (T11, 2026-11-26)

The review moved to the `ed-fi-extension-review` skill. T11 ran again in the *with skill* condition, with both
skills installed (`--extra-skills ed-fi-extension-review`). Both assistants loaded the review skill, not the
builder.

| Run | Claude Code | Copilot | Notes |
|---|---|---|---|
| First | ✅ 13/13 | ❌ 12/13 | Copilot missed the undeclared `BusEligibility` (key outcome 2); it couldn't run the build and didn't look for the errors the build would give |
| After the fix to `review.md` | ✅ 13/13 | ✅ 13/13, twice | `review.md` now says to check, when the build can't run, that every referenced name is declared |

## Not tested yet

- The MetaEd build and the Ed-Fi API from the assistant's own output: the assistants couldn't run tools here.
  The [deploy test](extension-builder-deploy-test.md) ran the same steps by hand.
- GitHub Copilot in VS Code agent mode (the Copilot CLI was used), and other models.
- Repeated runs; each condition ran once (the rerun prompts twice).
- Data Standard 6.1.
