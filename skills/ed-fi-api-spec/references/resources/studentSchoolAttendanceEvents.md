# studentSchoolAttendanceEvents

`/ed-fi/studentSchoolAttendanceEvents`

This event entity represents the recording of whether a student is in attendance for a school day.

## Natural key

`attendanceEventCategoryDescriptor`, `eventDate`, `schoolReference`, `sessionReference`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `attendanceEventCategoryDescriptor` | key | descriptor URI | A code describing the attendance event, for example: Present Unexcused absence Excused absence Tardy. |
| `eventDate` | key | string (date) | Date for this attendance event. |
| `schoolReference` | key | reference: `schoolId` |  |
| `sessionReference` | key | reference: `schoolId`, `schoolYear`, `sessionName` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `arrivalTime` |  | string | The time of day the student arrived for the attendance event in ISO 8601 format. |
| `attendanceEventReason` |  | string max 255 | The reported reason for a student's absence. |
| `departureTime` |  | string | The time of day the student departed for the attendance event in ISO 8601 format. |
| `educationalEnvironmentDescriptor` |  | descriptor URI | The setting in which a child receives education and related services. |
| `eventDuration` |  | number (double) | The amount of time in days for the event as recognized by the school: 1 day = 1, 1/2 day = 0.5, 1/3 day = 0.33. |
| `schoolAttendanceDuration` |  | integer (int32) | The duration in minutes of the school attendance event. |

## Endpoints

- `DELETE /ed-fi/studentSchoolAttendanceEvents/{id}`
- `GET /ed-fi/studentSchoolAttendanceEvents/deletes`
- `GET /ed-fi/studentSchoolAttendanceEvents/keyChanges`
- `GET /ed-fi/studentSchoolAttendanceEvents/partitions`
- `GET /ed-fi/studentSchoolAttendanceEvents/{id}`
- `GET /ed-fi/studentSchoolAttendanceEvents`
- `POST /ed-fi/studentSchoolAttendanceEvents`
- `PUT /ed-fi/studentSchoolAttendanceEvents/{id}`
