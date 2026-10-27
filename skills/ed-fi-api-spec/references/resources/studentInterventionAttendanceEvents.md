# studentInterventionAttendanceEvents

`/ed-fi/studentInterventionAttendanceEvents`

This event entity represents the recording of whether a student is in attendance for an intervention service.

## Natural key

`attendanceEventCategoryDescriptor`, `eventDate`, `educationOrganizationId`, `interventionIdentificationCode`,
`studentUniqueId`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `attendanceEventCategoryDescriptor` | yes | descriptor URI | A code describing the attendance event, for example: Present Unexcused absence Excused absence Tardy. |
| `eventDate` | yes | string (date) | Date for this attendance event. |
| `interventionReference` | yes | reference; supply `educationOrganizationId`, `interventionIdentificationCode` | An implementation of an instructional approach focusing on the specific techniques and materials used to teach a given subject. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `attendanceEventReason` |  | string max 255 | The reported reason for a student's absence. |
| `educationalEnvironmentDescriptor` |  | descriptor URI | The setting in which a child receives education and related services. |
| `eventDuration` |  | number (double) | The amount of time in days for the event as recognized by the school: 1 day = 1, 1/2 day = 0.5, 1/3 day = 0.33. |
| `interventionDuration` |  | integer (int32) | The duration in minutes of the intervention attendance event. |

## Endpoints

- `GET /ed-fi/studentInterventionAttendanceEvents`
- `POST /ed-fi/studentInterventionAttendanceEvents`
- `GET /ed-fi/studentInterventionAttendanceEvents/deletes`
- `GET /ed-fi/studentInterventionAttendanceEvents/keyChanges`
- `GET /ed-fi/studentInterventionAttendanceEvents/partitions`
- `GET /ed-fi/studentInterventionAttendanceEvents/{id}`
- `PUT /ed-fi/studentInterventionAttendanceEvents/{id}`
- `DELETE /ed-fi/studentInterventionAttendanceEvents/{id}`
