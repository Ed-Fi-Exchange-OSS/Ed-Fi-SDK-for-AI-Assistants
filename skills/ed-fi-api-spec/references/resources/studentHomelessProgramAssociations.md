# studentHomelessProgramAssociations

`/ed-fi/studentHomelessProgramAssociations`

This association represents the McKinney-Vento Homeless Program program(s) that a student participates in or
from which the student receives services. The association is a subclass of the
GeneralStudentProgramAssociation specifically designed for homeless programs.

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
| `awaitingFosterCare` |  | boolean | State defined definition for awaiting foster care. |
| `endDate` |  | string (date) | The month, day, and year on which the student exited the program or stopped receiving services. |
| `homelessPrimaryNighttimeResidenceDescriptor` |  | descriptor URI | The primary nighttime residence of the student at the time the student is identified as homeless. |
| `homelessProgramServices` |  | array of edFi_studentHomelessProgramAssociationHomelessProgramService | An unordered collection of studentHomelessProgramAssociationHomelessProgramServices. |
| `homelessUnaccompaniedYouth` |  | boolean | A homeless unaccompanied youth is a youth who is not in the physical custody of a parent or guardian and who fits the McKinney-Vento definition of homeless. |
| `programParticipationStatuses` |  | array of edFi_generalStudentProgramAssociationProgramParticipationStatus | An unordered collection of generalStudentProgramAssociationProgramParticipationStatuses. |
| `reasonExitedDescriptor` |  | descriptor URI | The reason the student left the program within a school or district. |
| `servedOutsideOfRegularSession` |  | boolean | Indicates whether the student received services during the summer session or between sessions. |

### Items in `homelessProgramServices`

| Field | Required | Type | Description |
|---|---|---|---|
| `homelessProgramServiceDescriptor` | yes | descriptor URI | Indicates the service being provided to the student by the homeless program. |
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

- `GET /ed-fi/studentHomelessProgramAssociations`
- `POST /ed-fi/studentHomelessProgramAssociations`
- `GET /ed-fi/studentHomelessProgramAssociations/deletes`
- `GET /ed-fi/studentHomelessProgramAssociations/keyChanges`
- `GET /ed-fi/studentHomelessProgramAssociations/partitions`
- `GET /ed-fi/studentHomelessProgramAssociations/{id}`
- `PUT /ed-fi/studentHomelessProgramAssociations/{id}`
- `DELETE /ed-fi/studentHomelessProgramAssociations/{id}`
