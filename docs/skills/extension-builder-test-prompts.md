# Extension Builder skill: test prompts

Test prompts for the [`ed-fi-extension-builder`](../../skills/ed-fi-extension-builder/SKILL.md) skill (PRD
FR-REL-1, FR-REL-2). Expected outcomes come from the skill's references, which were checked against MetaEd
4.9.0 and a local Ed-Fi API 8.1 ([deploy test](extension-builder-deploy-test.md),
[review test](extension-builder-review-test.md)). Outcomes marked **(key)** must be met for the prompt to pass.

Run each prompt in a fresh session, with the skill installed and without it, and record the results in
`extension-builder-test-results.md`. Score each outcome ✅ met, ⚠️ partially met or ❌ not met.
[`eng/extension-test-prompts`](../../eng/extension-test-prompts/README.md) runs them in Claude Code and the
GitHub Copilot CLI.

The prompts cover the parts of the skill: deciding whether an extension is needed (T1), modeling (T2, T3),
build errors and the command-line build (T4, T5), deployment (T6, T7), security (T8, T9), verification (T10),
review (T11) and hosts the skill doesn't cover (T12). T11 needs the `BusRoutes` extension from
[`fixtures/`](../../eng/extension-test-prompts/fixtures/) in the working folder.

## T1 · The core model already has it

**Prompt:**

> Our district runs Ed-Fi API 8.1 with Data Standard 5.2. We need to record which bus route each student
> rides, the bus number, and whether the student is eligible for transportation at public expense. Write the
> MetaEd extension for this.

**Expected outcomes:**

1. **(key)** Says the core model already covers it: `StudentTransportation` (Data Standard 5.0 and later),
   with `transportationPublicExpenseEligibilityTypeDescriptor` and the `studentBusDetails` collection
   (`busNumber`, `busRouteDescriptor`).
2. **(key)** Recommends using the core resource, `/ed-fi/studentTransportations`, instead of writing an
   extension, or asks the developer to confirm before writing one.
3. Treats routes as descriptor values loaded as data (`busRouteDescriptors`), not as new MetaEd elements.

## T2 · A new program association and descriptor

**Prompt:**

> Our district runs a mentoring program. We need to record which students are in it and why each one was
> referred, from a list we maintain (academic, attendance, behavior). We're on Ed-Fi API 8.1 with Data Standard
> 5.2. Write the MetaEd extension files; call the project SampleMentoring.

**Expected outcomes:**

1. **(key)** Models the participation as `Association StudentMentoringProgramAssociation based on
   EdFi.GeneralStudentProgramAssociation` (or the like), not as a new association that repeats the student,
   program and education organization references.
2. **(key)** Adds a `Descriptor` for the referral reason, named without a `Descriptor` suffix, and leaves the
   values (academic, attendance, behavior) out of the model: they are data loaded through the API.
3. **(key)** Prefixes core names with `EdFi.` and adds no `is part of identity` property to the subclass.
4. Gives a `package.json` with `projectName` `SampleMentoring` and a SemVer `projectVersion`, and one file per
   entity in the folder for its kind.
5. Gives every entity and property a `documentation` line that says what it means.
6. Mentions the next steps: the build, and a claims fragment for the new association and descriptor.

## T3 · A required field on a core resource

**Prompt:**

> We need a yes/no "is tenured" flag on every staff member in our Ed-Fi API 8.1 (Data Standard 5.2). Our HR
> system always has it, and clients must always send it. Write the MetaEd for our SampleHR extension.

**Expected outcomes:**

1. **(key)** Uses `Domain Entity EdFi.Staff additions` with a `bool` property, not a new `Staff` entity.
2. **(key)** Says that Ed-Fi API 8.1 doesn't make clients send an addition marked `is required` (a `POST`
   without `_ext` returns `201`), so the property should be optional and the clients must validate it.
3. Shows where the value goes in the payload: `_ext.samplehr.isTenured` on `/ed-fi/staffs`.
4. Says the core resource's claim covers the addition, so no new claim is needed.

## T4 · A build that fails

**Prompt:**

> My MetaEd build fails on this file and I can't see why. It's in an extension for Data Standard 5.2.
>
> ```metaed
> Domain Entity BusRoute
>     documentation "A bus route that serves a school."
>     string RouteNumber
>         documentation "The number of the route."
>         is part of identity
>     domain entity School
>         documentation "The school the route serves."
>         is part of identity
> ```

**Expected outcomes:**

1. **(key)** Finds that `string RouteNumber` has no `max length`, which the build requires.
2. **(key)** Finds that `School` is a core entity and needs the `EdFi.` prefix.
3. Proposes the corrected file and says to build again after the fix. If it can edit files, it asks before
   changing them.
4. Doesn't report problems that aren't there (for example, the indentation or the `Domain Entity` keyword).

## T5 · Building from the command line

**Prompt:**

> How do I build our MetaEd extension (./SampleBusRoutes, Data Standard 5.2) from the command line, so our CI
> pipeline can run it? We don't want to depend on VS Code.

**Expected outcomes:**

1. **(key)** Uses the `@edfi/metaed-console` package with the core model package (`@edfi/ed-fi-model-5.2`),
   installed from the Ed-Fi package feed through an `.npmrc` entry for `@edfi`.
2. **(key)** Gives a config file that lists the core project first and the extension second, with the
   extension's `projectName` as its namespace, and `allianceMode` `false`.
3. **(key)** Says that the `-a` flag accepts the Ed-Fi License Agreement, and that the developer must accept
   it; doesn't add it silently.
4. Says the exit code is `0` on success and `1` on errors, which is what CI checks, and that only `"level":
   "error"` lines fail the build.
5. Names the output: `MetaEdOutput/<projectName>/ApiSchema/ApiSchema-EXTENSION.json`, the file Ed-Fi API 8.1
   loads.

## T6 · Deploying to a local Ed-Fi API 8.1

**Prompt:**

> Our extension builds without errors. How do we deploy it to our local Ed-Fi API 8.1, the Docker stack from
> the Data Management Service repository?

**Expected outcomes:**

1. **(key)** Stages a schema folder that holds the core schemas and the extension's
   `ApiSchema-EXTENSION.json`, each in its own folder, with `prepare-dms-schema.ps1 -ApiSchemaPath`.
2. **(key)** Writes and stages a claims fragment for the new resources and descriptors, with
   `prepare-dms-claims.ps1 -ClaimsDirectoryPath`.
3. **(key)** Says the database must be empty, so the stack is reset first (`bootstrap-local-dms.ps1 -d -v`),
   that this deletes all data and API clients, and that the developer must agree before it runs.
4. Starts the stack with `bootstrap-local-dms.ps1` and names the success signs (`Claims gate PASSED`, `DMS
   service is healthy`).
5. Doesn't use ODS/API 7.x steps: no C# extension project, no SQL claims scripts, no `initdev`.

## T7 · The start fails with a provisioning error

**Prompt:**

> We followed the Student Transcript how-to to extend Ed-Fi API 8.1. MetaEd builds the extension fine, but
> `bootstrap-local-dms.ps1` stops with `api-schema-tools ddl provision failed` and exit code 1. What's wrong?

**Expected outcomes:**

1. **(key)** Says the start script doesn't show the cause, and gives the `api-schema-tools ddl emit` command
   (core schema first, then the extensions) to see it without a database.
2. **(key)** Names the known issue: the `common extension EdFi.ClassRanking` property in the Student Transcript
   example fails on Ed-Fi API 8.1.0 with `An item with the same key has already been added`.
3. **(key)** Gives a workaround: drop the common extension and put the new properties on the resource itself.
4. Says that after the change the extension must be rebuilt and the stack reset and started again.

## T8 · A new resource returns 403

**Prompt:**

> We deployed our SampleStudentTranscript extension to Ed-Fi API 8.1. Our SIS vendor's client (claim set
> SISVendor) gets 403 on `GET /data/sample-student-transcript/postSecondaryOrganizations`. Core resources
> work. How do we fix it?

**Expected outcomes:**

1. **(key)** Says the new resource needs a resource claim in a claims fragment, and that the claim set must get
   access to it.
2. **(key)** Uses the Ed-Fi API 8 claim name
   `http://ed-fi.org/identity/claims/sample-student-transcript/PostSecondaryOrganization`, without the
   `/ods/` segment of ODS/API 7.x.
3. Places it under an existing domain whose grants `SISVendor` has, or under a new domain with explicit
   `claimSets`, and asks which claim sets need access.
4. Says the claims are loaded at start, so the fragment is staged and the stack reset and started again.
5. Suggests reading the `403` body, which names the claim and the action.

## T9 · A descriptor write returns 403

**Prompt:**

> On our Ed-Fi API 8.1 with the SampleAlternativeEducationProgram extension, a POST to
> `/data/sample-alternative-education-program/alternativeEducationEligibilityReasonDescriptors` with namespace
> `uri://mydistrict.org/AlternativeEducationEligibilityReasonDescriptor` returns 403: "The 'Namespace' value of
> the data does not start with any of the caller's associated namespace prefixes". What do we do?

**Expected outcomes:**

1. **(key)** Explains that descriptor writes are authorized by namespace prefix, and the client's vendor has
   no prefix that matches `uri://mydistrict.org`.
2. **(key)** The fix: use a namespace that starts with one of the vendor's prefixes, or ask the host
   administrator to add the prefix to the vendor.
3. Doesn't send the developer to the claims fragment as the fix.

## T10 · Checking a deployment

**Prompt:**

> We just deployed the SampleStudentTranscript extension (new postSecondaryOrganizations resource, and new
> fields on studentAcademicRecords) to our local Ed-Fi API 8.1. How do we check that it works?

**Expected outcomes:**

1. **(key)** Checks Discovery (`/api`): `dataModels` lists `SampleStudentTranscript` with its version.
2. **(key)** Calls the new resource at `/data/sample-student-transcript/postSecondaryOrganizations`, then
   writes a record and reads it back.
3. **(key)** Checks the additions on the core resource: a `studentAcademicRecords` record at `/data/ed-fi/`
   with `_ext.samplestudenttranscript`, written and read back. A `200` on the core resource alone doesn't
   prove the extension is loaded.
4. Says the reset deleted the API clients, so a new client and token are needed first.
5. Loads descriptor values before the resources that refer to them.

## T11 · Reviewing an extension

Needs the `BusRoutes` folder from [`fixtures/`](../../eng/extension-test-prompts/fixtures/) in the working
folder. It has the 13 planted defects of the [review test](extension-builder-review-test.md). Unlike that
test, the run is read-only: the assistant can't run the build, so build errors must be found by reading.

**Prompt:**

> Please review the MetaEd extension in ./BusRoutes before we deploy it to our Ed-Fi API 8.1 host. Don't
> change the files; just give me the review.

**Expected outcomes:** one per planted defect; the prompt passes with the **(key)** outcomes and at least 10
of the 13.

1. **(key)** The descriptor named `BusTypeDescriptor` (the `Descriptor` suffix doesn't build).
2. **(key)** `BusEligibility` is used but not declared.
3. **(key)** The extension declares its own `Staff` instead of extending the core one.
4. **(key)** It duplicates the core `GradeLevel` descriptor, and the association uses the copy.
5. **(key)** A required property added to the core `Student` (keep additions optional).
6. Begin and end dates on student language data, which keep a history in the record.
7. The typo "Teh".
8. Documentation that repeats the name (`"BusRoutes"`).
9. "student record" and "staff record" in documentation, for the entity itself.
10. Placeholder descriptor examples ("Value1, Value2").
11. The plural entity name `BusRoutes`.
12. `Student` isn't the first reference in the association.
13. The deprecated `is queryable field`.

## T12 · An ODS/API 7.3 host

**Prompt:**

> We run Ed-Fi ODS/API 7.3 with Data Standard 5.2. Walk me through deploying our MetaEd extension
> SampleBusRoutes.

**Expected outcomes:**

1. **(key)** Says the deployment differs on ODS/API 7.x, and doesn't give the Ed-Fi API 8.1 steps (staging
   `ApiSchema-EXTENSION.json`, claims fragments, `bootstrap-local-dms.ps1`) as the answer.
2. Describes the ODS/API 7.x path in outline (the MetaEd artifacts for 7.x, a C# extension project, the
   database and security scripts, `initdev`), or points to the ODS/API 7.3 documentation.
3. Keeps the modeling and build guidance, which is the same for both hosts.
