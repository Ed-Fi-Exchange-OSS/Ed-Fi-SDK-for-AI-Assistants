# professionalDevelopmentEventAttendances

`/ed-fi/professionalDevelopmentEventAttendances`

This event entity represents the recording of whether a staff is in attendance for professional development.

## Natural key

`attendanceDate`, `personId`, `sourceSystemDescriptor`, `namespace`, `professionalDevelopmentTitle`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `attendanceDate` | yes | string (date) | Date for this attendance event. |
| `personReference` | yes | reference; supply `personId`, `sourceSystemDescriptor` | Reference to person. |
| `professionalDevelopmentEventReference` | yes | reference; supply `namespace`, `professionalDevelopmentTitle` | Information about a professional development event. |
| `attendanceEventCategoryDescriptor` | yes | descriptor URI | A code describing the attendance event. |
| `attendanceEventReason` |  | string max 255 | The reported reason for a teacher candidate's absence. |

## Endpoints

- `GET /ed-fi/professionalDevelopmentEventAttendances`
- `POST /ed-fi/professionalDevelopmentEventAttendances`
- `GET /ed-fi/professionalDevelopmentEventAttendances/deletes`
- `GET /ed-fi/professionalDevelopmentEventAttendances/keyChanges`
- `GET /ed-fi/professionalDevelopmentEventAttendances/partitions`
- `GET /ed-fi/professionalDevelopmentEventAttendances/{id}`
- `PUT /ed-fi/professionalDevelopmentEventAttendances/{id}`
- `DELETE /ed-fi/professionalDevelopmentEventAttendances/{id}`
