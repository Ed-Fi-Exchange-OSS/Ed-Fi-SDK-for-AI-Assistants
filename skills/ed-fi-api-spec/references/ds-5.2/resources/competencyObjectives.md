# competencyObjectives

`/ed-fi/competencyObjectives`

This entity holds additional competencies for student achievement that are not associated with specific
learning objectives (e.g., paying attention in class).

## Natural key

`objectiveGradeLevelDescriptor`, `objective`, `educationOrganizationId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `objective` | yes | string max 60 | The designated title of the competency objective. |
| `objectiveGradeLevelDescriptor` | yes | descriptor URI | The grade level for which the competency objective is targeted. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `competencyObjectiveId` |  | string max 60 | The Identifier for the competency objective. |
| `description` |  | string max 1024 | The description of the student competency objective. |
| `successCriteria` |  | string max 150 | One or more statements that describes the criteria used by teachers and students to check for attainment of a competency objective. |

## Endpoints

- `GET /ed-fi/competencyObjectives`
- `POST /ed-fi/competencyObjectives`
- `GET /ed-fi/competencyObjectives/deletes`
- `GET /ed-fi/competencyObjectives/keyChanges`
- `GET /ed-fi/competencyObjectives/partitions`
- `GET /ed-fi/competencyObjectives/{id}`
- `PUT /ed-fi/competencyObjectives/{id}`
- `DELETE /ed-fi/competencyObjectives/{id}`
