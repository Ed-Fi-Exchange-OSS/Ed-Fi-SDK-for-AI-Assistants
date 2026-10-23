# studentDisciplineIncidentBehaviorAssociations

`/ed-fi/studentDisciplineIncidentBehaviorAssociations`

This association describes the behavior of students involved in a discipline incident.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `behaviorDescriptor` | yes | descriptor URI | Describes behavior by category. |
| `disciplineIncidentReference` | yes | reference; supply `incidentIdentifier`, `schoolId` | This event entity represents an occurrence of an infraction ranging from a minor behavioral problem that disrupts the orderly functioning of a school or classr… |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `behaviorDetailedDescription` |  | string max 1024 | Specifies a more granular level of detail of a behavior involved in the incident. |
| `disciplineIncidentParticipationCodes` |  | array of edFi_studentDisciplineIncidentBehaviorAssociationDisciplineIncidentParticipationCode | An unordered collection of studentDisciplineIncidentBehaviorAssociationDisciplineIncidentParticipationCodes. |
| `weapons` |  | array of edFi_studentDisciplineIncidentBehaviorAssociationWeapon | An unordered collection of studentDisciplineIncidentBehaviorAssociationWeapons. |

### Items in `disciplineIncidentParticipationCodes`

| Field | Required | Type | Description |
|---|---|---|---|
| `disciplineIncidentParticipationCodeDescriptor` | yes | descriptor URI | The role or type of participation of a student in a discipline incident. |

### Items in `weapons`

| Field | Required | Type | Description |
|---|---|---|---|
| `weaponDescriptor` | yes | descriptor URI | Identifies the type(s) of weapon used by the student during a discipline incident. |

## Endpoints

- `GET /ed-fi/studentDisciplineIncidentBehaviorAssociations`
- `POST /ed-fi/studentDisciplineIncidentBehaviorAssociations`
- `GET /ed-fi/studentDisciplineIncidentBehaviorAssociations/deletes`
- `GET /ed-fi/studentDisciplineIncidentBehaviorAssociations/keyChanges`
- `GET /ed-fi/studentDisciplineIncidentBehaviorAssociations/partitions`
- `GET /ed-fi/studentDisciplineIncidentBehaviorAssociations/{id}`
- `PUT /ed-fi/studentDisciplineIncidentBehaviorAssociations/{id}`
- `DELETE /ed-fi/studentDisciplineIncidentBehaviorAssociations/{id}`
