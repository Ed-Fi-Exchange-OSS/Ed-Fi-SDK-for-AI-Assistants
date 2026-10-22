# courseOfferings

`/ed-fi/courseOfferings`

This entity represents an entry in the course catalog of available courses offered by the school during a session.

## Natural key

`localCourseCode`, `courseReference`, `schoolReference`, `sessionReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `localCourseCode` | key | string max 60 | The local code assigned by the School that identifies the course offering provided for the instruction of students. |
| `courseReference` | key | reference: `courseCode`, `educationOrganizationId` |  |
| `schoolReference` | key | reference: `schoolId` |  |
| `sessionReference` | key | reference: `schoolId`, `schoolYear`, `sessionName` |  |
| `courseLevelCharacteristics` |  | array of edFi_courseOfferingCourseLevelCharacteristic | An unordered collection of courseOfferingCourseLevelCharacteristics. |
| `curriculumUseds` |  | array of edFi_courseOfferingCurriculumUsed | An unordered collection of courseOfferingCurriculumUseds. |
| `instructionalTimePlanned` |  | integer (int32) | The planned total number of clock minutes of instruction for this course offering. |
| `localCourseTitle` |  | string max 60 | The descriptive name given to a course of study offered in the school, if different from the course title. |
| `offeredGradeLevels` |  | array of edFi_courseOfferingOfferedGradeLevel | An unordered collection of courseOfferingOfferedGradeLevels. |

## Endpoints

- `DELETE /ed-fi/courseOfferings/{id}`
- `GET /ed-fi/courseOfferings/deletes`
- `GET /ed-fi/courseOfferings/keyChanges`
- `GET /ed-fi/courseOfferings/partitions`
- `GET /ed-fi/courseOfferings/{id}`
- `GET /ed-fi/courseOfferings`
- `POST /ed-fi/courseOfferings`
- `PUT /ed-fi/courseOfferings/{id}`
