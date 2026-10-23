# postSecondaryEvents

`/ed-fi/postSecondaryEvents`

This entity captures significant postsecondary events during a student's high school tenure (e.g., FAFSA
application or college application, acceptance, and enrollment) or during a student's enrollment at a
post-secondary institution.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `eventDate` | yes | string (date) | The date the event occurred or was recorded. |
| `postSecondaryEventCategoryDescriptor` | yes | descriptor URI | The post secondary event that is logged. |
| `postSecondaryInstitutionReference` |  | reference; supply `postSecondaryInstitutionId` | An organization that provides educational programs for individuals who have completed or otherwise left educational programs in secondary school(s). |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |

## Endpoints

- `GET /ed-fi/postSecondaryEvents`
- `POST /ed-fi/postSecondaryEvents`
- `GET /ed-fi/postSecondaryEvents/deletes`
- `GET /ed-fi/postSecondaryEvents/keyChanges`
- `GET /ed-fi/postSecondaryEvents/partitions`
- `GET /ed-fi/postSecondaryEvents/{id}`
- `PUT /ed-fi/postSecondaryEvents/{id}`
- `DELETE /ed-fi/postSecondaryEvents/{id}`
