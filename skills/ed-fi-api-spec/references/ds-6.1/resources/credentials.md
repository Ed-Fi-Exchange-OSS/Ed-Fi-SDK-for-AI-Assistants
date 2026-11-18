# credentials

`/ed-fi/credentials`

The legal document giving authorization to perform teaching assignment services.

## Natural key

`stateOfIssueStateAbbreviationDescriptor`, `credentialIdentifier`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `credentialIdentifier` | yes | string max 120 | Identifier or serial number assigned to the credential. |
| `stateOfIssueStateAbbreviationDescriptor` | yes | descriptor URI | The abbreviation for the name of the state (within the United States) or extra-state jurisdiction in which a license/credential was issued. |
| `certificationReference` |  | reference; supply `certificationIdentifier`, `namespace` | An offering by an official granting authority of a certification or license that qualifies persons to perform specific job functions, such as fulfill a teachin… |
| `personReference` |  | reference; supply `personId`, `sourceSystemDescriptor` | Reference to person. |
| `academicSubjects` |  | array of edFi_credentialAcademicSubject | An unordered collection of credentialAcademicSubjects. |
| `boardCertificationIndicator` |  | boolean | Indicator that the credential was granted under the authority of a national board certification. |
| `certificationRouteDescriptor` |  | descriptor URI | The process, program, or pathway used to obtain certification. |
| `certificationTitle` |  | string max 64 | The title of the certification obtained by the person. |
| `credentialFieldDescriptor` |  | descriptor URI | The field of certification for the credential. |
| `credentialStatusDate` |  | string (date) | The month, day, and year on which the credential status was effective. |
| `credentialStatusDescriptor` |  | descriptor URI | The current status of the credential. |
| `credentialTypeDescriptor` | yes | descriptor URI | An indication of the category of the credential a person holds. |
| `educatorRoleDescriptor` |  | descriptor URI | The specific roles or positions within an organization that the credential is intended to authorize, typically associated with service and administrative certi… |
| `effectiveDate` |  | string (date) | The month, day, and year on which an active credential held by a person was issued. |
| `endorsements` |  | array of edFi_credentialEndorsement | An unordered collection of credentialEndorsements. |
| `expirationDate` |  | string (date) | The month, day, and year on which an active credential held by a person will expire. |
| `gradeLevels` |  | array of edFi_credentialGradeLevel | An unordered collection of credentialGradeLevels. |
| `issuanceDate` | yes | string (date) | The month, day, and year on which an active credential was issued to a person. |
| `namespace` | yes | string max 255 | The namespace for the credential. |
| `studentAcademicRecords` |  | array of edFi_credentialStudentAcademicRecord | An unordered collection of credentialStudentAcademicRecords. |
| `teachingCredentialBasisDescriptor` |  | descriptor URI | An indication of the pre-determined criteria for granting the teaching credential that a person holds. |
| `teachingCredentialDescriptor` |  | descriptor URI | An indication of the category of a legal document giving authorization to perform teaching assignment services. |

### Items in `academicSubjects`

| Field | Required | Type | Description |
|---|---|---|---|
| `academicSubjectDescriptor` | yes | descriptor URI | The academic subjects to which the credential pertains. |

### Items in `endorsements`

| Field | Required | Type | Description |
|---|---|---|---|
| `credentialEndorsement` | yes | string max 255 | The endorsements that are attached to teaching certificates and indicate areas of specialization. |

### Items in `gradeLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `gradeLevelDescriptor` | yes | descriptor URI | The grade level(s) certified for teaching. |

### Items in `studentAcademicRecords`

| Field | Required | Type | Description |
|---|---|---|---|
| `studentAcademicRecordReference` | yes | reference; supply `educationOrganizationId`, `schoolYear`, `studentUniqueId`, `termDescriptor` | This educational entity represents the cumulative record of academic achievement for a student. |

## Endpoints

- `GET /ed-fi/credentials`
- `POST /ed-fi/credentials`
- `GET /ed-fi/credentials/deletes`
- `GET /ed-fi/credentials/keyChanges`
- `GET /ed-fi/credentials/partitions`
- `GET /ed-fi/credentials/{id}`
- `PUT /ed-fi/credentials/{id}`
- `DELETE /ed-fi/credentials/{id}`
