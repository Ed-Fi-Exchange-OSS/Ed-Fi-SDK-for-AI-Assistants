# postSecondaryInstitutions

`/ed-fi/postSecondaryInstitutions`

An organization that provides educational programs for individuals who have completed or otherwise left
educational programs in secondary school(s).

## Natural key

`postSecondaryInstitutionId`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `categories` | yes | array of edFi_educationOrganizationCategory | An unordered collection of educationOrganizationCategories. |
| `postSecondaryInstitutionId` | key | integer (int64) | The ID of the post secondary institution. |
| `addresses` |  | array of edFi_educationOrganizationAddress | An unordered collection of educationOrganizationAddresses. |
| `administrativeFundingControlDescriptor` |  | descriptor URI | A classification of whether a postsecondary institution is operated by publicly elected or appointed officials (public control) or by privately elected or appo… |
| `identificationCodes` |  | array of edFi_educationOrganizationIdentificationCode | An unordered collection of educationOrganizationIdentificationCodes. |
| `indicators` |  | array of edFi_educationOrganizationIndicator | An unordered collection of educationOrganizationIndicators. |
| `institutionTelephones` |  | array of edFi_educationOrganizationInstitutionTelephone | An unordered collection of educationOrganizationInstitutionTelephones. |
| `internationalAddresses` |  | array of edFi_educationOrganizationInternationalAddress | An unordered collection of educationOrganizationInternationalAddresses. |
| `mediumOfInstructions` |  | array of edFi_postSecondaryInstitutionMediumOfInstruction | An unordered collection of postSecondaryInstitutionMediumOfInstructions. |
| `nameOfInstitution` | yes | string max 75 | The full, legally accepted name of the institution. |
| `operationalStatusDescriptor` |  | descriptor URI | The current operational status of the education organization (e.g., active, inactive). |
| `postSecondaryInstitutionLevelDescriptor` |  | descriptor URI | A classification of whether a post secondary institution's highest level of offering is a program of 4-years or higher (4 year), 2-but-less-than 4-years (2 yea… |
| `shortNameOfInstitution` |  | string max 75 | A short name for the institution. |
| `webSite` |  | string max 255 | The public web site address (URL) for the education organization. |

## Endpoints

- `DELETE /ed-fi/postSecondaryInstitutions/{id}`
- `GET /ed-fi/postSecondaryInstitutions/deletes`
- `GET /ed-fi/postSecondaryInstitutions/keyChanges`
- `GET /ed-fi/postSecondaryInstitutions/partitions`
- `GET /ed-fi/postSecondaryInstitutions/{id}`
- `GET /ed-fi/postSecondaryInstitutions`
- `POST /ed-fi/postSecondaryInstitutions`
- `PUT /ed-fi/postSecondaryInstitutions/{id}`
