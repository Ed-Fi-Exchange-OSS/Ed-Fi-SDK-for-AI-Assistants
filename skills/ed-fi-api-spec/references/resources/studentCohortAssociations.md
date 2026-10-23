# studentCohortAssociations

`/ed-fi/studentCohortAssociations`

This association represents the cohort(s) for which a student is designated.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | yes | string (date) | The month, day, and year on which the student was first identified as part of the cohort. |
| `cohortReference` | yes | reference; supply `cohortIdentifier`, `educationOrganizationId` | This entity represents any type of list of designated students for tracking, analysis, or intervention. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `endDate` |  | string (date) | The month, day, and year on which the student was removed as part of the cohort. |
| `sections` |  | array of edFi_studentCohortAssociationSection | An unordered collection of studentCohortAssociationSections. |

### Items in `sections`

| Field | Required | Type | Description |
|---|---|---|---|
| `sectionReference` | yes | reference; supply `localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName` | This entity represents a setting in which organized instruction of course content is provided, in-person or otherwise, to one or more students for a given peri… |

## Endpoints

- `GET /ed-fi/studentCohortAssociations`
- `POST /ed-fi/studentCohortAssociations`
- `GET /ed-fi/studentCohortAssociations/deletes`
- `GET /ed-fi/studentCohortAssociations/keyChanges`
- `GET /ed-fi/studentCohortAssociations/partitions`
- `GET /ed-fi/studentCohortAssociations/{id}`
- `PUT /ed-fi/studentCohortAssociations/{id}`
- `DELETE /ed-fi/studentCohortAssociations/{id}`
