# staffSectionAssociations

`/ed-fi/staffSectionAssociations`

This association indicates the class sections to which a staff member is assigned.

Also searched as: teacher.

## Natural key

`beginDate`, `sectionReference`, `staffReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | key | string (date) | Month, day, and year of a teacher's assignment to the section. |
| `sectionReference` | key | reference: `localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName` |  |
| `staffReference` | key | reference: `staffUniqueId` |  |
| `classroomPositionDescriptor` | yes | descriptor URI | The type of position the staff member holds in the specific class/section. |
| `endDate` |  | string (date) | Month, day, and year of the last day of a staff member's assignment to the section. |
| `highlyQualifiedTeacher` |  | boolean | An indication of whether a teacher is classified as highly qualified for his/her assignment according to state definition. |
| `percentageContribution` |  | number (double) | Indicates the percentage of the total scheduled course time, academic standards, and/or learning activities delivered in this section by this staff member. |
| `teacherStudentDataLinkExclusion` |  | boolean | Indicates that the entire section is excluded from calculation of value-added or growth attribution calculations used for a particular teacher evaluation. |

## Endpoints

- `DELETE /ed-fi/staffSectionAssociations/{id}`
- `GET /ed-fi/staffSectionAssociations/deletes`
- `GET /ed-fi/staffSectionAssociations/keyChanges`
- `GET /ed-fi/staffSectionAssociations/partitions`
- `GET /ed-fi/staffSectionAssociations/{id}`
- `GET /ed-fi/staffSectionAssociations`
- `POST /ed-fi/staffSectionAssociations`
- `PUT /ed-fi/staffSectionAssociations/{id}`
