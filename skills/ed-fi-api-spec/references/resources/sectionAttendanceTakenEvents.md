# sectionAttendanceTakenEvents

`/ed-fi/sectionAttendanceTakenEvents`

Captures attendance taken event for given section.

## Natural key

`calendarDateReference`, `sectionReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `calendarDateReference` | key | reference: `calendarCode`, `date`, `schoolId`, `schoolYear` |  |
| `sectionReference` | key | reference: `localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName` |  |
| `staffReference` |  | reference: `staffUniqueId` |  |
| `eventDate` | yes | string (date) | The date the section attendance taken event was submitted, which could be a different date than the instructional day. |

## Endpoints

- `DELETE /ed-fi/sectionAttendanceTakenEvents/{id}`
- `GET /ed-fi/sectionAttendanceTakenEvents/deletes`
- `GET /ed-fi/sectionAttendanceTakenEvents/keyChanges`
- `GET /ed-fi/sectionAttendanceTakenEvents/partitions`
- `GET /ed-fi/sectionAttendanceTakenEvents/{id}`
- `GET /ed-fi/sectionAttendanceTakenEvents`
- `POST /ed-fi/sectionAttendanceTakenEvents`
- `PUT /ed-fi/sectionAttendanceTakenEvents/{id}`
