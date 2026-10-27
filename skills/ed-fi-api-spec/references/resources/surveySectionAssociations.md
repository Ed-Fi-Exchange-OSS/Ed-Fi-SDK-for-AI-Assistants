# surveySectionAssociations

`/ed-fi/surveySectionAssociations`

The section associated with the survey.

## Natural key

`localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName`, `namespace`,
`surveyIdentifier`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `sectionReference` | yes | reference; supply `localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName` | This entity represents a setting in which organized instruction of course content is provided, in-person or otherwise, to one or more students for a given peri… |
| `surveyReference` | yes | reference; supply `namespace`, `surveyIdentifier` | A survey to identified or anonymous respondents. |

## Endpoints

- `GET /ed-fi/surveySectionAssociations`
- `POST /ed-fi/surveySectionAssociations`
- `GET /ed-fi/surveySectionAssociations/deletes`
- `GET /ed-fi/surveySectionAssociations/keyChanges`
- `GET /ed-fi/surveySectionAssociations/partitions`
- `GET /ed-fi/surveySectionAssociations/{id}`
- `PUT /ed-fi/surveySectionAssociations/{id}`
- `DELETE /ed-fi/surveySectionAssociations/{id}`
