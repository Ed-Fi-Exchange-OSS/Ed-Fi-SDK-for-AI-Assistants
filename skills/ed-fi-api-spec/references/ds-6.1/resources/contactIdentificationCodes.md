# contactIdentificationCodes

`/ed-fi/contactIdentificationCodes`

This entity holds different identity codes for a contact.

## Natural key

`contactIdentificationSystemDescriptor`, `contactUniqueId`, `educationOrganizationId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `contactIdentificationSystemDescriptor` | yes | descriptor URI | A coding scheme that is used for identification and record-keeping. |
| `contactReference` | yes | reference; supply `contactUniqueId` | This entity represents a contact of a student, such as a parent, guardian or caretaker. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `assigningOrganizationIdentificationCode` |  | string max 60 | the organization code or name assigning the IdentificationCode. |
| `identificationCode` | yes | string max 120 | A unique number or alphanumeric code assigned to an individual by a school, LEA, SEA, or other agency. |

## Endpoints

- `GET /ed-fi/contactIdentificationCodes`
- `POST /ed-fi/contactIdentificationCodes`
- `GET /ed-fi/contactIdentificationCodes/deletes`
- `GET /ed-fi/contactIdentificationCodes/keyChanges`
- `GET /ed-fi/contactIdentificationCodes/partitions`
- `GET /ed-fi/contactIdentificationCodes/{id}`
- `PUT /ed-fi/contactIdentificationCodes/{id}`
- `DELETE /ed-fi/contactIdentificationCodes/{id}`
