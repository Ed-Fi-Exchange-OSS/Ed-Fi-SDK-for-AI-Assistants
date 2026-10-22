# surveyResponses

`/ed-fi/surveyResponses`

Responses to a Survey for named or anonymous persons.

## Natural key

`surveyResponseIdentifier`, `surveyReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `surveyResponseIdentifier` | key | string max 60 | The identifier of the survey typically from the survey application. |
| `contactReference` |  | reference: `contactUniqueId` |  |
| `staffReference` |  | reference: `staffUniqueId` |  |
| `studentReference` |  | reference: `studentUniqueId` |  |
| `surveyReference` | key | reference: `namespace`, `surveyIdentifier` |  |
| `electronicMailAddress` |  | string max 128 | Email address of the respondent. |
| `fullName` |  | string max 80 | Full name of the respondent. |
| `location` |  | string max 75 | Location of the respondent, often a city, district, or school. |
| `responseDate` | yes | string (date) | Date of the survey response. |
| `responseTime` |  | integer (int32) | The amount of time in seconds it took for the respondent to complete the survey. |
| `surveyLevels` |  | array of edFi_surveyResponseSurveyLevel | An unordered collection of surveyResponseSurveyLevels. |
| `_ext` |  | surveyResponseExtensions |  |

## Endpoints

- `DELETE /ed-fi/surveyResponses/{id}`
- `GET /ed-fi/surveyResponses/deletes`
- `GET /ed-fi/surveyResponses/keyChanges`
- `GET /ed-fi/surveyResponses/partitions`
- `GET /ed-fi/surveyResponses/{id}`
- `GET /ed-fi/surveyResponses`
- `POST /ed-fi/surveyResponses`
- `PUT /ed-fi/surveyResponses/{id}`
