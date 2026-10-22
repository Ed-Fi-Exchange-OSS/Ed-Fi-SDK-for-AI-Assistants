# staffEducationOrganizationAssignmentAssociations

`/ed-fi/staffEducationOrganizationAssignmentAssociations`

This association indicates the education organization to which a staff member provides services.

## Natural key

`beginDate`, `staffClassificationDescriptor`, `educationOrganizationReference`, `staffReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | key | string (date) | Month, day, and year of the start or effective date of a staff member's employment, contract, or relationship with the education organization. |
| `staffClassificationDescriptor` | key | descriptor URI | The titles of employment, official status, or rank of education staff. |
| `credentialReference` |  | reference: `credentialIdentifier`, `stateOfIssueStateAbbreviationDescriptor` |  |
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `employmentStaffEducationOrganizationEmploymentAssociationReference` |  | reference: `educationOrganizationId`, `employmentStatusDescriptor`, `hireDate`, `staffUniqueId` |  |
| `staffReference` | key | reference: `staffUniqueId` |  |
| `endDate` |  | string (date) | Month, day, and year of the end or termination date of a staff member's employment, contract, or relationship with the education organization. |
| `fullTimeEquivalency` |  | number (double) | The ratio between the hours of work expected in a position and the hours of work normally expected in a full-time position in the same setting. |
| `orderOfAssignment` |  | integer (int32) | Describes whether the assignment is this the staff member's primary assignment, secondary assignment, etc. |
| `positionTitle` |  | string max 100 | The descriptive name of an individual's position. |

## Endpoints

- `DELETE /ed-fi/staffEducationOrganizationAssignmentAssociations/{id}`
- `GET /ed-fi/staffEducationOrganizationAssignmentAssociations/deletes`
- `GET /ed-fi/staffEducationOrganizationAssignmentAssociations/keyChanges`
- `GET /ed-fi/staffEducationOrganizationAssignmentAssociations/partitions`
- `GET /ed-fi/staffEducationOrganizationAssignmentAssociations/{id}`
- `GET /ed-fi/staffEducationOrganizationAssignmentAssociations`
- `POST /ed-fi/staffEducationOrganizationAssignmentAssociations`
- `PUT /ed-fi/staffEducationOrganizationAssignmentAssociations/{id}`
