# staffDisciplineIncidentAssociations

`/ed-fi/staffDisciplineIncidentAssociations`

This association indicates those staff who were victims, perpetrators, witnesses, and reporters for a
discipline incident.

## Natural key

`incidentIdentifier`, `schoolId`, `staffUniqueId`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `disciplineIncidentParticipationCodes` | yes | array of edFi_staffDisciplineIncidentAssociationDisciplineIncidentParticipationCode | An unordered collection of staffDisciplineIncidentAssociationDisciplineIncidentParticipationCodes. |
| `disciplineIncidentReference` | yes | reference; supply `incidentIdentifier`, `schoolId` | This event entity represents an occurrence of an infraction ranging from a minor behavioral problem that disrupts the orderly functioning of a school or classr… |
| `staffReference` | yes | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |

### Items in `disciplineIncidentParticipationCodes`

| Field | Required | Type | Description |
|---|---|---|---|
| `disciplineIncidentParticipationCodeDescriptor` | yes | descriptor URI | The role or type of participation of a student in a discipline incident. |

## Endpoints

- `GET /ed-fi/staffDisciplineIncidentAssociations`
- `POST /ed-fi/staffDisciplineIncidentAssociations`
- `GET /ed-fi/staffDisciplineIncidentAssociations/deletes`
- `GET /ed-fi/staffDisciplineIncidentAssociations/keyChanges`
- `GET /ed-fi/staffDisciplineIncidentAssociations/partitions`
- `GET /ed-fi/staffDisciplineIncidentAssociations/{id}`
- `PUT /ed-fi/staffDisciplineIncidentAssociations/{id}`
- `DELETE /ed-fi/staffDisciplineIncidentAssociations/{id}`
