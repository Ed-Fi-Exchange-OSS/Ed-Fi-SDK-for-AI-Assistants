# studentProgramAttendanceEvents

`/ed-fi/studentProgramAttendanceEvents`

This event entity represents the recording of whether a student is in attendance to receive or participate in
program services.

## Natural key

`attendanceEventCategoryDescriptor`, `eventDate`, `educationOrganizationReference`, `programReference`,
`studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `attendanceEventCategoryDescriptor` | key | descriptor URI | A code describing the attendance event, for example: Present Unexcused absence Excused absence Tardy. |
| `eventDate` | key | string (date) | Date for this attendance event. |
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `programReference` | key | reference: `educationOrganizationId`, `programName`, `programTypeDescriptor` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `attendanceEventReason` |  | string max 255 | The reported reason for a student's absence. |
| `educationalEnvironmentDescriptor` |  | descriptor URI | The setting in which a child receives education and related services. |
| `eventDuration` |  | number (double) | The amount of time in days for the event as recognized by the school: 1 day = 1, 1/2 day = 0.5, 1/3 day = 0.33. |
| `programAttendanceDuration` |  | integer (int32) | The duration in minutes of the program attendance event. |

## Endpoints

- `DELETE /ed-fi/studentProgramAttendanceEvents/{id}`
- `GET /ed-fi/studentProgramAttendanceEvents/deletes`
- `GET /ed-fi/studentProgramAttendanceEvents/keyChanges`
- `GET /ed-fi/studentProgramAttendanceEvents/partitions`
- `GET /ed-fi/studentProgramAttendanceEvents/{id}`
- `GET /ed-fi/studentProgramAttendanceEvents`
- `POST /ed-fi/studentProgramAttendanceEvents`
- `PUT /ed-fi/studentProgramAttendanceEvents/{id}`
