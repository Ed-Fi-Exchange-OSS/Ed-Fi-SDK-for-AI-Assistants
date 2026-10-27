# surveyResponses

`/ed-fi/surveyResponses`

Responses to a Survey for named or anonymous persons.

## Natural key

`surveyResponseIdentifier`, `namespace`, `surveyIdentifier`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `surveyResponseIdentifier` | yes | string max 60 | The identifier of the survey typically from the survey application. |
| `contactReference` |  | reference; supply `contactUniqueId` | This entity represents a contact of a student, such as a parent, guardian or caretaker. |
| `staffReference` |  | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |
| `studentReference` |  | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `surveyReference` | yes | reference; supply `namespace`, `surveyIdentifier` | A survey to identified or anonymous respondents. |
| `electronicMailAddress` |  | string max 128 | Email address of the respondent. |
| `fullName` |  | string max 80 | Full name of the respondent. |
| `location` |  | string max 75 | Location of the respondent, often a city, district, or school. |
| `responseDate` | yes | string (date) | Date of the survey response. |
| `responseTime` |  | integer (int32) | The amount of time in seconds it took for the respondent to complete the survey. |
| `surveyLevels` |  | array of edFi_surveyResponseSurveyLevel | An unordered collection of surveyResponseSurveyLevels. |
| `_ext` |  | surveyResponseExtensions |  |

### Items in `surveyLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `surveyLevelDescriptor` | yes | descriptor URI | Provides information about the respondents of a survey and how they can be grouped together. |

## Endpoints

- `GET /ed-fi/surveyResponses`
- `POST /ed-fi/surveyResponses`
- `GET /ed-fi/surveyResponses/deletes`
- `GET /ed-fi/surveyResponses/keyChanges`
- `GET /ed-fi/surveyResponses/partitions`
- `GET /ed-fi/surveyResponses/{id}`
- `PUT /ed-fi/surveyResponses/{id}`
- `DELETE /ed-fi/surveyResponses/{id}`
