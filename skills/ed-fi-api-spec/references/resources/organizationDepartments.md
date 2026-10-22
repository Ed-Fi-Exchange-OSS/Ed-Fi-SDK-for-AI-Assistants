# organizationDepartments

`/ed-fi/organizationDepartments`

An organizational unit of another education organization, often devoted to a particular academic discipline, area of study, or organization function.

## Natural key

`organizationDepartmentId`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `categories` | yes | array of edFi_educationOrganizationCategory | An unordered collection of educationOrganizationCategories. |
| `organizationDepartmentId` | key | integer (int64) | The unique identification code for the organization department. |
| `parentEducationOrganizationReference` |  | reference: `educationOrganizationId` |  |
| `academicSubjectDescriptor` |  | descriptor URI | The intended major subject area of the department. |
| `addresses` |  | array of edFi_educationOrganizationAddress | An unordered collection of educationOrganizationAddresses. |
| `identificationCodes` |  | array of edFi_educationOrganizationIdentificationCode | An unordered collection of educationOrganizationIdentificationCodes. |
| `indicators` |  | array of edFi_educationOrganizationIndicator | An unordered collection of educationOrganizationIndicators. |
| `institutionTelephones` |  | array of edFi_educationOrganizationInstitutionTelephone | An unordered collection of educationOrganizationInstitutionTelephones. |
| `internationalAddresses` |  | array of edFi_educationOrganizationInternationalAddress | An unordered collection of educationOrganizationInternationalAddresses. |
| `nameOfInstitution` | yes | string max 75 | The full, legally accepted name of the institution. |
| `operationalStatusDescriptor` |  | descriptor URI | The current operational status of the education organization (e.g., active, inactive). |
| `shortNameOfInstitution` |  | string max 75 | A short name for the institution. |
| `webSite` |  | string max 255 | The public web site address (URL) for the education organization. |

## Endpoints

- `DELETE /ed-fi/organizationDepartments/{id}`
- `GET /ed-fi/organizationDepartments/deletes`
- `GET /ed-fi/organizationDepartments/keyChanges`
- `GET /ed-fi/organizationDepartments/partitions`
- `GET /ed-fi/organizationDepartments/{id}`
- `GET /ed-fi/organizationDepartments`
- `POST /ed-fi/organizationDepartments`
- `PUT /ed-fi/organizationDepartments/{id}`
