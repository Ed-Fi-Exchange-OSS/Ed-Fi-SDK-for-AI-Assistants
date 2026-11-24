# educatorPreparationPrograms

`/tpdm/educatorPreparationPrograms`

The Educator Preparation Program is designed to prepare students to become licensed educators.

## Natural key

`programTypeDescriptor`, `programName`, `educationOrganizationId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `programName` | yes | string max 255 | The name of the Educator Preparation Program. |
| `programTypeDescriptor` | yes | descriptor URI | The type of program. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `accreditationStatusDescriptor` |  | descriptor URI | The current accreditation status of the Educator Preparation Program. |
| `gradeLevels` |  | array of tpdm_educatorPreparationProgramGradeLevel | An unordered collection of educatorPreparationProgramGradeLevels. |
| `programId` |  | string max 20 | A unique number or alphanumeric code assigned to a program by a school, school system, a state, or other agency or entity. |

### Items in `gradeLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `gradeLevelDescriptor` | yes | descriptor URI | The grade levels served at the EPP Program. |

## Endpoints

- `GET /tpdm/educatorPreparationPrograms`
- `POST /tpdm/educatorPreparationPrograms`
- `GET /tpdm/educatorPreparationPrograms/deletes`
- `GET /tpdm/educatorPreparationPrograms/keyChanges`
- `GET /tpdm/educatorPreparationPrograms/partitions`
- `GET /tpdm/educatorPreparationPrograms/{id}`
- `PUT /tpdm/educatorPreparationPrograms/{id}`
- `DELETE /tpdm/educatorPreparationPrograms/{id}`
