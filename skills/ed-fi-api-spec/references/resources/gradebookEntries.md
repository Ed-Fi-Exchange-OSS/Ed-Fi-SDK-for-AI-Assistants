# gradebookEntries

`/ed-fi/gradebookEntries`

This entity represents an assignment, homework, or classroom assessment to be recorded in a gradebook.

## Natural key

`gradebookEntryIdentifier`, `namespace`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `gradebookEntryIdentifier` | yes | string max 60 | A unique number or alphanumeric code assigned to a gradebook entry by the source system. |
| `namespace` | yes | string max 255 | Namespace URI for the source of the gradebook entry. |
| `gradingPeriodReference` |  | reference; supply `gradingPeriodDescriptor`, `gradingPeriodName`, `schoolId`, `schoolYear` | This entity represents the time span for which grades are reported. |
| `sectionReference` |  | reference; supply `localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName` | This entity represents a setting in which organized instruction of course content is provided, in-person or otherwise, to one or more students for a given peri… |
| `dateAssigned` | yes | string (date) | The date the assignment, homework, or assessment was assigned or executed. |
| `description` |  | string max 1024 | A description of the assignment, homework, or classroom assessment. |
| `dueDate` |  | string (date) | The date the assignment, homework, or assessment is due. |
| `dueTime` |  | string | The time the assignment, homework, or assessment is due. |
| `gradebookEntryTypeDescriptor` |  | descriptor URI | The type of the gradebook entry. |
| `learningStandards` |  | array of edFi_gradebookEntryLearningStandard | An unordered collection of gradebookEntryLearningStandards. |
| `maxPoints` |  | number (double) | The maximum number of points that can be earned for the submission. |
| `sourceSectionIdentifier` | yes | string max 255 | The local identifier assigned to a section. |
| `title` | yes | string max 100 | The name or title of the activity to be recorded in the gradebook entry. |

### Items in `learningStandards`

| Field | Required | Type | Description |
|---|---|---|---|
| `learningStandardReference` | yes | reference; supply `learningStandardId` | A statement that describes a specific competency or academic standard. |

## Endpoints

- `GET /ed-fi/gradebookEntries`
- `POST /ed-fi/gradebookEntries`
- `GET /ed-fi/gradebookEntries/deletes`
- `GET /ed-fi/gradebookEntries/keyChanges`
- `GET /ed-fi/gradebookEntries/partitions`
- `GET /ed-fi/gradebookEntries/{id}`
- `PUT /ed-fi/gradebookEntries/{id}`
- `DELETE /ed-fi/gradebookEntries/{id}`

`PUT` can change this resource's identifying values; the API cascades the change to records that reference it
(cascading key updates, `x-Ed-Fi-isUpdatable` in the specification).
