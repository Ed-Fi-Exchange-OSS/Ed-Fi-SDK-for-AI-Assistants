# crisisEvents

`/ed-fi/crisisEvents`

A natural or man-made event that causes the disruption of school-level activities and the temporary or
permanent displacement of students.

## Natural key

`crisisEventName`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `crisisEventName` | yes | string max 100 | The name of the crisis event that occurred. |
| `crisisDescription` |  | string max 1024 | Provides a textual description of the crisis event affecting the student. |
| `crisisEndDate` |  | string (date) | The date on which the crisis ceased to affect the student. |
| `crisisStartDate` |  | string (date) | The year, month and day on which the crisis affected the student. |
| `crisisTypeDescriptor` | yes | descriptor URI | The type or category of crisis. |

## Endpoints

- `GET /ed-fi/crisisEvents`
- `POST /ed-fi/crisisEvents`
- `GET /ed-fi/crisisEvents/deletes`
- `GET /ed-fi/crisisEvents/keyChanges`
- `GET /ed-fi/crisisEvents/partitions`
- `GET /ed-fi/crisisEvents/{id}`
- `PUT /ed-fi/crisisEvents/{id}`
- `DELETE /ed-fi/crisisEvents/{id}`
