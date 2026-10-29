# staffAbsenceEvents

`/ed-fi/staffAbsenceEvents`

This event entity represents the recording of the dates of staff absence.

## Natural key

`absenceEventCategoryDescriptor`, `eventDate`, `staffUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `absenceEventCategoryDescriptor` | yes | descriptor URI | The code describing the type of absence. |
| `eventDate` | yes | string (date) | Date for this leave event. |
| `staffReference` | yes | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |
| `absenceEventReason` |  | string max 40 | Expanded reason for the staff absence. |
| `hoursAbsent` |  | number (double) | The hours the staff was absent, if not the entire working day. |

## Endpoints

- `GET /ed-fi/staffAbsenceEvents`
- `POST /ed-fi/staffAbsenceEvents`
- `GET /ed-fi/staffAbsenceEvents/deletes`
- `GET /ed-fi/staffAbsenceEvents/keyChanges`
- `GET /ed-fi/staffAbsenceEvents/partitions`
- `GET /ed-fi/staffAbsenceEvents/{id}`
- `PUT /ed-fi/staffAbsenceEvents/{id}`
- `DELETE /ed-fi/staffAbsenceEvents/{id}`
