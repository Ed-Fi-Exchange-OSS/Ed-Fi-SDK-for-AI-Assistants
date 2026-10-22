# staffs

`/ed-fi/staffs`

This entity represents an individual who performs specified activities for any public or private education
institution or agency that provides instructional and/or support services to students or staff at the early
childhood level through high school completion.

Also searched as: teacher.

## Natural key

`staffUniqueId`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `staffUniqueId` | key | string max 32 | A unique alphanumeric code assigned to a staff. |
| `personReference` |  | reference: `personId`, `sourceSystemDescriptor` |  |
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

## Endpoints

- `DELETE /ed-fi/staffs/{id}`
- `GET /ed-fi/staffs/deletes`
- `GET /ed-fi/staffs/keyChanges`
- `GET /ed-fi/staffs/partitions`
- `GET /ed-fi/staffs/{id}`
- `GET /ed-fi/staffs`
- `POST /ed-fi/staffs`
- `PUT /ed-fi/staffs/{id}`
