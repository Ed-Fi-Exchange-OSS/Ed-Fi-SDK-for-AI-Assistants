# studentIdentificationCodes

`/ed-fi/studentIdentificationCodes`

This entity holds different identity codes for a student

Also searched as: student ID.

## Natural key

`studentIdentificationSystemDescriptor`, `educationOrganizationId`, `studentUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `studentIdentificationSystemDescriptor` | yes | descriptor URI | A coding scheme that is used for identification and record-keeping purposes by schools, LEAs, SEAs, or other agencies refer to a student. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `assigningOrganizationIdentificationCode` |  | string max 60 | the organization code or name assigning the IdentificationCode. |
| `identificationCode` | yes | string max 120 | A unique number or alphanumeric code assigned to an individual by a school, LEA, SEA, or other agency. |

## Endpoints

- `GET /ed-fi/studentIdentificationCodes`
- `POST /ed-fi/studentIdentificationCodes`
- `GET /ed-fi/studentIdentificationCodes/deletes`
- `GET /ed-fi/studentIdentificationCodes/keyChanges`
- `GET /ed-fi/studentIdentificationCodes/partitions`
- `GET /ed-fi/studentIdentificationCodes/{id}`
- `PUT /ed-fi/studentIdentificationCodes/{id}`
- `DELETE /ed-fi/studentIdentificationCodes/{id}`
