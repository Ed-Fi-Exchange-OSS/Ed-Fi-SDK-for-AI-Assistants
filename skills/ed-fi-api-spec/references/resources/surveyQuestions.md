# surveyQuestions

`/ed-fi/surveyQuestions`

The questions for the survey.

## Natural key

`questionCode`, `surveyReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `questionCode` | key | string max 60 | The identifying code for the question, unique for the survey. |
| `surveyReference` | key | reference: `namespace`, `surveyIdentifier` |  |
| `surveySectionReference` |  | reference: `namespace`, `surveyIdentifier`, `surveySectionTitle` |  |
| `matrices` |  | array of edFi_surveyQuestionMatrix | An unordered collection of surveyQuestionMatrices. |
| `questionFormDescriptor` | yes | descriptor URI | The form or type of question. |
| `questionText` | yes | string max 1024 | The text of the question. |
| `responseChoices` |  | array of edFi_surveyQuestionResponseChoice | An unordered collection of surveyQuestionResponseChoices. |

## Endpoints

- `DELETE /ed-fi/surveyQuestions/{id}`
- `GET /ed-fi/surveyQuestions/deletes`
- `GET /ed-fi/surveyQuestions/keyChanges`
- `GET /ed-fi/surveyQuestions/partitions`
- `GET /ed-fi/surveyQuestions/{id}`
- `GET /ed-fi/surveyQuestions`
- `POST /ed-fi/surveyQuestions`
- `PUT /ed-fi/surveyQuestions/{id}`
