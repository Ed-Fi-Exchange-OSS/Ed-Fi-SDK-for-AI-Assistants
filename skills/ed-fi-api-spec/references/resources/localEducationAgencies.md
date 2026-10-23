# localEducationAgencies

`/ed-fi/localEducationAgencies`

This entity represents an administrative unit at the local level which exists primarily to operate schools or
to contract for educational services. It includes school districts, charter schools, charter management
organizations, or other local administrative organizations.

Also searched as: district.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `categories` | yes | array of edFi_educationOrganizationCategory | An unordered collection of educationOrganizationCategories. |
| `localEducationAgencyId` | yes | integer (int64) | The identifier assigned to a local education agency. |
| `educationServiceCenterReference` |  | reference; supply `educationServiceCenterId` | This entity represents a regional, multi-services public agency authorized by state law to develop, manage and provide services, programs, or other support opt… |
| `parentLocalEducationAgencyReference` |  | reference; supply `localEducationAgencyId` | This entity represents an administrative unit at the local level which exists primarily to operate schools or to contract for educational services. |
| `stateEducationAgencyReference` |  | reference; supply `stateEducationAgencyId` | This entity represents the agency of the state charged with the primary responsibility for coordinating and supervising public instruction, including the setti… |
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

### Items in `categories`

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationCategoryDescriptor` | yes | descriptor URI | The classification of the education agency within the geographic boundaries of a state according to the level of administrative and operational control granted… |

### Items in `accountabilities`

| Field | Required | Type | Description |
|---|---|---|---|
| `gunFreeSchoolsActReportingStatusDescriptor` |  | descriptor URI | An indication of whether the school or Local Education Agency (LEA) submitted a Gun-Free Schools Act (GFSA) of 1994 report to the state, as defined by Title 18… |
| `schoolChoiceImplementStatusDescriptor` |  | descriptor URI | An indication of whether the LEA was able to implement the provisions for public school choice under Title I, Part A, Section 1116 of ESEA as amended. |
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
| `innovativeDollarsSpent` |  | number (double) | The total Title V, Part A funds expended by LEAs. |
| `innovativeDollarsSpentStrategicPriorities` |  | number (double) | The total amount of Title V, Part A funds expended by LEAs for the four strategic priorities. |
| `innovativeProgramsFundsReceived` |  | number (double) | The total Title V, Part A funds received by LEAs. |
| `schoolImprovementAllocation` |  | number (double) | The amount of Section 1003(a) and 1003(g) allocations to LEAs. |
| `schoolImprovementReservedFundsPercentage` |  | number (double) | An indication of the percentage of the Title I, Part A allocation that the SEA reserved in accordance with Section 1003(a) of ESEA and 200.100(a) of ED's regul… |
| `stateAssessmentAdministrationFunding` |  | number (double) | The percentage of funds used to administer assessments required by Section 1111(b) or to carry out other activities described in Section 6111 and other activit… |
| `supplementalEducationalServicesFundsSpent` |  | number (double) | The dollar amount spent on supplemental educational services during the school year under Title I, Part A, Section 1116 of ESEA as amended. |
| `supplementalEducationalServicesPerPupilExpenditure` |  | number (double) | The maximum dollar amount that may be spent per child for expenditures related to supplemental educational services under Title I of the ESEA. |

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

- `GET /ed-fi/localEducationAgencies`
- `POST /ed-fi/localEducationAgencies`
- `GET /ed-fi/localEducationAgencies/deletes`
- `GET /ed-fi/localEducationAgencies/keyChanges`
- `GET /ed-fi/localEducationAgencies/partitions`
- `GET /ed-fi/localEducationAgencies/{id}`
- `PUT /ed-fi/localEducationAgencies/{id}`
- `DELETE /ed-fi/localEducationAgencies/{id}`
