# grades

`/ed-fi/grades`

This educational entity represents an overall score or assessment tied to a course over a period of time (i.e., the grading period). Student grades are usually a compilation of marks and other scores.

## Natural key

`gradeTypeDescriptor`, `gradingPeriodReference`, `studentSectionAssociationReference`. The natural key can be changed with PUT (cascading key updates).

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `gradeTypeDescriptor` | key | descriptor URI | The type of grade reported (e.g., exam, final, grading period). |
| `gradingPeriodReference` | key | reference: `gradingPeriodDescriptor`, `gradingPeriodName`, `schoolId`, `schoolYear` |  |
| `studentSectionAssociationReference` | key | reference: `beginDate`, `localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName`, `studentUniqueId` |  |
| `currentGradeAsOfDate` |  | string (date) | As-Of date for a grade posted as the current grade. |
| `currentGradeIndicator` |  | boolean | An indicator that the posted grade is an interim grade for the grading period and not the final grade. |
| `diagnosticStatement` |  | string max 1024 | A statement provided by the teacher that provides information in addition to the grade or assessment score. |
| `gradeEarnedDescription` |  | string max 64 | A description of the grade earned by the learner. |
| `learningStandardGrades` |  | array of edFi_gradeLearningStandardGrade | An unordered collection of gradeLearningStandardGrades. |
| `letterGradeEarned` |  | string max 20 | A final or interim (grading period) indicator of student performance in a class as submitted by the instructor. |
| `numericGradeEarned` |  | number (double) | A final or interim (grading period) indicator of student performance in a class as submitted by the instructor. |
| `performanceBaseConversionDescriptor` |  | descriptor URI | A conversion of the level to a standard set of performance levels. |

## Endpoints

- `DELETE /ed-fi/grades/{id}`
- `GET /ed-fi/grades/deletes`
- `GET /ed-fi/grades/keyChanges`
- `GET /ed-fi/grades/partitions`
- `GET /ed-fi/grades/{id}`
- `GET /ed-fi/grades`
- `POST /ed-fi/grades`
- `PUT /ed-fi/grades/{id}`
