# surveyResponseEducationOrganizationTargetAssociations

`/ed-fi/surveyResponseEducationOrganizationTargetAssociations`

This association provides information about the survey being taken and the education organization the survey is about.

## Natural key

`educationOrganizationReference`, `surveyResponseReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `surveyResponseReference` | key | reference: `namespace`, `surveyIdentifier`, `surveyResponseIdentifier` |  |

## Endpoints

- `DELETE /ed-fi/surveyResponseEducationOrganizationTargetAssociations/{id}`
- `GET /ed-fi/surveyResponseEducationOrganizationTargetAssociations/deletes`
- `GET /ed-fi/surveyResponseEducationOrganizationTargetAssociations/keyChanges`
- `GET /ed-fi/surveyResponseEducationOrganizationTargetAssociations/partitions`
- `GET /ed-fi/surveyResponseEducationOrganizationTargetAssociations/{id}`
- `GET /ed-fi/surveyResponseEducationOrganizationTargetAssociations`
- `POST /ed-fi/surveyResponseEducationOrganizationTargetAssociations`
- `PUT /ed-fi/surveyResponseEducationOrganizationTargetAssociations/{id}`
