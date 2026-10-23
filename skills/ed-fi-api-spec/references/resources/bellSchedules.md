# bellSchedules

`/ed-fi/bellSchedules`

This entity represents the schedule of class period meeting times.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `bellScheduleName` | yes | string max 60 | Name or title of the bell schedule. |
| `classPeriods` | yes | array of edFi_bellScheduleClassPeriod | An unordered collection of bellScheduleClassPeriods. |
| `schoolReference` | yes | reference; supply `schoolId` | This entity represents an educational organization that includes staff and students who participate in classes and educational activity groups. |
| `alternateDayName` |  | string max 20 | An alternate name for the day (e.g., Red, Blue). |
| `dates` |  | array of edFi_bellScheduleDate | An unordered collection of bellScheduleDates. |
| `endTime` |  | string | An indication of the time of day the bell schedule ends. |
| `gradeLevels` |  | array of edFi_bellScheduleGradeLevel | An unordered collection of bellScheduleGradeLevels. |
| `startTime` |  | string | An indication of the time of day the bell schedule begins. |
| `totalInstructionalTime` |  | integer (int32) | The total instructional time in minutes per day for the bell schedule. |

### Items in `classPeriods`

| Field | Required | Type | Description |
|---|---|---|---|
| `classPeriodReference` | yes | reference; supply `classPeriodName`, `schoolId` | This entity represents the designation of a regularly scheduled series of class meetings at designated times and days of the week. |

### Items in `dates`

| Field | Required | Type | Description |
|---|---|---|---|
| `date` | yes | string (date) | The dates for which the bell schedule applies. |

### Items in `gradeLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `gradeLevelDescriptor` | yes | descriptor URI | The grade levels the particular bell schedule applies to. |

## Endpoints

- `GET /ed-fi/bellSchedules`
- `POST /ed-fi/bellSchedules`
- `GET /ed-fi/bellSchedules/deletes`
- `GET /ed-fi/bellSchedules/keyChanges`
- `GET /ed-fi/bellSchedules/partitions`
- `GET /ed-fi/bellSchedules/{id}`
- `PUT /ed-fi/bellSchedules/{id}`
- `DELETE /ed-fi/bellSchedules/{id}`
