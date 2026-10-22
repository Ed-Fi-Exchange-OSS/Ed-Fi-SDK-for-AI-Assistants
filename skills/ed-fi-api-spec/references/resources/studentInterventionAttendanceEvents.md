# studentInterventionAttendanceEvents

`/ed-fi/studentInterventionAttendanceEvents`

This event entity represents the recording of whether a student is in attendance for an intervention service.

## Natural key

`attendanceEventCategoryDescriptor`, `eventDate`, `interventionReference`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `attendanceEventCategoryDescriptor` | key | descriptor URI | A code describing the attendance event, for example: Present Unexcused absence Excused absence Tardy. |
| `eventDate` | key | string (date) | Date for this attendance event. |
| `interventionReference` | key | reference: `educationOrganizationId`, `interventionIdentificationCode` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `attendanceEventReason` |  | string max 255 | The reported reason for a student's absence. |
| `educationalEnvironmentDescriptor` |  | descriptor URI | The setting in which a child receives education and related services. |
| `eventDuration` |  | number (double) | The amount of time in days for the event as recognized by the school: 1 day = 1, 1/2 day = 0.5, 1/3 day = 0.33. |
| `interventionDuration` |  | integer (int32) | The duration in minutes of the intervention attendance event. |

## Endpoints

- `DELETE /ed-fi/studentInterventionAttendanceEvents/{id}`
- `GET /ed-fi/studentInterventionAttendanceEvents/deletes`
- `GET /ed-fi/studentInterventionAttendanceEvents/keyChanges`
- `GET /ed-fi/studentInterventionAttendanceEvents/partitions`
- `GET /ed-fi/studentInterventionAttendanceEvents/{id}`
- `GET /ed-fi/studentInterventionAttendanceEvents`
- `POST /ed-fi/studentInterventionAttendanceEvents`
- `PUT /ed-fi/studentInterventionAttendanceEvents/{id}`
