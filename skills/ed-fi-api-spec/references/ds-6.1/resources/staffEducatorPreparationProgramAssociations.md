# staffEducatorPreparationProgramAssociations

`/ed-fi/staffEducatorPreparationProgramAssociations`

This association indicates the educator preparation program associated with a staff.

## Natural key

`educationOrganizationId`, `programName`, `programTypeDescriptor`, `staffUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educatorPreparationProgramReference` | yes | reference; supply `educationOrganizationId`, `programName`, `programTypeDescriptor` | The educator preparation program designed to prepare students to become licensed educators. |
| `staffReference` | yes | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |
| `beginDate` | yes | string (date) | The start date for the association of staff to this program. |
| `completer` |  | boolean | Indicator of whether the staff completed the educator preparation program. |
| `endDate` |  | string (date) | The end date for the association of staff to this program. |

## Endpoints

- `GET /ed-fi/staffEducatorPreparationProgramAssociations`
- `POST /ed-fi/staffEducatorPreparationProgramAssociations`
- `GET /ed-fi/staffEducatorPreparationProgramAssociations/deletes`
- `GET /ed-fi/staffEducatorPreparationProgramAssociations/keyChanges`
- `GET /ed-fi/staffEducatorPreparationProgramAssociations/partitions`
- `GET /ed-fi/staffEducatorPreparationProgramAssociations/{id}`
- `PUT /ed-fi/staffEducatorPreparationProgramAssociations/{id}`
- `DELETE /ed-fi/staffEducatorPreparationProgramAssociations/{id}`
