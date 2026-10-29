# restraintEvents

`/ed-fi/restraintEvents`

This event entity represents the instances where a special education student was physically or mechanically
restrained due to imminent serious physical harm to themselves or others, imminent serious property
destruction or a combination of both imminent serious physical harm to themselves or others and imminent
serious property destruction.

## Natural key

`restraintEventIdentifier`, `schoolId`, `studentUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `restraintEventIdentifier` | yes | string max 36 | A unique number or alphanumeric code assigned to a restraint event by a school, school system, state, or other agency or entity. |
| `disciplineIncidentReference` |  | reference; supply `incidentIdentifier`, `schoolId` | This event entity represents an occurrence of an infraction ranging from a minor behavioral problem that disrupts the orderly functioning of a school or classr… |
| `schoolReference` | yes | reference; supply `schoolId` | This entity represents an educational organization that includes staff and students who participate in classes and educational activity groups. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `educationalEnvironmentDescriptor` |  | descriptor URI | The setting where the RestraintEvent was exercised. |
| `eventDate` | yes | string (date) | Month, day, and year of the restraint event. |
| `programs` |  | array of edFi_restraintEventProgram | An unordered collection of restraintEventPrograms. |
| `reasons` |  | array of edFi_restraintEventReason | An unordered collection of restraintEventReasons. |

### Items in `programs`

| Field | Required | Type | Description |
|---|---|---|---|
| `programReference` | yes | reference; supply `educationOrganizationId`, `programName`, `programTypeDescriptor` | This entity represents any program designed to work in conjunction with, or as a supplement to, the main academic program. |

### Items in `reasons`

| Field | Required | Type | Description |
|---|---|---|---|
| `restraintEventReasonDescriptor` | yes | descriptor URI | A categorization of the circumstances or reason for the RestraintEvent. |

## Endpoints

- `GET /ed-fi/restraintEvents`
- `POST /ed-fi/restraintEvents`
- `GET /ed-fi/restraintEvents/deletes`
- `GET /ed-fi/restraintEvents/keyChanges`
- `GET /ed-fi/restraintEvents/partitions`
- `GET /ed-fi/restraintEvents/{id}`
- `PUT /ed-fi/restraintEvents/{id}`
- `DELETE /ed-fi/restraintEvents/{id}`
