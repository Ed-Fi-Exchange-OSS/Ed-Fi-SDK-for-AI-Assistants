# communityOrganizations

`/ed-fi/communityOrganizations`

This entity represents an administrative unit at the state level which exists primarily to operate local
community providers.

## Natural key

`communityOrganizationId`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `categories` | yes | array of edFi_educationOrganizationCategory | An unordered collection of educationOrganizationCategories. |
| `communityOrganizationId` | key | integer (int64) | The identifier assigned to a community organization. |
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

- `DELETE /ed-fi/communityOrganizations/{id}`
- `GET /ed-fi/communityOrganizations/deletes`
- `GET /ed-fi/communityOrganizations/keyChanges`
- `GET /ed-fi/communityOrganizations/partitions`
- `GET /ed-fi/communityOrganizations/{id}`
- `GET /ed-fi/communityOrganizations`
- `POST /ed-fi/communityOrganizations`
- `PUT /ed-fi/communityOrganizations/{id}`
