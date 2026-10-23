# classPeriods

`/ed-fi/classPeriods`

This entity represents the designation of a regularly scheduled series of class meetings at designated times
and days of the week.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `classPeriodName` | yes | string max 60 | An indication of the portion of a typical daily session in which students receive instruction in a specified subject (e.g., morning, sixth period, block period… |
| `schoolReference` | yes | reference; supply `schoolId` | This entity represents an educational organization that includes staff and students who participate in classes and educational activity groups. |
| `meetingTimes` |  | array of edFi_classPeriodMeetingTime | An unordered collection of classPeriodMeetingTimes. |
| `officialAttendancePeriod` |  | boolean | Indicator of whether this class period is used for official daily attendance. |

### Items in `meetingTimes`

| Field | Required | Type | Description |
|---|---|---|---|
| `endTime` | yes | string | An indication of the time of day the meeting time ends. |
| `startTime` | yes | string | An indication of the time of day the meeting time begins. |

## Endpoints

- `GET /ed-fi/classPeriods`
- `POST /ed-fi/classPeriods`
- `GET /ed-fi/classPeriods/deletes`
- `GET /ed-fi/classPeriods/keyChanges`
- `GET /ed-fi/classPeriods/partitions`
- `GET /ed-fi/classPeriods/{id}`
- `PUT /ed-fi/classPeriods/{id}`
- `DELETE /ed-fi/classPeriods/{id}`

`PUT` can change this resource's identifying values; the API cascades the change to records that reference it
(cascading key updates, `x-Ed-Fi-isUpdatable` in the specification).
