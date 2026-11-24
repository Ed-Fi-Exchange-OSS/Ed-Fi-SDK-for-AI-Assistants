# fieldworkExperienceSectionAssociations

`/ed-fi/fieldworkExperienceSectionAssociations`

Associates field work experience with a section.

## Natural key

`beginDate`, `fieldworkIdentifier`, `studentUniqueId`, `localCourseCode`, `schoolId`, `schoolYear`,
`sectionIdentifier`, `sessionName`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `fieldworkExperienceReference` | yes | reference; supply `beginDate`, `fieldworkIdentifier`, `studentUniqueId` | The information regarding a post-secondary instructional course in a particular field of study that typically involves a prescribed number, instruction periods… |
| `sectionReference` | yes | reference; supply `localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName` | This entity represents a setting in which organized instruction of course content is provided, in-person or otherwise, to one or more students for a given peri… |

## Endpoints

- `GET /ed-fi/fieldworkExperienceSectionAssociations`
- `POST /ed-fi/fieldworkExperienceSectionAssociations`
- `GET /ed-fi/fieldworkExperienceSectionAssociations/deletes`
- `GET /ed-fi/fieldworkExperienceSectionAssociations/keyChanges`
- `GET /ed-fi/fieldworkExperienceSectionAssociations/partitions`
- `GET /ed-fi/fieldworkExperienceSectionAssociations/{id}`
- `PUT /ed-fi/fieldworkExperienceSectionAssociations/{id}`
- `DELETE /ed-fi/fieldworkExperienceSectionAssociations/{id}`
