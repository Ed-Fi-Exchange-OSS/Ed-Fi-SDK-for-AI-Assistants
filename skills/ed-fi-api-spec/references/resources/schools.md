# schools

`/ed-fi/schools`

This entity represents an educational organization that includes staff and students who participate in classes
and educational activity groups.

## Natural key

`schoolId`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationCategories` | yes | array of edFi_educationOrganizationCategory | An unordered collection of educationOrganizationCategories. |
| `gradeLevels` | yes | array of edFi_schoolGradeLevel | An unordered collection of schoolGradeLevels. |
| `schoolId` | key | integer (int64) | The identifier assigned to a school. |
| `charterApprovalSchoolYearTypeReference` |  | reference: `schoolYear` |  |
| `localEducationAgencyReference` |  | reference: `localEducationAgencyId` |  |
| `addresses` |  | array of edFi_educationOrganizationAddress | An unordered collection of educationOrganizationAddresses. |
| `administrativeFundingControlDescriptor` |  | descriptor URI | The type of education institution as classified by its funding source, for example public or private. |
| `charterApprovalAgencyTypeDescriptor` |  | descriptor URI | The type of agency that approved the establishment or continuation of a charter school. |
| `charterStatusDescriptor` |  | descriptor URI | A school or agency providing free public elementary or secondary education to eligible students under a specific charter granted by the state legislature or ot… |
| `identificationCodes` |  | array of edFi_educationOrganizationIdentificationCode | An unordered collection of educationOrganizationIdentificationCodes. |
| `indicators` |  | array of edFi_educationOrganizationIndicator | An unordered collection of educationOrganizationIndicators. |
| `institutionTelephones` |  | array of edFi_educationOrganizationInstitutionTelephone | An unordered collection of educationOrganizationInstitutionTelephones. |
| `internationalAddresses` |  | array of edFi_educationOrganizationInternationalAddress | An unordered collection of educationOrganizationInternationalAddresses. |
| `internetAccessDescriptor` |  | descriptor URI | The type of Internet access available. |
| `magnetSpecialProgramEmphasisSchoolDescriptor` |  | descriptor URI | A school that has been designed: 1) to attract students of different racial/ethnic backgrounds for the purpose of reducing, preventing, or eliminating racial i… |
| `nameOfInstitution` | yes | string max 75 | The full, legally accepted name of the institution. |
| `operationalStatusDescriptor` |  | descriptor URI | The current operational status of the education organization (e.g., active, inactive). |
| `schoolCategories` |  | array of edFi_schoolCategory | An unordered collection of schoolCategories. |
| `schoolTypeDescriptor` |  | descriptor URI | The type of education institution as classified by its primary focus. |
| `shortNameOfInstitution` |  | string max 75 | A short name for the institution. |
| `titleIPartASchoolDesignationDescriptor` |  | descriptor URI | Denotes the Title I Part A designation for the school. |
| `webSite` |  | string max 255 | The public web site address (URL) for the education organization. |
| `_ext` |  | schoolExtensions |  |

## Endpoints

- `DELETE /ed-fi/schools/{id}`
- `GET /ed-fi/schools/deletes`
- `GET /ed-fi/schools/keyChanges`
- `GET /ed-fi/schools/partitions`
- `GET /ed-fi/schools/{id}`
- `GET /ed-fi/schools`
- `POST /ed-fi/schools`
- `PUT /ed-fi/schools/{id}`
