# studentPathMilestoneStatuses

`/ed-fi/studentPathMilestoneStatuses`

The status of the student's achievement of the path milestone.

## Natural key

`pathMilestoneName`, `pathMilestoneTypeDescriptor`, `educationOrganizationId`, `pathName`, `studentUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `pathMilestoneReference` | yes | reference; supply `pathMilestoneName`, `pathMilestoneTypeDescriptor` | A significant event or achievement as part of a path of study. |
| `pathPhaseReference` |  | reference; supply `educationOrganizationId`, `pathName`, `pathPhaseName` | A stage in the process of a student achieving milestones. |
| `studentPathReference` | yes | reference; supply `educationOrganizationId`, `pathName`, `studentUniqueId` | The entity representing the association or assignment of the student to the path of study being pursued. |
| `completionIndicator` |  | boolean | Indicator on whether the student has completed the path milestone. |
| `event` |  | edFi_studentPathMilestoneStatusEvent |  |

## Endpoints

- `GET /ed-fi/studentPathMilestoneStatuses`
- `POST /ed-fi/studentPathMilestoneStatuses`
- `GET /ed-fi/studentPathMilestoneStatuses/deletes`
- `GET /ed-fi/studentPathMilestoneStatuses/keyChanges`
- `GET /ed-fi/studentPathMilestoneStatuses/partitions`
- `GET /ed-fi/studentPathMilestoneStatuses/{id}`
- `PUT /ed-fi/studentPathMilestoneStatuses/{id}`
- `DELETE /ed-fi/studentPathMilestoneStatuses/{id}`
