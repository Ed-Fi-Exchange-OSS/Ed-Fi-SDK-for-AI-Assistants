# calendars

`/ed-fi/calendars`

A set of dates associated with an organization.

## Natural key

`calendarCode`, `schoolReference`, `schoolYearTypeReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `calendarCode` | key | string max 60 | The identifier for the calendar. |
| `schoolReference` | key | reference: `schoolId` |  |
| `schoolYearTypeReference` | key | reference: `schoolYear` |  |
| `calendarTypeDescriptor` | yes | descriptor URI | Indicates the type of calendar. |
| `gradeLevels` |  | array of edFi_calendarGradeLevel | An unordered collection of calendarGradeLevels. |

## Endpoints

- `DELETE /ed-fi/calendars/{id}`
- `GET /ed-fi/calendars/deletes`
- `GET /ed-fi/calendars/keyChanges`
- `GET /ed-fi/calendars/partitions`
- `GET /ed-fi/calendars/{id}`
- `GET /ed-fi/calendars`
- `POST /ed-fi/calendars`
- `PUT /ed-fi/calendars/{id}`
