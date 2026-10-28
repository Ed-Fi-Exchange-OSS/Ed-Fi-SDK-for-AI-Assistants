# learningStandards

`/ed-fi/learningStandards`

A statement that describes a specific competency or academic standard.

## Natural key

`learningStandardId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `academicSubjects` | yes | array of edFi_learningStandardAcademicSubject | An unordered collection of learningStandardAcademicSubjects. |
| `gradeLevels` | yes | array of edFi_learningStandardGradeLevel | An unordered collection of learningStandardGradeLevels. |
| `learningStandardId` | yes | string max 60 | The identifier for the specific learning standard (e.g., 111.15.3.1.A). |
| `parentLearningStandardReference` |  | reference; supply `learningStandardId` | A statement that describes a specific competency or academic standard. |
| `contentStandard` | yes | edFi_learningStandardContentStandard |  |
| `courseTitle` |  | string max 60 | The official course title with which this learning standard is associated. |
| `description` | yes | string max 1024 | The text of the statement. |
| `identificationCodes` |  | array of edFi_learningStandardIdentificationCode | An unordered collection of learningStandardIdentificationCodes. |
| `learningStandardCategoryDescriptor` |  | descriptor URI | An additional classification of the type of a specific learning standard. |
| `learningStandardItemCode` |  | string max 60 | A code designated by the promulgating body to identify the statement, e.g. 1.N.3 (usually not globally unique). |
| `learningStandardScopeDescriptor` |  | descriptor URI | Signals the scope of usage the standard. |
| `namespace` | yes | string max 255 | The namespace of the organization or entity who governs the standard. |
| `successCriteria` |  | string max 150 | One or more statements that describes the criteria used by teachers and students to check for attainment of a learning standard. |
| `uri` |  | string max 255 | An unambiguous reference to the statement using a network-resolvable URI. |

### Items in `academicSubjects`

| Field | Required | Type | Description |
|---|---|---|---|
| `academicSubjectDescriptor` | yes | descriptor URI | Subject area for the learning standard. |

### Items in `gradeLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `gradeLevelDescriptor` | yes | descriptor URI | The grade levels for the specific learning standard. |

### Items in `identificationCodes`

| Field | Required | Type | Description |
|---|---|---|---|
| `contentStandardName` | yes | string max 65 | The name of the content standard, for example Common Core. |
| `identificationCode` | yes | string max 60 | A unique number or alphanumeric code assigned to a Learning Standard. |

## Endpoints

- `GET /ed-fi/learningStandards`
- `POST /ed-fi/learningStandards`
- `GET /ed-fi/learningStandards/deletes`
- `GET /ed-fi/learningStandards/keyChanges`
- `GET /ed-fi/learningStandards/partitions`
- `GET /ed-fi/learningStandards/{id}`
- `PUT /ed-fi/learningStandards/{id}`
- `DELETE /ed-fi/learningStandards/{id}`
