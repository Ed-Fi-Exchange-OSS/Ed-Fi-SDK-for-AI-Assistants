# stateEducationAgencies

`/ed-fi/stateEducationAgencies`

This entity represents the agency of the state charged with the primary responsibility for coordinating and
supervising public instruction, including the setting of standards for elementary and secondary instructional
programs.

Also searched as: state agency.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `categories` | yes | array of edFi_educationOrganizationCategory | An unordered collection of educationOrganizationCategories. |
| `stateEducationAgencyId` | yes | integer (int64) | The identifier assigned to a state education agency. |
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

### Items in `categories`

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationCategoryDescriptor` | yes | descriptor URI | The classification of the education agency within the geographic boundaries of a state according to the level of administrative and operational control granted… |

### Items in `accountabilities`

| Field | Required | Type | Description |
|---|---|---|---|
| `cteGraduationRateInclusion` |  | boolean | An indication of whether CTE concentrators are included in the state's computation of its graduation rate. |
| `schoolYearTypeReference` | yes | reference; supply `schoolYear` | Identifier for a school year. |

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

### Items in `federalFunds`

| Field | Required | Type | Description |
|---|---|---|---|
| `fiscalYear` | yes | integer (int32) | The fiscal year for which the federal funds are received. |
| `federalProgramsFundingAllocation` |  | number (double) | The amount of federal dollars distributed to Local Education Agencies (LEAs), retained by the State Education Agency (SEA) for program administration or other… |

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

## Endpoints

- `GET /ed-fi/stateEducationAgencies`
- `POST /ed-fi/stateEducationAgencies`
- `GET /ed-fi/stateEducationAgencies/deletes`
- `GET /ed-fi/stateEducationAgencies/keyChanges`
- `GET /ed-fi/stateEducationAgencies/partitions`
- `GET /ed-fi/stateEducationAgencies/{id}`
- `PUT /ed-fi/stateEducationAgencies/{id}`
- `DELETE /ed-fi/stateEducationAgencies/{id}`
