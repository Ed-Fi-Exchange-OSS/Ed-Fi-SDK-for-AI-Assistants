# calendarDates

`/ed-fi/calendarDates`

The type of scheduled or unscheduled event for the day.

## Natural key

`date`, `calendarReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `calendarEvents` | yes | array of edFi_calendarDateCalendarEvent | An unordered collection of calendarDateCalendarEvents. |
| `date` | key | string (date) | The month, day, and year of the calendar event. |
| `calendarReference` | key | reference: `calendarCode`, `schoolId`, `schoolYear` |  |

## Endpoints

- `DELETE /ed-fi/calendarDates/{id}`
- `GET /ed-fi/calendarDates/deletes`
- `GET /ed-fi/calendarDates/keyChanges`
- `GET /ed-fi/calendarDates/partitions`
- `GET /ed-fi/calendarDates/{id}`
- `GET /ed-fi/calendarDates`
- `POST /ed-fi/calendarDates`
- `PUT /ed-fi/calendarDates/{id}`
