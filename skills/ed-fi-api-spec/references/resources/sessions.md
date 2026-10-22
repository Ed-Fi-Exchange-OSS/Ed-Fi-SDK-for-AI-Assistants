# sessions

`/ed-fi/sessions`

A specific designated unit of time during which instruction is provided, grades are reported and academic
credits are awarded to students (whenever applicable). Sessions serve as organized segments of the academic
year and can be interrupted by vacations or other events.

## Natural key

`sessionName`, `schoolReference`, `schoolYearTypeReference`. The natural key can be changed with PUT
(cascading key updates).

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `sessionName` | key | string max 60 | The identifier for the calendar for the academic session. |
| `schoolReference` | key | reference: `schoolId` |  |
| `schoolYearTypeReference` | key | reference: `schoolYear` |  |
| `academicWeeks` |  | array of edFi_sessionAcademicWeek | An unordered collection of sessionAcademicWeeks. |
| `beginDate` | yes | string (date) | Month, day, and year of the first day of the session. |
| `endDate` | yes | string (date) | Month, day and year of the last day of the session. |
| `gradingPeriods` |  | array of edFi_sessionGradingPeriod | An unordered collection of sessionGradingPeriods. |
| `termDescriptor` | yes | descriptor URI | A descriptor value to indicate the term that the session is associated with. |
| `totalInstructionalDays` | yes | integer (int32) | The total number of instructional days in the school calendar. |

## Endpoints

- `DELETE /ed-fi/sessions/{id}`
- `GET /ed-fi/sessions/deletes`
- `GET /ed-fi/sessions/keyChanges`
- `GET /ed-fi/sessions/partitions`
- `GET /ed-fi/sessions/{id}`
- `GET /ed-fi/sessions`
- `POST /ed-fi/sessions`
- `PUT /ed-fi/sessions/{id}`
