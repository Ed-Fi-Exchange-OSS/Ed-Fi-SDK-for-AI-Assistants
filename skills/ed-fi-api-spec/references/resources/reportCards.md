# reportCards

`/ed-fi/reportCards`

This educational entity represents the collection of student grades for courses taken during a grading period.

## Natural key

`educationOrganizationReference`, `gradingPeriodReference`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `gradingPeriodReference` | key | reference: `gradingPeriodDescriptor`, `gradingPeriodName`, `schoolId`, `schoolYear` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `gradePointAverages` |  | array of edFi_reportCardGradePointAverage | An unordered collection of reportCardGradePointAverages. |
| `grades` |  | array of edFi_reportCardGrade | An unordered collection of reportCardGrades. |
| `numberOfDaysAbsent` |  | number (double) | The number of days an individual is absent when school is in session during a given reporting period. |
| `numberOfDaysInAttendance` |  | number (double) | The number of days an individual is present when school is in session during a given reporting period. |
| `numberOfDaysTardy` |  | integer (int32) | The number of days an individual is tardy during a given reporting period. |
| `studentCompetencyObjectives` |  | array of edFi_reportCardStudentCompetencyObjective | An unordered collection of reportCardStudentCompetencyObjectives. |

## Endpoints

- `DELETE /ed-fi/reportCards/{id}`
- `GET /ed-fi/reportCards/deletes`
- `GET /ed-fi/reportCards/keyChanges`
- `GET /ed-fi/reportCards/partitions`
- `GET /ed-fi/reportCards/{id}`
- `GET /ed-fi/reportCards`
- `POST /ed-fi/reportCards`
- `PUT /ed-fi/reportCards/{id}`
