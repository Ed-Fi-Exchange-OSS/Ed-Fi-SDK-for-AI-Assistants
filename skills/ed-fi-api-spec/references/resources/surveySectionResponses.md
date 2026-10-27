# surveySectionResponses

`/ed-fi/surveySectionResponses`

Optional information about the responses provided for a section of a survey.

## Natural key

`namespace`, `surveyIdentifier`, `surveyResponseIdentifier`, `surveySectionTitle`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `surveyResponseReference` | yes | reference; supply `namespace`, `surveyIdentifier`, `surveyResponseIdentifier` | Responses to a Survey for named or anonymous persons. |
| `surveySectionReference` | yes | reference; supply `namespace`, `surveyIdentifier`, `surveySectionTitle` | The section of questions for the survey. |
| `sectionRating` |  | number (double) | Numeric rating computed from the survey responses for the section. |

## Endpoints

- `GET /ed-fi/surveySectionResponses`
- `POST /ed-fi/surveySectionResponses`
- `GET /ed-fi/surveySectionResponses/deletes`
- `GET /ed-fi/surveySectionResponses/keyChanges`
- `GET /ed-fi/surveySectionResponses/partitions`
- `GET /ed-fi/surveySectionResponses/{id}`
- `PUT /ed-fi/surveySectionResponses/{id}`
- `DELETE /ed-fi/surveySectionResponses/{id}`
