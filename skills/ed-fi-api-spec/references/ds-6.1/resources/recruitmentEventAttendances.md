# recruitmentEventAttendances

`/ed-fi/recruitmentEventAttendances`

A prospect for employment or acceptance that has not yet made a formal application but has attended a
recruitment event, such as a job fair or university recruiting visit.

## Natural key

`recruitmentEventAttendeeIdentifier`, `educationOrganizationId`, `eventDate`, `eventTitle`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `recruitmentEventAttendeeIdentifier` | yes | string max 32 | The identifier for the attendee to a recruitment event. |
| `recruitmentEventReference` | yes | reference; supply `educationOrganizationId`, `eventDate`, `eventTitle` | Events associated with the recruitment process. |
| `applied` |  | boolean | Indicator of whether the prospect applied for a position. |
| `currentPosition` |  | edFi_recruitmentEventAttendanceCurrentPosition |  |
| `disabilities` |  | array of edFi_recruitmentEventAttendanceDisability | An unordered collection of recruitmentEventAttendanceDisabilities. |
| `electronicMailAddress` | yes | string max 128 | The numbers, letters, and symbols used to identify an electronic mail (e-mail) user within the network to which the individual or organization belongs. |
| `firstName` | yes | string max 75 | A name given to an individual at birth, baptism, or during another naming ceremony, or through legal change. |
| `genderIdentity` |  | string max 60 | The gender the person identifies themselves as. |
| `generationCodeSuffix` |  | string max 10 | An appendage, if any, used to denote an individual's generation in his family (e.g., Jr., Sr., III). |
| `hispanicLatinoEthnicity` |  | boolean | An indication that the individual traces his or her origin or descent to Mexico, Puerto Rico, Cuba, Central, and South America, and other Spanish cultures, reg… |
| `lastSurname` | yes | string max 75 | The name borne in common by members of a family. |
| `maidenName` |  | string max 75 | The individual's maiden name. |
| `met` |  | boolean | Indicator whether the person was met by a representative of the education organization. |
| `middleName` |  | string max 75 | A secondary name given to an individual at birth, baptism, or during another naming ceremony. |
| `notes` |  | string max 255 | Additional notes about the prospect. |
| `personalIdentificationDocuments` |  | array of edFi_recruitmentEventAttendancePersonalIdentificationDocument | An unordered collection of recruitmentEventAttendancePersonalIdentificationDocuments. |
| `personalTitlePrefix` |  | string max 30 | A prefix used to denote the title, degree, position, or seniority of the individual. |
| `preferredFirstName` |  | string max 75 | The first name the individual prefers, if different from their legal first name |
| `preferredLastSurname` |  | string max 75 | The last name the individual prefers, if different from their legal last name |
| `preScreeningRating` |  | integer (int32) | The rating initially assigned to the prospect prior to an official screening. |
| `races` |  | array of edFi_recruitmentEventAttendanceRace | An unordered collection of recruitmentEventAttendanceRaces. |
| `recruitmentEventAttendeeQualifications` |  | edFi_recruitmentEventAttendanceRecruitmentEventAttendeeQualifications |  |
| `recruitmentEventAttendeeTypeDescriptor` |  | descriptor URI | Reflects the type of prospect, such as EPP Applicant, Hire, or Mentor Teacher. |
| `referral` |  | boolean | Indicator of whether the prospect was a referral. |
| `referredBy` |  | string max 50 | The person making the referral. |
| `sexDescriptor` |  | descriptor URI | A person's birth sex. |
| `socialMediaNetworkName` |  | string max 50 | The social media network name associated with the social media user name. |
| `socialMediaUserName` |  | string max 50 | The user name of the person on social media. |
| `telephones` |  | array of edFi_recruitmentEventAttendanceTelephone | An unordered collection of recruitmentEventAttendanceTelephones. |
| `touchpoints` |  | array of edFi_recruitmentEventAttendanceTouchpoint | An unordered collection of recruitmentEventAttendanceTouchpoints. |

### Items in `disabilities`

| Field | Required | Type | Description |
|---|---|---|---|
| `disabilityDescriptor` | yes | descriptor URI | A disability category that describes a individual's impairment. |
| `disabilityDeterminationSourceTypeDescriptor` |  | descriptor URI | The source that provided the disability determination. |
| `disabilityDiagnosis` |  | string max 80 | A description of the disability diagnosis. |
| `orderOfDisability` |  | integer (int32) | The order by severity of individual's disabilities: 1- Primary, 2 - Secondary, 3 - Tertiary, etc. |
| `designations` |  | array of edFi_recruitmentEventAttendanceDisabilityDesignation | An unordered collection of recruitmentEventAttendanceDisabilityDesignations. |

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

### Items in `touchpoints`

| Field | Required | Type | Description |
|---|---|---|---|
| `touchpointContent` | yes | string max 255 | The content associated with or an artifact from the touchpoint. |
| `touchpointDate` | yes | string (date) | The date of the touchpoint. |

## Endpoints

- `GET /ed-fi/recruitmentEventAttendances`
- `POST /ed-fi/recruitmentEventAttendances`
- `GET /ed-fi/recruitmentEventAttendances/deletes`
- `GET /ed-fi/recruitmentEventAttendances/keyChanges`
- `GET /ed-fi/recruitmentEventAttendances/partitions`
- `GET /ed-fi/recruitmentEventAttendances/{id}`
- `PUT /ed-fi/recruitmentEventAttendances/{id}`
- `DELETE /ed-fi/recruitmentEventAttendances/{id}`
