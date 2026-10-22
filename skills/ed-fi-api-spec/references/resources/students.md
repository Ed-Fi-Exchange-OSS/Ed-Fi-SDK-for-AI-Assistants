# students

`/ed-fi/students`

This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational program under the jurisdiction of a school, education agency or other institution or program. A student is a person who has been enrolled in a school or other educational institution.

## Natural key

`studentUniqueId`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `studentUniqueId` | key | string max 32 | A unique alphanumeric code assigned to a student. |
| `personReference` |  | reference: `personId`, `sourceSystemDescriptor` |  |
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

## Endpoints

- `DELETE /ed-fi/students/{id}`
- `GET /ed-fi/students/deletes`
- `GET /ed-fi/students/keyChanges`
- `GET /ed-fi/students/partitions`
- `GET /ed-fi/students/{id}`
- `GET /ed-fi/students`
- `POST /ed-fi/students`
- `PUT /ed-fi/students/{id}`
