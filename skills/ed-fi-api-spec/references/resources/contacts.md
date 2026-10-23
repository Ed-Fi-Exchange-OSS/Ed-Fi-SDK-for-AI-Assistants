# contacts

`/ed-fi/contacts`

This entity represents a contact of a student, such as a parent, guardian or caretaker.

Also searched as: parent, guardian.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `contactUniqueId` | yes | string max 32 | A unique alphanumeric code assigned to a contact. |
| `personReference` |  | reference; supply `personId`, `sourceSystemDescriptor` | Reference to person. |
| `addresses` |  | array of edFi_contactAddress | An unordered collection of contactAddresses. |
| `electronicMails` |  | array of edFi_contactElectronicMail | An unordered collection of contactElectronicMails. |
| `firstName` | yes | string max 75 | A name given to an individual at birth, baptism, or during another naming ceremony, or through legal change. |
| `genderIdentity` |  | string max 60 | The gender the contact identifies themselves as. |
| `generationCodeSuffix` |  | string max 10 | An appendage, if any, used to denote an individual's generation in his family (e.g., Jr., Sr., III). |
| `highestCompletedLevelOfEducationDescriptor` |  | descriptor URI | The extent of formal instruction an individual has received (e.g., the highest grade in school completed or its equivalent or the highest degree received). |
| `internationalAddresses` |  | array of edFi_contactInternationalAddress | An unordered collection of contactInternationalAddresses. |
| `languages` |  | array of edFi_contactLanguage | An unordered collection of contactLanguages. |
| `lastSurname` | yes | string max 75 | The name borne in common by members of a family. |
| `loginId` |  | string max 60 | The login ID for the user; used for security access control interface. |
| `maidenName` |  | string max 75 | The individual's maiden name. |
| `middleName` |  | string max 75 | A secondary name given to an individual at birth, baptism, or during another naming ceremony. |
| `otherNames` |  | array of edFi_contactOtherName | An unordered collection of contactOtherNames. |
| `personalIdentificationDocuments` |  | array of edFi_contactPersonalIdentificationDocument | An unordered collection of contactPersonalIdentificationDocuments. |
| `personalTitlePrefix` |  | string max 30 | A prefix used to denote the title, degree, position, or seniority of the individual. |
| `preferredFirstName` |  | string max 75 | The first name the individual prefers, if different from their legal first name |
| `preferredLastSurname` |  | string max 75 | The last name the individual prefers, if different from their legal last name |
| `sexDescriptor` |  | descriptor URI | A person's birth sex. |
| `telephones` |  | array of edFi_contactTelephone | An unordered collection of contactTelephones. |

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
| `periods` |  | array of edFi_contactAddressPeriod | An unordered collection of contactAddressPeriods. |

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
| `uses` |  | array of edFi_contactLanguageUse | An unordered collection of contactLanguageUses. |

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

### Items in `telephones`

| Field | Required | Type | Description |
|---|---|---|---|
| `telephoneNumberTypeDescriptor` | yes | descriptor URI | The type of communication number listed for an individual or organization. |
| `telephoneNumber` | yes | string max 24 | The telephone number including the area code, and extension, if applicable. |
| `doNotPublishIndicator` |  | boolean | An indication that the telephone number should not be published. |
| `orderOfPriority` |  | integer (int32) | The order of priority assigned to telephone numbers to define which number to attempt first, second, etc. |
| `textMessageCapabilityIndicator` |  | boolean | An indication that the telephone number is technically capable of sending and receiving Short Message Service (SMS) text messages. |

## Endpoints

- `GET /ed-fi/contacts`
- `POST /ed-fi/contacts`
- `GET /ed-fi/contacts/deletes`
- `GET /ed-fi/contacts/keyChanges`
- `GET /ed-fi/contacts/partitions`
- `GET /ed-fi/contacts/{id}`
- `PUT /ed-fi/contacts/{id}`
- `DELETE /ed-fi/contacts/{id}`
