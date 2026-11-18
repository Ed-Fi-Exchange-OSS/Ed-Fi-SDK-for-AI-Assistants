# applicantProfiles

`/ed-fi/applicantProfiles`

The profile of the person making an application.

## Natural key

`applicantProfileIdentifier`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `applicantProfileIdentifier` | yes | string max 32 | Identifier assigned to a person making formal application for entrance into a program or an open staff position. |
| `addresses` |  | array of edFi_applicantProfileAddress | An unordered collection of applicantProfileAddresses. |
| `applicantCharacteristics` |  | array of edFi_applicantProfileApplicantCharacteristic | An unordered collection of applicantProfileApplicantCharacteristics. |
| `backgroundChecks` |  | array of edFi_applicantProfileBackgroundCheck | An unordered collection of applicantProfileBackgroundChecks. |
| `birthDate` |  | string (date) | The month, day, and year on which an individual was born. |
| `citizenshipStatusDescriptor` |  | descriptor URI | An indicator of whether or not the person is a U.S. |
| `disabilities` |  | array of edFi_applicantProfileDisability | An unordered collection of applicantProfileDisabilities. |
| `economicDisadvantageDescriptor` |  | descriptor URI | An indication of inadequate financial condition of an individual's family, as determined by family income, number of family members/dependents, participation i… |
| `educatorPreparationProgramNames` |  | array of edFi_applicantProfileEducatorPreparationProgramName | An unordered collection of applicantProfileEducatorPreparationProgramNames. |
| `electronicMails` |  | array of edFi_applicantProfileElectronicMail | An unordered collection of applicantProfileElectronicMails. |
| `firstGenerationStudent` |  | boolean | Indicator of whether individual is a first generation college student. |
| `firstName` | yes | string max 75 | A name given to an individual at birth, baptism, or during another naming ceremony, or through legal change. |
| `genderIdentity` |  | string max 60 | The gender the person identifies themselves as. |
| `generationCodeSuffix` |  | string max 10 | An appendage, if any, used to denote an individual's generation in his family (e.g., Jr., Sr., III). |
| `gradePointAverages` |  | array of edFi_applicantProfileGradePointAverage | An unordered collection of applicantProfileGradePointAverages. |
| `highestCompletedLevelOfEducationDescriptor` |  | descriptor URI | The extent of formal instruction an individual has received. |
| `highlyQualifiedAcademicSubjects` |  | array of edFi_applicantProfileHighlyQualifiedAcademicSubject | An unordered collection of applicantProfileHighlyQualifiedAcademicSubjects. |
| `highlyQualifiedTeacher` |  | boolean | An indication of whether a teacher is classified as highly qualified for his/her assignment according to state definition. |
| `hispanicLatinoEthnicity` |  | boolean | An indication that the individual traces his or her origin or descent to Mexico, Puerto Rico, Cuba, Central, and South America, and other Spanish cultures, reg… |
| `identificationDocuments` |  | array of edFi_applicantProfileIdentificationDocument | An unordered collection of applicantProfileIdentificationDocuments. |
| `internationalAddresses` |  | array of edFi_applicantProfileInternationalAddress | An unordered collection of applicantProfileInternationalAddresses. |
| `languages` |  | array of edFi_applicantProfileLanguage | An unordered collection of applicantProfileLanguages. |
| `lastSurname` | yes | string max 75 | The name borne in common by members of a family. |
| `maidenName` |  | string max 75 | The individual's maiden name. |
| `middleName` |  | string max 75 | A secondary name given to an individual at birth, baptism, or during another naming ceremony. |
| `personalIdentificationDocuments` |  | array of edFi_applicantProfilePersonalIdentificationDocument | An unordered collection of applicantProfilePersonalIdentificationDocuments. |
| `personalTitlePrefix` |  | string max 30 | A prefix used to denote the title, degree, position, or seniority of the individual. |
| `preferredFirstName` |  | string max 75 | The first name the individual prefers, if different from their legal first name |
| `preferredLastSurname` |  | string max 75 | The last name the individual prefers, if different from their legal last name |
| `races` |  | array of edFi_applicantProfileRace | An unordered collection of applicantProfileRaces. |
| `sexDescriptor` |  | descriptor URI | A person's birth sex. |
| `telephones` |  | array of edFi_applicantProfileTelephone | An unordered collection of applicantProfileTelephones. |
| `visas` |  | array of edFi_applicantProfileVisa | An unordered collection of applicantProfileVisas. |
| `yearsOfPriorProfessionalExperience` |  | number (double) | The total number of years that an individual has previously held a similar professional position in one or more education institutions. |
| `yearsOfPriorTeachingExperience` |  | number (double) | The total number of years that an individual has previously held a teaching position in one or more education institutions. |

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
| `characteristics` |  | array of edFi_applicantProfileAddressCharacteristic | An unordered collection of applicantProfileAddressCharacteristics. |
| `periods` |  | array of edFi_applicantProfileAddressPeriod | An unordered collection of applicantProfileAddressPeriods. |

### Items in `applicantCharacteristics`

| Field | Required | Type | Description |
|---|---|---|---|
| `studentCharacteristicDescriptor` | yes | descriptor URI | The characteristic designated for the student applicant. |
| `beginDate` |  | string (date) | The date the characteristic was designated. |
| `designatedBy` |  | string max 60 | The person, organization, or department that designated the characteristic. |
| `endDate` |  | string (date) | The date the characteristic was removed. |

### Items in `backgroundChecks`

| Field | Required | Type | Description |
|---|---|---|---|
| `backgroundCheckTypeDescriptor` | yes | descriptor URI | The type of background check. |
| `backgroundCheckStatusDescriptor` |  | descriptor URI | The status of the background check. |
| `backgroundCheckCompletedDate` |  | string (date) | The date the background check was completed. |
| `backgroundCheckRequestedDate` | yes | string (date) | The date the background check was requested. |
| `fingerprint` |  | boolean | Indicates that a person has or has not completed a fingerprint. |

### Items in `disabilities`

| Field | Required | Type | Description |
|---|---|---|---|
| `disabilityDescriptor` | yes | descriptor URI | A disability category that describes a individual's impairment. |
| `disabilityDeterminationSourceTypeDescriptor` |  | descriptor URI | The source that provided the disability determination. |
| `disabilityDiagnosis` |  | string max 80 | A description of the disability diagnosis. |
| `orderOfDisability` |  | integer (int32) | The order by severity of individual's disabilities: 1- Primary, 2 - Secondary, 3 - Tertiary, etc. |
| `designations` |  | array of edFi_applicantProfileDisabilityDesignation | An unordered collection of applicantProfileDisabilityDesignations. |

### Items in `educatorPreparationProgramNames`

| Field | Required | Type | Description |
|---|---|---|---|
| `educatorPreparationProgramName` | yes | string max 255 | The teacher preparation program(s) completed by the teacher. |

### Items in `electronicMails`

| Field | Required | Type | Description |
|---|---|---|---|
| `electronicMailTypeDescriptor` | yes | descriptor URI | The type of email listed for an individual or organization. |
| `electronicMailAddress` | yes | string max 128 | The electronic mail (e-mail) address listed for an individual or organization. |
| `doNotPublishIndicator` |  | boolean | An indication that the electronic email address should not be published. |
| `primaryEmailAddressIndicator` |  | boolean | An indication that the electronic mail address should be used as the principal electronic mail address for an individual or organization. |

### Items in `gradePointAverages`

| Field | Required | Type | Description |
|---|---|---|---|
| `gradePointAverageTypeDescriptor` | yes | descriptor URI | The system used for calculating the grade point average for an individual. |
| `gradePointAverageValue` | yes | number (double) | The value of the grade points earned divided by the number of credits attempted. |
| `isCumulative` |  | boolean | Indicator of whether or not the Grade Point Average value is cumulative. |
| `maxGradePointAverageValue` |  | number (double) | The maximum value for the grade point average. |

### Items in `highlyQualifiedAcademicSubjects`

| Field | Required | Type | Description |
|---|---|---|---|
| `academicSubjectDescriptor` | yes | descriptor URI | The academic subject(s) in which the staff is deemed to be "highly qualified". |

### Items in `identificationDocuments`

| Field | Required | Type | Description |
|---|---|---|---|
| `identificationDocumentUseDescriptor` | yes | descriptor URI | The primary function of the document used for establishing identity. |
| `personalInformationVerificationDescriptor` | yes | descriptor URI | The category of the document relative to its purpose. |
| `issuerCountryDescriptor` |  | descriptor URI | Country of origin of the document. |
| `documentExpirationDate` |  | string (date) | The day when the document expires, if null then never expires. |
| `documentTitle` |  | string max 60 | The title of the document given by the issuer. |
| `issuerDocumentIdentificationCode` |  | string max 120 | The unique identifier on the issuer's identification system. |
| `issuerName` |  | string max 150 | Name of the entity or institution that issued the document. |

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
| `uses` |  | array of edFi_applicantProfileLanguageUse | An unordered collection of applicantProfileLanguageUses. |

### Items in `personalIdentificationDocuments`

| Field | Required | Type | Description |
|---|---|---|---|
| `identificationDocumentUseDescriptor` | yes | descriptor URI | The primary function of the document used for establishing identity. |
| `personalInformationVerificationDescriptor` | yes | descriptor URI | The category of the document relative to its purpose. |
| `issuerCountryDescriptor` |  | descriptor URI | Country of origin of the document. |
| `documentExpirationDate` |  | string (date) | The day when the document expires, if null then never expires. |
| `documentTitle` |  | string max 60 | The title of the document given by the issuer. |
| `issuerDocumentIdentificationCode` |  | string max 120 | The unique identifier on the issuer's identification system. |
| `issuerName` |  | string max 150 | Name of the entity or institution that issued the document. |

### Items in `races`

| Field | Required | Type | Description |
|---|---|---|---|
| `raceDescriptor` | yes | descriptor URI | The general racial category which most clearly reflects the individual's recognition of his or her community or with which the individual most identifies. |

### Items in `telephones`

| Field | Required | Type | Description |
|---|---|---|---|
| `telephoneNumberTypeDescriptor` | yes | descriptor URI | The type of communication number listed for an individual or organization. |
| `telephoneNumber` | yes | string max 24 | The telephone number including the area code, and extension, if applicable. |
| `doNotPublishIndicator` |  | boolean | An indication that the telephone number should not be published. |
| `orderOfPriority` |  | integer (int32) | The order of priority assigned to telephone numbers to define which number to attempt first, second, etc. |
| `textMessageCapabilityIndicator` |  | boolean | An indication that the telephone number is technically capable of sending and receiving Short Message Service (SMS) text messages. |

### Items in `visas`

| Field | Required | Type | Description |
|---|---|---|---|
| `visaDescriptor` | yes | descriptor URI | An indicator of a non-US citizen's Visa type. |

## Endpoints

- `GET /ed-fi/applicantProfiles`
- `POST /ed-fi/applicantProfiles`
- `GET /ed-fi/applicantProfiles/deletes`
- `GET /ed-fi/applicantProfiles/keyChanges`
- `GET /ed-fi/applicantProfiles/partitions`
- `GET /ed-fi/applicantProfiles/{id}`
- `PUT /ed-fi/applicantProfiles/{id}`
- `DELETE /ed-fi/applicantProfiles/{id}`
