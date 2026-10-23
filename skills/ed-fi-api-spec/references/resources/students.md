# students

`/ed-fi/students`

This entity represents an individual for whom instruction, services, and/or care are provided in an early
childhood, elementary, or secondary educational program under the jurisdiction of a school, education agency
or other institution or program. A student is a person who has been enrolled in a school or other educational
institution.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `studentUniqueId` | yes | string max 32 | A unique alphanumeric code assigned to a student. |
| `personReference` |  | reference; supply `personId`, `sourceSystemDescriptor` | Reference to person. |
| `birthCity` |  | string max 30 | The city the student was born in. |
| `birthCountryDescriptor` |  | descriptor URI | The country in which an individual is born. |
| `birthDate` | yes | string (date) | The month, day, and year on which an individual was born. |
| `birthInternationalProvince` |  | string max 150 | For students born outside of the U.S., the Province or jurisdiction in which an individual is born. |
| `birthSexDescriptor` |  | descriptor URI | A person's sex at birth. |
| `birthStateAbbreviationDescriptor` |  | descriptor URI | The abbreviation for the name of the state (within the United States) or extra-state jurisdiction in which an individual was born. |
| `citizenshipStatusDescriptor` |  | descriptor URI | An indicator of whether or not the person is a U.S. |
| `dateEnteredUS` |  | string (date) | For students born outside of the U.S., the date the student entered the U.S. |
| `firstName` | yes | string max 75 | A name given to an individual at birth, baptism, or during another naming ceremony, or through legal change. |
| `generationCodeSuffix` |  | string max 10 | An appendage, if any, used to denote an individual's generation in his family (e.g., Jr., Sr., III). |
| `identificationDocuments` |  | array of edFi_studentIdentificationDocument | An unordered collection of studentIdentificationDocuments. |
| `lastSurname` | yes | string max 75 | The name borne in common by members of a family. |
| `maidenName` |  | string max 75 | The individual's maiden name. |
| `middleName` |  | string max 75 | A secondary name given to an individual at birth, baptism, or during another naming ceremony. |
| `multipleBirthStatus` |  | boolean | Indicator of whether the student was born with other siblings (i.e., twins, triplets, etc.) |
| `otherNames` |  | array of edFi_studentOtherName | An unordered collection of studentOtherNames. |
| `personalIdentificationDocuments` |  | array of edFi_studentPersonalIdentificationDocument | An unordered collection of studentPersonalIdentificationDocuments. |
| `personalTitlePrefix` |  | string max 30 | A prefix used to denote the title, degree, position, or seniority of the individual. |
| `preferredFirstName` |  | string max 75 | The first name the individual prefers, if different from their legal first name |
| `preferredLastSurname` |  | string max 75 | The last name the individual prefers, if different from their legal last name |
| `visas` |  | array of edFi_studentVisa | An unordered collection of studentVisas. |

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

### Items in `visas`

| Field | Required | Type | Description |
|---|---|---|---|
| `visaDescriptor` | yes | descriptor URI | An indicator of a non-US citizen's Visa type. |

## Endpoints

- `GET /ed-fi/students`
- `POST /ed-fi/students`
- `GET /ed-fi/students/deletes`
- `GET /ed-fi/students/keyChanges`
- `GET /ed-fi/students/partitions`
- `GET /ed-fi/students/{id}`
- `PUT /ed-fi/students/{id}`
- `DELETE /ed-fi/students/{id}`
