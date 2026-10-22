# classPeriods

`/ed-fi/classPeriods`

This entity represents the designation of a regularly scheduled series of class meetings at designated times
and days of the week.

## Natural key

`classPeriodName`, `schoolReference`. The natural key can be changed with PUT (cascading key updates).

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `classPeriodName` | key | string max 60 | An indication of the portion of a typical daily session in which students receive instruction in a specified subject (e.g., morning, sixth period, block period… |
| `schoolReference` | key | reference: `schoolId` |  |
| `meetingTimes` |  | array of edFi_classPeriodMeetingTime | An unordered collection of classPeriodMeetingTimes. |
| `officialAttendancePeriod` |  | boolean | Indicator of whether this class period is used for official daily attendance. |

## Endpoints

- `DELETE /ed-fi/classPeriods/{id}`
- `GET /ed-fi/classPeriods/deletes`
- `GET /ed-fi/classPeriods/keyChanges`
- `GET /ed-fi/classPeriods/partitions`
- `GET /ed-fi/classPeriods/{id}`
- `GET /ed-fi/classPeriods`
- `POST /ed-fi/classPeriods`
- `PUT /ed-fi/classPeriods/{id}`
