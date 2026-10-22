# studentHomelessProgramAssociations

`/ed-fi/studentHomelessProgramAssociations`

This association represents the McKinney-Vento Homeless Program program(s) that a student participates in or from which the student receives services. The association is a subclass of the GeneralStudentProgramAssociation specifically designed for homeless programs.

## Natural key

`beginDate`, `educationOrganizationReference`, `programReference`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | key | string (date) | The earliest date the student is involved with the program. |
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `programReference` | key | reference: `educationOrganizationId`, `programName`, `programTypeDescriptor` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `awaitingFosterCare` |  | boolean | State defined definition for awaiting foster care. |
| `endDate` |  | string (date) | The month, day, and year on which the student exited the program or stopped receiving services. |
| `homelessPrimaryNighttimeResidenceDescriptor` |  | descriptor URI | The primary nighttime residence of the student at the time the student is identified as homeless. |
| `homelessProgramServices` |  | array of edFi_studentHomelessProgramAssociationHomelessProgramService | An unordered collection of studentHomelessProgramAssociationHomelessProgramServices. |
| `homelessUnaccompaniedYouth` |  | boolean | A homeless unaccompanied youth is a youth who is not in the physical custody of a parent or guardian and who fits the McKinney-Vento definition of homeless. |
| `programParticipationStatuses` |  | array of edFi_generalStudentProgramAssociationProgramParticipationStatus | An unordered collection of generalStudentProgramAssociationProgramParticipationStatuses. |
| `reasonExitedDescriptor` |  | descriptor URI | The reason the student left the program within a school or district. |
| `servedOutsideOfRegularSession` |  | boolean | Indicates whether the student received services during the summer session or between sessions. |

## Endpoints

- `DELETE /ed-fi/studentHomelessProgramAssociations/{id}`
- `GET /ed-fi/studentHomelessProgramAssociations/deletes`
- `GET /ed-fi/studentHomelessProgramAssociations/keyChanges`
- `GET /ed-fi/studentHomelessProgramAssociations/partitions`
- `GET /ed-fi/studentHomelessProgramAssociations/{id}`
- `GET /ed-fi/studentHomelessProgramAssociations`
- `POST /ed-fi/studentHomelessProgramAssociations`
- `PUT /ed-fi/studentHomelessProgramAssociations/{id}`
