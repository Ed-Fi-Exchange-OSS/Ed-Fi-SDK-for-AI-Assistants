# credentials

`/ed-fi/credentials`

The legal document giving authorization to perform teaching assignment services.

## Natural key

`credentialIdentifier`, `stateOfIssueStateAbbreviationDescriptor`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `credentialIdentifier` | key | string max 60 | Identifier or serial number assigned to the credential. |
| `stateOfIssueStateAbbreviationDescriptor` | key | descriptor URI | The abbreviation for the name of the state (within the United States) or extra-state jurisdiction in which a license/credential was issued. |
| `academicSubjects` |  | array of edFi_credentialAcademicSubject | An unordered collection of credentialAcademicSubjects. |
| `credentialFieldDescriptor` |  | descriptor URI | The field of certification for the certificate (e.g., Mathematics, Music). |
| `credentialTypeDescriptor` | yes | descriptor URI | An indication of the category of credential an individual holds. |
| `effectiveDate` |  | string (date) | The year, month and day on which an active credential held by an individual was issued. |
| `endorsements` |  | array of edFi_credentialEndorsement | An unordered collection of credentialEndorsements. |
| `expirationDate` |  | string (date) | The month, day, and year on which an active credential held by an individual will expire. |
| `gradeLevels` |  | array of edFi_credentialGradeLevel | An unordered collection of credentialGradeLevels. |
| `issuanceDate` | yes | string (date) | The month, day, and year on which an active credential was issued to an individual. |
| `namespace` | yes | string max 255 | Namespace for the credential. |
| `teachingCredentialBasisDescriptor` |  | descriptor URI | An indication of the pre-determined criteria for granting the teaching credential that an individual holds. |
| `teachingCredentialDescriptor` |  | descriptor URI | An indication of the category of a legal document giving authorization to perform teaching assignment services. |
| `_ext` |  | credentialExtensions |  |

## Endpoints

- `DELETE /ed-fi/credentials/{id}`
- `GET /ed-fi/credentials/deletes`
- `GET /ed-fi/credentials/keyChanges`
- `GET /ed-fi/credentials/partitions`
- `GET /ed-fi/credentials/{id}`
- `GET /ed-fi/credentials`
- `POST /ed-fi/credentials`
- `PUT /ed-fi/credentials/{id}`
