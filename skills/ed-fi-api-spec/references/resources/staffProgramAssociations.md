# staffProgramAssociations

`/ed-fi/staffProgramAssociations`

This association indicates the staff associated with a program.

## Natural key

`beginDate`, `programReference`, `staffReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | key | string (date) | Start date for the association of staff to this program. |
| `programReference` | key | reference: `educationOrganizationId`, `programName`, `programTypeDescriptor` |  |
| `staffReference` | key | reference: `staffUniqueId` |  |
| `endDate` |  | string (date) | End date for the association of staff to this program. |
| `studentRecordAccess` |  | boolean | Indicator of whether the staff has access to the student records of the program per district interpretation of FERPA and other privacy laws, regulations, and p… |

## Endpoints

- `DELETE /ed-fi/staffProgramAssociations/{id}`
- `GET /ed-fi/staffProgramAssociations/deletes`
- `GET /ed-fi/staffProgramAssociations/keyChanges`
- `GET /ed-fi/staffProgramAssociations/partitions`
- `GET /ed-fi/staffProgramAssociations/{id}`
- `GET /ed-fi/staffProgramAssociations`
- `POST /ed-fi/staffProgramAssociations`
- `PUT /ed-fi/staffProgramAssociations/{id}`
