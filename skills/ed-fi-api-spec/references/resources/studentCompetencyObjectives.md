# studentCompetencyObjectives

`/ed-fi/studentCompetencyObjectives`

This entity represents the competency assessed or evaluated for the student against a specific competency
objective.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `gradingPeriodReference` | yes | reference; supply `gradingPeriodDescriptor`, `gradingPeriodName`, `schoolId`, `schoolYear` | This entity represents the time span for which grades are reported. |
| `objectiveCompetencyObjectiveReference` | yes | reference; supply `educationOrganizationId`, `objective`, `objectiveGradeLevelDescriptor` | This entity holds additional competencies for student achievement that are not associated with specific learning objectives (e.g., paying attention in class). |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `competencyLevelDescriptor` | yes | descriptor URI | The competency level assessed for the student for the referenced competency objective. |
| `diagnosticStatement` |  | string max 1024 | A statement provided by the teacher that provides information in addition to the grade or assessment score. |
| `generalStudentProgramAssociations` |  | array of edFi_studentCompetencyObjectiveGeneralStudentProgramAssociation | An unordered collection of studentCompetencyObjectiveGeneralStudentProgramAssociations. |
| `studentSectionAssociations` |  | array of edFi_studentCompetencyObjectiveStudentSectionAssociation | An unordered collection of studentCompetencyObjectiveStudentSectionAssociations. |

### Items in `generalStudentProgramAssociations`

| Field | Required | Type | Description |
|---|---|---|---|
| `generalStudentProgramAssociationReference` | yes | reference; supply `beginDate`, `educationOrganizationId`, `programEducationOrganizationId`, `programName`, `programTypeDescriptor`, `studentUniqueId` | Reference to generalStudentProgramAssociation. |

### Items in `studentSectionAssociations`

| Field | Required | Type | Description |
|---|---|---|---|
| `studentSectionAssociationReference` | yes | reference; supply `beginDate`, `localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName`, `studentUniqueId` | This association indicates the course sections to which a student is assigned. |

## Endpoints

- `GET /ed-fi/studentCompetencyObjectives`
- `POST /ed-fi/studentCompetencyObjectives`
- `GET /ed-fi/studentCompetencyObjectives/deletes`
- `GET /ed-fi/studentCompetencyObjectives/keyChanges`
- `GET /ed-fi/studentCompetencyObjectives/partitions`
- `GET /ed-fi/studentCompetencyObjectives/{id}`
- `PUT /ed-fi/studentCompetencyObjectives/{id}`
- `DELETE /ed-fi/studentCompetencyObjectives/{id}`
