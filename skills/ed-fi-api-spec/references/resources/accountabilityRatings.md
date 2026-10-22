# accountabilityRatings

`/ed-fi/accountabilityRatings`

An accountability rating for a school or district.

## Natural key

`ratingTitle`, `educationOrganizationReference`, `schoolYearTypeReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `ratingTitle` | key | string max 60 | The title of the rating. |
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `schoolYearTypeReference` | key | reference: `schoolYear` |  |
| `rating` | yes | string max 35 | An accountability rating level, designation, or assessment. |
| `ratingDate` |  | string (date) | The date the rating was awarded. |
| `ratingOrganization` |  | string max 35 | The organization that assessed the rating. |
| `ratingProgram` |  | string max 30 | The program associated with the accountability rating (e.g., NCLB, AEIS). |

## Endpoints

- `DELETE /ed-fi/accountabilityRatings/{id}`
- `GET /ed-fi/accountabilityRatings/deletes`
- `GET /ed-fi/accountabilityRatings/keyChanges`
- `GET /ed-fi/accountabilityRatings/partitions`
- `GET /ed-fi/accountabilityRatings/{id}`
- `GET /ed-fi/accountabilityRatings`
- `POST /ed-fi/accountabilityRatings`
- `PUT /ed-fi/accountabilityRatings/{id}`
