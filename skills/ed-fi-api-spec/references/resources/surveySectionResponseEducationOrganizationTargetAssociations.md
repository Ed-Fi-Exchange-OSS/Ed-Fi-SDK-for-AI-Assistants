# surveySectionResponseEducationOrganizationTargetAssociations

`/ed-fi/surveySectionResponseEducationOrganizationTargetAssociations`

This association provides information about the survey section and the education organization the survey
section is about.

## Natural key

`educationOrganizationId`, `namespace`, `surveyIdentifier`, `surveyResponseIdentifier`, `surveySectionTitle`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `surveySectionResponseReference` | yes | reference; supply `namespace`, `surveyIdentifier`, `surveyResponseIdentifier`, `surveySectionTitle` | Optional information about the responses provided for a section of a survey. |

## Endpoints

- `GET /ed-fi/surveySectionResponseEducationOrganizationTargetAssociations`
- `POST /ed-fi/surveySectionResponseEducationOrganizationTargetAssociations`
- `GET /ed-fi/surveySectionResponseEducationOrganizationTargetAssociations/deletes`
- `GET /ed-fi/surveySectionResponseEducationOrganizationTargetAssociations/keyChanges`
- `GET /ed-fi/surveySectionResponseEducationOrganizationTargetAssociations/partitions`
- `GET /ed-fi/surveySectionResponseEducationOrganizationTargetAssociations/{id}`
- `PUT /ed-fi/surveySectionResponseEducationOrganizationTargetAssociations/{id}`
- `DELETE /ed-fi/surveySectionResponseEducationOrganizationTargetAssociations/{id}`
