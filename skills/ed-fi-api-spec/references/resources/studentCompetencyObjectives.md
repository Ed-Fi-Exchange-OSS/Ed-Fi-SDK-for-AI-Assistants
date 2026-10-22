# studentCompetencyObjectives

`/ed-fi/studentCompetencyObjectives`

This entity represents the competency assessed or evaluated for the student against a specific competency
objective.

## Natural key

`gradingPeriodReference`, `objectiveCompetencyObjectiveReference`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `gradingPeriodReference` | key | reference: `gradingPeriodDescriptor`, `gradingPeriodName`, `schoolId`, `schoolYear` |  |
| `objectiveCompetencyObjectiveReference` | key | reference: `educationOrganizationId`, `objective`, `objectiveGradeLevelDescriptor` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `competencyLevelDescriptor` | yes | descriptor URI | The competency level assessed for the student for the referenced competency objective. |
| `diagnosticStatement` |  | string max 1024 | A statement provided by the teacher that provides information in addition to the grade or assessment score. |
| `generalStudentProgramAssociations` |  | array of edFi_studentCompetencyObjectiveGeneralStudentProgramAssociation | An unordered collection of studentCompetencyObjectiveGeneralStudentProgramAssociations. |
| `studentSectionAssociations` |  | array of edFi_studentCompetencyObjectiveStudentSectionAssociation | An unordered collection of studentCompetencyObjectiveStudentSectionAssociations. |

## Endpoints

- `DELETE /ed-fi/studentCompetencyObjectives/{id}`
- `GET /ed-fi/studentCompetencyObjectives/deletes`
- `GET /ed-fi/studentCompetencyObjectives/keyChanges`
- `GET /ed-fi/studentCompetencyObjectives/partitions`
- `GET /ed-fi/studentCompetencyObjectives/{id}`
- `GET /ed-fi/studentCompetencyObjectives`
- `POST /ed-fi/studentCompetencyObjectives`
- `PUT /ed-fi/studentCompetencyObjectives/{id}`
