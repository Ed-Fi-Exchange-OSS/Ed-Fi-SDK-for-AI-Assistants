# educationOrganizationIdentificationCodes

`/ed-fi/educationOrganizationIdentificationCodes`

This entity holds different identity codes for an education organization.

## Natural key

`educationOrganizationIdentificationSystemDescriptor`, `educationOrganizationId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationIdentificationSystemDescriptor` | yes | descriptor URI | A coding scheme that is used for identification and record-keeping. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `assigningOrganizationIdentificationCode` |  | string max 60 | The organization code or name assigning the IdentificationCode. |
| `identificationCode` | yes | string max 120 | A unique number or alphanumeric code assigned to an education organization by an SEA or other agency. |

## Endpoints

- `GET /ed-fi/educationOrganizationIdentificationCodes`
- `POST /ed-fi/educationOrganizationIdentificationCodes`
- `GET /ed-fi/educationOrganizationIdentificationCodes/deletes`
- `GET /ed-fi/educationOrganizationIdentificationCodes/keyChanges`
- `GET /ed-fi/educationOrganizationIdentificationCodes/partitions`
- `GET /ed-fi/educationOrganizationIdentificationCodes/{id}`
- `PUT /ed-fi/educationOrganizationIdentificationCodes/{id}`
- `DELETE /ed-fi/educationOrganizationIdentificationCodes/{id}`
