# pathMilestones

`/ed-fi/pathMilestones`

A significant event or achievement as part of a path of study.

## Natural key

`pathMilestoneTypeDescriptor`, `pathMilestoneName`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `pathMilestoneName` | yes | string max 60 | The descriptive name of the path milestone. |
| `pathMilestoneTypeDescriptor` | yes | descriptor URI | The type of milestone defined for the student's path of study. |
| `pathMilestoneCode` |  | string max 60 | The code or identifier associated with an element associated with the path milestone. |
| `pathMilestoneDescription` |  | string max 1024 | Additional information describing the path milestone to be achieved. |

## Endpoints

- `GET /ed-fi/pathMilestones`
- `POST /ed-fi/pathMilestones`
- `GET /ed-fi/pathMilestones/deletes`
- `GET /ed-fi/pathMilestones/keyChanges`
- `GET /ed-fi/pathMilestones/partitions`
- `GET /ed-fi/pathMilestones/{id}`
- `PUT /ed-fi/pathMilestones/{id}`
- `DELETE /ed-fi/pathMilestones/{id}`
