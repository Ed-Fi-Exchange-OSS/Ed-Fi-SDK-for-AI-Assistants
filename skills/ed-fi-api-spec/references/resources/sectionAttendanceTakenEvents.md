# sectionAttendanceTakenEvents

`/ed-fi/sectionAttendanceTakenEvents`

Captures attendance taken event for given section.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `calendarDateReference` | yes | reference; supply `calendarCode`, `date`, `schoolId`, `schoolYear` | The type of scheduled or unscheduled event for the day. |
| `sectionReference` | yes | reference; supply `localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName` | This entity represents a setting in which organized instruction of course content is provided, in-person or otherwise, to one or more students for a given peri… |
| `staffReference` |  | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |
| `eventDate` | yes | string (date) | The date the section attendance taken event was submitted, which could be a different date than the instructional day. |

## Endpoints

- `GET /ed-fi/sectionAttendanceTakenEvents`
- `POST /ed-fi/sectionAttendanceTakenEvents`
- `GET /ed-fi/sectionAttendanceTakenEvents/deletes`
- `GET /ed-fi/sectionAttendanceTakenEvents/keyChanges`
- `GET /ed-fi/sectionAttendanceTakenEvents/partitions`
- `GET /ed-fi/sectionAttendanceTakenEvents/{id}`
- `PUT /ed-fi/sectionAttendanceTakenEvents/{id}`
- `DELETE /ed-fi/sectionAttendanceTakenEvents/{id}`
