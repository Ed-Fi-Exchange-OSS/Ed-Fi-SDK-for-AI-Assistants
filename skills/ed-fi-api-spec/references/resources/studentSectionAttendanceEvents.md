# studentSectionAttendanceEvents

`/ed-fi/studentSectionAttendanceEvents`

This event entity represents the recording of whether a student is in attendance for a section.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `attendanceEventCategoryDescriptor` | yes | descriptor URI | A code describing the attendance event, for example: Present Unexcused absence Excused absence Tardy. |
| `eventDate` | yes | string (date) | Date for this attendance event. |
| `sectionReference` | yes | reference; supply `localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName` | This entity represents a setting in which organized instruction of course content is provided, in-person or otherwise, to one or more students for a given peri… |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `arrivalTime` |  | string | The time of day the student arrived for the attendance event in ISO 8601 format. |
| `attendanceEventReason` |  | string max 255 | The reported reason for a student's absence. |
| `classPeriods` |  | array of edFi_studentSectionAttendanceEventClassPeriod | An unordered collection of studentSectionAttendanceEventClassPeriods. |
| `departureTime` |  | string | The time of day the student departed for the attendance event in ISO 8601 format. |
| `educationalEnvironmentDescriptor` |  | descriptor URI | The setting in which a child receives education and related services. |
| `eventDuration` |  | number (double) | The amount of time in days for the event as recognized by the school: 1 day = 1, 1/2 day = 0.5, 1/3 day = 0.33. |
| `sectionAttendanceDuration` |  | integer (int32) | The duration in minutes of the section attendance event. |

### Items in `classPeriods`

| Field | Required | Type | Description |
|---|---|---|---|
| `classPeriodReference` | yes | reference; supply `classPeriodName`, `schoolId` | This entity represents the designation of a regularly scheduled series of class meetings at designated times and days of the week. |

## Endpoints

- `GET /ed-fi/studentSectionAttendanceEvents`
- `POST /ed-fi/studentSectionAttendanceEvents`
- `GET /ed-fi/studentSectionAttendanceEvents/deletes`
- `GET /ed-fi/studentSectionAttendanceEvents/keyChanges`
- `GET /ed-fi/studentSectionAttendanceEvents/partitions`
- `GET /ed-fi/studentSectionAttendanceEvents/{id}`
- `PUT /ed-fi/studentSectionAttendanceEvents/{id}`
- `DELETE /ed-fi/studentSectionAttendanceEvents/{id}`
