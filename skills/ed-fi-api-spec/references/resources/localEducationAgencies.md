# localEducationAgencies

`/ed-fi/localEducationAgencies`

This entity represents an administrative unit at the local level which exists primarily to operate schools or
to contract for educational services. It includes school districts, charter schools, charter management
organizations, or other local administrative organizations.

Also searched as: district.

## Natural key

`localEducationAgencyId`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `categories` | yes | array of edFi_educationOrganizationCategory | An unordered collection of educationOrganizationCategories. |
| `localEducationAgencyId` | key | integer (int64) | The identifier assigned to a local education agency. |
| `educationServiceCenterReference` |  | reference: `educationServiceCenterId` |  |
| `parentLocalEducationAgencyReference` |  | reference: `localEducationAgencyId` |  |
| `stateEducationAgencyReference` |  | reference: `stateEducationAgencyId` |  |
| `accountabilities` |  | array of edFi_localEducationAgencyAccountability | An unordered collection of localEducationAgencyAccountabilities. |
| `addresses` |  | array of edFi_educationOrganizationAddress | An unordered collection of educationOrganizationAddresses. |
| `charterStatusDescriptor` |  | descriptor URI | A school or agency providing free public elementary or secondary education to eligible students under a specific charter granted by the state legislature or ot… |
| `federalFunds` |  | array of edFi_localEducationAgencyFederalFunds | An unordered collection of localEducationAgencyFederalFunds. |
| `identificationCodes` |  | array of edFi_educationOrganizationIdentificationCode | An unordered collection of educationOrganizationIdentificationCodes. |
| `indicators` |  | array of edFi_educationOrganizationIndicator | An unordered collection of educationOrganizationIndicators. |
| `institutionTelephones` |  | array of edFi_educationOrganizationInstitutionTelephone | An unordered collection of educationOrganizationInstitutionTelephones. |
| `internationalAddresses` |  | array of edFi_educationOrganizationInternationalAddress | An unordered collection of educationOrganizationInternationalAddresses. |
| `localEducationAgencyCategoryDescriptor` | yes | descriptor URI | The category of local education agency/district. |
| `nameOfInstitution` | yes | string max 75 | The full, legally accepted name of the institution. |
| `operationalStatusDescriptor` |  | descriptor URI | The current operational status of the education organization (e.g., active, inactive). |
| `shortNameOfInstitution` |  | string max 75 | A short name for the institution. |
| `webSite` |  | string max 255 | The public web site address (URL) for the education organization. |

## Endpoints

- `DELETE /ed-fi/localEducationAgencies/{id}`
- `GET /ed-fi/localEducationAgencies/deletes`
- `GET /ed-fi/localEducationAgencies/keyChanges`
- `GET /ed-fi/localEducationAgencies/partitions`
- `GET /ed-fi/localEducationAgencies/{id}`
- `GET /ed-fi/localEducationAgencies`
- `POST /ed-fi/localEducationAgencies`
- `PUT /ed-fi/localEducationAgencies/{id}`
