# studentNeglectedOrDelinquentProgramAssociations

`/ed-fi/studentNeglectedOrDelinquentProgramAssociations`

This association represents the Title I Part D Neglected or Delinquent program(s) that a student participates
in or from which the student receives services. The association is a subclass of the
GeneralStudentProgramAssociation specifically designed for Title I Part D Neglected or Delinquent programs.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | yes | string (date) | The earliest date the student is involved with the program. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `programReference` | yes | reference; supply `educationOrganizationId`, `programName`, `programTypeDescriptor` | This entity represents any program designed to work in conjunction with, or as a supplement to, the main academic program. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `elaProgressLevelDescriptor` |  | descriptor URI | The progress measured from pre- to post- test for ELA. |
| `endDate` |  | string (date) | The month, day, and year on which the student exited the program or stopped receiving services. |
| `mathematicsProgressLevelDescriptor` |  | descriptor URI | The progress measured from pre- to post-test for Mathematics. |
| `neglectedOrDelinquentProgramDescriptor` |  | descriptor URI | The type of program under ESEA Title I, Part D, Subpart 1 (state programs) or Subpart 2 (LEA). |
| `neglectedOrDelinquentProgramServices` |  | array of edFi_studentNeglectedOrDelinquentProgramAssociationNeglectedOrDelinquentProgramService | An unordered collection of studentNeglectedOrDelinquentProgramAssociationNeglectedOrDelinquentProgramServices. |
| `programParticipationStatuses` |  | array of edFi_generalStudentProgramAssociationProgramParticipationStatus | An unordered collection of generalStudentProgramAssociationProgramParticipationStatuses. |
| `reasonExitedDescriptor` |  | descriptor URI | The reason the student left the program within a school or district. |
| `servedOutsideOfRegularSession` |  | boolean | Indicates whether the student received services during the summer session or between sessions. |

### Items in `neglectedOrDelinquentProgramServices`

| Field | Required | Type | Description |
|---|---|---|---|
| `neglectedOrDelinquentProgramServiceDescriptor` | yes | descriptor URI | Indicates the service being provided to the student by the neglected or delinquent program. |
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

- `GET /ed-fi/studentNeglectedOrDelinquentProgramAssociations`
- `POST /ed-fi/studentNeglectedOrDelinquentProgramAssociations`
- `GET /ed-fi/studentNeglectedOrDelinquentProgramAssociations/deletes`
- `GET /ed-fi/studentNeglectedOrDelinquentProgramAssociations/keyChanges`
- `GET /ed-fi/studentNeglectedOrDelinquentProgramAssociations/partitions`
- `GET /ed-fi/studentNeglectedOrDelinquentProgramAssociations/{id}`
- `PUT /ed-fi/studentNeglectedOrDelinquentProgramAssociations/{id}`
- `DELETE /ed-fi/studentNeglectedOrDelinquentProgramAssociations/{id}`
