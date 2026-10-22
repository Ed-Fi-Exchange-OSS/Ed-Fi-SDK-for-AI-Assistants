# sections

`/ed-fi/sections`

This entity represents a setting in which organized instruction of course content is provided, in-person or otherwise, to one or more students for a given period of time. A course offering may be offered to more than one section.

Also searched as: class.

## Natural key

`sectionIdentifier`, `courseOfferingReference`. The natural key can be changed with PUT (cascading key updates).

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `sectionIdentifier` | key | string max 255 | The local identifier assigned to a section. |
| `courseOfferingReference` | key | reference: `localCourseCode`, `schoolId`, `schoolYear`, `sessionName` |  |
| `locationReference` |  | reference: `classroomIdentificationCode`, `schoolId` |  |
| `locationSchoolReference` |  | reference: `schoolId` |  |
| `availableCreditConversion` |  | number (double) | Conversion factor that when multiplied by the number of credits is equivalent to Carnegie units. |
| `availableCredits` |  | number (double) | The value of credits or units of value awarded for the completion of a course. |
| `availableCreditTypeDescriptor` |  | descriptor URI | The type of credits or units of value awarded for the completion of a course. |
| `characteristics` |  | array of edFi_sectionCharacteristic | An unordered collection of sectionCharacteristics. |
| `classPeriods` |  | array of edFi_sectionClassPeriod | An unordered collection of sectionClassPeriods. |
| `courseLevelCharacteristics` |  | array of edFi_sectionCourseLevelCharacteristic | An unordered collection of sectionCourseLevelCharacteristics. |
| `educationalEnvironmentDescriptor` |  | descriptor URI | The setting in which a student receives education and related services. |
| `instructionLanguageDescriptor` |  | descriptor URI | The primary language of instruction. |
| `mediumOfInstructionDescriptor` |  | descriptor URI | The media through which teachers provide instruction to students and students and teachers communicate about instructional matters. |
| `offeredGradeLevels` |  | array of edFi_sectionOfferedGradeLevel | An unordered collection of sectionOfferedGradeLevels. |
| `officialAttendancePeriod` |  | boolean | Indicator of whether this section is used for official daily attendance. |
| `populationServedDescriptor` |  | descriptor URI | The type of students the section is offered and tailored to. |
| `programs` |  | array of edFi_sectionProgram | An unordered collection of sectionPrograms. |
| `sectionName` |  | string max 100 | A locally-defined name for the section, generally created to make the section more recognizable in informal contexts and generally distinct from the section id… |
| `sectionTypeDescriptor` |  | descriptor URI | Specifies whether the section is for attendance only, credit only, or both. |
| `sequenceOfCourse` |  | integer (int32) | When a section is part of a sequence of parts for a course, the number of the sequence. |

## Endpoints

- `DELETE /ed-fi/sections/{id}`
- `GET /ed-fi/sections/deletes`
- `GET /ed-fi/sections/keyChanges`
- `GET /ed-fi/sections/partitions`
- `GET /ed-fi/sections/{id}`
- `GET /ed-fi/sections`
- `POST /ed-fi/sections`
- `PUT /ed-fi/sections/{id}`
