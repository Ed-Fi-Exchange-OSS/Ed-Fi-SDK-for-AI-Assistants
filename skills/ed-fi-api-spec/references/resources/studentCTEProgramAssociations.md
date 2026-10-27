# studentCTEProgramAssociations

`/ed-fi/studentCTEProgramAssociations`

This association represents the career and technical education (CTE) program that a student participates in.
The association is a subclass of the GeneralStudentProgramAssociation specifically designed for CTE programs.

## Natural key

`beginDate`, `educationOrganizationId`, `programEducationOrganizationId`, `programName`,
`programTypeDescriptor`, `studentUniqueId`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | yes | string (date) | The earliest date the student is involved with the program. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `programReference` | yes | reference; supply `educationOrganizationId`, `programName`, `programTypeDescriptor` | This entity represents any program designed to work in conjunction with, or as a supplement to, the main academic program. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `cteProgramServices` |  | array of edFi_studentCTEProgramAssociationCTEProgramService | An unordered collection of studentCTEProgramAssociationCTEProgramServices. |
| `endDate` |  | string (date) | The month, day, and year on which the student exited the program or stopped receiving services. |
| `nonTraditionalGenderStatus` |  | boolean | Indicator that student is from a gender group that comprises less than 25% of the individuals employed in an occupation or field of work. |
| `privateCTEProgram` |  | boolean | Indicator that student participated in career and technical education at private agencies or institutions that are reported by the state for purposes of the El… |
| `programParticipationStatuses` |  | array of edFi_generalStudentProgramAssociationProgramParticipationStatus | An unordered collection of generalStudentProgramAssociationProgramParticipationStatuses. |
| `reasonExitedDescriptor` |  | descriptor URI | The reason the student left the program within a school or district. |
| `servedOutsideOfRegularSession` |  | boolean | Indicates whether the student received services during the summer session or between sessions. |
| `technicalSkillsAssessmentDescriptor` |  | descriptor URI | Results of technical skills assessment aligned with industry recognized standards. |

### Items in `cteProgramServices`

| Field | Required | Type | Description |
|---|---|---|---|
| `cteProgramServiceDescriptor` | yes | descriptor URI | Indicates the service being provided to the student by the CTE program. |
| `cipCode` |  | string max 120 | Number and description of the CIP code associated with the student's CTE program. |
| `primaryIndicator` |  | boolean | True if service is a primary service. |
| `serviceBeginDate` |  | string (date) | First date the student was in this option for the current school year. |
| `serviceEndDate` |  | string (date) | Last date the student was in this option for the current school year. |

### Items in `programParticipationStatuses`

| Field | Required | Type | Description |
|---|---|---|---|
| `participationStatusDescriptor` | yes | descriptor URI | The student's program participation status. |
| `statusBeginDate` | yes | string (date) | The date the student's program participation status began. |
| `designatedBy` |  | string max 60 | The person, organization, or department that designated the participation status. |
| `statusEndDate` |  | string (date) | The date the student's program participation status ended. |

## Endpoints

- `GET /ed-fi/studentCTEProgramAssociations`
- `POST /ed-fi/studentCTEProgramAssociations`
- `GET /ed-fi/studentCTEProgramAssociations/deletes`
- `GET /ed-fi/studentCTEProgramAssociations/keyChanges`
- `GET /ed-fi/studentCTEProgramAssociations/partitions`
- `GET /ed-fi/studentCTEProgramAssociations/{id}`
- `PUT /ed-fi/studentCTEProgramAssociations/{id}`
- `DELETE /ed-fi/studentCTEProgramAssociations/{id}`
