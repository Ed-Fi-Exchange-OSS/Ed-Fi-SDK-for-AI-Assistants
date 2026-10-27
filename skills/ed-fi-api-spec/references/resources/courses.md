# courses

`/ed-fi/courses`

This educational entity represents the organization of subject matter and related learning experiences
provided for the instruction of students on a regular or systematic basis.

## Natural key

`courseCode`, `educationOrganizationId`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `courseCode` | yes | string max 60 | A unique alphanumeric code assigned to a course. |
| `identificationCodes` | yes | array of edFi_courseIdentificationCode | An unordered collection of courseIdentificationCodes. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `academicSubjects` |  | array of edFi_courseAcademicSubject | An unordered collection of courseAcademicSubjects. |
| `careerPathwayDescriptor` |  | descriptor URI | Indicates the career cluster or pathway the course is associated with as part of a CTE curriculum. |
| `competencyLevels` |  | array of edFi_courseCompetencyLevel | An unordered collection of courseCompetencyLevels. |
| `courseDefinedByDescriptor` |  | descriptor URI | Specifies whether the course was defined by the SEA, LEA, School, or national organization. |
| `courseDescription` |  | string max 1024 | A description of the content standards and goals covered in the course. |
| `courseGPAApplicabilityDescriptor` |  | descriptor URI | An indicator of whether or not the course being described is included in the computation of the student's grade point average, and if so, if it is weighted dif… |
| `courseTitle` | yes | string max 60 | The descriptive name given to a course of study offered in a school or other institution or organization. |
| `dateCourseAdopted` |  | string (date) | Date the course was adopted by the education agency. |
| `highSchoolCourseRequirement` |  | boolean | An indication that this course may satisfy high school graduation requirements in the course's subject area. |
| `learningStandards` |  | array of edFi_courseLearningStandard | An unordered collection of courseLearningStandards. |
| `levelCharacteristics` |  | array of edFi_courseLevelCharacteristic | An unordered collection of courseLevelCharacteristics. |
| `maxCompletionsForCredit` |  | integer (int32) | Designates how many times the course may be taken with credit received by the student. |
| `maximumAvailableCreditConversion` |  | number (double) | Conversion factor that when multiplied by the number of credits is equivalent to Carnegie units. |
| `maximumAvailableCredits` |  | number (double) | The value of credits or units of value awarded for the completion of a course. |
| `maximumAvailableCreditTypeDescriptor` |  | descriptor URI | The type of credits or units of value awarded for the completion of a course. |
| `minimumAvailableCreditConversion` |  | number (double) | Conversion factor that when multiplied by the number of credits is equivalent to Carnegie units. |
| `minimumAvailableCredits` |  | number (double) | The value of credits or units of value awarded for the completion of a course. |
| `minimumAvailableCreditTypeDescriptor` |  | descriptor URI | The type of credits or units of value awarded for the completion of a course. |
| `numberOfParts` | yes | integer (int32) | The number of parts identified for a course. |
| `offeredGradeLevels` |  | array of edFi_courseOfferedGradeLevel | An unordered collection of courseOfferedGradeLevels. |
| `timeRequiredForCompletion` |  | integer (int32) | The actual or estimated number of clock minutes required for class completion. |

### Items in `identificationCodes`

| Field | Required | Type | Description |
|---|---|---|---|
| `courseIdentificationSystemDescriptor` | yes | descriptor URI | A system that is used to identify the organization of subject matter and related learning experiences provided for the instruction of students. |
| `assigningOrganizationIdentificationCode` |  | string max 60 | The organization code or name assigning the Identification Code. |
| `courseCatalogURL` |  | string max 255 | The URL for the course catalog that defines the course identification code. |
| `identificationCode` | yes | string max 60 | A unique number or alphanumeric code assigned to a course by a school, school system, state, or other agency or entity. |

### Items in `academicSubjects`

| Field | Required | Type | Description |
|---|---|---|---|
| `academicSubjectDescriptor` | yes | descriptor URI | The intended major subject/s area of the course. |

### Items in `competencyLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `competencyLevelDescriptor` | yes | descriptor URI | The competency levels defined to rate the student for the course. |

### Items in `learningStandards`

| Field | Required | Type | Description |
|---|---|---|---|
| `learningStandardReference` | yes | reference; supply `learningStandardId` | A statement that describes a specific competency or academic standard. |

### Items in `levelCharacteristics`

| Field | Required | Type | Description |
|---|---|---|---|
| `courseLevelCharacteristicDescriptor` | yes | descriptor URI | The type of specific program or designation with which the course is associated (e.g., AP, IB, Dual Credit, CTE). |

### Items in `offeredGradeLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `gradeLevelDescriptor` | yes | descriptor URI | The grade levels in which the course is offered. |

## Endpoints

- `GET /ed-fi/courses`
- `POST /ed-fi/courses`
- `GET /ed-fi/courses/deletes`
- `GET /ed-fi/courses/keyChanges`
- `GET /ed-fi/courses/partitions`
- `GET /ed-fi/courses/{id}`
- `PUT /ed-fi/courses/{id}`
- `DELETE /ed-fi/courses/{id}`
