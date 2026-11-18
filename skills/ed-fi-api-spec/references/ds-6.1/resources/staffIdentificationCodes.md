# staffIdentificationCodes

`/ed-fi/staffIdentificationCodes`

This entity holds different identity codes for staff member.

## Natural key

`staffIdentificationSystemDescriptor`, `educationOrganizationId`, `staffUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `staffIdentificationSystemDescriptor` | yes | descriptor URI | A coding scheme that is used for identification and record-keeping purposes by schools, LEAs, SEAs, or other agencies refer to a staff member. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `staffReference` | yes | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |
| `assigningOrganizationIdentificationCode` |  | string max 60 | The organization code or name assigning the IdentificationCode. |
| `identificationCode` | yes | string max 120 | A unique number or alphanumeric code assigned to an individual by a school, LEA, SEA, or other agency. |

## Endpoints

- `GET /ed-fi/staffIdentificationCodes`
- `POST /ed-fi/staffIdentificationCodes`
- `GET /ed-fi/staffIdentificationCodes/deletes`
- `GET /ed-fi/staffIdentificationCodes/keyChanges`
- `GET /ed-fi/staffIdentificationCodes/partitions`
- `GET /ed-fi/staffIdentificationCodes/{id}`
- `PUT /ed-fi/staffIdentificationCodes/{id}`
- `DELETE /ed-fi/staffIdentificationCodes/{id}`
