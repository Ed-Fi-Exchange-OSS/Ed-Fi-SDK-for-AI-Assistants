# staffAbsenceEvents

`/ed-fi/staffAbsenceEvents`

This event entity represents the recording of the dates of staff absence.

## Natural key

`absenceEventCategoryDescriptor`, `eventDate`, `staffReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `absenceEventCategoryDescriptor` | key | descriptor URI | The code describing the type of absence. |
| `eventDate` | key | string (date) | Date for this leave event. |
| `staffReference` | key | reference: `staffUniqueId` |  |
| `absenceEventReason` |  | string max 40 | Expanded reason for the staff absence. |
| `hoursAbsent` |  | number (double) | The hours the staff was absent, if not the entire working day. |

## Endpoints

- `DELETE /ed-fi/staffAbsenceEvents/{id}`
- `GET /ed-fi/staffAbsenceEvents/deletes`
- `GET /ed-fi/staffAbsenceEvents/keyChanges`
- `GET /ed-fi/staffAbsenceEvents/partitions`
- `GET /ed-fi/staffAbsenceEvents/{id}`
- `GET /ed-fi/staffAbsenceEvents`
- `POST /ed-fi/staffAbsenceEvents`
- `PUT /ed-fi/staffAbsenceEvents/{id}`
