# gradebookEntries

`/ed-fi/gradebookEntries`

This entity represents an assignment, homework, or classroom assessment to be recorded in a gradebook.

## Natural key

`gradebookEntryIdentifier`, `namespace`. The natural key can be changed with PUT (cascading key updates).

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `gradebookEntryIdentifier` | key | string max 60 | A unique number or alphanumeric code assigned to a gradebook entry by the source system. |
| `namespace` | key | string max 255 | Namespace URI for the source of the gradebook entry. |
| `gradingPeriodReference` |  | reference: `gradingPeriodDescriptor`, `gradingPeriodName`, `schoolId`, `schoolYear` |  |
| `sectionReference` |  | reference: `localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName` |  |
| `dateAssigned` | yes | string (date) | The date the assignment, homework, or assessment was assigned or executed. |
| `description` |  | string max 1024 | A description of the assignment, homework, or classroom assessment. |
| `dueDate` |  | string (date) | The date the assignment, homework, or assessment is due. |
| `dueTime` |  | string | The time the assignment, homework, or assessment is due. |
| `gradebookEntryTypeDescriptor` |  | descriptor URI | The type of the gradebook entry. |
| `learningStandards` |  | array of edFi_gradebookEntryLearningStandard | An unordered collection of gradebookEntryLearningStandards. |
| `maxPoints` |  | number (double) | The maximum number of points that can be earned for the submission. |
| `sourceSectionIdentifier` | yes | string max 255 | The local identifier assigned to a section. |
| `title` | yes | string max 100 | The name or title of the activity to be recorded in the gradebook entry. |

## Endpoints

- `DELETE /ed-fi/gradebookEntries/{id}`
- `GET /ed-fi/gradebookEntries/deletes`
- `GET /ed-fi/gradebookEntries/keyChanges`
- `GET /ed-fi/gradebookEntries/partitions`
- `GET /ed-fi/gradebookEntries/{id}`
- `GET /ed-fi/gradebookEntries`
- `POST /ed-fi/gradebookEntries`
- `PUT /ed-fi/gradebookEntries/{id}`
