# calendarDates

`/ed-fi/calendarDates`

The type of scheduled or unscheduled event for the day.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `calendarEvents` | yes | array of edFi_calendarDateCalendarEvent | An unordered collection of calendarDateCalendarEvents. |
| `date` | yes | string (date) | The month, day, and year of the calendar event. |
| `calendarReference` | yes | reference; supply `calendarCode`, `schoolId`, `schoolYear` | A set of dates associated with an organization. |

### Items in `calendarEvents`

| Field | Required | Type | Description |
|---|---|---|---|
| `calendarEventDescriptor` | yes | descriptor URI | The type of scheduled or unscheduled event for the day. |

## Endpoints

- `GET /ed-fi/calendarDates`
- `POST /ed-fi/calendarDates`
- `GET /ed-fi/calendarDates/deletes`
- `GET /ed-fi/calendarDates/keyChanges`
- `GET /ed-fi/calendarDates/partitions`
- `GET /ed-fi/calendarDates/{id}`
- `PUT /ed-fi/calendarDates/{id}`
- `DELETE /ed-fi/calendarDates/{id}`
