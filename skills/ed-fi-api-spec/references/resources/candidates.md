# candidates

`/tpdm/candidates`

A candidate is both a person enrolled in a educator preparation program and a candidate to become an educator.

## Natural key

`candidateIdentifier`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `candidateIdentifier` | key | string max 32 | A unique alphanumeric code assigned to a candidate. |
| `personReference` |  | reference: `personId`, `sourceSystemDescriptor` |  |
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

## Endpoints

- `DELETE /tpdm/candidates/{id}`
- `GET /tpdm/candidates/deletes`
- `GET /tpdm/candidates/keyChanges`
- `GET /tpdm/candidates/partitions`
- `GET /tpdm/candidates/{id}`
- `GET /tpdm/candidates`
- `POST /tpdm/candidates`
- `PUT /tpdm/candidates/{id}`
