# studentSchoolAttendanceEvents

`/ed-fi/studentSchoolAttendanceEvents`

This event entity represents the recording of whether a student is in attendance for a school day.

## Natural key

`attendanceEventCategoryDescriptor`, `eventDate`, `schoolId`, `schoolYear`, `sessionName`, `studentUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `attendanceEventCategoryDescriptor` | yes | descriptor URI | A code describing the attendance event, for example: Present Unexcused absence Excused absence Tardy. |
| `eventDate` | yes | string (date) | Date for this attendance event. |
| `schoolReference` | yes | reference; supply `schoolId` | This entity represents an educational organization that includes staff and students who participate in classes and educational activity groups. |
| `sessionReference` | yes | reference; supply `schoolId`, `schoolYear`, `sessionName` | A specific designated unit of time during which instruction is provided, grades are reported and academic credits are awarded to students (whenever applicable). |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `arrivalTime` |  | string | The time of day the student arrived for the attendance event in ISO 8601 format. |
| `attendanceEventReason` |  | string max 255 | The reported reason for a student's absence. |
| `departureTime` |  | string | The time of day the student departed for the attendance event in ISO 8601 format. |
| `educationalEnvironmentDescriptor` |  | descriptor URI | The setting in which a child receives education and related services. |
| `eventDuration` |  | number (double) | The amount of time in days for the event as recognized by the school: 1 day = 1, 1/2 day = 0.5, 1/3 day = 0.33. |
| `schoolAttendanceDuration` |  | integer (int32) | The duration in minutes of the school attendance event. |

## Endpoints

- `GET /ed-fi/studentSchoolAttendanceEvents`
- `POST /ed-fi/studentSchoolAttendanceEvents`
- `GET /ed-fi/studentSchoolAttendanceEvents/deletes`
- `GET /ed-fi/studentSchoolAttendanceEvents/keyChanges`
- `GET /ed-fi/studentSchoolAttendanceEvents/partitions`
- `GET /ed-fi/studentSchoolAttendanceEvents/{id}`
- `PUT /ed-fi/studentSchoolAttendanceEvents/{id}`
- `DELETE /ed-fi/studentSchoolAttendanceEvents/{id}`
