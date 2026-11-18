# staffSchoolAssociations

`/ed-fi/staffSchoolAssociations`

This association indicates the school(s) to which a staff member provides instructional services.

## Natural key

`programAssignmentDescriptor`, `schoolId`, `staffUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `programAssignmentDescriptor` | yes | descriptor URI | The name of the program for which the individual is assigned. |
| `calendarReference` |  | reference; supply `calendarCode`, `schoolId`, `schoolYear` | A set of dates associated with an organization. |
| `schoolReference` | yes | reference; supply `schoolId` | This entity represents an educational organization that includes staff and students who participate in classes and educational activity groups. |
| `schoolYearTypeReference` |  | reference; supply `schoolYear` | Identifier for a school year. |
| `staffReference` | yes | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |
| `academicSubjects` |  | array of edFi_staffSchoolAssociationAcademicSubject | An unordered collection of staffSchoolAssociationAcademicSubjects. |
| `gradeLevels` |  | array of edFi_staffSchoolAssociationGradeLevel | An unordered collection of staffSchoolAssociationGradeLevels. |

### Items in `academicSubjects`

| Field | Required | Type | Description |
|---|---|---|---|
| `academicSubjectDescriptor` | yes | descriptor URI | The academic subjects the individual is eligible to teach. |

### Items in `gradeLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `gradeLevelDescriptor` | yes | descriptor URI | The grade levels the individual is eligible to teach. |

## Endpoints

- `GET /ed-fi/staffSchoolAssociations`
- `POST /ed-fi/staffSchoolAssociations`
- `GET /ed-fi/staffSchoolAssociations/deletes`
- `GET /ed-fi/staffSchoolAssociations/keyChanges`
- `GET /ed-fi/staffSchoolAssociations/partitions`
- `GET /ed-fi/staffSchoolAssociations/{id}`
- `PUT /ed-fi/staffSchoolAssociations/{id}`
- `DELETE /ed-fi/staffSchoolAssociations/{id}`
