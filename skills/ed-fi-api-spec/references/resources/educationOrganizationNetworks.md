# educationOrganizationNetworks

`/ed-fi/educationOrganizationNetworks`

This entity is a self-organized membership network of peer-level education organizations intended to provide
shared services or collective procurement.

## Natural key

`educationOrganizationNetworkId`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `categories` | yes | array of edFi_educationOrganizationCategory | An unordered collection of educationOrganizationCategories. |
| `educationOrganizationNetworkId` | key | integer (int64) | The identifier assigned to a network of education organizations. |
| `addresses` |  | array of edFi_educationOrganizationAddress | An unordered collection of educationOrganizationAddresses. |
| `identificationCodes` |  | array of edFi_educationOrganizationIdentificationCode | An unordered collection of educationOrganizationIdentificationCodes. |
| `indicators` |  | array of edFi_educationOrganizationIndicator | An unordered collection of educationOrganizationIndicators. |
| `institutionTelephones` |  | array of edFi_educationOrganizationInstitutionTelephone | An unordered collection of educationOrganizationInstitutionTelephones. |
| `internationalAddresses` |  | array of edFi_educationOrganizationInternationalAddress | An unordered collection of educationOrganizationInternationalAddresses. |
| `nameOfInstitution` | yes | string max 75 | The full, legally accepted name of the institution. |
| `networkPurposeDescriptor` | yes | descriptor URI | The purpose(s) of the network (e.g., shared services, collective procurement). |
| `operationalStatusDescriptor` |  | descriptor URI | The current operational status of the education organization (e.g., active, inactive). |
| `shortNameOfInstitution` |  | string max 75 | A short name for the institution. |
| `webSite` |  | string max 255 | The public web site address (URL) for the education organization. |

## Endpoints

- `DELETE /ed-fi/educationOrganizationNetworks/{id}`
- `GET /ed-fi/educationOrganizationNetworks/deletes`
- `GET /ed-fi/educationOrganizationNetworks/keyChanges`
- `GET /ed-fi/educationOrganizationNetworks/partitions`
- `GET /ed-fi/educationOrganizationNetworks/{id}`
- `GET /ed-fi/educationOrganizationNetworks`
- `POST /ed-fi/educationOrganizationNetworks`
- `PUT /ed-fi/educationOrganizationNetworks/{id}`
