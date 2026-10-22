# contacts

`/ed-fi/contacts`

This entity represents a contact of a student, such as a parent, guardian or caretaker.

Also searched as: parent, guardian.

## Natural key

`contactUniqueId`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `contactUniqueId` | key | string max 32 | A unique alphanumeric code assigned to a contact. |
| `personReference` |  | reference: `personId`, `sourceSystemDescriptor` |  |
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

## Endpoints

- `DELETE /ed-fi/contacts/{id}`
- `GET /ed-fi/contacts/deletes`
- `GET /ed-fi/contacts/keyChanges`
- `GET /ed-fi/contacts/partitions`
- `GET /ed-fi/contacts/{id}`
- `GET /ed-fi/contacts`
- `POST /ed-fi/contacts`
- `PUT /ed-fi/contacts/{id}`
