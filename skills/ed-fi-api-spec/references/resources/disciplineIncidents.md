# disciplineIncidents

`/ed-fi/disciplineIncidents`

This event entity represents an occurrence of an infraction ranging from a minor behavioral problem that
disrupts the orderly functioning of a school or classroom (such as tardiness) to a criminal act that results
in the involvement of a law enforcement official (such as robbery). A single event (e.g., a fight) is one
incident regardless of how many perpetrators or victims are involved. Discipline incidents are events
classified as warranting discipline action.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `incidentIdentifier` | yes | string max 36 | A locally assigned unique identifier (within the school or school district) to identify each specific DisciplineIncident or occurrence. |
| `schoolReference` | yes | reference; supply `schoolId` | This entity represents an educational organization that includes staff and students who participate in classes and educational activity groups. |
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

### Items in `behaviors`

| Field | Required | Type | Description |
|---|---|---|---|
| `behaviorDescriptor` | yes | descriptor URI | Describes behavior by category and provides a detailed description. |
| `behaviorDetailedDescription` |  | string max 1024 | Specifies a more granular level of detail of a behavior involved in the incident. |

### Items in `externalParticipants`

| Field | Required | Type | Description |
|---|---|---|---|
| `disciplineIncidentParticipationCodeDescriptor` | yes | descriptor URI | The role or type of participation of an individual in the discipline incident. |
| `firstName` | yes | string max 75 | A name given to an individual at birth, baptism, or during another naming ceremony, or through legal change. |
| `lastSurname` | yes | string max 75 | The name borne in common by members of a family. |

### Items in `weapons`

| Field | Required | Type | Description |
|---|---|---|---|
| `weaponDescriptor` | yes | descriptor URI | Identifies the type of weapon used during an incident. |

## Endpoints

- `GET /ed-fi/disciplineIncidents`
- `POST /ed-fi/disciplineIncidents`
- `GET /ed-fi/disciplineIncidents/deletes`
- `GET /ed-fi/disciplineIncidents/keyChanges`
- `GET /ed-fi/disciplineIncidents/partitions`
- `GET /ed-fi/disciplineIncidents/{id}`
- `PUT /ed-fi/disciplineIncidents/{id}`
- `DELETE /ed-fi/disciplineIncidents/{id}`
