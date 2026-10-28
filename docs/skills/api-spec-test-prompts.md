# API spec lookup skill: test prompts

Test prompts for the [`ed-fi-api-spec`](../../skills/ed-fi-api-spec/SKILL.md) skill (PRD FR-REL-2). Each prompt
asks for something an assistant would otherwise find by loading the Resources or Descriptors specification.
Expected outcomes come from the Data Standard 5.2 specification; outcomes marked **(key)** must be met for the
prompt to pass.

Run each prompt in a fresh session, with the skill installed and without it, and record the answer, the files
read and the tokens used in [api-spec-test-results.md](api-spec-test-results.md).

## T1 · Exact resource: required fields and references

**Prompt:**

> Which fields are required to POST an Ed-Fi studentSectionAssociation, and what goes inside its references?

**Expected outcomes:**

1. **(key)** Required: `beginDate`, `sectionReference` and `studentReference`.
2. **(key)** Fields to supply in `sectionReference`: `localCourseCode`, `schoolId`, `schoolYear`,
   `sectionIdentifier`, `sessionName`; in `studentReference`: `studentUniqueId`.
3. Does not present the required fields as the natural key.

## T2 · Natural language: enrollment

**Prompt:**

> I need to record that a student enrolled in a school through the Ed-Fi API. Which resource do I use, and which
> fields are required?

**Expected outcomes:**

1. **(key)** Resource `studentSchoolAssociations` (`/ed-fi/studentSchoolAssociations`).
2. **(key)** Required: `entryDate`, `schoolReference` (`schoolId`), `studentReference` (`studentUniqueId`),
   `entryGradeLevelDescriptor`.
3. Does not invent a resource such as `enrollments` or `studentEnrollments`.

## T3 · Synonym: parents and guardians

**Prompt:**

> How do I send a student's parents or guardians to an Ed-Fi API (Data Standard 5.2)?

**Expected outcomes:**

1. **(key)** Resources `contacts` and `studentContactAssociations` (Data Standard 5 renamed "parents" to
   "contacts"); does not use `/ed-fi/parents`.
2. **(key)** `studentContactAssociations` requires `contactReference` (`contactUniqueId`) and
   `studentReference` (`studentUniqueId`).
3. The contact is created before the association.

## T4 · Choosing between similar resources: daily attendance

**Prompt:**

> Our SIS records whether a student was absent for the whole school day. Which Ed-Fi resource should hold that,
> and which fields are required?

**Expected outcomes:**

1. **(key)** `studentSchoolAttendanceEvents` (daily, school level), not `studentSectionAttendanceEvents`.
2. **(key)** Required: `attendanceEventCategoryDescriptor`, `eventDate`, `schoolReference`, `sessionReference`
   and `studentReference`.
3. Notes that the attendance category is a descriptor value.

## T5 · Descriptors

**Prompt:**

> Which descriptor holds a student's grade level in Ed-Fi, and where do I get its valid values?

**Expected outcomes:**

1. **(key)** `gradeLevelDescriptors` (`GradeLevelDescriptor`), sent as a URI such as
   `uri://ed-fi.org/GradeLevelDescriptor#Ninth grade`.
2. **(key)** The valid values come from the target API (`GET .../ed-fi/gradeLevelDescriptors`), not from the
   specification.

## T6 · Fields inside a reference

**Prompt:**

> I'm posting an Ed-Fi grade. What exactly goes inside its studentSectionAssociationReference, and what else is
> required?

**Expected outcomes:**

1. **(key)** `studentSectionAssociationReference` fields: `beginDate`, `localCourseCode`, `schoolId`,
   `schoolYear`, `sectionIdentifier`, `sessionName`, `studentUniqueId`.
2. **(key)** Also required: `gradeTypeDescriptor` and `gradingPeriodReference` (`gradingPeriodDescriptor`,
   `gradingPeriodName`, `schoolId`, `schoolYear`).

## T7 · Synonym: test scores

**Prompt:**

> Where do I put students' state test scores in Ed-Fi?

**Expected outcomes:**

1. **(key)** `studentAssessments`, which requires `studentAssessmentIdentifier`, `assessmentReference`
   (`assessmentIdentifier`, `namespace`) and `studentReference`.
2. The `assessments` record must exist first; scores go in the student assessment's score results.

## T8 · Limits: key changes

**Prompt:**

> Can I change a section's sectionIdentifier with a PUT in Ed-Fi, or do I have to delete and recreate it?

**Expected outcomes:**

1. **(key)** Says the key can be changed with a PUT, without deleting and recreating the section, because the
   spec index marks `sections` as supporting cascading key updates.
2. Gives the section's natural key from the index: `sectionIdentifier` plus the fields from
   `courseOfferingReference` (`localCourseCode`, `schoolId`, `schoolYear`, `sessionName`).
3. Presents the cascade as depending on the platform and host, with a way to confirm it.

## T9 · Change-query endpoints

**Prompt:**

> For an incremental sync, which Ed-Fi endpoint tells me which studentSchoolAssociations were deleted?

**Expected outcomes:**

1. **(key)** `GET /ed-fi/studentSchoolAssociations/deletes`, with `minChangeVersion`/`maxChangeVersion`.
2. Mentions `/keyChanges` as the companion endpoint for key changes.

## T10 · Limits: extensions

**Prompt:**

> Our Ed-Fi host has an extension resource called busRoutes in the "sample" namespace. What fields does it have?

**Expected outcomes:**

1. **(key)** Says extensions are not in the index and does not invent fields.
2. **(key)** Points to the host's own metadata (or regenerating the index from it with
   `eng/spec-knowledge-graph/generate.py`).

## T11 · Regression: identity is not inferred from required references

**Prompt:**

> Which references are part of an Ed-Fi localAccount's natural key?

**Expected outcomes:**

1. **(key)** The natural key is `accountIdentifier`, `educationOrganizationId` and `fiscalYear`.
2. **(key)** Does not say `chartOfAccountReference` is part of the natural key because it is required.

## T12 · Nested collections

**Prompt:**

> When I POST an Ed-Fi section, what is required in each item of its classPeriods?

**Expected outcomes:**

1. **(key)** Each item requires `classPeriodReference`, with `classPeriodName` and `schoolId`.

## T13 · Natural key

**Prompt:**

> What's the natural key of an Ed-Fi studentSectionAssociation?

**Expected outcomes:**

1. **(key)** `beginDate`, `localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName` and
   `studentUniqueId` (the section and student references' fields plus `beginDate`).
