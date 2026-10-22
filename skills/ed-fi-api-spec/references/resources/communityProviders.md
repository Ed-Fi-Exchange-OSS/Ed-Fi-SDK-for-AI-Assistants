# communityProviders

`/ed-fi/communityProviders`

This entity represents an educational organization that includes staff and students who participate in classes and educational activity groups.

## Natural key

`communityProviderId`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `categories` | yes | array of edFi_educationOrganizationCategory | An unordered collection of educationOrganizationCategories. |
| `communityProviderId` | key | integer (int64) | The identifier assigned to a community provider. |
| `communityOrganizationReference` |  | reference: `communityOrganizationId` |  |
| `addresses` |  | array of edFi_educationOrganizationAddress | An unordered collection of educationOrganizationAddresses. |
| `identificationCodes` |  | array of edFi_educationOrganizationIdentificationCode | An unordered collection of educationOrganizationIdentificationCodes. |
| `indicators` |  | array of edFi_educationOrganizationIndicator | An unordered collection of educationOrganizationIndicators. |
| `institutionTelephones` |  | array of edFi_educationOrganizationInstitutionTelephone | An unordered collection of educationOrganizationInstitutionTelephones. |
| `internationalAddresses` |  | array of edFi_educationOrganizationInternationalAddress | An unordered collection of educationOrganizationInternationalAddresses. |
| `licenseExemptIndicator` |  | boolean | An indication of whether the provider is exempt from having a license. |
| `nameOfInstitution` | yes | string max 75 | The full, legally accepted name of the institution. |
| `operationalStatusDescriptor` |  | descriptor URI | The current operational status of the education organization (e.g., active, inactive). |
| `providerCategoryDescriptor` | yes | descriptor URI | Indicates the category of the provider. |
| `providerProfitabilityDescriptor` |  | descriptor URI | Indicates the profitability status of the provider. |
| `providerStatusDescriptor` | yes | descriptor URI | Indicates the status of the provider. |
| `schoolIndicator` |  | boolean | An indication of whether the community provider is a school. |
| `shortNameOfInstitution` |  | string max 75 | A short name for the institution. |
| `webSite` |  | string max 255 | The public web site address (URL) for the education organization. |

## Endpoints

- `DELETE /ed-fi/communityProviders/{id}`
- `GET /ed-fi/communityProviders/deletes`
- `GET /ed-fi/communityProviders/keyChanges`
- `GET /ed-fi/communityProviders/partitions`
- `GET /ed-fi/communityProviders/{id}`
- `GET /ed-fi/communityProviders`
- `POST /ed-fi/communityProviders`
- `PUT /ed-fi/communityProviders/{id}`
