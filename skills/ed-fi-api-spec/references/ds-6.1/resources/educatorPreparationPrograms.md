# educatorPreparationPrograms

`/ed-fi/educatorPreparationPrograms`

The educator preparation program designed to prepare students to become licensed educators.

## Natural key

`programTypeDescriptor`, `programName`, `educationOrganizationId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `programName` | yes | string max 255 | The name of the educator preparation program. |
| `programTypeDescriptor` | yes | descriptor URI | The type of program. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `accreditationStatusDescriptor` |  | descriptor URI | The current accreditation status of the educator preparation program. |
| `gradeLevels` |  | array of edFi_educatorPreparationProgramGradeLevel | An unordered collection of educatorPreparationProgramGradeLevels. |
| `programId` |  | string max 20 | A unique number or alphanumeric code assigned to a program by a school, school system, a state, or other agency or entity. |

### Items in `gradeLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `gradeLevelDescriptor` | yes | descriptor URI | The grade levels served at the educator preparation program. |

## Endpoints

- `GET /ed-fi/educatorPreparationPrograms`
- `POST /ed-fi/educatorPreparationPrograms`
- `GET /ed-fi/educatorPreparationPrograms/deletes`
- `GET /ed-fi/educatorPreparationPrograms/keyChanges`
- `GET /ed-fi/educatorPreparationPrograms/partitions`
- `GET /ed-fi/educatorPreparationPrograms/{id}`
- `PUT /ed-fi/educatorPreparationPrograms/{id}`
- `DELETE /ed-fi/educatorPreparationPrograms/{id}`
