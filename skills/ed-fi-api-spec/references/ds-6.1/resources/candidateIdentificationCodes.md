# candidateIdentificationCodes

`/ed-fi/candidateIdentificationCodes`

This entity holds different identity codes for a candidate.

## Natural key

`candidateIdentificationSystemDescriptor`, `candidateIdentifier`, `educationOrganizationId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `candidateIdentificationSystemDescriptor` | yes | descriptor URI | A coding scheme that is used for identification and record-keeping. |
| `candidateReference` | yes | reference; supply `candidateIdentifier` | A candidate is both a person enrolled in a educator preparation program and a candidate to become an educator. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `assigningOrganizationIdentificationCode` |  | string max 60 | The organization code or name assigning the IdentificationCode. |
| `identificationCode` | yes | string max 120 | A unique number or alphanumeric code assigned to an individual by a school, LEA, SEA, or other agency. |

## Endpoints

- `GET /ed-fi/candidateIdentificationCodes`
- `POST /ed-fi/candidateIdentificationCodes`
- `GET /ed-fi/candidateIdentificationCodes/deletes`
- `GET /ed-fi/candidateIdentificationCodes/keyChanges`
- `GET /ed-fi/candidateIdentificationCodes/partitions`
- `GET /ed-fi/candidateIdentificationCodes/{id}`
- `PUT /ed-fi/candidateIdentificationCodes/{id}`
- `DELETE /ed-fi/candidateIdentificationCodes/{id}`
