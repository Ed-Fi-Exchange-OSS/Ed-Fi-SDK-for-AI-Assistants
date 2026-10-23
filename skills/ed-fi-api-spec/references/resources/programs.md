# programs

`/ed-fi/programs`

This entity represents any program designed to work in conjunction with, or as a supplement to, the main
academic program. Programs may provide instruction, training, services, or benefits through federal, state, or
local agencies. Programs may also include organized extracurricular activities for students.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `programName` | yes | string max 60 | The formal name of the program of instruction, training, services, or benefits available through federal, state, or local agencies. |
| `programTypeDescriptor` | yes | descriptor URI | The type of program. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `characteristics` |  | array of edFi_programCharacteristic | An unordered collection of programCharacteristics. |
| `learningStandards` |  | array of edFi_programLearningStandard | An unordered collection of programLearningStandards. |
| `programId` |  | string max 20 | A unique number or alphanumeric code assigned to a program by a school, school system, a state, or other agency or entity. |
| `sponsors` |  | array of edFi_programSponsor | An unordered collection of programSponsors. |

### Items in `characteristics`

| Field | Required | Type | Description |
|---|---|---|---|
| `programCharacteristicDescriptor` | yes | descriptor URI | Reflects important characteristics of the program, such as categories or particular indications. |

### Items in `learningStandards`

| Field | Required | Type | Description |
|---|---|---|---|
| `learningStandardReference` | yes | reference; supply `learningStandardId` | A statement that describes a specific competency or academic standard. |

### Items in `sponsors`

| Field | Required | Type | Description |
|---|---|---|---|
| `programSponsorDescriptor` | yes | descriptor URI | Ultimate and intermediate providers of funds for a particular educational or service program or activity, or for an individual's participation in the program o… |

## Endpoints

- `GET /ed-fi/programs`
- `POST /ed-fi/programs`
- `GET /ed-fi/programs/deletes`
- `GET /ed-fi/programs/keyChanges`
- `GET /ed-fi/programs/partitions`
- `GET /ed-fi/programs/{id}`
- `PUT /ed-fi/programs/{id}`
- `DELETE /ed-fi/programs/{id}`
