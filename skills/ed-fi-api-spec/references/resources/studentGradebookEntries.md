# studentGradebookEntries

`/ed-fi/studentGradebookEntries`

This entity holds a student's grade or competency level for a gradebook entry.

## Natural key

`gradebookEntryReference`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `gradebookEntryReference` | key | reference: `gradebookEntryIdentifier`, `namespace` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `assignmentLateStatusDescriptor` |  | descriptor URI | Status of whether the assignment was submitted after the due date and/or marked as. |
| `competencyLevelDescriptor` |  | descriptor URI | The competency level assessed for the student for the referenced learning objective. |
| `dateFulfilled` |  | string (date) | The date an assignment was turned in or the date of an assessment. |
| `diagnosticStatement` |  | string max 1024 | A statement provided by the teacher that provides information in addition to the grade or assessment score. |
| `letterGradeEarned` |  | string max 20 | A final or interim (grading period) indicator of student performance in a class as submitted by the instructor. |
| `numericGradeEarned` |  | number (double) | A final or interim (grading period) indicator of student performance in a class as submitted by the instructor. |
| `pointsEarned` |  | number (double) | The points earned for the submission. |
| `submissionStatusDescriptor` |  | descriptor URI | The status of the student's submission. |
| `timeFulfilled` |  | string | The time an assignment was turned in on the date fulfilled. |

## Endpoints

- `DELETE /ed-fi/studentGradebookEntries/{id}`
- `GET /ed-fi/studentGradebookEntries/deletes`
- `GET /ed-fi/studentGradebookEntries/keyChanges`
- `GET /ed-fi/studentGradebookEntries/partitions`
- `GET /ed-fi/studentGradebookEntries/{id}`
- `GET /ed-fi/studentGradebookEntries`
- `POST /ed-fi/studentGradebookEntries`
- `PUT /ed-fi/studentGradebookEntries/{id}`
