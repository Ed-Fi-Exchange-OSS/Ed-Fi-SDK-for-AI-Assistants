# bellSchedules

`/ed-fi/bellSchedules`

This entity represents the schedule of class period meeting times.

## Natural key

`bellScheduleName`, `schoolReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `bellScheduleName` | key | string max 60 | Name or title of the bell schedule. |
| `classPeriods` | yes | array of edFi_bellScheduleClassPeriod | An unordered collection of bellScheduleClassPeriods. |
| `schoolReference` | key | reference: `schoolId` |  |
| `alternateDayName` |  | string max 20 | An alternate name for the day (e.g., Red, Blue). |
| `dates` |  | array of edFi_bellScheduleDate | An unordered collection of bellScheduleDates. |
| `endTime` |  | string | An indication of the time of day the bell schedule ends. |
| `gradeLevels` |  | array of edFi_bellScheduleGradeLevel | An unordered collection of bellScheduleGradeLevels. |
| `startTime` |  | string | An indication of the time of day the bell schedule begins. |
| `totalInstructionalTime` |  | integer (int32) | The total instructional time in minutes per day for the bell schedule. |

## Endpoints

- `DELETE /ed-fi/bellSchedules/{id}`
- `GET /ed-fi/bellSchedules/deletes`
- `GET /ed-fi/bellSchedules/keyChanges`
- `GET /ed-fi/bellSchedules/partitions`
- `GET /ed-fi/bellSchedules/{id}`
- `GET /ed-fi/bellSchedules`
- `POST /ed-fi/bellSchedules`
- `PUT /ed-fi/bellSchedules/{id}`
