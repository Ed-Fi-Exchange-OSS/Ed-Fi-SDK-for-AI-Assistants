# studentMigrantEducationProgramAssociations

`/ed-fi/studentMigrantEducationProgramAssociations`

This association represents the migrant education program(s) that a student participates in or receives
services from. The association is a subclass of the GeneralStudentProgramAssociation specifically designed for
migrant education programs.

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
| `continuationOfServicesReasonDescriptor` |  | descriptor URI | The "continuation of services" provision found in Section 1304(e) of the statute provides that (1) a child who ceases to be a migratory child during a school t… |
| `eligibilityExpirationDate` |  | string (date) | The eligibility expiration date is used to determine end of eligibility and to account for a child's eligibility expiring earlier than 36 months from the child… |
| `endDate` |  | string (date) | The month, day, and year on which the student exited the program or stopped receiving services. |
| `lastQualifyingMove` | yes | string (date) | Date the last qualifying move occurred; used to compute MEP status. |
| `migrantEducationProgramServices` |  | array of edFi_studentMigrantEducationProgramAssociationMigrantEducationProgramService | An unordered collection of studentMigrantEducationProgramAssociationMigrantEducationProgramServices. |
| `priorityForServices` | yes | boolean | Report migratory children who are classified as having "priority for services" because they are failing, or most at risk of failing to meet the state's challen… |
| `programParticipationStatuses` |  | array of edFi_generalStudentProgramAssociationProgramParticipationStatus | An unordered collection of generalStudentProgramAssociationProgramParticipationStatuses. |
| `qualifyingArrivalDate` |  | string (date) | The qualifying arrival date (QAD) is the date the child joins the worker who has already moved, or the date when the worker joins the child who has already mov… |
| `reasonExitedDescriptor` |  | descriptor URI | The reason the student left the program within a school or district. |
| `servedOutsideOfRegularSession` |  | boolean | Indicates whether the student received services during the summer session or between sessions. |
| `stateResidencyDate` |  | string (date) | The verified state residency for the student. |
| `usInitialEntry` |  | string (date) | The month, day, and year on which the student first entered the U.S. |
| `usInitialSchoolEntry` |  | string (date) | The month, day, and year on which the student first entered a U.S. |
| `usMostRecentEntry` |  | string (date) | The month, day, and year of the student's most recent entry into the U.S. |

### Items in `migrantEducationProgramServices`

| Field | Required | Type | Description |
|---|---|---|---|
| `migrantEducationProgramServiceDescriptor` | yes | descriptor URI | Indicates the service being provided to the student by the migrant education program. |
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

- `GET /ed-fi/studentMigrantEducationProgramAssociations`
- `POST /ed-fi/studentMigrantEducationProgramAssociations`
- `GET /ed-fi/studentMigrantEducationProgramAssociations/deletes`
- `GET /ed-fi/studentMigrantEducationProgramAssociations/keyChanges`
- `GET /ed-fi/studentMigrantEducationProgramAssociations/partitions`
- `GET /ed-fi/studentMigrantEducationProgramAssociations/{id}`
- `PUT /ed-fi/studentMigrantEducationProgramAssociations/{id}`
- `DELETE /ed-fi/studentMigrantEducationProgramAssociations/{id}`
