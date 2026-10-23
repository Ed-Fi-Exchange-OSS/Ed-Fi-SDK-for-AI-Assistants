# grades

`/ed-fi/grades`

This educational entity represents an overall score or assessment tied to a course over a period of time
(i.e., the grading period). Student grades are usually a compilation of marks and other scores.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `gradeTypeDescriptor` | yes | descriptor URI | The type of grade reported (e.g., exam, final, grading period). |
| `gradingPeriodReference` | yes | reference; supply `gradingPeriodDescriptor`, `gradingPeriodName`, `schoolId`, `schoolYear` | This entity represents the time span for which grades are reported. |
| `studentSectionAssociationReference` | yes | reference; supply `beginDate`, `localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName`, `studentUniqueId` | This association indicates the course sections to which a student is assigned. |
| `currentGradeAsOfDate` |  | string (date) | As-Of date for a grade posted as the current grade. |
| `currentGradeIndicator` |  | boolean | An indicator that the posted grade is an interim grade for the grading period and not the final grade. |
| `diagnosticStatement` |  | string max 1024 | A statement provided by the teacher that provides information in addition to the grade or assessment score. |
| `gradeEarnedDescription` |  | string max 64 | A description of the grade earned by the learner. |
| `learningStandardGrades` |  | array of edFi_gradeLearningStandardGrade | An unordered collection of gradeLearningStandardGrades. |
| `letterGradeEarned` |  | string max 20 | A final or interim (grading period) indicator of student performance in a class as submitted by the instructor. |
| `numericGradeEarned` |  | number (double) | A final or interim (grading period) indicator of student performance in a class as submitted by the instructor. |
| `performanceBaseConversionDescriptor` |  | descriptor URI | A conversion of the level to a standard set of performance levels. |

### Items in `learningStandardGrades`

| Field | Required | Type | Description |
|---|---|---|---|
| `performanceBaseConversionDescriptor` |  | descriptor URI | A performance level that describes the student proficiency. |
| `diagnosticStatement` |  | string max 1024 | A statement provided by the teacher that provides information in addition to the grade or assessment score. |
| `letterGradeEarned` |  | string max 20 | A final or interim (grading period) indicator of student performance for a learning standard as submitted by the instructor. |
| `numericGradeEarned` |  | number (double) | A final or interim (grading period) indicator of student performance for a learning standard as submitted by the instructor. |
| `learningStandardReference` | yes | reference; supply `learningStandardId` | A statement that describes a specific competency or academic standard. |

## Endpoints

- `GET /ed-fi/grades`
- `POST /ed-fi/grades`
- `GET /ed-fi/grades/deletes`
- `GET /ed-fi/grades/keyChanges`
- `GET /ed-fi/grades/partitions`
- `GET /ed-fi/grades/{id}`
- `PUT /ed-fi/grades/{id}`
- `DELETE /ed-fi/grades/{id}`
