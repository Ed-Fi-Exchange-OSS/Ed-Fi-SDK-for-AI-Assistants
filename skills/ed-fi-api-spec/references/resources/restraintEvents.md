# restraintEvents

`/ed-fi/restraintEvents`

This event entity represents the instances where a special education student was physically or mechanically
restrained due to imminent serious physical harm to themselves or others, imminent serious property
destruction or a combination of both imminent serious physical harm to themselves or others and imminent
serious property destruction.

## Natural key

`restraintEventIdentifier`, `schoolReference`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `restraintEventIdentifier` | key | string max 36 | A unique number or alphanumeric code assigned to a restraint event by a school, school system, state, or other agency or entity. |
| `disciplineIncidentReference` |  | reference: `incidentIdentifier`, `schoolId` |  |
| `schoolReference` | key | reference: `schoolId` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `educationalEnvironmentDescriptor` |  | descriptor URI | The setting where the RestraintEvent was exercised. |
| `eventDate` | yes | string (date) | Month, day, and year of the restraint event. |
| `programs` |  | array of edFi_restraintEventProgram | An unordered collection of restraintEventPrograms. |
| `reasons` |  | array of edFi_restraintEventReason | An unordered collection of restraintEventReasons. |

## Endpoints

- `DELETE /ed-fi/restraintEvents/{id}`
- `GET /ed-fi/restraintEvents/deletes`
- `GET /ed-fi/restraintEvents/keyChanges`
- `GET /ed-fi/restraintEvents/partitions`
- `GET /ed-fi/restraintEvents/{id}`
- `GET /ed-fi/restraintEvents`
- `POST /ed-fi/restraintEvents`
- `PUT /ed-fi/restraintEvents/{id}`
