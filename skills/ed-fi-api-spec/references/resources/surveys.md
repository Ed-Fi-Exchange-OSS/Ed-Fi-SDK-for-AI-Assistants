# surveys

`/ed-fi/surveys`

A survey to identified or anonymous respondents.

## Natural key

`namespace`, `surveyIdentifier`, `schoolYearTypeReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `namespace` | key | string max 255 | Namespace for the survey. |
| `surveyIdentifier` | key | string max 60 | The unique survey identifier from the survey tool. |
| `educationOrganizationReference` |  | reference: `educationOrganizationId` |  |
| `schoolYearTypeReference` | key | reference: `schoolYear` |  |
| `sessionReference` |  | reference: `schoolId`, `schoolYear`, `sessionName` |  |
| `numberAdministered` |  | integer (int32) | Number of persons to whom this survey was administered. |
| `surveyCategoryDescriptor` |  | descriptor URI | The category or type of survey. |
| `surveyTitle` | yes | string max 255 | The title of the survey. |

## Endpoints

- `DELETE /ed-fi/surveys/{id}`
- `GET /ed-fi/surveys/deletes`
- `GET /ed-fi/surveys/keyChanges`
- `GET /ed-fi/surveys/partitions`
- `GET /ed-fi/surveys/{id}`
- `GET /ed-fi/surveys`
- `POST /ed-fi/surveys`
- `PUT /ed-fi/surveys/{id}`
