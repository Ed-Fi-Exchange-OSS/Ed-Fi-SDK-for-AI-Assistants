# courseOfferings

`/ed-fi/courseOfferings`

This entity represents an entry in the course catalog of available courses offered by the school during a
session.

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `localCourseCode` | yes | string max 60 | The local code assigned by the School that identifies the course offering provided for the instruction of students. |
| `courseReference` | yes | reference; supply `courseCode`, `educationOrganizationId` | This educational entity represents the organization of subject matter and related learning experiences provided for the instruction of students on a regular or… |
| `schoolReference` | yes | reference; supply `schoolId` | This entity represents an educational organization that includes staff and students who participate in classes and educational activity groups. |
| `sessionReference` | yes | reference; supply `schoolId`, `schoolYear`, `sessionName` | A specific designated unit of time during which instruction is provided, grades are reported and academic credits are awarded to students (whenever applicable). |
| `courseLevelCharacteristics` |  | array of edFi_courseOfferingCourseLevelCharacteristic | An unordered collection of courseOfferingCourseLevelCharacteristics. |
| `curriculumUseds` |  | array of edFi_courseOfferingCurriculumUsed | An unordered collection of courseOfferingCurriculumUseds. |
| `instructionalTimePlanned` |  | integer (int32) | The planned total number of clock minutes of instruction for this course offering. |
| `localCourseTitle` |  | string max 60 | The descriptive name given to a course of study offered in the school, if different from the course title. |
| `offeredGradeLevels` |  | array of edFi_courseOfferingOfferedGradeLevel | An unordered collection of courseOfferingOfferedGradeLevels. |

### Items in `courseLevelCharacteristics`

| Field | Required | Type | Description |
|---|---|---|---|
| `courseLevelCharacteristicDescriptor` | yes | descriptor URI | The type of specific program or designation with which the course offering is associated (e.g., AP, IB, Dual Credit, CTE). |

### Items in `curriculumUseds`

| Field | Required | Type | Description |
|---|---|---|---|
| `curriculumUsedDescriptor` | yes | descriptor URI | The type of curriculum used in an early learning classroom or group. |

### Items in `offeredGradeLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `gradeLevelDescriptor` | yes | descriptor URI | The grade levels in which the course is offered. |

## Endpoints

- `GET /ed-fi/courseOfferings`
- `POST /ed-fi/courseOfferings`
- `GET /ed-fi/courseOfferings/deletes`
- `GET /ed-fi/courseOfferings/keyChanges`
- `GET /ed-fi/courseOfferings/partitions`
- `GET /ed-fi/courseOfferings/{id}`
- `PUT /ed-fi/courseOfferings/{id}`
- `DELETE /ed-fi/courseOfferings/{id}`
