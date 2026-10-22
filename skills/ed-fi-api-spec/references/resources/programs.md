# programs

`/ed-fi/programs`

This entity represents any program designed to work in conjunction with, or as a supplement to, the main
academic program. Programs may provide instruction, training, services, or benefits through federal, state, or
local agencies. Programs may also include organized extracurricular activities for students.

## Natural key

`programName`, `programTypeDescriptor`, `educationOrganizationReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `programName` | key | string max 60 | The formal name of the program of instruction, training, services, or benefits available through federal, state, or local agencies. |
| `programTypeDescriptor` | key | descriptor URI | The type of program. |
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `characteristics` |  | array of edFi_programCharacteristic | An unordered collection of programCharacteristics. |
| `learningStandards` |  | array of edFi_programLearningStandard | An unordered collection of programLearningStandards. |
| `programId` |  | string max 20 | A unique number or alphanumeric code assigned to a program by a school, school system, a state, or other agency or entity. |
| `sponsors` |  | array of edFi_programSponsor | An unordered collection of programSponsors. |

## Endpoints

- `DELETE /ed-fi/programs/{id}`
- `GET /ed-fi/programs/deletes`
- `GET /ed-fi/programs/keyChanges`
- `GET /ed-fi/programs/partitions`
- `GET /ed-fi/programs/{id}`
- `GET /ed-fi/programs`
- `POST /ed-fi/programs`
- `PUT /ed-fi/programs/{id}`
