# schools

`/ed-fi/schools`

This entity represents an educational organization that includes staff and students who participate in classes
and educational activity groups.

## Natural key

`schoolId`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationCategories` | yes | array of edFi_educationOrganizationCategory | An unordered collection of educationOrganizationCategories. |
| `gradeLevels` | yes | array of edFi_schoolGradeLevel | An unordered collection of schoolGradeLevels. |
| `schoolId` | yes | integer (int64) | The identifier assigned to a school. |
| `charterApprovalSchoolYearTypeReference` |  | reference; supply `schoolYear` | Identifier for a school year. |
| `localEducationAgencyReference` |  | reference; supply `localEducationAgencyId` | This entity represents an administrative unit at the local level which exists primarily to operate schools or to contract for educational services. |
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

### Items in `educationOrganizationCategories`

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationCategoryDescriptor` | yes | descriptor URI | The classification of the education agency within the geographic boundaries of a state according to the level of administrative and operational control granted… |

### Items in `gradeLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `gradeLevelDescriptor` | yes | descriptor URI | The grade levels served at the school. |

### Items in `addresses`

| Field | Required | Type | Description |
|---|---|---|---|
| `addressTypeDescriptor` | yes | descriptor URI | The type of address listed for an individual or organization. |
| `stateAbbreviationDescriptor` | yes | descriptor URI | The abbreviation for the state (within the United States) or outlying area in which an address is located. |
| `city` | yes | string max 30 | The name of the city in which an address is located. |
| `postalCode` | yes | string max 17 | The five or nine digit zip code or overseas postal code portion of an address. |
| `streetNumberName` | yes | string max 150 | The street number and street name or post office box number of an address. |
| `localeDescriptor` |  | descriptor URI | A general geographic indicator that categorizes U.S. |
| `apartmentRoomSuiteNumber` |  | string max 50 | The apartment, room, or suite number of an address. |
| `buildingSiteNumber` |  | string max 20 | The number of the building on the site, if more than one building shares the same address. |
| `congressionalDistrict` |  | string max 30 | The congressional district in which an address is located. |
| `countyFIPSCode` |  | string max 5 | The Federal Information Processing Standards (FIPS) numeric code for the county issued by the National Institute of Standards and Technology (NIST). |
| `doNotPublishIndicator` |  | boolean | An indication that the address should not be published. |
| `latitude` |  | string max 20 | The geographic latitude of the physical address. |
| `longitude` |  | string max 20 | The geographic longitude of the physical address. |
| `nameOfCounty` |  | string max 30 | The name of the county, parish, borough, or comparable unit (within a state) in which an address is located. |
| `periods` |  | array of edFi_educationOrganizationAddressPeriod | An unordered collection of educationOrganizationAddressPeriods. |

### Items in `identificationCodes`

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationIdentificationSystemDescriptor` | yes | descriptor URI | The school system, state, or agency assigning the identification code. |
| `identificationCode` | yes | string max 60 | A unique number or alphanumeric code that is assigned to an education organization by a school, school system, state, or other agency or entity. |

### Items in `indicators`

| Field | Required | Type | Description |
|---|---|---|---|
| `indicatorDescriptor` | yes | descriptor URI | The name or code for the indicator or metric. |
| `indicatorGroupDescriptor` |  | descriptor URI | The name for a group of indicators. |
| `indicatorLevelDescriptor` |  | descriptor URI | The value of the indicator or metric, as a value from a controlled vocabulary. |
| `designatedBy` |  | string max 60 | The person, organization, or department that defined the metric. |
| `indicatorValue` |  | string max 60 | The value of the indicator or metric. |
| `periods` |  | array of edFi_educationOrganizationIndicatorPeriod | An unordered collection of educationOrganizationIndicatorPeriods. |

### Items in `institutionTelephones`

| Field | Required | Type | Description |
|---|---|---|---|
| `institutionTelephoneNumberTypeDescriptor` | yes | descriptor URI | The type of communication number listed for an individual or organization. |
| `telephoneNumber` | yes | string max 24 | The telephone number including the area code, and extension, if applicable. |

### Items in `internationalAddresses`

| Field | Required | Type | Description |
|---|---|---|---|
| `addressTypeDescriptor` | yes | descriptor URI | The type of address listed for an individual or organization. |
| `countryDescriptor` | yes | descriptor URI | The name of the country. |
| `addressLine1` | yes | string max 150 | The first line of the address. |
| `addressLine2` |  | string max 150 | The second line of the address. |
| `addressLine3` |  | string max 150 | The third line of the address. |
| `addressLine4` |  | string max 150 | The fourth line of the address. |
| `beginDate` |  | string (date) | The first date the address is valid. |
| `endDate` |  | string (date) | The last date the address is valid. |
| `latitude` |  | string max 20 | The geographic latitude of the physical address. |
| `longitude` |  | string max 20 | The geographic longitude of the physical address. |

### Items in `schoolCategories`

| Field | Required | Type | Description |
|---|---|---|---|
| `schoolCategoryDescriptor` | yes | descriptor URI | The one or more categories of school. |

## Endpoints

- `GET /ed-fi/schools`
- `POST /ed-fi/schools`
- `GET /ed-fi/schools/deletes`
- `GET /ed-fi/schools/keyChanges`
- `GET /ed-fi/schools/partitions`
- `GET /ed-fi/schools/{id}`
- `PUT /ed-fi/schools/{id}`
- `DELETE /ed-fi/schools/{id}`
