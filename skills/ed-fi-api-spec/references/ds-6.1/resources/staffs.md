# staffs

`/ed-fi/staffs`

This entity represents an individual who performs specified activities for any public or private education
institution or agency that provides instructional and/or support services to students or staff at the early
childhood level through high school completion.

Also searched as: teacher.

## Natural key

`staffUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `staffUniqueId` | yes | string max 32 | A unique alphanumeric code assigned to a staff. |
| `openStaffPositionReference` |  | reference; supply `educationOrganizationId`, `requisitionNumber` | This entity represents an open staff position that the education organization is seeking to fill. |
| `personReference` |  | reference; supply `personId`, `sourceSystemDescriptor` | Reference to person. |
| `birthDate` |  | string (date) | The month, day, and year on which an individual was born. |
| `credentials` |  | array of edFi_staffCredential | An unordered collection of staffCredentials. |
| `educatorPreparationPrograms` |  | array of edFi_staffEducatorPreparationProgram | An unordered collection of staffEducatorPreparationPrograms. |
| `educatorResearch` |  | edFi_staffEducatorResearch |  |
| `firstName` | yes | string max 75 | A name given to an individual at birth, baptism, or during another naming ceremony, or through legal change. |
| `generationCodeSuffix` |  | string max 10 | An appendage, if any, used to denote an individual's generation in his family (e.g., Jr., Sr., III). |
| `highestCompletedLevelOfEducationDescriptor` |  | descriptor URI | The extent of formal instruction an individual has received (e.g., the highest grade in school completed or its equivalent or the highest degree received). |
| `highlyQualifiedAcademicSubjects` |  | array of edFi_staffHighlyQualifiedAcademicSubject | An unordered collection of staffHighlyQualifiedAcademicSubjects. |
| `highlyQualifiedTeacher` |  | boolean | An indication of whether a teacher is classified as highly qualified for his/her assignment according to state definition. |
| `lastSurname` | yes | string max 75 | The name borne in common by members of a family. |
| `loginId` |  | string max 120 | The login ID for the user; used for security access control interface. |
| `maidenName` |  | string max 75 | The individual's maiden name. |
| `middleName` |  | string max 75 | A secondary name given to an individual at birth, baptism, or during another naming ceremony. |
| `otherNames` |  | array of edFi_staffOtherName | An unordered collection of staffOtherNames. |
| `personalIdentificationDocuments` |  | array of edFi_staffPersonalIdentificationDocument | An unordered collection of staffPersonalIdentificationDocuments. |
| `personalTitlePrefix` |  | string max 30 | A prefix used to denote the title, degree, position, or seniority of the individual. |
| `preferredFirstName` |  | string max 75 | The first name the individual prefers, if different from their legal first name |
| `preferredLastSurname` |  | string max 75 | The last name the individual prefers, if different from their legal last name |
| `recognitions` |  | array of edFi_staffRecognition | An unordered collection of staffRecognitions. |
| `yearsOfPriorProfessionalExperience` |  | number (double) | The total number of years that an individual has previously held a similar professional position in one or more education institutions prior to the current sch… |
| `yearsOfPriorTeachingExperience` |  | number (double) | The total number of years that an individual has previously held a teaching position in one or more education institutions prior to the current school year. |

### Items in `credentials`

| Field | Required | Type | Description |
|---|---|---|---|
| `credentialReference` | yes | reference; supply `credentialIdentifier`, `stateOfIssueStateAbbreviationDescriptor` | The legal document giving authorization to perform teaching assignment services. |

### Items in `educatorPreparationPrograms`

| Field | Required | Type | Description |
|---|---|---|---|
| `educatorPreparationProgramReference` | yes | reference; supply `educationOrganizationId`, `programName`, `programTypeDescriptor` | The educator preparation program designed to prepare students to become licensed educators. |

### Items in `highlyQualifiedAcademicSubjects`

| Field | Required | Type | Description |
|---|---|---|---|
| `academicSubjectDescriptor` | yes | descriptor URI | The academic subject(s) in which the staff is deemed to be "highly qualified". |

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
| `issuerDocumentIdentificationCode` |  | string max 120 | The unique identifier on the issuer's identification system. |
| `issuerName` |  | string max 150 | Name of the entity or institution that issued the document. |

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

## Endpoints

- `GET /ed-fi/staffs`
- `POST /ed-fi/staffs`
- `GET /ed-fi/staffs/deletes`
- `GET /ed-fi/staffs/keyChanges`
- `GET /ed-fi/staffs/partitions`
- `GET /ed-fi/staffs/{id}`
- `PUT /ed-fi/staffs/{id}`
- `DELETE /ed-fi/staffs/{id}`
