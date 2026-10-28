# studentEducationOrganizationAssociations

`/ed-fi/studentEducationOrganizationAssociations`

This association represents student information as reported in the context of the student's relationship to
the education organization. Enrollment relationship semantics are covered by StudentSchoolAssociation.

## Natural key

`educationOrganizationId`, `studentUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `addresses` |  | array of edFi_studentEducationOrganizationAssociationAddress | An unordered collection of studentEducationOrganizationAssociationAddresses. |
| `ancestryEthnicOrigins` |  | array of edFi_studentEducationOrganizationAssociationAncestryEthnicOrigin | An unordered collection of studentEducationOrganizationAssociationAncestryEthnicOrigins. |
| `barrierToInternetAccessInResidenceDescriptor` |  | descriptor URI | An indication of the barrier to having internet access in the student s primary place of residence. |
| `cohortYears` |  | array of edFi_studentEducationOrganizationAssociationCohortYear | An unordered collection of studentEducationOrganizationAssociationCohortYears. |
| `disabilities` |  | array of edFi_studentEducationOrganizationAssociationDisability | An unordered collection of studentEducationOrganizationAssociationDisabilities. |
| `displacedStudents` |  | array of edFi_studentEducationOrganizationAssociationDisplacedStudent | An unordered collection of studentEducationOrganizationAssociationDisplacedStudents. |
| `electronicMails` |  | array of edFi_studentEducationOrganizationAssociationElectronicMail | An unordered collection of studentEducationOrganizationAssociationElectronicMails. |
| `genderIdentity` |  | string max 60 | The student's gender as last reported to the education organization. |
| `hispanicLatinoEthnicity` |  | boolean | An indication that the individual traces his or her origin or descent to Mexico, Puerto Rico, Cuba, Central, and South America, and other Spanish cultures, reg… |
| `internationalAddresses` |  | array of edFi_studentEducationOrganizationAssociationInternationalAddress | An unordered collection of studentEducationOrganizationAssociationInternationalAddresses. |
| `internetAccessInResidence` |  | boolean | An indication of whether the student is able to access the internet in their primary place of residence. |
| `internetAccessTypeInResidenceDescriptor` |  | descriptor URI | The primary type of internet service used in the student s primary place of residence. |
| `internetPerformanceInResidenceDescriptor` |  | descriptor URI | An indication of whether the student can complete the full range of learning activities, including video streaming and assignment upload, without interruptions… |
| `languages` |  | array of edFi_studentEducationOrganizationAssociationLanguage | An unordered collection of studentEducationOrganizationAssociationLanguages. |
| `limitedEnglishProficiencyDescriptor` |  | descriptor URI | An indication that the student has been identified as limited English proficient by the Language Proficiency Assessment Committee (LPAC), or English proficient. |
| `loginId` |  | string max 60 | The login ID for the user; used for security access control interface. |
| `primaryLearningDeviceAccessDescriptor` |  | descriptor URI | An indication of whether the primary learning device is shared or not shared with another individual. |
| `primaryLearningDeviceAwayFromSchoolDescriptor` |  | descriptor URI | The type of device the student uses most often to complete learning activities away from school. |
| `primaryLearningDeviceProviderDescriptor` |  | descriptor URI | The provider of the primary learning device. |
| `profileThumbnail` |  | string max 255 | Locator reference for the student photo. |
| `races` |  | array of edFi_studentEducationOrganizationAssociationRace | An unordered collection of studentEducationOrganizationAssociationRaces. |
| `sexDescriptor` |  | descriptor URI | The student's birth sex as reported to the education organization. |
| `studentCharacteristics` |  | array of edFi_studentEducationOrganizationAssociationStudentCharacteristic | An unordered collection of studentEducationOrganizationAssociationStudentCharacteristics. |
| `studentIdentificationCodes` |  | array of edFi_studentEducationOrganizationAssociationStudentIdentificationCode | An unordered collection of studentEducationOrganizationAssociationStudentIdentificationCodes. |
| `studentIndicators` |  | array of edFi_studentEducationOrganizationAssociationStudentIndicator | An unordered collection of studentEducationOrganizationAssociationStudentIndicators. |
| `supporterMilitaryConnectionDescriptor` |  | descriptor URI | Military connection of the person/people whom the student is a dependent of. |
| `telephones` |  | array of edFi_studentEducationOrganizationAssociationTelephone | An unordered collection of studentEducationOrganizationAssociationTelephones. |
| `tribalAffiliations` |  | array of edFi_studentEducationOrganizationAssociationTribalAffiliation | An unordered collection of studentEducationOrganizationAssociationTribalAffiliations. |

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
| `periods` |  | array of edFi_studentEducationOrganizationAssociationAddressPeriod | An unordered collection of studentEducationOrganizationAssociationAddressPeriods. |

### Items in `ancestryEthnicOrigins`

| Field | Required | Type | Description |
|---|---|---|---|
| `ancestryEthnicOriginDescriptor` | yes | descriptor URI | The original peoples or cultures with which the individual identifies. |

### Items in `cohortYears`

| Field | Required | Type | Description |
|---|---|---|---|
| `cohortYearTypeDescriptor` | yes | descriptor URI | The type of cohort year (9th grade, graduation). |
| `termDescriptor` |  | descriptor URI | The term associated with the cohort year; for example, the intended term of graduation. |
| `schoolYearTypeReference` | yes | reference; supply `schoolYear` | Identifier for a school year. |

### Items in `disabilities`

| Field | Required | Type | Description |
|---|---|---|---|
| `disabilityDescriptor` | yes | descriptor URI | A disability category that describes a individual's impairment. |
| `disabilityDeterminationSourceTypeDescriptor` |  | descriptor URI | The source that provided the disability determination. |
| `disabilityDiagnosis` |  | string max 80 | A description of the disability diagnosis. |
| `orderOfDisability` |  | integer (int32) | The order by severity of individual's disabilities: 1- Primary, 2 - Secondary, 3 - Tertiary, etc. |
| `designations` |  | array of edFi_studentEducationOrganizationAssociationDisabilityDesignation | An unordered collection of studentEducationOrganizationAssociationDisabilityDesignations. |

### Items in `displacedStudents`

| Field | Required | Type | Description |
|---|---|---|---|
| `displacedStudentStatusDescriptor` | yes | descriptor URI | Indicates whether a student has been displaced as a result of a crisis event. |
| `crisisHomelessnessIndicator` |  | boolean | Any student considered homeless (defined by the McKinney-Vento Homeless Education Assistance Act as lacking a fixed, regular, and adequate nighttime residence)… |
| `displacedStudentEndDate` |  | string (date) | The date marking the end of the period during which a student is considered displaced due to a crisis event. |
| `displacedStudentStartDate` |  | string (date) | The date on which a student is officially identified as displaced due to a crisis event. |
| `crisisEventReference` | yes | reference; supply `crisisEventName` | A natural or man-made event that causes the disruption of school-level activities and the temporary or permanent displacement of students. |

### Items in `electronicMails`

| Field | Required | Type | Description |
|---|---|---|---|
| `electronicMailTypeDescriptor` | yes | descriptor URI | The type of email listed for an individual or organization. |
| `electronicMailAddress` | yes | string max 128 | The electronic mail (e-mail) address listed for an individual or organization. |
| `doNotPublishIndicator` |  | boolean | An indication that the electronic email address should not be published. |
| `primaryEmailAddressIndicator` |  | boolean | An indication that the electronic mail address should be used as the principal electronic mail address for an individual or organization. |

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

### Items in `languages`

| Field | Required | Type | Description |
|---|---|---|---|
| `languageDescriptor` | yes | descriptor URI | A specification of which written or spoken communication is being used. |
| `uses` |  | array of edFi_studentEducationOrganizationAssociationLanguageUse | An unordered collection of studentEducationOrganizationAssociationLanguageUses. |

### Items in `races`

| Field | Required | Type | Description |
|---|---|---|---|
| `raceDescriptor` | yes | descriptor URI | The general racial category which most clearly reflects the individual's recognition of his or her community or with which the individual most identifies as la… |

### Items in `studentCharacteristics`

| Field | Required | Type | Description |
|---|---|---|---|
| `studentCharacteristicDescriptor` | yes | descriptor URI | The characteristic designated for the student. |
| `designatedBy` |  | string max 60 | The person, organization, or department that designated the characteristic. |
| `periods` |  | array of edFi_studentEducationOrganizationAssociationStudentCharacteristicPeriod | An unordered collection of studentEducationOrganizationAssociationStudentCharacteristicPeriods. |

### Items in `studentIdentificationCodes`

| Field | Required | Type | Description |
|---|---|---|---|
| `studentIdentificationSystemDescriptor` | yes | descriptor URI | A coding scheme that is used for identification and record-keeping purposes by schools, social services, or other agencies to refer to a student. |
| `assigningOrganizationIdentificationCode` | yes | string max 60 | The organization code or name assigning the StudentIdentificationCode. |
| `identificationCode` | yes | string max 60 | A unique number or alphanumeric code assigned to a student by a school, school system, a state, or other agency or entity. |

### Items in `studentIndicators`

| Field | Required | Type | Description |
|---|---|---|---|
| `indicatorName` | yes | string max 200 | The name of the indicator or metric. |
| `designatedBy` |  | string max 60 | The person, organization, or department that designated the program association. |
| `indicator` | yes | string max 60 | The value of the indicator or metric. |
| `indicatorGroup` |  | string max 200 | The name for a group of indicators. |
| `periods` |  | array of edFi_studentEducationOrganizationAssociationStudentIndicatorPeriod | An unordered collection of studentEducationOrganizationAssociationStudentIndicatorPeriods. |

### Items in `telephones`

| Field | Required | Type | Description |
|---|---|---|---|
| `telephoneNumberTypeDescriptor` | yes | descriptor URI | The type of communication number listed for an individual or organization. |
| `telephoneNumber` | yes | string max 24 | The telephone number including the area code, and extension, if applicable. |
| `doNotPublishIndicator` |  | boolean | An indication that the telephone number should not be published. |
| `orderOfPriority` |  | integer (int32) | The order of priority assigned to telephone numbers to define which number to attempt first, second, etc. |
| `textMessageCapabilityIndicator` |  | boolean | An indication that the telephone number is technically capable of sending and receiving Short Message Service (SMS) text messages. |

### Items in `tribalAffiliations`

| Field | Required | Type | Description |
|---|---|---|---|
| `tribalAffiliationDescriptor` | yes | descriptor URI | An American Indian tribe with which the student is affiliated as last reported to the education organization. |

## Endpoints

- `GET /ed-fi/studentEducationOrganizationAssociations`
- `POST /ed-fi/studentEducationOrganizationAssociations`
- `GET /ed-fi/studentEducationOrganizationAssociations/deletes`
- `GET /ed-fi/studentEducationOrganizationAssociations/keyChanges`
- `GET /ed-fi/studentEducationOrganizationAssociations/partitions`
- `GET /ed-fi/studentEducationOrganizationAssociations/{id}`
- `PUT /ed-fi/studentEducationOrganizationAssociations/{id}`
- `DELETE /ed-fi/studentEducationOrganizationAssociations/{id}`
