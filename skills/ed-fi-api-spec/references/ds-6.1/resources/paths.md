# paths

`/ed-fi/paths`

A scheme for achieving milestones organized by phases for students to follow and be tracked against.

## Natural key

`pathName`, `educationOrganizationId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `pathName` | yes | string max 60 | The name of the path of study. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `graduationPlanReference` |  | reference; supply `educationOrganizationId`, `graduationPlanTypeDescriptor`, `graduationSchoolYear` | This entity is a plan outlining the required credits, credits by subject, credits by course, and other criteria required for graduation. |

## Endpoints

- `GET /ed-fi/paths`
- `POST /ed-fi/paths`
- `GET /ed-fi/paths/deletes`
- `GET /ed-fi/paths/keyChanges`
- `GET /ed-fi/paths/partitions`
- `GET /ed-fi/paths/{id}`
- `PUT /ed-fi/paths/{id}`
- `DELETE /ed-fi/paths/{id}`
