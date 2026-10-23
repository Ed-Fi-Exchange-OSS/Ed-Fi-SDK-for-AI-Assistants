# calendars

`/ed-fi/calendars`

A set of dates associated with an organization.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `calendarCode` | yes | string max 60 | The identifier for the calendar. |
| `schoolReference` | yes | reference; supply `schoolId` | This entity represents an educational organization that includes staff and students who participate in classes and educational activity groups. |
| `schoolYearTypeReference` | yes | reference; supply `schoolYear` | Identifier for a school year. |
| `calendarTypeDescriptor` | yes | descriptor URI | Indicates the type of calendar. |
| `gradeLevels` |  | array of edFi_calendarGradeLevel | An unordered collection of calendarGradeLevels. |

### Items in `gradeLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `gradeLevelDescriptor` | yes | descriptor URI | Indicates the grade level associated with the calendar. |

## Endpoints

- `GET /ed-fi/calendars`
- `POST /ed-fi/calendars`
- `GET /ed-fi/calendars/deletes`
- `GET /ed-fi/calendars/keyChanges`
- `GET /ed-fi/calendars/partitions`
- `GET /ed-fi/calendars/{id}`
- `PUT /ed-fi/calendars/{id}`
- `DELETE /ed-fi/calendars/{id}`
