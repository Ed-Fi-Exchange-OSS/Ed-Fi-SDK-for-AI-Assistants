# studentDisciplineIncidentNonOffenderAssociations

`/ed-fi/studentDisciplineIncidentNonOffenderAssociations`

This association indicates those students who were involved and not perpetrators for a discipline incident.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `disciplineIncidentReference` | yes | reference; supply `incidentIdentifier`, `schoolId` | This event entity represents an occurrence of an infraction ranging from a minor behavioral problem that disrupts the orderly functioning of a school or classr… |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `disciplineIncidentParticipationCodes` |  | array of edFi_studentDisciplineIncidentNonOffenderAssociationDisciplineIncidentParticipationCode | An unordered collection of studentDisciplineIncidentNonOffenderAssociationDisciplineIncidentParticipationCodes. |

### Items in `disciplineIncidentParticipationCodes`

| Field | Required | Type | Description |
|---|---|---|---|
| `disciplineIncidentParticipationCodeDescriptor` | yes | descriptor URI | The role or type of participation of a student in a discipline incident. |

## Endpoints

- `GET /ed-fi/studentDisciplineIncidentNonOffenderAssociations`
- `POST /ed-fi/studentDisciplineIncidentNonOffenderAssociations`
- `GET /ed-fi/studentDisciplineIncidentNonOffenderAssociations/deletes`
- `GET /ed-fi/studentDisciplineIncidentNonOffenderAssociations/keyChanges`
- `GET /ed-fi/studentDisciplineIncidentNonOffenderAssociations/partitions`
- `GET /ed-fi/studentDisciplineIncidentNonOffenderAssociations/{id}`
- `PUT /ed-fi/studentDisciplineIncidentNonOffenderAssociations/{id}`
- `DELETE /ed-fi/studentDisciplineIncidentNonOffenderAssociations/{id}`
