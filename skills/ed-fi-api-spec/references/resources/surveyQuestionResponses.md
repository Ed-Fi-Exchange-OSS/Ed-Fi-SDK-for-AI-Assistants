# surveyQuestionResponses

`/ed-fi/surveyQuestionResponses`

The response to a survey question.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `surveyQuestionReference` | yes | reference; supply `namespace`, `questionCode`, `surveyIdentifier` | The questions for the survey. |
| `surveyResponseReference` | yes | reference; supply `namespace`, `surveyIdentifier`, `surveyResponseIdentifier` | Responses to a Survey for named or anonymous persons. |
| `comment` |  | string max 1024 | Additional information provided by the responder about the question in the survey. |
| `noResponse` |  | boolean | Indicates there was no response to the question. |
| `surveyQuestionMatrixElementResponses` |  | array of edFi_surveyQuestionResponseSurveyQuestionMatrixElementResponse | An unordered collection of surveyQuestionResponseSurveyQuestionMatrixElementResponses. |
| `values` |  | array of edFi_surveyQuestionResponseValue | An unordered collection of surveyQuestionResponseValues. |

### Items in `surveyQuestionMatrixElementResponses`

| Field | Required | Type | Description |
|---|---|---|---|
| `matrixElement` | yes | string max 255 | For matrix questions, the text identifying each row of the matrix. |
| `maxNumericResponse` |  | integer (int32) | The maximum score response to the question. |
| `minNumericResponse` |  | integer (int32) | The minimum score response to the question. |
| `noResponse` |  | boolean | Indicates there was no response to the question. |
| `numericResponse` |  | integer (int32) | The numeric response to the question. |
| `textResponse` |  | string max 2048 | The text response(s) for the question. |

### Items in `values`

| Field | Required | Type | Description |
|---|---|---|---|
| `surveyQuestionResponseValueIdentifier` | yes | integer (int32) | Primary key for the response value; a unique, usually sequential numeric value for a collection of responses, or potentially the value of NumericResponse for a… |
| `numericResponse` |  | integer (int32) | A numeric response to the question. |
| `textResponse` |  | string max 2048 | A text response to the question. |

## Endpoints

- `GET /ed-fi/surveyQuestionResponses`
- `POST /ed-fi/surveyQuestionResponses`
- `GET /ed-fi/surveyQuestionResponses/deletes`
- `GET /ed-fi/surveyQuestionResponses/keyChanges`
- `GET /ed-fi/surveyQuestionResponses/partitions`
- `GET /ed-fi/surveyQuestionResponses/{id}`
- `PUT /ed-fi/surveyQuestionResponses/{id}`
- `DELETE /ed-fi/surveyQuestionResponses/{id}`
