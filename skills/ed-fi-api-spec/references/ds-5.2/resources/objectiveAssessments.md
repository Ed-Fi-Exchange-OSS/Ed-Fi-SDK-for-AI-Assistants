# objectiveAssessments

`/ed-fi/objectiveAssessments`

This entity represents subtests that assess specific learning objectives.

## Natural key

`identificationCode`, `assessmentIdentifier`, `namespace`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `identificationCode` | yes | string max 60 | A unique number or alphanumeric code assigned to an objective assessment by a school, school system, a state, or other agency or entity. |
| `assessmentReference` | yes | reference; supply `assessmentIdentifier`, `namespace` | This entity represents a tool, instrument, process, or exhibition composed of a systematic sampling of behavior for measuring a student's competence, knowledge… |
| `parentObjectiveAssessmentReference` |  | reference; supply `assessmentIdentifier`, `identificationCode`, `namespace` | This entity represents subtests that assess specific learning objectives. |
| `academicSubjectDescriptor` |  | descriptor URI | The subject area of the objective assessment. |
| `assessmentItems` |  | array of edFi_objectiveAssessmentAssessmentItem | An unordered collection of objectiveAssessmentAssessmentItems. |
| `description` |  | string max 1024 | The description of the objective assessment (e.g., vocabulary, measurement, or geometry). |
| `learningStandards` |  | array of edFi_objectiveAssessmentLearningStandard | An unordered collection of objectiveAssessmentLearningStandards. |
| `maxRawScore` |  | number (double) | The maximum raw score achievable across all assessment items that are correct and scored at the maximum. |
| `nomenclature` |  | string max 100 | Reflects the specific nomenclature used for this level of objective assessment. |
| `percentOfAssessment` |  | number (double) | The percentage of the assessment that tests this objective. |
| `performanceLevels` |  | array of edFi_objectiveAssessmentPerformanceLevel | An unordered collection of objectiveAssessmentPerformanceLevels. |
| `scores` |  | array of edFi_objectiveAssessmentScore | An unordered collection of objectiveAssessmentScores. |

### Items in `assessmentItems`

| Field | Required | Type | Description |
|---|---|---|---|
| `assessmentItemReference` | yes | reference; supply `assessmentIdentifier`, `identificationCode`, `namespace` | This entity represents one of many single measures that make up an assessment. |

### Items in `learningStandards`

| Field | Required | Type | Description |
|---|---|---|---|
| `learningStandardReference` | yes | reference; supply `learningStandardId` | A statement that describes a specific competency or academic standard. |

### Items in `performanceLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `assessmentReportingMethodDescriptor` | yes | descriptor URI | The method that the instructor of the class uses to report the performance and achievement of all students. |
| `performanceLevelDescriptor` | yes | descriptor URI | The performance level(s) defined for the assessment. |
| `resultDatatypeTypeDescriptor` |  | descriptor URI | The datatype of the result. |
| `maximumScore` |  | string max 35 | The maximum score to make the indicated level of performance. |
| `minimumScore` |  | string max 35 | The minimum score required to make the indicated level of performance. |
| `performanceLevelIndicatorName` |  | string max 60 | The name of the indicator being measured for a collection of performance level values. |

### Items in `scores`

| Field | Required | Type | Description |
|---|---|---|---|
| `assessmentReportingMethodDescriptor` | yes | descriptor URI | The method that the administrator of the assessment uses to report the performance and achievement of all students. |
| `resultDatatypeTypeDescriptor` |  | descriptor URI | The datatype of the result. |
| `maximumScore` |  | string max 35 | The maximum score possible on the assessment. |
| `minimumScore` |  | string max 35 | The minimum score possible on the assessment. |

## Endpoints

- `GET /ed-fi/objectiveAssessments`
- `POST /ed-fi/objectiveAssessments`
- `GET /ed-fi/objectiveAssessments/deletes`
- `GET /ed-fi/objectiveAssessments/keyChanges`
- `GET /ed-fi/objectiveAssessments/partitions`
- `GET /ed-fi/objectiveAssessments/{id}`
- `PUT /ed-fi/objectiveAssessments/{id}`
- `DELETE /ed-fi/objectiveAssessments/{id}`
