# studentDisciplineIncidentBehaviorAssociations

`/ed-fi/studentDisciplineIncidentBehaviorAssociations`

This association describes the behavior of students involved in a discipline incident.

## Natural key

`behaviorDescriptor`, `disciplineIncidentReference`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `behaviorDescriptor` | key | descriptor URI | Describes behavior by category. |
| `disciplineIncidentReference` | key | reference: `incidentIdentifier`, `schoolId` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `behaviorDetailedDescription` |  | string max 1024 | Specifies a more granular level of detail of a behavior involved in the incident. |
| `disciplineIncidentParticipationCodes` |  | array of edFi_studentDisciplineIncidentBehaviorAssociationDisciplineIncidentParticipationCode | An unordered collection of studentDisciplineIncidentBehaviorAssociationDisciplineIncidentParticipationCodes. |
| `weapons` |  | array of edFi_studentDisciplineIncidentBehaviorAssociationWeapon | An unordered collection of studentDisciplineIncidentBehaviorAssociationWeapons. |

## Endpoints

- `DELETE /ed-fi/studentDisciplineIncidentBehaviorAssociations/{id}`
- `GET /ed-fi/studentDisciplineIncidentBehaviorAssociations/deletes`
- `GET /ed-fi/studentDisciplineIncidentBehaviorAssociations/keyChanges`
- `GET /ed-fi/studentDisciplineIncidentBehaviorAssociations/partitions`
- `GET /ed-fi/studentDisciplineIncidentBehaviorAssociations/{id}`
- `GET /ed-fi/studentDisciplineIncidentBehaviorAssociations`
- `POST /ed-fi/studentDisciplineIncidentBehaviorAssociations`
- `PUT /ed-fi/studentDisciplineIncidentBehaviorAssociations/{id}`
