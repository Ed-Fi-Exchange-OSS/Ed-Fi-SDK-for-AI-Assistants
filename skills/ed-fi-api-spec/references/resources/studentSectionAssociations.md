# studentSectionAssociations

`/ed-fi/studentSectionAssociations`

This association indicates the course sections to which a student is assigned.

## Natural key

`beginDate`, `sectionReference`, `studentReference`. The natural key can be changed with PUT (cascading key updates).

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | key | string (date) | Month, day, and year of the student's entry or assignment to the section. |
| `dualCreditEducationOrganizationReference` |  | reference: `educationOrganizationId` |  |
| `sectionReference` | key | reference: `localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `attemptStatusDescriptor` |  | descriptor URI | An indication of the student's completion status for the section. |
| `dualCreditIndicator` |  | boolean | Indicates whether the student assigned to the section is to receive dual credit upon successful completion. |
| `dualCreditInstitutionDescriptor` |  | descriptor URI | Descriptor for the postsecondary institution offering college credit. |
| `dualCreditTypeDescriptor` |  | descriptor URI | For a student taking a dual credit course in a college or high school setting, indicates the type of dual credit program. |
| `dualHighSchoolCreditIndicator` |  | boolean | Indicates whether successful completion of the course will result in credits toward high school graduation. |
| `endDate` |  | string (date) | Month, day, and year of the withdrawal or exit of the student from the section. |
| `homeroomIndicator` |  | boolean | Indicates the section is the student's homeroom. |
| `programs` |  | array of edFi_studentSectionAssociationProgram | An unordered collection of studentSectionAssociationPrograms. |
| `repeatIdentifierDescriptor` |  | descriptor URI | An indication as to whether a student has previously taken a given course. |
| `teacherStudentDataLinkExclusion` |  | boolean | Indicates that the student-section combination is excluded from calculation of value-added or growth attribution calculations used for a particular teacher eva… |

## Endpoints

- `DELETE /ed-fi/studentSectionAssociations/{id}`
- `GET /ed-fi/studentSectionAssociations/deletes`
- `GET /ed-fi/studentSectionAssociations/keyChanges`
- `GET /ed-fi/studentSectionAssociations/partitions`
- `GET /ed-fi/studentSectionAssociations/{id}`
- `GET /ed-fi/studentSectionAssociations`
- `POST /ed-fi/studentSectionAssociations`
- `PUT /ed-fi/studentSectionAssociations/{id}`
