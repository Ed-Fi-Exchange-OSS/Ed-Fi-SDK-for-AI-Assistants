# staffProgramAssociations

`/ed-fi/staffProgramAssociations`

This association indicates the staff associated with a program.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | yes | string (date) | Start date for the association of staff to this program. |
| `programReference` | yes | reference; supply `educationOrganizationId`, `programName`, `programTypeDescriptor` | This entity represents any program designed to work in conjunction with, or as a supplement to, the main academic program. |
| `staffReference` | yes | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |
| `endDate` |  | string (date) | End date for the association of staff to this program. |
| `studentRecordAccess` |  | boolean | Indicator of whether the staff has access to the student records of the program per district interpretation of FERPA and other privacy laws, regulations, and p… |

## Endpoints

- `GET /ed-fi/staffProgramAssociations`
- `POST /ed-fi/staffProgramAssociations`
- `GET /ed-fi/staffProgramAssociations/deletes`
- `GET /ed-fi/staffProgramAssociations/keyChanges`
- `GET /ed-fi/staffProgramAssociations/partitions`
- `GET /ed-fi/staffProgramAssociations/{id}`
- `PUT /ed-fi/staffProgramAssociations/{id}`
- `DELETE /ed-fi/staffProgramAssociations/{id}`
