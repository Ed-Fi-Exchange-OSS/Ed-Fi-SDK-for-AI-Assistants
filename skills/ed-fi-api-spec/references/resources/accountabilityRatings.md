# accountabilityRatings

`/ed-fi/accountabilityRatings`

An accountability rating for a school or district.

## Natural key

`ratingTitle`, `educationOrganizationId`, `schoolYear`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `ratingTitle` | yes | string max 60 | The title of the rating. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `schoolYearTypeReference` | yes | reference; supply `schoolYear` | Identifier for a school year. |
| `rating` | yes | string max 35 | An accountability rating level, designation, or assessment. |
| `ratingDate` |  | string (date) | The date the rating was awarded. |
| `ratingOrganization` |  | string max 35 | The organization that assessed the rating. |
| `ratingProgram` |  | string max 30 | The program associated with the accountability rating (e.g., NCLB, AEIS). |

## Endpoints

- `GET /ed-fi/accountabilityRatings`
- `POST /ed-fi/accountabilityRatings`
- `GET /ed-fi/accountabilityRatings/deletes`
- `GET /ed-fi/accountabilityRatings/keyChanges`
- `GET /ed-fi/accountabilityRatings/partitions`
- `GET /ed-fi/accountabilityRatings/{id}`
- `PUT /ed-fi/accountabilityRatings/{id}`
- `DELETE /ed-fi/accountabilityRatings/{id}`
