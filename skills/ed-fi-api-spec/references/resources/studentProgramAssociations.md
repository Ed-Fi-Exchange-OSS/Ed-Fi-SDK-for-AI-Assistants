# studentProgramAssociations

`/ed-fi/studentProgramAssociations`

This association represents the program(s) that a student participates in or is served by.

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
| `endDate` |  | string (date) | The month, day, and year on which the student exited the program or stopped receiving services. |
| `programParticipationStatuses` |  | array of edFi_generalStudentProgramAssociationProgramParticipationStatus | An unordered collection of generalStudentProgramAssociationProgramParticipationStatuses. |
| `reasonExitedDescriptor` |  | descriptor URI | The reason the student left the program within a school or district. |
| `servedOutsideOfRegularSession` |  | boolean | Indicates whether the student received services during the summer session or between sessions. |
| `services` |  | array of edFi_studentProgramAssociationService | An unordered collection of studentProgramAssociationServices. |

## Endpoints

- `DELETE /ed-fi/studentProgramAssociations/{id}`
- `GET /ed-fi/studentProgramAssociations/deletes`
- `GET /ed-fi/studentProgramAssociations/keyChanges`
- `GET /ed-fi/studentProgramAssociations/partitions`
- `GET /ed-fi/studentProgramAssociations/{id}`
- `GET /ed-fi/studentProgramAssociations`
- `POST /ed-fi/studentProgramAssociations`
- `PUT /ed-fi/studentProgramAssociations/{id}`
