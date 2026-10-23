# sessions

`/ed-fi/sessions`

A specific designated unit of time during which instruction is provided, grades are reported and academic
credits are awarded to students (whenever applicable). Sessions serve as organized segments of the academic
year and can be interrupted by vacations or other events.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `sessionName` | yes | string max 60 | The identifier for the calendar for the academic session. |
| `schoolReference` | yes | reference; supply `schoolId` | This entity represents an educational organization that includes staff and students who participate in classes and educational activity groups. |
| `schoolYearTypeReference` | yes | reference; supply `schoolYear` | Identifier for a school year. |
| `academicWeeks` |  | array of edFi_sessionAcademicWeek | An unordered collection of sessionAcademicWeeks. |
| `beginDate` | yes | string (date) | Month, day, and year of the first day of the session. |
| `endDate` | yes | string (date) | Month, day and year of the last day of the session. |
| `gradingPeriods` |  | array of edFi_sessionGradingPeriod | An unordered collection of sessionGradingPeriods. |
| `termDescriptor` | yes | descriptor URI | A descriptor value to indicate the term that the session is associated with. |
| `totalInstructionalDays` | yes | integer (int32) | The total number of instructional days in the school calendar. |

### Items in `academicWeeks`

| Field | Required | Type | Description |
|---|---|---|---|
| `academicWeekReference` | yes | reference; supply `schoolId`, `weekIdentifier` | This entity represents the academic weeks for a school year, optionally captured to support analyses. |

### Items in `gradingPeriods`

| Field | Required | Type | Description |
|---|---|---|---|
| `gradingPeriodReference` | yes | reference; supply `gradingPeriodDescriptor`, `gradingPeriodName`, `schoolId`, `schoolYear` | This entity represents the time span for which grades are reported. |

## Endpoints

- `GET /ed-fi/sessions`
- `POST /ed-fi/sessions`
- `GET /ed-fi/sessions/deletes`
- `GET /ed-fi/sessions/keyChanges`
- `GET /ed-fi/sessions/partitions`
- `GET /ed-fi/sessions/{id}`
- `PUT /ed-fi/sessions/{id}`
- `DELETE /ed-fi/sessions/{id}`

`PUT` can change this resource's identifying values; the API cascades the change to records that reference it
(cascading key updates, `x-Ed-Fi-isUpdatable` in the specification).
