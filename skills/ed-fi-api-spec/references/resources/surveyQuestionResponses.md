# surveyQuestionResponses

`/ed-fi/surveyQuestionResponses`

The response to a survey question.

## Natural key

`surveyQuestionReference`, `surveyResponseReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `surveyQuestionReference` | key | reference: `namespace`, `questionCode`, `surveyIdentifier` |  |
| `surveyResponseReference` | key | reference: `namespace`, `surveyIdentifier`, `surveyResponseIdentifier` |  |
| `comment` |  | string max 1024 | Additional information provided by the responder about the question in the survey. |
| `noResponse` |  | boolean | Indicates there was no response to the question. |
| `surveyQuestionMatrixElementResponses` |  | array of edFi_surveyQuestionResponseSurveyQuestionMatrixElementResponse | An unordered collection of surveyQuestionResponseSurveyQuestionMatrixElementResponses. |
| `values` |  | array of edFi_surveyQuestionResponseValue | An unordered collection of surveyQuestionResponseValues. |

## Endpoints

- `DELETE /ed-fi/surveyQuestionResponses/{id}`
- `GET /ed-fi/surveyQuestionResponses/deletes`
- `GET /ed-fi/surveyQuestionResponses/keyChanges`
- `GET /ed-fi/surveyQuestionResponses/partitions`
- `GET /ed-fi/surveyQuestionResponses/{id}`
- `GET /ed-fi/surveyQuestionResponses`
- `POST /ed-fi/surveyQuestionResponses`
- `PUT /ed-fi/surveyQuestionResponses/{id}`
