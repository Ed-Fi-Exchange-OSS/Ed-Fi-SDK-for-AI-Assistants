# What's New - v5.0

Scope: Data Standard 4.0 -> 5.0 changes. Breaking: B. Everything else non-breaking. Domains with
breaking changes are: alternative and supplemental services (federal programs), discipline, enrollment,
graduation, intervention, student academic record, student attendance, student cohort, student identification
and demographics, survey, teaching and learning. It does not itemize which fields were removed.

## Added resources

- `studentSpecialEducationProgramEligibilityAssociations`: new association, fields below.
- Student Program Evaluation model: `studentProgramEvaluations`, `programEvaluations`,
  `programEvaluationObjectives`, `programEvaluationElements`, `evaluationRubricDimensions`. The source
  gives no field detail; read each resource file.

### studentSpecialEducationProgramEligibilityAssociations fields

R = required, O = optional. Names as in the API; the source names are the same without the `Descriptor` suffix.

| Field | R/O | Meaning |
|---|---|---|
| `educationOrganizationReference` | R | Where the student was evaluated (school or district) |
| `studentReference` | R | Student evaluated |
| `programReference` | R | Program evaluated for, e.g. Special Education Program |
| `consentToEvaluationReceivedDate` | R | LEA received written parental consent; first day of evaluation timeframe |
| `ideaPartDescriptor` | R | Part B or Part C IDEA |
| `eligibilityEvaluationTypeDescriptor` | R | Initial or reevaluation |
| `originalECIServicesDate` | O | Began early childhood intervention (ECI), birth through age 2 |
| `consentToEvaluationDate` | O | Parent consent date |
| `evaluationCompleteIndicator` | O | Evaluation completed (true/false) |
| `eligibilityEvaluationDate` | O | Written individual evaluation report completed |
| `evaluationDelayReasonDescriptor` | O | Why report was completed beyond the state timeframe |
| `evaluationLateReason` | O | Free text, additional delay information |
| `evaluationDelayDays` | O | Student absences from first instructional day after consent |
| `eligibilityDeterminationDate` | O | Admission, review, and dismissal committee meeting date on eligibility |
| `ideaIndicator` | O | Determined eligible as a result of the evaluation |
| `eligibilityDelayReasonDescriptor` | O | Why determination was beyond the required timeframe |
| `transitionNotificationDate` | O | ECI contractor sent LEA notification of potential Part B eligibility |
| `transitionConferenceDate` | O | Transition conference date (ECI lead agency, family, LEA) |
| `eligibilityConferenceDate` | O | Eligibility conference date (parents/guardians and responsible staff) |

## Renamed (B)

- Parent domain entity -> Contact: `parents` -> `contacts`, `studentParentAssociations` ->
  `studentContactAssociations`. The source says the rename also updates name and definition of the survey
  response entity (`surveyResponses`) and the student identification and demographics domain, without
  listing fields. Check `contacts`, `studentContactAssociations`, `staffEducationOrganizationContactAssociations`
  and `surveyResponses`.

## Added fields

| Resource | Field | Type / notes |
|---|---|---|
| `studentSpecialEducationProgramAssociations` | `specialEducationExitDate` | date, optional |
| | `specialEducationExitReasonDescriptor` | descriptor, optional; 7 predefined categories |
| | `specialEducationExitExplained` | string, optional; long explanation of exit |
| Name common (`students`, `staffs`, `contacts`, `candidates`) | `preferredFirstName`, `preferredLastName` | optional |
| `studentSchoolAssociations` | `nextYearSchoolReference` | school, optional (source: NextYearSchool number) |
| | `nextYearGradeLevelDescriptor` | descriptor |
| | `schoolChoice` | boolean |
| | `schoolChoiceBasisDescriptor` | descriptor |
| | `enrollmentTypeDescriptor` | descriptor |
| `gradingPeriods` | `gradingPeriodName` | required (B) |
| `staffEducationOrganizationEmploymentAssociations` | `annualWage` | optional |
| `studentEducationOrganizationAssociations` | `supporterMilitaryConnectionDescriptor` | optional; values Active Duty, Reserve, Veteran, DoD Civilian, Not Military Connected, Unknown |

The source also adds a Gender Identity string, described as "added to the core model". In 5.2 it is
`genderIdentity` on `contacts`, `staffs` and `studentEducationOrganizationAssociations`. The Sex descriptor
definition and where it is collected were updated.

## Changed fields

| Resource | Change |
|---|---|
| `gradingPeriods` | `gradingPeriodName` replaces `periodSequence` in the natural key, which is now `gradingPeriodDescriptor`, `gradingPeriodName`, `schoolId`, `schoolYear` (B). Every grading period reference changes (`grades`, `gradebookEntries`, ...). `gradingPeriodDescriptor` is now the SEA-predefined name. `periodSequence` required -> optional |
| `staffSectionAssociations` | `beginDate` is now part of the identity (natural key) (B) |
| `courseTranscripts` | `earnedCredit` required -> optional |
| `studentSchoolAttendanceEvents` | `eventDuration`: minimum and maximum constraints added |
| `letterGradeEarned` (resource not named in source) | maximum length 20 -> 64 |
| Session and Term | definitions updated only |

The source says the Section model was updated (scheduling vs. attempted credits, grades and responsible
teacher) with no further detail. The ticket title "Change schoolId from int32 to varchar 30 or int64" is
listed but no outcome is stated.

## Deprecated

- `studentSchoolAssociations.schoolChoiceTransfer`: deprecated, removal scheduled for Data Standard 7.0.

## Removed (B)

- Previously deprecated elements (more than two dozen, since Suite 2 to Suite 3) were removed. The source does
  not list them. Removal policy: deprecated elements are removed in the same breaking year of the next
  Break-Break-Rest cycle, together with their sample data.
