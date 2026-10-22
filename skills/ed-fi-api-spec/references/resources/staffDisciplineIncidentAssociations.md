# staffDisciplineIncidentAssociations

`/ed-fi/staffDisciplineIncidentAssociations`

This association indicates those staff who were victims, perpetrators, witnesses, and reporters for a
discipline incident.

## Natural key

`disciplineIncidentReference`, `staffReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `disciplineIncidentParticipationCodes` | yes | array of edFi_staffDisciplineIncidentAssociationDisciplineIncidentParticipationCode | An unordered collection of staffDisciplineIncidentAssociationDisciplineIncidentParticipationCodes. |
| `disciplineIncidentReference` | key | reference: `incidentIdentifier`, `schoolId` |  |
| `staffReference` | key | reference: `staffUniqueId` |  |

## Endpoints

- `DELETE /ed-fi/staffDisciplineIncidentAssociations/{id}`
- `GET /ed-fi/staffDisciplineIncidentAssociations/deletes`
- `GET /ed-fi/staffDisciplineIncidentAssociations/keyChanges`
- `GET /ed-fi/staffDisciplineIncidentAssociations/partitions`
- `GET /ed-fi/staffDisciplineIncidentAssociations/{id}`
- `GET /ed-fi/staffDisciplineIncidentAssociations`
- `POST /ed-fi/staffDisciplineIncidentAssociations`
- `PUT /ed-fi/staffDisciplineIncidentAssociations/{id}`
