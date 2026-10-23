# staffEducationOrganizationEmploymentAssociations

`/ed-fi/staffEducationOrganizationEmploymentAssociations`

This association indicates the education organization an employee, contractor, volunteer, or other service
provider is formally associated with typically indicated by which organization the staff member has a services
contract with or receives compensation from.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `employmentStatusDescriptor` | yes | descriptor URI | Reflects the type of employment or contract. |
| `hireDate` | yes | string (date) | The month, day, and year on which an individual was hired for a position. |
| `credentialReference` |  | reference; supply `credentialIdentifier`, `stateOfIssueStateAbbreviationDescriptor` | The legal document giving authorization to perform teaching assignment services. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `staffReference` | yes | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |
| `annualWage` |  | number (double) | Annual wage associated with the employment position being reported. |
| `department` |  | string max 60 | The department or suborganization the employee/contractor is associated with in the education organization. |
| `endDate` |  | string (date) | The month, day, and year on which a contract between an individual and a governing authority ends or is terminated under the provisions of the contract (or the… |
| `fullTimeEquivalency` |  | number (double) | The ratio between the hours of work expected in a position and the hours of work normally expected in a full-time position in the same setting. |
| `hourlyWage` |  | number (double) | Hourly wage associated with the employment position being reported. |
| `offerDate` |  | string (date) | Date at which the staff member was made an official offer for this employment. |
| `separationDescriptor` |  | descriptor URI | Type of employment separation. |
| `separationReasonDescriptor` |  | descriptor URI | Reason for terminating the employment. |

## Endpoints

- `GET /ed-fi/staffEducationOrganizationEmploymentAssociations`
- `POST /ed-fi/staffEducationOrganizationEmploymentAssociations`
- `GET /ed-fi/staffEducationOrganizationEmploymentAssociations/deletes`
- `GET /ed-fi/staffEducationOrganizationEmploymentAssociations/keyChanges`
- `GET /ed-fi/staffEducationOrganizationEmploymentAssociations/partitions`
- `GET /ed-fi/staffEducationOrganizationEmploymentAssociations/{id}`
- `PUT /ed-fi/staffEducationOrganizationEmploymentAssociations/{id}`
- `DELETE /ed-fi/staffEducationOrganizationEmploymentAssociations/{id}`
