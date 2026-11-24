# studentProgramAssociations

`/ed-fi/studentProgramAssociations`

This association represents the program(s) that a student participates in or is served by.

## Natural key

`beginDate`, `educationOrganizationId`, `programEducationOrganizationId`, `programName`,
`programTypeDescriptor`, `studentUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | yes | string (date) | The earliest date the student is involved with the program. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `programReference` | yes | reference; supply `educationOrganizationId`, `programName`, `programTypeDescriptor` | This entity represents any program designed to work in conjunction with, or as a supplement to, the main academic program. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `endDate` |  | string (date) | The month, day, and year on which the student exited the program or stopped receiving services. |
| `programParticipationStatuses` |  | array of edFi_generalStudentProgramAssociationProgramParticipationStatus | An unordered collection of generalStudentProgramAssociationProgramParticipationStatuses. |
| `reasonExitedDescriptor` |  | descriptor URI | The reason the student left the program within a school or district. |
| `servedOutsideOfRegularSession` |  | boolean | Indicates whether the student received services during the summer session or between sessions. |
| `services` |  | array of edFi_studentProgramAssociationService | An unordered collection of studentProgramAssociationServices. |

### Items in `programParticipationStatuses`

| Field | Required | Type | Description |
|---|---|---|---|
| `participationStatusDescriptor` | yes | descriptor URI | The student's program participation status. |
| `statusBeginDate` | yes | string (date) | The date the student's program participation status began. |
| `designatedBy` |  | string max 60 | The person, organization, or department that designated the participation status. |
| `statusEndDate` |  | string (date) | The date the student's program participation status ended. |

### Items in `services`

| Field | Required | Type | Description |
|---|---|---|---|
| `serviceDescriptor` | yes | descriptor URI | Indicates the service being provided to the student by the program. |
| `primaryIndicator` |  | boolean | True if service is a primary service. |
| `serviceBeginDate` |  | string (date) | First date the student was in this option for the current school year. |
| `serviceEndDate` |  | string (date) | Last date the student was in this option for the current school year. |

## Endpoints

- `GET /ed-fi/studentProgramAssociations`
- `POST /ed-fi/studentProgramAssociations`
- `GET /ed-fi/studentProgramAssociations/deletes`
- `GET /ed-fi/studentProgramAssociations/keyChanges`
- `GET /ed-fi/studentProgramAssociations/partitions`
- `GET /ed-fi/studentProgramAssociations/{id}`
- `PUT /ed-fi/studentProgramAssociations/{id}`
- `DELETE /ed-fi/studentProgramAssociations/{id}`
