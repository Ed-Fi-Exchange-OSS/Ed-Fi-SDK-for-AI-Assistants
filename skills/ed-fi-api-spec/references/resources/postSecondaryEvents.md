# postSecondaryEvents

`/ed-fi/postSecondaryEvents`

This entity captures significant postsecondary events during a student's high school tenure (e.g., FAFSA application or college application, acceptance, and enrollment) or during a student's enrollment at a post-secondary institution.

## Natural key

`eventDate`, `postSecondaryEventCategoryDescriptor`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `eventDate` | key | string (date) | The date the event occurred or was recorded. |
| `postSecondaryEventCategoryDescriptor` | key | descriptor URI | The post secondary event that is logged. |
| `postSecondaryInstitutionReference` |  | reference: `postSecondaryInstitutionId` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |

## Endpoints

- `DELETE /ed-fi/postSecondaryEvents/{id}`
- `GET /ed-fi/postSecondaryEvents/deletes`
- `GET /ed-fi/postSecondaryEvents/keyChanges`
- `GET /ed-fi/postSecondaryEvents/partitions`
- `GET /ed-fi/postSecondaryEvents/{id}`
- `GET /ed-fi/postSecondaryEvents`
- `POST /ed-fi/postSecondaryEvents`
- `PUT /ed-fi/postSecondaryEvents/{id}`
