# pathPhases

`/ed-fi/pathPhases`

A stage in the process of a student achieving milestones.

## Natural key

`pathPhaseName`, `educationOrganizationId`, `pathName`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `pathPhaseName` | yes | string max 60 | The name of the phase associated with the path of study. |
| `pathReference` | yes | reference; supply `educationOrganizationId`, `pathName` | A scheme for achieving milestones organized by phases for students to follow and be tracked against. |
| `pathMilestones` |  | array of edFi_pathPhasePathMilestone | An unordered collection of pathPhasePathMilestones. |
| `pathPhaseSequence` |  | integer (int32) | Indicates the number in order, starting with 1, that the phases are organized into. |
| `phasePathDescription` |  | string max 1024 | Additional information describing the path's phase. |

### Items in `pathMilestones`

| Field | Required | Type | Description |
|---|---|---|---|
| `pathMilestoneReference` | yes | reference; supply `pathMilestoneName`, `pathMilestoneTypeDescriptor` | A significant event or achievement as part of a path of study. |

## Endpoints

- `GET /ed-fi/pathPhases`
- `POST /ed-fi/pathPhases`
- `GET /ed-fi/pathPhases/deletes`
- `GET /ed-fi/pathPhases/keyChanges`
- `GET /ed-fi/pathPhases/partitions`
- `GET /ed-fi/pathPhases/{id}`
- `PUT /ed-fi/pathPhases/{id}`
- `DELETE /ed-fi/pathPhases/{id}`
