# disciplineActions

`/ed-fi/disciplineActions`

This event entity represents actions taken by an education organization after a disruptive event that is
recorded as a discipline incident.

## Natural key

`disciplineActionIdentifier`, `disciplineDate`, `responsibilitySchoolReference`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `disciplineActionIdentifier` | key | string max 36 | Identifier assigned by the education organization to the discipline action. |
| `disciplineDate` | key | string (date) | The date of the discipline action. |
| `disciplines` | yes | array of edFi_disciplineActionDiscipline | An unordered collection of disciplineActionDisciplines. |
| `assignmentSchoolReference` |  | reference: `schoolId` |  |
| `responsibilitySchoolReference` | key | reference: `schoolId` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `actualDisciplineActionLength` |  | number (double) | Indicates the actual length in school days of a student's disciplinary assignment. |
| `disciplineActionLength` |  | number (double) | The length of time in school days for the discipline action (e.g. |
| `disciplineActionLengthDifferenceReasonDescriptor` |  | descriptor URI | Indicates the reason for the difference, if any, between the official and actual lengths of a student's disciplinary assignment. |
| `iepPlacementMeetingIndicator` |  | boolean | An indication as to whether an offense and/or disciplinary action resulted in a meeting of a student's Individualized Education Program (IEP) team to determine… |
| `relatedToZeroTolerancePolicy` |  | boolean | An indication of whether or not this disciplinary action taken against a student was imposed as a consequence of state or local zero tolerance policies. |
| `staffs` |  | array of edFi_disciplineActionStaff | An unordered collection of disciplineActionStaffs. |
| `studentDisciplineIncidentBehaviorAssociations` |  | array of edFi_disciplineActionStudentDisciplineIncidentBehaviorAssociation | An unordered collection of disciplineActionStudentDisciplineIncidentBehaviorAssociations. |

## Endpoints

- `DELETE /ed-fi/disciplineActions/{id}`
- `GET /ed-fi/disciplineActions/deletes`
- `GET /ed-fi/disciplineActions/keyChanges`
- `GET /ed-fi/disciplineActions/partitions`
- `GET /ed-fi/disciplineActions/{id}`
- `GET /ed-fi/disciplineActions`
- `POST /ed-fi/disciplineActions`
- `PUT /ed-fi/disciplineActions/{id}`
