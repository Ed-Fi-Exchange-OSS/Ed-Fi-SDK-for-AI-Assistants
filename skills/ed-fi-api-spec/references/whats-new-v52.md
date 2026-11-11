# Changes from Data Standard 5.1 to 5.2

Scope: v5.1 -> v5.2. The source states the release is non-breaking: additions, definition updates and
code-value changes only.

## Added resources (Assessment Registration domain)

- `assessmentAdministrations`: administration of an assessment. References assigning education organization
  and `assessment`. Tracks `administrationIdentifier`, assessment administration period,
  assessment battery part.
- `assessmentAdministrationParticipations`: planned participation of an education organization in an
  assessment administration.
- `assessmentBatteryParts`: parts organized for administering an assessment. Reference `objectiveAssessments`
  when aligned.
- `studentAssessmentRegistrations`: student expected to participate in an assessment administration. Has
  reporting education organization, assessment accommodation, assessment customization.
- `studentAssessmentRegistrationBatteryPartAssociations`: battery parts the student is to be tested on in
  the administration.
- `studentEducationOrganizationAssessmentAccommodations`: general accommodations required or expected for
  all assessments, as determined by the education organization.
- Usage:
  - An assessment may have 0..n `assessmentAdministrations` per school year.
  - Create the `assessment` first if it does not exist; create `assessmentBatteryParts` first if parts are
    delivered selectively.
  - Registration is not required to report a `studentAssessment`, but every registered student should have
    a `studentAssessment`, even if untested.
  - Use the battery part association only when the student gets selected parts or per-part accommodations.

## Added resource (Alternative and Supplemental Services)

- `studentSection504ProgramAssociations`, a sub-program of general student program association.
  Properties:
  - `section504Eligibility`: boolean
  - `accommodationPlan`: indicator that the eligibility decision requires an accommodation
  - `section504DisabilityDescriptor`: descriptor, disability qualifying the student
  - `section504MeetingDate`: date of meeting with parent/guardian on eligibility
  - `section504EligibilityDecisionDate`: date of the eligibility (or ineligibility) decision

## Added properties

| Resource | Property | Notes |
|---|---|---|
| `studentSectionAssociations` | `dualCreditIndicator` | boolean, student receives dual credit on completion |
| `studentSectionAssociations` | `dualCreditTypeDescriptor` | values: Dual Enrollment (post-secondary course in post-secondary setting), Advanced Courses Eligible for College Credit (secondary course in secondary setting), Concurrent Enrollment (post-secondary course in secondary setting) |
| `studentSectionAssociations` | `dualHighSchoolCreditIndicator` | boolean, completion gives high school graduation credit |
| `studentSectionAssociations` | `dualCreditEducationOrganizationReference` | reference to an existing education organization |
| `studentSectionAssociations` | `dualCreditInstitutionDescriptor` | custom descriptor for institutions unknown to Ed-Fi |
| `studentSpecialEducationProgramAssociations` | `shortenedSchoolDayIndicator` | optional |
| `studentSpecialEducationProgramAssociations` | `reductionInHoursPerWeekComparedToPeers` | optional |
| `restraintEvents` | `disciplineIncidentReference` | optional |
| `studentDisciplineIncidentBehaviorAssociations` | `weapons` (`weaponDescriptor`) | Weapon descriptor added |

Dual credit fields are on `studentSectionAssociations`, not `sections`, because students in one section may
differ in credit.

## Removed or changed

- `studentCTEProgramAssociations`: `CTEProgram` common removed.
- `studentSpecialEducationProgramEligibilityAssociations`: role name added for `Program`
  (source: "Adding role name for Program"); `programEducationOrganizationId` is now in the natural key.
- Orphaned data elements removed from the model (elements not named in source).

## Definition-only changes (names unchanged, not breaking)

- Duration properties now state their unit (renaming deferred to a later release):
  `assessmentItems.expectedTimeAssessed`, `learningResources.timeRequired`,
  `studentAssessments` items' `timeAssessed`, `studentInterventionAttendanceEvents.attendanceEventDuration`,
  `studentProgramEvaluations.duration`, `surveyResponses.responseTime`, attendance events `eventDuration`.

## Descriptors

- 19 descriptors: about 110 code values that were deprecated moved to the suggested descriptor values list;
  to be removed in the next data standard version.
- New code values to align with CEDS: `attendanceEventCategoryDescriptor`,
  `charterApprovalAgencyTypeDescriptor`, `credentialTypeDescriptor`, `diplomaTypeDescriptor`.
- New descriptors: `dualCreditTypeDescriptor`, `dualCreditInstitutionDescriptor`,
  `section504DisabilityDescriptor`, `weaponDescriptor`.
