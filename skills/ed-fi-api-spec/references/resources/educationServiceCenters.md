# educationServiceCenters

`/ed-fi/educationServiceCenters`

This entity represents a regional, multi-services public agency authorized by state law to develop, manage and provide services, programs, or other support options (e.g., construction, food services, and technology services) to LEAs.

## Natural key

`educationServiceCenterId`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `categories` | yes | array of edFi_educationOrganizationCategory | An unordered collection of educationOrganizationCategories. |
| `educationServiceCenterId` | key | integer (int64) | The identifier assigned to an education service center. |
| `stateEducationAgencyReference` |  | reference: `stateEducationAgencyId` |  |
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

- `DELETE /ed-fi/educationServiceCenters/{id}`
- `GET /ed-fi/educationServiceCenters/deletes`
- `GET /ed-fi/educationServiceCenters/keyChanges`
- `GET /ed-fi/educationServiceCenters/partitions`
- `GET /ed-fi/educationServiceCenters/{id}`
- `GET /ed-fi/educationServiceCenters`
- `POST /ed-fi/educationServiceCenters`
- `PUT /ed-fi/educationServiceCenters/{id}`
