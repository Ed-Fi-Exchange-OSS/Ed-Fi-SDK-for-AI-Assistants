# studentPathPhaseStatuses

`/ed-fi/studentPathPhaseStatuses`

The status of the student's association with the path's phase.

## Natural key

`educationOrganizationId`, `pathName`, `pathPhaseName`, `studentUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `pathPhaseReference` | yes | reference; supply `educationOrganizationId`, `pathName`, `pathPhaseName` | A stage in the process of a student achieving milestones. |
| `studentPathReference` | yes | reference; supply `educationOrganizationId`, `pathName`, `studentUniqueId` | The entity representing the association or assignment of the student to the path of study being pursued. |
| `completionIndicator` |  | boolean | Indicator on whether the student has completed the phase associated with the path of study. |
| `events` |  | array of edFi_studentPathPhaseStatusEvent | An unordered collection of studentPathPhaseStatusEvents. |
| `periods` |  | array of edFi_studentPathPhaseStatusPeriod | An unordered collection of studentPathPhaseStatusPeriods. |

### Items in `events`

| Field | Required | Type | Description |
|---|---|---|---|
| `pathPhaseStatusDescriptor` | yes | descriptor URI | The student's status associated with entering or completing the path phase. |
| `pathPhaseStatusDate` | yes | string (date) | The month, day and year on which the status was achieved for the path phase. |

### Items in `periods`

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | yes | string (date) | The month, day, and year for the start of the period. |
| `endDate` |  | string (date) | The month, day, and year for the end of the period. |

## Endpoints

- `GET /ed-fi/studentPathPhaseStatuses`
- `POST /ed-fi/studentPathPhaseStatuses`
- `GET /ed-fi/studentPathPhaseStatuses/deletes`
- `GET /ed-fi/studentPathPhaseStatuses/keyChanges`
- `GET /ed-fi/studentPathPhaseStatuses/partitions`
- `GET /ed-fi/studentPathPhaseStatuses/{id}`
- `PUT /ed-fi/studentPathPhaseStatuses/{id}`
- `DELETE /ed-fi/studentPathPhaseStatuses/{id}`
