# studentMigrantEducationProgramAssociations

`/ed-fi/studentMigrantEducationProgramAssociations`

This association represents the migrant education program(s) that a student participates in or receives services from. The association is a subclass of the GeneralStudentProgramAssociation specifically designed for migrant education programs.

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

## Endpoints

- `DELETE /ed-fi/studentMigrantEducationProgramAssociations/{id}`
- `GET /ed-fi/studentMigrantEducationProgramAssociations/deletes`
- `GET /ed-fi/studentMigrantEducationProgramAssociations/keyChanges`
- `GET /ed-fi/studentMigrantEducationProgramAssociations/partitions`
- `GET /ed-fi/studentMigrantEducationProgramAssociations/{id}`
- `GET /ed-fi/studentMigrantEducationProgramAssociations`
- `POST /ed-fi/studentMigrantEducationProgramAssociations`
- `PUT /ed-fi/studentMigrantEducationProgramAssociations/{id}`
