# educatorPreparationPrograms

`/tpdm/educatorPreparationPrograms`

The Educator Preparation Program is designed to prepare students to become licensed educators.

## Natural key

`programName`, `programTypeDescriptor`, `educationOrganizationReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `programName` | key | string max 255 | The name of the Educator Preparation Program. |
| `programTypeDescriptor` | key | descriptor URI | The type of program. |
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `accreditationStatusDescriptor` |  | descriptor URI | The current accreditation status of the Educator Preparation Program. |
| `gradeLevels` |  | array of tpdm_educatorPreparationProgramGradeLevel | An unordered collection of educatorPreparationProgramGradeLevels. |
| `programId` |  | string max 20 | A unique number or alphanumeric code assigned to a program by a school, school system, a state, or other agency or entity. |

## Endpoints

- `DELETE /tpdm/educatorPreparationPrograms/{id}`
- `GET /tpdm/educatorPreparationPrograms/deletes`
- `GET /tpdm/educatorPreparationPrograms/keyChanges`
- `GET /tpdm/educatorPreparationPrograms/partitions`
- `GET /tpdm/educatorPreparationPrograms/{id}`
- `GET /tpdm/educatorPreparationPrograms`
- `POST /tpdm/educatorPreparationPrograms`
- `PUT /tpdm/educatorPreparationPrograms/{id}`
