# studentSectionAssociations

`/ed-fi/studentSectionAssociations`

This association indicates the course sections to which a student is assigned.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | yes | string (date) | Month, day, and year of the student's entry or assignment to the section. |
| `dualCreditEducationOrganizationReference` |  | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `sectionReference` | yes | reference; supply `localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName` | This entity represents a setting in which organized instruction of course content is provided, in-person or otherwise, to one or more students for a given peri… |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
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

### Items in `programs`

| Field | Required | Type | Description |
|---|---|---|---|
| `programReference` | yes | reference; supply `educationOrganizationId`, `programName`, `programTypeDescriptor` | This entity represents any program designed to work in conjunction with, or as a supplement to, the main academic program. |

## Endpoints

- `GET /ed-fi/studentSectionAssociations`
- `POST /ed-fi/studentSectionAssociations`
- `GET /ed-fi/studentSectionAssociations/deletes`
- `GET /ed-fi/studentSectionAssociations/keyChanges`
- `GET /ed-fi/studentSectionAssociations/partitions`
- `GET /ed-fi/studentSectionAssociations/{id}`
- `PUT /ed-fi/studentSectionAssociations/{id}`
- `DELETE /ed-fi/studentSectionAssociations/{id}`
