# stateEducationAgencies

`/ed-fi/stateEducationAgencies`

This entity represents the agency of the state charged with the primary responsibility for coordinating and
supervising public instruction, including the setting of standards for elementary and secondary instructional
programs.

Also searched as: state agency.

## Natural key

`stateEducationAgencyId`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `categories` | yes | array of edFi_educationOrganizationCategory | An unordered collection of educationOrganizationCategories. |
| `stateEducationAgencyId` | key | integer (int64) | The identifier assigned to a state education agency. |
| `accountabilities` |  | array of edFi_stateEducationAgencyAccountability | An unordered collection of stateEducationAgencyAccountabilities. |
| `addresses` |  | array of edFi_educationOrganizationAddress | An unordered collection of educationOrganizationAddresses. |
| `federalFunds` |  | array of edFi_stateEducationAgencyFederalFunds | An unordered collection of stateEducationAgencyFederalFunds. |
| `identificationCodes` |  | array of edFi_educationOrganizationIdentificationCode | An unordered collection of educationOrganizationIdentificationCodes. |
| `indicators` |  | array of edFi_educationOrganizationIndicator | An unordered collection of educationOrganizationIndicators. |
| `institutionTelephones` |  | array of edFi_educationOrganizationInstitutionTelephone | An unordered collection of educationOrganizationInstitutionTelephones. |
| `internationalAddresses` |  | array of edFi_educationOrganizationInternationalAddress | An unordered collection of educationOrganizationInternationalAddresses. |
| `nameOfInstitution` | yes | string max 75 | The full, legally accepted name of the institution. |
| `operationalStatusDescriptor` |  | descriptor URI | The current operational status of the education organization (e.g., active, inactive). |
| `shortNameOfInstitution` |  | string max 75 | A short name for the institution. |
| `webSite` |  | string max 255 | The public web site address (URL) for the education organization. |

## Endpoints

- `DELETE /ed-fi/stateEducationAgencies/{id}`
- `GET /ed-fi/stateEducationAgencies/deletes`
- `GET /ed-fi/stateEducationAgencies/keyChanges`
- `GET /ed-fi/stateEducationAgencies/partitions`
- `GET /ed-fi/stateEducationAgencies/{id}`
- `GET /ed-fi/stateEducationAgencies`
- `POST /ed-fi/stateEducationAgencies`
- `PUT /ed-fi/stateEducationAgencies/{id}`
