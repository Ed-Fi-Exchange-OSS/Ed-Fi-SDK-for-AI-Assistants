# credentialEvents

`/ed-fi/credentialEvents`

An event associated with a person's credential.

## Natural key

`credentialEventTypeDescriptor`, `credentialEventDate`, `credentialIdentifier`,
`stateOfIssueStateAbbreviationDescriptor`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `credentialEventDate` | yes | string (date) | The month, day, and year of the credential event. |
| `credentialEventTypeDescriptor` | yes | descriptor URI | The type of event associated with a person's credential. |
| `credentialReference` | yes | reference; supply `credentialIdentifier`, `stateOfIssueStateAbbreviationDescriptor` | The legal document giving authorization to perform teaching assignment services. |
| `credentialEventReason` |  | string max 1024 | The reason for the credential event, or any other descriptive text. |

## Endpoints

- `GET /ed-fi/credentialEvents`
- `POST /ed-fi/credentialEvents`
- `GET /ed-fi/credentialEvents/deletes`
- `GET /ed-fi/credentialEvents/keyChanges`
- `GET /ed-fi/credentialEvents/partitions`
- `GET /ed-fi/credentialEvents/{id}`
- `PUT /ed-fi/credentialEvents/{id}`
- `DELETE /ed-fi/credentialEvents/{id}`
