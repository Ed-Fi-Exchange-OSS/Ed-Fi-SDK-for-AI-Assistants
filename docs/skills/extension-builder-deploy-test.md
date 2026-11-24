# Extension deployment: test on a local Ed-Fi API 8.1

Test of the deployment, security and verification guidance in `ed-fi-extension-builder`
([deploy.md](../../skills/ed-fi-extension-builder/references/deploy.md),
[security.md](../../skills/ed-fi-extension-builder/references/security.md),
[verify.md](../../skills/ed-fi-extension-builder/references/verify.md)). Run on 2026-11-23 by following the
guidance step by step, not through an assistant; assistant runs are part of the full test prompt set.

## Setup

- Data Management Service repository, `main` at `df7e234` (2026-11-20), local stack with PostgreSQL and the
  self-contained identity provider. The API reports version `8.0.0` in Discovery.
- API on port `8090` and PostgreSQL on `5445` (`.env`), because another Ed-Fi API used `8080` and `5435`.
- Extensions built with MetaEd 4.9.0 and the Data Standard 5.2 model, loaded together with the core and TPDM
  schemas:
  - `SampleAlternativeEducationProgram` (the how-to example).
  - `SampleStudentTranscript` (the how-to example; see the first result).
  - `SampleTest`: `Domain Entity EdFi.Staff additions` with `bool IsTenured ... is required`, to check rule
    CORE-5.
- Claims fragments from the guide for the first two extensions; `SampleTest` has no new resources.

## Results

| # | Check | Result |
|---|---|---|
| 1 | Start with the Student Transcript example as written | ❌ `api-schema-tools ddl provision failed ... exit code 1`. `ddl emit` shows `An item with the same key has already been added. Key: samplestudenttranscript.StudentAcademicRecordExtension`. Same with the `v8.1.0` tag. |
| 2 | Same, without the `ClassRanking` additions | ✅ Starts; claims gate passed (3 checks, 10 deferred) |
| 3 | `ddl emit` with only the `ClassRanking` additions | ❌ Corrected on 2026-11-24, see below. The first run had the `Common` file but not the `common extension` property, so it tested nothing. |
| 4 | Discovery | ✅ Lists `SampleAlternativeEducationProgram`, `SampleStudentTranscript` and `SampleTest` 1.0.0 |
| 5 | GET on the new endpoints (EdFiSandbox) | ✅ `200 []` on the AEP descriptor and association, and on `postSecondaryOrganizations` |
| 6 | POST descriptor values with namespace `uri://sample.org/...` | ❌ `403 namespace-mismatch` (expected: not one of the vendor's prefixes) |
| 7 | Same with `uri://sample.ed-fi.org/...` | ✅ `201` for the AEP descriptor and three Student Transcript descriptors; read back |
| 8 | POST and GET `postSecondaryOrganizations` | ✅ `201`, read back with both descriptors |
| 9 | POST `studentAcademicRecords` with `_ext.samplestudenttranscript` | ✅ `201`; GET returns the `_ext` values and a link to the postsecondary organization (after creating the school, student, `studentSchoolAssociation` and school year) |
| 10 | Same, `_ext` referring to a missing postsecondary organization | ✅ `409`, error on `$._ext.samplestudenttranscript.postSecondaryOrganizationReference` |
| 11 | OpenAPI schema of `studentAcademicRecords` | ✅ Has `samplestudenttranscript_EdFi_StudentAcademicRecordExtension` |
| 12 | `AssessmentVendor` client, not granted the new domain | ✅ `403` on `postSecondaryOrganizations`; `200` on `institutionLevelDescriptors` (inherited from `systemDescriptors`) |
| 13 | Wrong URL segment (`samplestudenttranscript`) | ✅ `404` |
| 14 | CORE-5: POST `staffs` without `_ext` | `201`; the record has no `isTenured` |
| 15 | CORE-5: POST `staffs` with `_ext.sampletest` = `{}` | `201`; stored without `_ext` |
| 16 | CORE-5: POST `staffs` with `isTenured` = `"notabool"` | `400`, `isTenured Value is "string" but should be "boolean"` |
| 17 | CORE-5: POST `staffs` with `isTenured` `true` and `false` | `201`; read back with the value |

### Common extension, rechecked on 2026-11-24

After review, four variants of the Student Transcript example were built with MetaEd 4.9.0 and checked with
`ddl emit` from the `v8.1.0` tag, on PostgreSQL and SQL Server (same result on both). No stack was started.

| Additions to `StudentAcademicRecord` | `Common EdFi.ClassRanking additions` | Result |
|---|---|---|
| Only `common extension EdFi.ClassRanking` | Yes | ❌ `An item with the same key has already been added. Key: samplestudenttranscript.StudentAcademicRecordExtension` |
| None | Yes | ✅ Emits, but `studentAcademicRecords` isn't extended: `classRanking` gets no `_ext`. MetaEd gives no warning. |
| Only `descriptor SubmissionCertification` | No | ✅ Emits |
| Both, as in the example | Yes | ❌ Same error as the first row |

The `common extension` property is what fails, not the combination with other additions.

Other observations:

- The generated table column for the required addition is nullable (`"IsTenured" boolean NULL`).
- `EdFiSandbox` can't create `schoolYearTypes` (`403`); a client with `EdFiAPIPublisherWriter` did.
- A second `Get-SmokeTestCredential` call with the default vendor and application names fails with `400`.

## Changes from this test

- Rule CORE-5 now says that Ed-Fi API 8.1 doesn't enforce required additions (results 14 and 15). The earlier
  reason, that clients must send the value, was wrong.
- `deploy.md` documents the Student Transcript failure as a known issue, with the `ddl emit` command that shows
  the cause. Since the recheck, it says that the `common extension` property fails on its own.
- `security.md` and `verify.md` cover descriptor namespace prefixes and relationship-based access, which the
  guides don't mention.

## Not tested yet

- Assistants following the guidance (Claude Code, GitHub Copilot).
- SQL Server, Keycloak and hosts other than the local stack.
- Data Standard 6.1.
