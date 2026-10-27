# candidates

`/tpdm/candidates`

A candidate is both a person enrolled in a educator preparation program and a candidate to become an educator.

## Natural key

`candidateIdentifier`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `candidateIdentifier` | yes | string max 32 | A unique alphanumeric code assigned to a candidate. |
| `personReference` |  | reference; supply `personId`, `sourceSystemDescriptor` | Reference to person. |
| `addresses` |  | array of tpdm_candidateAddress | An unordered collection of candidateAddresses. |
| `birthCity` |  | string max 30 | The city the student was born in. |
| `birthCountryDescriptor` |  | descriptor URI | The country in which an individual is born. |
| `birthDate` | yes | string (date) | The month, day, and year on which an individual was born. |
| `birthInternationalProvince` |  | string max 150 | For students born outside of the U.S., the Province or jurisdiction in which an individual is born. |
| `birthSexDescriptor` |  | descriptor URI | A person's sex at birth. |
| `birthStateAbbreviationDescriptor` |  | descriptor URI | The abbreviation for the name of the state (within the United States) or extra-state jurisdiction in which an individual was born. |
| `dateEnteredUS` |  | string (date) | For students born outside of the U.S., the date the student entered the U.S. |
| `disabilities` |  | array of tpdm_candidateDisability | An unordered collection of candidateDisabilities. |
| `displacementStatus` |  | string max 30 | Indicates a state health or weather related event that displaces a group of students, and may require additional funding, educational, or social services. |
| `economicDisadvantaged` |  | boolean | An indication of inadequate financial condition of an individual's family, as determined by family income, number of family members/dependents, participation i… |
| `electronicMails` |  | array of tpdm_candidateElectronicMail | An unordered collection of candidateElectronicMails. |
| `englishLanguageExamDescriptor` |  | descriptor URI | Indicates that a person passed, failed, or did not take an English Language assessment (e.g., TOEFFL). |
| `firstGenerationStudent` |  | boolean | Indicator of whether individual is a first generation college student. |
| `firstName` | yes | string max 75 | A name given to an individual at birth, baptism, or during another naming ceremony, or through legal change. |
| `genderDescriptor` |  | descriptor URI | The gender of the candidate. |
| `generationCodeSuffix` |  | string max 10 | An appendage, if any, used to denote an individual's generation in his family (e.g., Jr., Sr., III). |
| `hispanicLatinoEthnicity` |  | boolean | An indication that the individual traces his or her origin or descent to Mexico, Puerto Rico, Cuba, Central, and South America, and other Spanish cultures, reg… |
| `languages` |  | array of tpdm_candidateLanguage | An unordered collection of candidateLanguages. |
| `lastSurname` | yes | string max 75 | The name borne in common by members of a family. |
| `limitedEnglishProficiencyDescriptor` |  | descriptor URI | An indication that the student has been identified as limited English proficient by the Language Proficiency Assessment Committee (LPAC), or English proficient. |
| `maidenName` |  | string max 75 | The individual's maiden name. |
| `middleName` |  | string max 75 | A secondary name given to an individual at birth, baptism, or during another naming ceremony. |
| `multipleBirthStatus` |  | boolean | Indicator of whether the student was born with other siblings (i.e., twins, triplets, etc.) |
| `otherNames` |  | array of tpdm_candidateOtherName | An unordered collection of candidateOtherNames. |
| `personalIdentificationDocuments` |  | array of tpdm_candidatePersonalIdentificationDocument | An unordered collection of candidatePersonalIdentificationDocuments. |
| `personalTitlePrefix` |  | string max 30 | A prefix used to denote the title, degree, position, or seniority of the individual. |
| `preferredFirstName` |  | string max 75 | The first name the individual prefers, if different from their legal first name |
| `preferredLastSurname` |  | string max 75 | The last name the individual prefers, if different from their legal last name |
| `races` |  | array of tpdm_candidateRace | An unordered collection of candidateRaces. |
| `sexDescriptor` |  | descriptor URI | The sex of the candidate. |
| `telephones` |  | array of tpdm_candidateTelephone | An unordered collection of candidateTelephones. |

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
| `periods` |  | array of tpdm_candidateAddressPeriod | An unordered collection of candidateAddressPeriods. |

### Items in `disabilities`

| Field | Required | Type | Description |
|---|---|---|---|
| `disabilityDescriptor` | yes | descriptor URI | A disability category that describes a individual's impairment. |
| `disabilityDeterminationSourceTypeDescriptor` |  | descriptor URI | The source that provided the disability determination. |
| `disabilityDiagnosis` |  | string max 80 | A description of the disability diagnosis. |
| `orderOfDisability` |  | integer (int32) | The order by severity of individual's disabilities: 1- Primary, 2 - Secondary, 3 - Tertiary, etc. |
| `designations` |  | array of tpdm_candidateDisabilityDesignation | An unordered collection of candidateDisabilityDesignations. |

### Items in `electronicMails`

| Field | Required | Type | Description |
|---|---|---|---|
| `electronicMailTypeDescriptor` | yes | descriptor URI | The type of email listed for an individual or organization. |
| `electronicMailAddress` | yes | string max 128 | The electronic mail (e-mail) address listed for an individual or organization. |
| `doNotPublishIndicator` |  | boolean | An indication that the electronic email address should not be published. |
| `primaryEmailAddressIndicator` |  | boolean | An indication that the electronic mail address should be used as the principal electronic mail address for an individual or organization. |

### Items in `languages`

| Field | Required | Type | Description |
|---|---|---|---|
| `languageDescriptor` | yes | descriptor URI | A specification of which written or spoken communication is being used. |
| `uses` |  | array of tpdm_candidateLanguageUse | An unordered collection of candidateLanguageUses. |

### Items in `otherNames`

| Field | Required | Type | Description |
|---|---|---|---|
| `otherNameTypeDescriptor` | yes | descriptor URI | The types of alternate names for an individual. |
| `firstName` | yes | string max 75 | A name given to an individual at birth, baptism, or during another naming ceremony, or through legal change. |
| `generationCodeSuffix` |  | string max 10 | An appendage, if any, used to denote an individual's generation in his family (e.g., Jr., Sr., III). |
| `lastSurname` | yes | string max 75 | The name borne in common by members of a family. |
| `middleName` |  | string max 75 | A secondary name given to an individual at birth, baptism, or during another naming ceremony. |
| `personalTitlePrefix` |  | string max 30 | A prefix used to denote the title, degree, position, or seniority of the individual. |

### Items in `personalIdentificationDocuments`

| Field | Required | Type | Description |
|---|---|---|---|
| `identificationDocumentUseDescriptor` | yes | descriptor URI | The primary function of the document used for establishing identity. |
| `personalInformationVerificationDescriptor` | yes | descriptor URI | The category of the document relative to its purpose. |
| `issuerCountryDescriptor` |  | descriptor URI | Country of origin of the document. |
| `documentExpirationDate` |  | string (date) | The day when the document expires, if null then never expires. |
| `documentTitle` |  | string max 60 | The title of the document given by the issuer. |
| `issuerDocumentIdentificationCode` |  | string max 60 | The unique identifier on the issuer's identification system. |
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

## Endpoints

- `GET /tpdm/candidates`
- `POST /tpdm/candidates`
- `GET /tpdm/candidates/deletes`
- `GET /tpdm/candidates/keyChanges`
- `GET /tpdm/candidates/partitions`
- `GET /tpdm/candidates/{id}`
- `PUT /tpdm/candidates/{id}`
- `DELETE /tpdm/candidates/{id}`
