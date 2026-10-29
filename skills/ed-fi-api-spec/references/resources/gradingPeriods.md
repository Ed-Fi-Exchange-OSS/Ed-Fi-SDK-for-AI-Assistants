# gradingPeriods

`/ed-fi/gradingPeriods`

This entity represents the time span for which grades are reported.

## Natural key

`gradingPeriodDescriptor`, `gradingPeriodName`, `schoolId`, `schoolYear`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `gradingPeriodDescriptor` | yes | descriptor URI | The state's name of the period for which grades are reported. |
| `gradingPeriodName` | yes | string max 60 | The school's descriptive name of the grading period. |
| `schoolReference` | yes | reference; supply `schoolId` | This entity represents an educational organization that includes staff and students who participate in classes and educational activity groups. |
| `schoolYearTypeReference` | yes | reference; supply `schoolYear` | Identifier for a school year. |
| `beginDate` | yes | string (date) | Month, day, and year of the first day of the grading period. |
| `endDate` | yes | string (date) | Month, day, and year of the last day of the grading period. |
| `periodSequence` |  | integer (int32) | The sequential order of this period relative to other periods. |
| `totalInstructionalDays` | yes | integer (int32) | Total days available for educational instruction during the grading period. |

## Endpoints

- `GET /ed-fi/gradingPeriods`
- `POST /ed-fi/gradingPeriods`
- `GET /ed-fi/gradingPeriods/deletes`
- `GET /ed-fi/gradingPeriods/keyChanges`
- `GET /ed-fi/gradingPeriods/partitions`
- `GET /ed-fi/gradingPeriods/{id}`
- `PUT /ed-fi/gradingPeriods/{id}`
- `DELETE /ed-fi/gradingPeriods/{id}`
