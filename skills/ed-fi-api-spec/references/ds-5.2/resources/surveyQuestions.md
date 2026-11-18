# surveyQuestions

`/ed-fi/surveyQuestions`

The questions for the survey.

## Natural key

`questionCode`, `namespace`, `surveyIdentifier`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `questionCode` | yes | string max 60 | The identifying code for the question, unique for the survey. |
| `surveyReference` | yes | reference; supply `namespace`, `surveyIdentifier` | A survey to identified or anonymous respondents. |
| `surveySectionReference` |  | reference; supply `namespace`, `surveyIdentifier`, `surveySectionTitle` | The section of questions for the survey. |
| `matrices` |  | array of edFi_surveyQuestionMatrix | An unordered collection of surveyQuestionMatrices. |
| `questionFormDescriptor` | yes | descriptor URI | The form or type of question. |
| `questionText` | yes | string max 1024 | The text of the question. |
| `responseChoices` |  | array of edFi_surveyQuestionResponseChoice | An unordered collection of surveyQuestionResponseChoices. |

### Items in `matrices`

| Field | Required | Type | Description |
|---|---|---|---|
| `matrixElement` | yes | string max 255 | For matrix questions, the text identifying each row of the matrix. |
| `maxRawScore` |  | integer (int32) | The maximum score possible on a survey. |
| `minRawScore` |  | integer (int32) | The minimum score possible on a survey. |

### Items in `responseChoices`

| Field | Required | Type | Description |
|---|---|---|---|
| `sortOrder` | yes | integer (int32) | Sort order of this ResponseChoice within the complete list of choices attached to a SurveyQuestion. |
| `numericValue` |  | integer (int32) | A valid numeric response. |
| `textValue` |  | string max 255 | A valid text response. |

## Endpoints

- `GET /ed-fi/surveyQuestions`
- `POST /ed-fi/surveyQuestions`
- `GET /ed-fi/surveyQuestions/deletes`
- `GET /ed-fi/surveyQuestions/keyChanges`
- `GET /ed-fi/surveyQuestions/partitions`
- `GET /ed-fi/surveyQuestions/{id}`
- `PUT /ed-fi/surveyQuestions/{id}`
- `DELETE /ed-fi/surveyQuestions/{id}`
