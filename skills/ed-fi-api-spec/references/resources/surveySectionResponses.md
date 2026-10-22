# surveySectionResponses

`/ed-fi/surveySectionResponses`

Optional information about the responses provided for a section of a survey.

## Natural key

`surveyResponseReference`, `surveySectionReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `surveyResponseReference` | key | reference: `namespace`, `surveyIdentifier`, `surveyResponseIdentifier` |  |
| `surveySectionReference` | key | reference: `namespace`, `surveyIdentifier`, `surveySectionTitle` |  |
| `sectionRating` |  | number (double) | Numeric rating computed from the survey responses for the section. |

## Endpoints

- `DELETE /ed-fi/surveySectionResponses/{id}`
- `GET /ed-fi/surveySectionResponses/deletes`
- `GET /ed-fi/surveySectionResponses/keyChanges`
- `GET /ed-fi/surveySectionResponses/partitions`
- `GET /ed-fi/surveySectionResponses/{id}`
- `GET /ed-fi/surveySectionResponses`
- `POST /ed-fi/surveySectionResponses`
- `PUT /ed-fi/surveySectionResponses/{id}`
