# gradingPeriods

`/ed-fi/gradingPeriods`

This entity represents the time span for which grades are reported.

## Natural key

`gradingPeriodDescriptor`, `gradingPeriodName`, `schoolReference`, `schoolYearTypeReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `gradingPeriodDescriptor` | key | descriptor URI | The state's name of the period for which grades are reported. |
| `gradingPeriodName` | key | string max 60 | The school's descriptive name of the grading period. |
| `schoolReference` | key | reference: `schoolId` |  |
| `schoolYearTypeReference` | key | reference: `schoolYear` |  |
| `beginDate` | yes | string (date) | Month, day, and year of the first day of the grading period. |
| `endDate` | yes | string (date) | Month, day, and year of the last day of the grading period. |
| `periodSequence` |  | integer (int32) | The sequential order of this period relative to other periods. |
| `totalInstructionalDays` | yes | integer (int32) | Total days available for educational instruction during the grading period. |

## Endpoints

- `DELETE /ed-fi/gradingPeriods/{id}`
- `GET /ed-fi/gradingPeriods/deletes`
- `GET /ed-fi/gradingPeriods/keyChanges`
- `GET /ed-fi/gradingPeriods/partitions`
- `GET /ed-fi/gradingPeriods/{id}`
- `GET /ed-fi/gradingPeriods`
- `POST /ed-fi/gradingPeriods`
- `PUT /ed-fi/gradingPeriods/{id}`
