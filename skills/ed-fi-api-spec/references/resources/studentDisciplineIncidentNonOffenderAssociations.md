# studentDisciplineIncidentNonOffenderAssociations

`/ed-fi/studentDisciplineIncidentNonOffenderAssociations`

This association indicates those students who were involved and not perpetrators for a discipline incident.

## Natural key

`disciplineIncidentReference`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `disciplineIncidentReference` | key | reference: `incidentIdentifier`, `schoolId` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `disciplineIncidentParticipationCodes` |  | array of edFi_studentDisciplineIncidentNonOffenderAssociationDisciplineIncidentParticipationCode | An unordered collection of studentDisciplineIncidentNonOffenderAssociationDisciplineIncidentParticipationCodes. |

## Endpoints

- `DELETE /ed-fi/studentDisciplineIncidentNonOffenderAssociations/{id}`
- `GET /ed-fi/studentDisciplineIncidentNonOffenderAssociations/deletes`
- `GET /ed-fi/studentDisciplineIncidentNonOffenderAssociations/keyChanges`
- `GET /ed-fi/studentDisciplineIncidentNonOffenderAssociations/partitions`
- `GET /ed-fi/studentDisciplineIncidentNonOffenderAssociations/{id}`
- `GET /ed-fi/studentDisciplineIncidentNonOffenderAssociations`
- `POST /ed-fi/studentDisciplineIncidentNonOffenderAssociations`
- `PUT /ed-fi/studentDisciplineIncidentNonOffenderAssociations/{id}`
