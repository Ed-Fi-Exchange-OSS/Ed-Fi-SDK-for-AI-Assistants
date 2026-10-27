# staffSectionAssociations

`/ed-fi/staffSectionAssociations`

This association indicates the class sections to which a staff member is assigned.

Also searched as: teacher.

## Natural key

`beginDate`, `localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName`, `staffUniqueId`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | yes | string (date) | Month, day, and year of a teacher's assignment to the section. |
| `sectionReference` | yes | reference; supply `localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName` | This entity represents a setting in which organized instruction of course content is provided, in-person or otherwise, to one or more students for a given peri… |
| `staffReference` | yes | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |
| `classroomPositionDescriptor` | yes | descriptor URI | The type of position the staff member holds in the specific class/section. |
| `endDate` |  | string (date) | Month, day, and year of the last day of a staff member's assignment to the section. |
| `highlyQualifiedTeacher` |  | boolean | An indication of whether a teacher is classified as highly qualified for his/her assignment according to state definition. |
| `percentageContribution` |  | number (double) | Indicates the percentage of the total scheduled course time, academic standards, and/or learning activities delivered in this section by this staff member. |
| `teacherStudentDataLinkExclusion` |  | boolean | Indicates that the entire section is excluded from calculation of value-added or growth attribution calculations used for a particular teacher evaluation. |

## Endpoints

- `GET /ed-fi/staffSectionAssociations`
- `POST /ed-fi/staffSectionAssociations`
- `GET /ed-fi/staffSectionAssociations/deletes`
- `GET /ed-fi/staffSectionAssociations/keyChanges`
- `GET /ed-fi/staffSectionAssociations/partitions`
- `GET /ed-fi/staffSectionAssociations/{id}`
- `PUT /ed-fi/staffSectionAssociations/{id}`
- `DELETE /ed-fi/staffSectionAssociations/{id}`
