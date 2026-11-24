# studentPaths

`/ed-fi/studentPaths`

The entity representing the association or assignment of the student to the path of study being pursued.

## Natural key

`educationOrganizationId`, `pathName`, `studentUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `pathReference` | yes | reference; supply `educationOrganizationId`, `pathName` | A scheme for achieving milestones organized by phases for students to follow and be tracked against. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `periods` |  | array of edFi_studentPathPeriod | An unordered collection of studentPathPeriods. |

### Items in `periods`

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | yes | string (date) | The month, day, and year for the start of the period. |
| `endDate` |  | string (date) | The month, day, and year for the end of the period. |

## Endpoints

- `GET /ed-fi/studentPaths`
- `POST /ed-fi/studentPaths`
- `GET /ed-fi/studentPaths/deletes`
- `GET /ed-fi/studentPaths/keyChanges`
- `GET /ed-fi/studentPaths/partitions`
- `GET /ed-fi/studentPaths/{id}`
- `PUT /ed-fi/studentPaths/{id}`
- `DELETE /ed-fi/studentPaths/{id}`
