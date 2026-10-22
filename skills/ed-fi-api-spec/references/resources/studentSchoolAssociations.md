# studentSchoolAssociations

`/ed-fi/studentSchoolAssociations`

This association represents the school in which a student is enrolled. The semantics of enrollment may differ slightly by state. Non-enrollment relationships between a student and an education organization may be described using the StudentEducationOrganizationAssociation.

Also searched as: enrollment.

## Natural key

`entryDate`, `schoolReference`, `studentReference`. The natural key can be changed with PUT (cascading key updates).

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `entryDate` | key | string (date) | The month, day, and year on which an individual enters and begins to receive instructional services in a school for each school year. |
| `calendarReference` |  | reference: `calendarCode`, `schoolId`, `schoolYear` |  |
| `classOfSchoolYearTypeReference` |  | reference: `schoolYear` |  |
| `graduationPlanReference` |  | reference: `educationOrganizationId`, `graduationPlanTypeDescriptor`, `graduationSchoolYear` |  |
| `nextYearSchoolReference` |  | reference: `schoolId` |  |
| `schoolReference` | key | reference: `schoolId` |  |
| `schoolYearTypeReference` |  | reference: `schoolYear` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `alternativeGraduationPlans` |  | array of edFi_studentSchoolAssociationAlternativeGraduationPlan | An unordered collection of studentSchoolAssociationAlternativeGraduationPlans. |
| `educationPlans` |  | array of edFi_studentSchoolAssociationEducationPlan | An unordered collection of studentSchoolAssociationEducationPlans. |
| `employedWhileEnrolled` |  | boolean | An individual who is a paid employee or works in his or her own business, profession, or farm and at the same time is enrolled in secondary, postsecondary, or… |
| `enrollmentTypeDescriptor` |  | descriptor URI | The type of enrollment reflected by the StudentSchoolAssociation. |
| `entryGradeLevelDescriptor` | yes | descriptor URI | The grade level or primary instructional level at which a student enters and receives services in a school or an educational institution during a given academi… |
| `entryGradeLevelReasonDescriptor` |  | descriptor URI | The primary reason as to why a staff member determined that a student should be promoted or not (or be demoted) at the end of a given school term. |
| `entryTypeDescriptor` |  | descriptor URI | The process by which a student enters a school during a given academic session. |
| `exitWithdrawDate` |  | string (date) | The recorded exit or withdraw date for the student. |
| `exitWithdrawTypeDescriptor` |  | descriptor URI | The circumstances under which the student exited from membership in an educational institution. |
| `fullTimeEquivalency` |  | number (double) | The full-time equivalent ratio for the student s assignment to a school for services or instruction. |
| `nextYearGradeLevelDescriptor` |  | descriptor URI | The anticipated grade level for the student for the next school year. |
| `primarySchool` |  | boolean | Indicates if a given enrollment record should be considered the primary record for a student. |
| `repeatGradeIndicator` |  | boolean | An indicator of whether the student is enrolling to repeat a grade level, either by failure or an agreement to hold the student back. |
| `residencyStatusDescriptor` |  | descriptor URI | An indication of the location of a persons legal residence relative to (within or outside of) the boundaries of the public school attended and its administrati… |
| `schoolChoice` |  | boolean | An indication of whether the student enrolled in this school under the provisions for public school choice |
| `schoolChoiceBasisDescriptor` |  | descriptor URI | The legal basis for the school choice enrollment according to local, state or federal policy or regulation. |
| `schoolChoiceTransfer` |  | boolean | An indication of whether students transferred in or out of the school did so during the school year under the provisions for public school choice in accordance… |
| `termCompletionIndicator` |  | boolean | Idicates whether or not a student completed the most recent school term. |

## Endpoints

- `DELETE /ed-fi/studentSchoolAssociations/{id}`
- `GET /ed-fi/studentSchoolAssociations/deletes`
- `GET /ed-fi/studentSchoolAssociations/keyChanges`
- `GET /ed-fi/studentSchoolAssociations/partitions`
- `GET /ed-fi/studentSchoolAssociations/{id}`
- `GET /ed-fi/studentSchoolAssociations`
- `POST /ed-fi/studentSchoolAssociations`
- `PUT /ed-fi/studentSchoolAssociations/{id}`
