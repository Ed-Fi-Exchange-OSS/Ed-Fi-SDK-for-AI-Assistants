# surveyResponseEducationOrganizationTargetAssociations

`/ed-fi/surveyResponseEducationOrganizationTargetAssociations`

This association provides information about the survey being taken and the education organization the survey
is about.

## Natural key

`educationOrganizationId`, `namespace`, `surveyIdentifier`, `surveyResponseIdentifier`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `surveyResponseReference` | yes | reference; supply `namespace`, `surveyIdentifier`, `surveyResponseIdentifier` | Responses to a Survey for named or anonymous persons. |

## Endpoints

- `GET /ed-fi/surveyResponseEducationOrganizationTargetAssociations`
- `POST /ed-fi/surveyResponseEducationOrganizationTargetAssociations`
- `GET /ed-fi/surveyResponseEducationOrganizationTargetAssociations/deletes`
- `GET /ed-fi/surveyResponseEducationOrganizationTargetAssociations/keyChanges`
- `GET /ed-fi/surveyResponseEducationOrganizationTargetAssociations/partitions`
- `GET /ed-fi/surveyResponseEducationOrganizationTargetAssociations/{id}`
- `PUT /ed-fi/surveyResponseEducationOrganizationTargetAssociations/{id}`
- `DELETE /ed-fi/surveyResponseEducationOrganizationTargetAssociations/{id}`
