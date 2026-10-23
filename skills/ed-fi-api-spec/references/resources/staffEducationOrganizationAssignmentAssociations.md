# staffEducationOrganizationAssignmentAssociations

`/ed-fi/staffEducationOrganizationAssignmentAssociations`

This association indicates the education organization to which a staff member provides services.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | yes | string (date) | Month, day, and year of the start or effective date of a staff member's employment, contract, or relationship with the education organization. |
| `staffClassificationDescriptor` | yes | descriptor URI | The titles of employment, official status, or rank of education staff. |
| `credentialReference` |  | reference; supply `credentialIdentifier`, `stateOfIssueStateAbbreviationDescriptor` | The legal document giving authorization to perform teaching assignment services. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `employmentStaffEducationOrganizationEmploymentAssociationReference` |  | reference; supply `educationOrganizationId`, `employmentStatusDescriptor`, `hireDate`, `staffUniqueId` | This association indicates the education organization an employee, contractor, volunteer, or other service provider is formally associated with typically indic… |
| `staffReference` | yes | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |
| `endDate` |  | string (date) | Month, day, and year of the end or termination date of a staff member's employment, contract, or relationship with the education organization. |
| `fullTimeEquivalency` |  | number (double) | The ratio between the hours of work expected in a position and the hours of work normally expected in a full-time position in the same setting. |
| `orderOfAssignment` |  | integer (int32) | Describes whether the assignment is this the staff member's primary assignment, secondary assignment, etc. |
| `positionTitle` |  | string max 100 | The descriptive name of an individual's position. |

## Endpoints

- `GET /ed-fi/staffEducationOrganizationAssignmentAssociations`
- `POST /ed-fi/staffEducationOrganizationAssignmentAssociations`
- `GET /ed-fi/staffEducationOrganizationAssignmentAssociations/deletes`
- `GET /ed-fi/staffEducationOrganizationAssignmentAssociations/keyChanges`
- `GET /ed-fi/staffEducationOrganizationAssignmentAssociations/partitions`
- `GET /ed-fi/staffEducationOrganizationAssignmentAssociations/{id}`
- `PUT /ed-fi/staffEducationOrganizationAssignmentAssociations/{id}`
- `DELETE /ed-fi/staffEducationOrganizationAssignmentAssociations/{id}`
