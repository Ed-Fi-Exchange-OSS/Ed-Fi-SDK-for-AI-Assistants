# studentTitleIPartAProgramAssociations

`/ed-fi/studentTitleIPartAProgramAssociations`

This association represents the Title I Part A program(s) that a student participates in or from which the student receives services. The association is a subclass of the GeneralStudentProgramAssociation specifically designed for Title I Part A programs.

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
| `titleIPartAParticipantDescriptor` | yes | descriptor URI | An indication of the type of Title I program, if any, in which the student is participating and by which the student is served. |
| `titleIPartAProgramServices` |  | array of edFi_studentTitleIPartAProgramAssociationTitleIPartAProgramService | An unordered collection of studentTitleIPartAProgramAssociationTitleIPartAProgramServices. |

## Endpoints

- `DELETE /ed-fi/studentTitleIPartAProgramAssociations/{id}`
- `GET /ed-fi/studentTitleIPartAProgramAssociations/deletes`
- `GET /ed-fi/studentTitleIPartAProgramAssociations/keyChanges`
- `GET /ed-fi/studentTitleIPartAProgramAssociations/partitions`
- `GET /ed-fi/studentTitleIPartAProgramAssociations/{id}`
- `GET /ed-fi/studentTitleIPartAProgramAssociations`
- `POST /ed-fi/studentTitleIPartAProgramAssociations`
- `PUT /ed-fi/studentTitleIPartAProgramAssociations/{id}`
