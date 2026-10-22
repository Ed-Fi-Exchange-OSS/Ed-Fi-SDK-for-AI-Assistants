# disciplineIncidents

`/ed-fi/disciplineIncidents`

This event entity represents an occurrence of an infraction ranging from a minor behavioral problem that disrupts the orderly functioning of a school or classroom (such as tardiness) to a criminal act that results in the involvement of a law enforcement official (such as robbery). A single event (e.g., a fight) is one incident regardless of how many perpetrators or victims are involved. Discipline incidents are events classified as warranting discipline action.

## Natural key

`incidentIdentifier`, `schoolReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `incidentIdentifier` | key | string max 36 | A locally assigned unique identifier (within the school or school district) to identify each specific DisciplineIncident or occurrence. |
| `schoolReference` | key | reference: `schoolId` |  |
| `behaviors` |  | array of edFi_disciplineIncidentBehavior | An unordered collection of disciplineIncidentBehaviors. |
| `caseNumber` |  | string max 20 | The case number assigned to the DisciplineIncident by law enforcement or other organization. |
| `externalParticipants` |  | array of edFi_disciplineIncidentExternalParticipant | An unordered collection of disciplineIncidentExternalParticipants. |
| `incidentCost` |  | number (double) | The value of any quantifiable monetary loss directly resulting from the discipline incident. |
| `incidentDate` | yes | string (date) | The month, day, and year on which the discipline incident occurred. |
| `incidentDescription` |  | string max 1024 | The description for an incident. |
| `incidentLocationDescriptor` |  | descriptor URI | Identifies where the discipline incident occurred and whether or not it occurred on school. |
| `incidentTime` |  | string | An indication of the time of day the incident took place. |
| `reportedToLawEnforcement` |  | boolean | Indicator of whether the incident was reported to law enforcement. |
| `reporterDescriptionDescriptor` |  | descriptor URI | Information on the type of individual who reported the discipline incident. |
| `reporterName` |  | string max 75 | Identifies the reporter of the discipline incident by name. |
| `weapons` |  | array of edFi_disciplineIncidentWeapon | An unordered collection of disciplineIncidentWeapons. |

## Endpoints

- `DELETE /ed-fi/disciplineIncidents/{id}`
- `GET /ed-fi/disciplineIncidents/deletes`
- `GET /ed-fi/disciplineIncidents/keyChanges`
- `GET /ed-fi/disciplineIncidents/partitions`
- `GET /ed-fi/disciplineIncidents/{id}`
- `GET /ed-fi/disciplineIncidents`
- `POST /ed-fi/disciplineIncidents`
- `PUT /ed-fi/disciplineIncidents/{id}`
