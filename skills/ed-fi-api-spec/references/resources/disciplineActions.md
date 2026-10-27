# disciplineActions

`/ed-fi/disciplineActions`

This event entity represents actions taken by an education organization after a disruptive event that is
recorded as a discipline incident.

## Natural key

`disciplineActionIdentifier`, `disciplineDate`, `studentUniqueId`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `disciplineActionIdentifier` | yes | string max 36 | Identifier assigned by the education organization to the discipline action. |
| `disciplineDate` | yes | string (date) | The date of the discipline action. |
| `disciplines` | yes | array of edFi_disciplineActionDiscipline | An unordered collection of disciplineActionDisciplines. |
| `assignmentSchoolReference` |  | reference; supply `schoolId` | This entity represents an educational organization that includes staff and students who participate in classes and educational activity groups. |
| `responsibilitySchoolReference` | yes | reference; supply `schoolId` | This entity represents an educational organization that includes staff and students who participate in classes and educational activity groups. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `actualDisciplineActionLength` |  | number (double) | Indicates the actual length in school days of a student's disciplinary assignment. |
| `disciplineActionLength` |  | number (double) | The length of time in school days for the discipline action (e.g. removal, detention), if applicable. |
| `disciplineActionLengthDifferenceReasonDescriptor` |  | descriptor URI | Indicates the reason for the difference, if any, between the official and actual lengths of a student's disciplinary assignment. |
| `iepPlacementMeetingIndicator` |  | boolean | An indication as to whether an offense and/or disciplinary action resulted in a meeting of a student's Individualized Education Program (IEP) team to determine… |
| `relatedToZeroTolerancePolicy` |  | boolean | An indication of whether or not this disciplinary action taken against a student was imposed as a consequence of state or local zero tolerance policies. |
| `staffs` |  | array of edFi_disciplineActionStaff | An unordered collection of disciplineActionStaffs. |
| `studentDisciplineIncidentBehaviorAssociations` |  | array of edFi_disciplineActionStudentDisciplineIncidentBehaviorAssociation | An unordered collection of disciplineActionStudentDisciplineIncidentBehaviorAssociations. |

### Items in `disciplines`

| Field | Required | Type | Description |
|---|---|---|---|
| `disciplineDescriptor` | yes | descriptor URI | Type of action, such as removal from the classroom, used to discipline the student involved as a perpetrator in a discipline incident. |

### Items in `staffs`

| Field | Required | Type | Description |
|---|---|---|---|
| `staffReference` | yes | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |

### Items in `studentDisciplineIncidentBehaviorAssociations`

| Field | Required | Type | Description |
|---|---|---|---|
| `studentDisciplineIncidentBehaviorAssociationReference` | yes | reference; supply `behaviorDescriptor`, `incidentIdentifier`, `schoolId`, `studentUniqueId` | This association describes the behavior of students involved in a discipline incident. |

## Endpoints

- `GET /ed-fi/disciplineActions`
- `POST /ed-fi/disciplineActions`
- `GET /ed-fi/disciplineActions/deletes`
- `GET /ed-fi/disciplineActions/keyChanges`
- `GET /ed-fi/disciplineActions/partitions`
- `GET /ed-fi/disciplineActions/{id}`
- `PUT /ed-fi/disciplineActions/{id}`
- `DELETE /ed-fi/disciplineActions/{id}`
