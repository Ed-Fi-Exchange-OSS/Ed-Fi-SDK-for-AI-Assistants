# studentSectionAttendanceEvents

`/ed-fi/studentSectionAttendanceEvents`

This event entity represents the recording of whether a student is in attendance for a section.

## Natural key

`attendanceEventCategoryDescriptor`, `eventDate`, `sectionReference`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `attendanceEventCategoryDescriptor` | key | descriptor URI | A code describing the attendance event, for example: Present Unexcused absence Excused absence Tardy. |
| `eventDate` | key | string (date) | Date for this attendance event. |
| `sectionReference` | key | reference: `localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `arrivalTime` |  | string | The time of day the student arrived for the attendance event in ISO 8601 format. |
| `attendanceEventReason` |  | string max 255 | The reported reason for a student's absence. |
| `classPeriods` |  | array of edFi_studentSectionAttendanceEventClassPeriod | An unordered collection of studentSectionAttendanceEventClassPeriods. |
| `departureTime` |  | string | The time of day the student departed for the attendance event in ISO 8601 format. |
| `educationalEnvironmentDescriptor` |  | descriptor URI | The setting in which a child receives education and related services. |
| `eventDuration` |  | number (double) | The amount of time in days for the event as recognized by the school: 1 day = 1, 1/2 day = 0.5, 1/3 day = 0.33. |
| `sectionAttendanceDuration` |  | integer (int32) | The duration in minutes of the section attendance event. |

## Endpoints

- `DELETE /ed-fi/studentSectionAttendanceEvents/{id}`
- `GET /ed-fi/studentSectionAttendanceEvents/deletes`
- `GET /ed-fi/studentSectionAttendanceEvents/keyChanges`
- `GET /ed-fi/studentSectionAttendanceEvents/partitions`
- `GET /ed-fi/studentSectionAttendanceEvents/{id}`
- `GET /ed-fi/studentSectionAttendanceEvents`
- `POST /ed-fi/studentSectionAttendanceEvents`
- `PUT /ed-fi/studentSectionAttendanceEvents/{id}`
