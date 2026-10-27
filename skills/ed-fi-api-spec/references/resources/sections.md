# sections

`/ed-fi/sections`

This entity represents a setting in which organized instruction of course content is provided, in-person or
otherwise, to one or more students for a given period of time. A course offering may be offered to more than
one section.

Also searched as: class.

## Natural key

`sectionIdentifier`, `localCourseCode`, `schoolId`, `schoolYear`, `sessionName`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `sectionIdentifier` | yes | string max 255 | The local identifier assigned to a section. |
| `courseOfferingReference` | yes | reference; supply `localCourseCode`, `schoolId`, `schoolYear`, `sessionName` | This entity represents an entry in the course catalog of available courses offered by the school during a session. |
| `locationReference` |  | reference; supply `classroomIdentificationCode`, `schoolId` | This entity represents the physical space where students gather for a particular class/section. |
| `locationSchoolReference` |  | reference; supply `schoolId` | This entity represents an educational organization that includes staff and students who participate in classes and educational activity groups. |
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

### Items in `characteristics`

| Field | Required | Type | Description |
|---|---|---|---|
| `sectionCharacteristicDescriptor` | yes | descriptor URI | Reflects important characteristics of the section, such as whether or not attendance is taken and the section is graded. |

### Items in `classPeriods`

| Field | Required | Type | Description |
|---|---|---|---|
| `classPeriodReference` | yes | reference; supply `classPeriodName`, `schoolId` | This entity represents the designation of a regularly scheduled series of class meetings at designated times and days of the week. |

### Items in `courseLevelCharacteristics`

| Field | Required | Type | Description |
|---|---|---|---|
| `courseLevelCharacteristicDescriptor` | yes | descriptor URI | The type of specific program or designation with which the section is associated. |

### Items in `offeredGradeLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `gradeLevelDescriptor` | yes | descriptor URI | The grade levels in which the section is offered. |

### Items in `programs`

| Field | Required | Type | Description |
|---|---|---|---|
| `programReference` | yes | reference; supply `educationOrganizationId`, `programName`, `programTypeDescriptor` | This entity represents any program designed to work in conjunction with, or as a supplement to, the main academic program. |

## Endpoints

- `GET /ed-fi/sections`
- `POST /ed-fi/sections`
- `GET /ed-fi/sections/deletes`
- `GET /ed-fi/sections/keyChanges`
- `GET /ed-fi/sections/partitions`
- `GET /ed-fi/sections/{id}`
- `PUT /ed-fi/sections/{id}`
- `DELETE /ed-fi/sections/{id}`

`PUT` can change this resource's identifying values; the API cascades the change to records that reference it
(cascading key updates, `x-Ed-Fi-isUpdatable` in the specification).
