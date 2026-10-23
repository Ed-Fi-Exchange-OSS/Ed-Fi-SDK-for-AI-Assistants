# studentProgramAttendanceEvents

`/ed-fi/studentProgramAttendanceEvents`

This event entity represents the recording of whether a student is in attendance to receive or participate in
program services.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `attendanceEventCategoryDescriptor` | yes | descriptor URI | A code describing the attendance event, for example: Present Unexcused absence Excused absence Tardy. |
| `eventDate` | yes | string (date) | Date for this attendance event. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `programReference` | yes | reference; supply `educationOrganizationId`, `programName`, `programTypeDescriptor` | This entity represents any program designed to work in conjunction with, or as a supplement to, the main academic program. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `attendanceEventReason` |  | string max 255 | The reported reason for a student's absence. |
| `educationalEnvironmentDescriptor` |  | descriptor URI | The setting in which a child receives education and related services. |
| `eventDuration` |  | number (double) | The amount of time in days for the event as recognized by the school: 1 day = 1, 1/2 day = 0.5, 1/3 day = 0.33. |
| `programAttendanceDuration` |  | integer (int32) | The duration in minutes of the program attendance event. |

## Endpoints

- `GET /ed-fi/studentProgramAttendanceEvents`
- `POST /ed-fi/studentProgramAttendanceEvents`
- `GET /ed-fi/studentProgramAttendanceEvents/deletes`
- `GET /ed-fi/studentProgramAttendanceEvents/keyChanges`
- `GET /ed-fi/studentProgramAttendanceEvents/partitions`
- `GET /ed-fi/studentProgramAttendanceEvents/{id}`
- `PUT /ed-fi/studentProgramAttendanceEvents/{id}`
- `DELETE /ed-fi/studentProgramAttendanceEvents/{id}`
