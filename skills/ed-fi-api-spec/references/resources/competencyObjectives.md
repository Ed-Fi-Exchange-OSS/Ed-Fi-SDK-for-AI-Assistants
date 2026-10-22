# competencyObjectives

`/ed-fi/competencyObjectives`

This entity holds additional competencies for student achievement that are not associated with specific learning objectives (e.g., paying attention in class).

## Natural key

`objective`, `objectiveGradeLevelDescriptor`, `educationOrganizationReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `objective` | key | string max 60 | The designated title of the competency objective. |
| `objectiveGradeLevelDescriptor` | key | descriptor URI | The grade level for which the competency objective is targeted. |
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `competencyObjectiveId` |  | string max 60 | The Identifier for the competency objective. |
| `description` |  | string max 1024 | The description of the student competency objective. |
| `successCriteria` |  | string max 150 | One or more statements that describes the criteria used by teachers and students to check for attainment of a competency objective. |

## Endpoints

- `DELETE /ed-fi/competencyObjectives/{id}`
- `GET /ed-fi/competencyObjectives/deletes`
- `GET /ed-fi/competencyObjectives/keyChanges`
- `GET /ed-fi/competencyObjectives/partitions`
- `GET /ed-fi/competencyObjectives/{id}`
- `GET /ed-fi/competencyObjectives`
- `POST /ed-fi/competencyObjectives`
- `PUT /ed-fi/competencyObjectives/{id}`
