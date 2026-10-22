# surveySectionAssociations

`/ed-fi/surveySectionAssociations`

The section associated with the survey.

## Natural key

`sectionReference`, `surveyReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `sectionReference` | key | reference: `localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName` |  |
| `surveyReference` | key | reference: `namespace`, `surveyIdentifier` |  |

## Endpoints

- `DELETE /ed-fi/surveySectionAssociations/{id}`
- `GET /ed-fi/surveySectionAssociations/deletes`
- `GET /ed-fi/surveySectionAssociations/keyChanges`
- `GET /ed-fi/surveySectionAssociations/partitions`
- `GET /ed-fi/surveySectionAssociations/{id}`
- `GET /ed-fi/surveySectionAssociations`
- `POST /ed-fi/surveySectionAssociations`
- `PUT /ed-fi/surveySectionAssociations/{id}`
