# studentNeglectedOrDelinquentProgramAssociations

`/ed-fi/studentNeglectedOrDelinquentProgramAssociations`

This association represents the Title I Part D Neglected or Delinquent program(s) that a student participates in or from which the student receives services. The association is a subclass of the GeneralStudentProgramAssociation specifically designed for Title I Part D Neglected or Delinquent programs.

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
| `elaProgressLevelDescriptor` |  | descriptor URI | The progress measured from pre- to post- test for ELA. |
| `endDate` |  | string (date) | The month, day, and year on which the student exited the program or stopped receiving services. |
| `mathematicsProgressLevelDescriptor` |  | descriptor URI | The progress measured from pre- to post-test for Mathematics. |
| `neglectedOrDelinquentProgramDescriptor` |  | descriptor URI | The type of program under ESEA Title I, Part D, Subpart 1 (state programs) or Subpart 2 (LEA). |
| `neglectedOrDelinquentProgramServices` |  | array of edFi_studentNeglectedOrDelinquentProgramAssociationNeglectedOrDelinquentProgramService | An unordered collection of studentNeglectedOrDelinquentProgramAssociationNeglectedOrDelinquentProgramServices. |
| `programParticipationStatuses` |  | array of edFi_generalStudentProgramAssociationProgramParticipationStatus | An unordered collection of generalStudentProgramAssociationProgramParticipationStatuses. |
| `reasonExitedDescriptor` |  | descriptor URI | The reason the student left the program within a school or district. |
| `servedOutsideOfRegularSession` |  | boolean | Indicates whether the student received services during the summer session or between sessions. |

## Endpoints

- `DELETE /ed-fi/studentNeglectedOrDelinquentProgramAssociations/{id}`
- `GET /ed-fi/studentNeglectedOrDelinquentProgramAssociations/deletes`
- `GET /ed-fi/studentNeglectedOrDelinquentProgramAssociations/keyChanges`
- `GET /ed-fi/studentNeglectedOrDelinquentProgramAssociations/partitions`
- `GET /ed-fi/studentNeglectedOrDelinquentProgramAssociations/{id}`
- `GET /ed-fi/studentNeglectedOrDelinquentProgramAssociations`
- `POST /ed-fi/studentNeglectedOrDelinquentProgramAssociations`
- `PUT /ed-fi/studentNeglectedOrDelinquentProgramAssociations/{id}`
