# objectiveAssessments

`/ed-fi/objectiveAssessments`

This entity represents subtests that assess specific learning objectives.

## Natural key

`identificationCode`, `assessmentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `identificationCode` | key | string max 60 | A unique number or alphanumeric code assigned to an objective assessment by a school, school system, a state, or other agency or entity. |
| `assessmentReference` | key | reference: `assessmentIdentifier`, `namespace` |  |
| `parentObjectiveAssessmentReference` |  | reference: `assessmentIdentifier`, `identificationCode`, `namespace` |  |
| `academicSubjectDescriptor` |  | descriptor URI | The subject area of the objective assessment. |
| `assessmentItems` |  | array of edFi_objectiveAssessmentAssessmentItem | An unordered collection of objectiveAssessmentAssessmentItems. |
| `description` |  | string max 1024 | The description of the objective assessment (e.g., vocabulary, measurement, or geometry). |
| `learningStandards` |  | array of edFi_objectiveAssessmentLearningStandard | An unordered collection of objectiveAssessmentLearningStandards. |
| `maxRawScore` |  | number (double) | The maximum raw score achievable across all assessment items that are correct and scored at the maximum. |
| `nomenclature` |  | string max 100 | Reflects the specific nomenclature used for this level of objective assessment. |
| `percentOfAssessment` |  | number (double) | The percentage of the assessment that tests this objective. |
| `performanceLevels` |  | array of edFi_objectiveAssessmentPerformanceLevel | An unordered collection of objectiveAssessmentPerformanceLevels. |
| `scores` |  | array of edFi_objectiveAssessmentScore | An unordered collection of objectiveAssessmentScores. |

## Endpoints

- `DELETE /ed-fi/objectiveAssessments/{id}`
- `GET /ed-fi/objectiveAssessments/deletes`
- `GET /ed-fi/objectiveAssessments/keyChanges`
- `GET /ed-fi/objectiveAssessments/partitions`
- `GET /ed-fi/objectiveAssessments/{id}`
- `GET /ed-fi/objectiveAssessments`
- `POST /ed-fi/objectiveAssessments`
- `PUT /ed-fi/objectiveAssessments/{id}`
