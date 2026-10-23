# reportCards

`/ed-fi/reportCards`

This educational entity represents the collection of student grades for courses taken during a grading period.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `gradingPeriodReference` | yes | reference; supply `gradingPeriodDescriptor`, `gradingPeriodName`, `schoolId`, `schoolYear` | This entity represents the time span for which grades are reported. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `gradePointAverages` |  | array of edFi_reportCardGradePointAverage | An unordered collection of reportCardGradePointAverages. |
| `grades` |  | array of edFi_reportCardGrade | An unordered collection of reportCardGrades. |
| `numberOfDaysAbsent` |  | number (double) | The number of days an individual is absent when school is in session during a given reporting period. |
| `numberOfDaysInAttendance` |  | number (double) | The number of days an individual is present when school is in session during a given reporting period. |
| `numberOfDaysTardy` |  | integer (int32) | The number of days an individual is tardy during a given reporting period. |
| `studentCompetencyObjectives` |  | array of edFi_reportCardStudentCompetencyObjective | An unordered collection of reportCardStudentCompetencyObjectives. |

### Items in `gradePointAverages`

| Field | Required | Type | Description |
|---|---|---|---|
| `gradePointAverageTypeDescriptor` | yes | descriptor URI | The system used for calculating the grade point average for an individual. |
| `gradePointAverageValue` | yes | number (double) | The value of the grade points earned divided by the number of credits attempted. |
| `isCumulative` |  | boolean | Indicator of whether or not the Grade Point Average value is cumulative. |
| `maxGradePointAverageValue` |  | number (double) | The maximum value for the grade point average. |

### Items in `grades`

| Field | Required | Type | Description |
|---|---|---|---|
| `gradeReference` | yes | reference; supply `beginDate`, `gradeTypeDescriptor`, `gradingPeriodDescriptor`, `gradingPeriodName`, `gradingPeriodSchoolYear`, `localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName`, `studentUniqueId` | This educational entity represents an overall score or assessment tied to a course over a period of time (i.e., the grading period). |

### Items in `studentCompetencyObjectives`

| Field | Required | Type | Description |
|---|---|---|---|
| `studentCompetencyObjectiveReference` | yes | reference; supply `gradingPeriodDescriptor`, `gradingPeriodName`, `gradingPeriodSchoolId`, `gradingPeriodSchoolYear`, `objective`, `objectiveEducationOrganizationId`, `objectiveGradeLevelDescriptor`, `studentUniqueId` | This entity represents the competency assessed or evaluated for the student against a specific competency objective. |

## Endpoints

- `GET /ed-fi/reportCards`
- `POST /ed-fi/reportCards`
- `GET /ed-fi/reportCards/deletes`
- `GET /ed-fi/reportCards/keyChanges`
- `GET /ed-fi/reportCards/partitions`
- `GET /ed-fi/reportCards/{id}`
- `PUT /ed-fi/reportCards/{id}`
- `DELETE /ed-fi/reportCards/{id}`
