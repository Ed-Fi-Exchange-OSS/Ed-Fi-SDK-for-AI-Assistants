# surveySectionResponseEducationOrganizationTargetAssociations

`/ed-fi/surveySectionResponseEducationOrganizationTargetAssociations`

This association provides information about the survey section and the education organization the survey section is about.

## Natural key

`educationOrganizationReference`, `surveySectionResponseReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `surveySectionResponseReference` | key | reference: `namespace`, `surveyIdentifier`, `surveyResponseIdentifier`, `surveySectionTitle` |  |

## Endpoints

- `DELETE /ed-fi/surveySectionResponseEducationOrganizationTargetAssociations/{id}`
- `GET /ed-fi/surveySectionResponseEducationOrganizationTargetAssociations/deletes`
- `GET /ed-fi/surveySectionResponseEducationOrganizationTargetAssociations/keyChanges`
- `GET /ed-fi/surveySectionResponseEducationOrganizationTargetAssociations/partitions`
- `GET /ed-fi/surveySectionResponseEducationOrganizationTargetAssociations/{id}`
- `GET /ed-fi/surveySectionResponseEducationOrganizationTargetAssociations`
- `POST /ed-fi/surveySectionResponseEducationOrganizationTargetAssociations`
- `PUT /ed-fi/surveySectionResponseEducationOrganizationTargetAssociations/{id}`
