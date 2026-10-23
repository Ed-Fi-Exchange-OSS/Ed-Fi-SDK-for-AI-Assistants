# studentInterventionAssociations

`/ed-fi/studentInterventionAssociations`

This association indicates the students participating in an intervention.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `cohortReference` |  | reference; supply `cohortIdentifier`, `educationOrganizationId` | This entity represents any type of list of designated students for tracking, analysis, or intervention. |
| `interventionReference` | yes | reference; supply `educationOrganizationId`, `interventionIdentificationCode` | An implementation of an instructional approach focusing on the specific techniques and materials used to teach a given subject. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `diagnosticStatement` |  | string max 1024 | A statement provided by the assigner that provides information regarding why the student was assigned to this intervention. |
| `dosage` |  | integer (int32) | The duration of time in minutes for which the student was assigned to participate in the intervention. |
| `interventionEffectivenesses` |  | array of edFi_studentInterventionAssociationInterventionEffectiveness | An unordered collection of studentInterventionAssociationInterventionEffectivenesses. |

### Items in `interventionEffectivenesses`

| Field | Required | Type | Description |
|---|---|---|---|
| `diagnosisDescriptor` | yes | descriptor URI | Targeted purpose of the intervention (e.g., attendance issue, dropout risk) for which the effectiveness is measured. |
| `gradeLevelDescriptor` | yes | descriptor URI | Grade level for which effectiveness is measured. |
| `populationServedDescriptor` | yes | descriptor URI | Population for which effectiveness is measured. |
| `interventionEffectivenessRatingDescriptor` | yes | descriptor URI | An intervention demonstrates effectiveness if the research has shown that the program caused an improvement in outcomes. |
| `improvementIndex` |  | integer (int32) | Along a percentile distribution of students, the improvement index represents the change in an average student's percentile rank that is considered to be due t… |

## Endpoints

- `GET /ed-fi/studentInterventionAssociations`
- `POST /ed-fi/studentInterventionAssociations`
- `GET /ed-fi/studentInterventionAssociations/deletes`
- `GET /ed-fi/studentInterventionAssociations/keyChanges`
- `GET /ed-fi/studentInterventionAssociations/partitions`
- `GET /ed-fi/studentInterventionAssociations/{id}`
- `PUT /ed-fi/studentInterventionAssociations/{id}`
- `DELETE /ed-fi/studentInterventionAssociations/{id}`
