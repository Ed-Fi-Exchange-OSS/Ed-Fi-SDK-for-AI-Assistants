# staffs

`/ed-fi/staffs`

This entity represents an individual who performs specified activities for any public or private education
institution or agency that provides instructional and/or support services to students or staff at the early
childhood level through high school completion.

Also searched as: teacher.

## Natural key

`staffUniqueId`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `staffUniqueId` | yes | string max 32 | A unique alphanumeric code assigned to a staff. |
| `personReference` |  | reference; supply `personId`, `sourceSystemDescriptor` | Reference to person. |
| `addresses` |  | array of edFi_staffAddress | An unordered collection of staffAddresses. |
| `ancestryEthnicOrigins` |  | array of edFi_staffAncestryEthnicOrigin | An unordered collection of staffAncestryEthnicOrigins. |
| `birthDate` |  | string (date) | The month, day, and year on which an individual was born. |
| `citizenshipStatusDescriptor` |  | descriptor URI | An indicator of whether or not the person is a U.S. |
| `credentials` |  | array of edFi_staffCredential | An unordered collection of staffCredentials. |
| `electronicMails` |  | array of edFi_staffElectronicMail | An unordered collection of staffElectronicMails. |
| `firstName` | yes | string max 75 | A name given to an individual at birth, baptism, or during another naming ceremony, or through legal change. |
| `genderIdentity` |  | string max 60 | The gender the staff member identifies themselves as. |
| `generationCodeSuffix` |  | string max 10 | An appendage, if any, used to denote an individual's generation in his family (e.g., Jr., Sr., III). |
| `highestCompletedLevelOfEducationDescriptor` |  | descriptor URI | The extent of formal instruction an individual has received (e.g., the highest grade in school completed or its equivalent or the highest degree received). |
| `highlyQualifiedTeacher` |  | boolean | An indication of whether a teacher is classified as highly qualified for his/her assignment according to state definition. |
| `hispanicLatinoEthnicity` |  | boolean | An indication that the individual traces his or her origin or descent to Mexico, Puerto Rico, Cuba, Central, and South America, and other Spanish cultures, reg… |
| `identificationCodes` |  | array of edFi_staffIdentificationCode | An unordered collection of staffIdentificationCodes. |
| `identificationDocuments` |  | array of edFi_staffIdentificationDocument | An unordered collection of staffIdentificationDocuments. |
| `internationalAddresses` |  | array of edFi_staffInternationalAddress | An unordered collection of staffInternationalAddresses. |
| `languages` |  | array of edFi_staffLanguage | An unordered collection of staffLanguages. |
| `lastSurname` | yes | string max 75 | The name borne in common by members of a family. |
| `loginId` |  | string max 60 | The login ID for the user; used for security access control interface. |
| `maidenName` |  | string max 75 | The individual's maiden name. |
| `middleName` |  | string max 75 | A secondary name given to an individual at birth, baptism, or during another naming ceremony. |
| `otherNames` |  | array of edFi_staffOtherName | An unordered collection of staffOtherNames. |
| `personalIdentificationDocuments` |  | array of edFi_staffPersonalIdentificationDocument | An unordered collection of staffPersonalIdentificationDocuments. |
| `personalTitlePrefix` |  | string max 30 | A prefix used to denote the title, degree, position, or seniority of the individual. |
| `preferredFirstName` |  | string max 75 | The first name the individual prefers, if different from their legal first name |
| `preferredLastSurname` |  | string max 75 | The last name the individual prefers, if different from their legal last name |
| `races` |  | array of edFi_staffRace | An unordered collection of staffRaces. |
| `recognitions` |  | array of edFi_staffRecognition | An unordered collection of staffRecognitions. |
| `sexDescriptor` |  | descriptor URI | The birth sex of the staff member. |
| `telephones` |  | array of edFi_staffTelephone | An unordered collection of staffTelephones. |
| `tribalAffiliations` |  | array of edFi_staffTribalAffiliation | An unordered collection of staffTribalAffiliations. |
| `visas` |  | array of edFi_staffVisa | An unordered collection of staffVisas. |
| `yearsOfPriorProfessionalExperience` |  | number (double) | The total number of years that an individual has previously held a similar professional position in one or more education institutions prior to the current sch… |
| `yearsOfPriorTeachingExperience` |  | number (double) | The total number of years that an individual has previously held a teaching position in one or more education institutions prior to the current school year. |

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
| `periods` |  | array of edFi_staffAddressPeriod | An unordered collection of staffAddressPeriods. |

### Items in `ancestryEthnicOrigins`

| Field | Required | Type | Description |
|---|---|---|---|
| `ancestryEthnicOriginDescriptor` | yes | descriptor URI | The original peoples or cultures with which the individual identifies. |

### Items in `credentials`

| Field | Required | Type | Description |
|---|---|---|---|
| `credentialReference` | yes | reference; supply `credentialIdentifier`, `stateOfIssueStateAbbreviationDescriptor` | The legal document giving authorization to perform teaching assignment services. |

### Items in `electronicMails`

| Field | Required | Type | Description |
|---|---|---|---|
| `electronicMailTypeDescriptor` | yes | descriptor URI | The type of email listed for an individual or organization. |
| `electronicMailAddress` | yes | string max 128 | The electronic mail (e-mail) address listed for an individual or organization. |
| `doNotPublishIndicator` |  | boolean | An indication that the electronic email address should not be published. |
| `primaryEmailAddressIndicator` |  | boolean | An indication that the electronic mail address should be used as the principal electronic mail address for an individual or organization. |

### Items in `identificationCodes`

| Field | Required | Type | Description |
|---|---|---|---|
| `staffIdentificationSystemDescriptor` | yes | descriptor URI | A coding scheme that is used for identification and record-keeping purposes by schools, social services, or other agencies to refer to a staff member. |
| `assigningOrganizationIdentificationCode` |  | string max 60 | The organization code or name assigning the staff Identification Code. |
| `identificationCode` | yes | string max 60 | A unique number or alphanumeric code assigned to a staff member by a school, school system, a state, or other agency or entity. |

### Items in `identificationDocuments`

| Field | Required | Type | Description |
|---|---|---|---|
| `identificationDocumentUseDescriptor` | yes | descriptor URI | The primary function of the document used for establishing identity. |
| `personalInformationVerificationDescriptor` | yes | descriptor URI | The category of the document relative to its purpose. |
| `issuerCountryDescriptor` |  | descriptor URI | Country of origin of the document. |
| `documentExpirationDate` |  | string (date) | The day when the document expires, if null then never expires. |
| `documentTitle` |  | string max 60 | The title of the document given by the issuer. |
| `issuerDocumentIdentificationCode` |  | string max 60 | The unique identifier on the issuer's identification system. |
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
| `uses` |  | array of edFi_staffLanguageUse | An unordered collection of staffLanguageUses. |

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

### Items in `recognitions`

| Field | Required | Type | Description |
|---|---|---|---|
| `recognitionTypeDescriptor` | yes | descriptor URI | The nature of recognition given to the individual for accomplishments in a co-curricular, or extra-curricular activity. |
| `achievementCategoryDescriptor` |  | descriptor URI | The category of achievement attributed to the individual. |
| `achievementCategorySystem` |  | string max 60 | The system that defines the categories by which an achievement is attributed to the individual. |
| `achievementTitle` |  | string max 60 | The title assigned to the achievement. |
| `criteria` |  | string max 150 | The criteria for competency-based completion of the achievement/award. |
| `criteriaURL` |  | string max 255 | The Uniform Resource Locator (URL) for the unique address of a web page describing the competency-based completion criteria for the achievement/award. |
| `evidenceStatement` |  | string max 150 | A statement or reference describing the evidence that the individual met the criteria for attainment of the achievement/award. |
| `imageURL` |  | string max 255 | The Uniform Resource Locator (URL) for the unique address of an image representing an award or badge associated with the achievement/award. |
| `issuerName` |  | string max 150 | The name of the agent, entity, or institution issuing the element. |
| `issuerOriginURL` |  | string max 255 | The Uniform Resource Locator (URL) from which the award was issued. |
| `recognitionAwardDate` |  | string (date) | The date the recognition was awarded or earned. |
| `recognitionAwardExpiresDate` |  | string (date) | Date on which the recognition expires. |
| `recognitionDescription` |  | string max 80 | A description of the type of recognition earned by or awarded to the individual. |

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
| `tribalAffiliationDescriptor` | yes | descriptor URI | An American Indian tribe with which the staff member is affiliated. |

### Items in `visas`

| Field | Required | Type | Description |
|---|---|---|---|
| `visaDescriptor` | yes | descriptor URI | An indicator of a non-US citizen's Visa type. |

## Endpoints

- `GET /ed-fi/staffs`
- `POST /ed-fi/staffs`
- `GET /ed-fi/staffs/deletes`
- `GET /ed-fi/staffs/keyChanges`
- `GET /ed-fi/staffs/partitions`
- `GET /ed-fi/staffs/{id}`
- `PUT /ed-fi/staffs/{id}`
- `DELETE /ed-fi/staffs/{id}`
