# courseTranscripts

`/ed-fi/courseTranscripts`

This entity is the final record of a student's performance in their courses at the end of a semester or school
year.

## Natural key

`courseAttemptResultDescriptor`, `courseCode`, `courseEducationOrganizationId`, `educationOrganizationId`,
`schoolYear`, `studentUniqueId`, `termDescriptor`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `courseAttemptResultDescriptor` | yes | descriptor URI | The result from the student's attempt to take the course. |
| `courseReference` | yes | reference; supply `courseCode`, `educationOrganizationId` | This educational entity represents the organization of subject matter and related learning experiences provided for the instruction of students on a regular or… |
| `externalEducationOrganizationReference` |  | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `responsibleTeacherStaffReference` |  | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |
| `studentAcademicRecordReference` | yes | reference; supply `educationOrganizationId`, `schoolYear`, `studentUniqueId`, `termDescriptor` | This educational entity represents the cumulative record of academic achievement for a student. |
| `academicSubjects` |  | array of edFi_courseTranscriptAcademicSubject | An unordered collection of courseTranscriptAcademicSubjects. |
| `alternativeCourseIdentificationCodes` |  | array of edFi_courseTranscriptAlternativeCourseIdentificationCode | An unordered collection of courseTranscriptAlternativeCourseIdentificationCodes. |
| `alternativeCourseTitle` |  | string max 60 | The descriptive name given to a course of study offered in the school, if different from the CourseTitle. |
| `assigningOrganizationIdentificationCode` |  | string max 60 | The organization code or name assigning the course identification code. |
| `attemptedCreditConversion` |  | number (double) | Conversion factor that when multiplied by the number of credits is equivalent to Carnegie units. |
| `attemptedCredits` |  | number (double) | The value of credits or units of value awarded for the completion of a course. |
| `attemptedCreditTypeDescriptor` |  | descriptor URI | The type of credits or units of value awarded for the completion of a course. |
| `courseCatalogURL` |  | string max 255 | The URL for the course catalog that defines the course identification code. |
| `coursePrograms` |  | array of edFi_courseTranscriptCourseProgram | An unordered collection of courseTranscriptCoursePrograms. |
| `courseRepeatCodeDescriptor` |  | descriptor URI | Indicates that an academic course has been repeated by a student and how that repeat is to be computed in the student's academic grade average. |
| `courseTitle` |  | string max 60 | The descriptive name given to a course of study offered in a school or other institution or organization. |
| `creditCategories` |  | array of edFi_courseTranscriptCreditCategory | An unordered collection of courseTranscriptCreditCategories. |
| `earnedAdditionalCredits` |  | array of edFi_courseTranscriptEarnedAdditionalCredits | An unordered collection of courseTranscriptEarnedAdditionalCredits. |
| `earnedCreditConversion` |  | number (double) | Conversion factor that when multiplied by the number of credits is equivalent to Carnegie units. |
| `earnedCredits` |  | number (double) | The value of credits or units of value awarded for the completion of a course. |
| `earnedCreditTypeDescriptor` |  | descriptor URI | The type of credits or units of value awarded for the completion of a course. |
| `externalEducationOrganizationNameOfInstitution` |  | string max 75 | Name of the external institution where the student completed the course; to be used only when the reference external education organization is not available. |
| `finalLetterGradeEarned` |  | string max 20 | The final indicator of student performance in a class as submitted by the instructor. |
| `finalNumericGradeEarned` |  | number (double) | The final indicator of student performance in a class as submitted by the instructor. |
| `methodCreditEarnedDescriptor` |  | descriptor URI | The method the credits were earned. |
| `partialCourseTranscriptAwards` |  | array of edFi_courseTranscriptPartialCourseTranscriptAwards | An unordered collection of courseTranscriptPartialCourseTranscriptAwards. |
| `sections` |  | array of edFi_courseTranscriptSection | An unordered collection of courseTranscriptSections. |
| `whenTakenGradeLevelDescriptor` |  | descriptor URI | Student's grade level at time of course. |

### Items in `academicSubjects`

| Field | Required | Type | Description |
|---|---|---|---|
| `academicSubjectDescriptor` | yes | descriptor URI | The subject area for the course transcript credits awarded in the course transcript. |

### Items in `alternativeCourseIdentificationCodes`

| Field | Required | Type | Description |
|---|---|---|---|
| `courseIdentificationSystemDescriptor` | yes | descriptor URI | A system that is used to identify the organization of subject matter and related learning experiences provided for the instruction of students. |
| `assigningOrganizationIdentificationCode` |  | string max 60 | The organization code or name assigning the Identification Code. |
| `courseCatalogURL` |  | string max 255 | The URL for the course catalog that defines the course identification code. |
| `identificationCode` | yes | string max 60 | A unique number or alphanumeric code assigned to a course by a school, school system, state, or other agency or entity. |

### Items in `coursePrograms`

| Field | Required | Type | Description |
|---|---|---|---|
| `courseProgramReference` | yes | reference; supply `educationOrganizationId`, `programName`, `programTypeDescriptor` | This entity represents any program designed to work in conjunction with, or as a supplement to, the main academic program. |

### Items in `creditCategories`

| Field | Required | Type | Description |
|---|---|---|---|
| `creditCategoryDescriptor` | yes | descriptor URI | A categorization for the course transcript credits awarded in the course transcript. |

### Items in `earnedAdditionalCredits`

| Field | Required | Type | Description |
|---|---|---|---|
| `additionalCreditTypeDescriptor` | yes | descriptor URI | The type of credits or units of value awarded for the completion of a course. |
| `credits` | yes | number (double) | The value of credits or units of value awarded for the completion of a course |

### Items in `partialCourseTranscriptAwards`

| Field | Required | Type | Description |
|---|---|---|---|
| `awardDate` | yes | string (date) | The date the partial credits and/or grades were awarded or earned. |
| `methodCreditEarnedDescriptor` |  | descriptor URI | The method the credits were earned. |
| `earnedCredits` | yes | number (double) | The number of credits a student earned for completing a given course. |
| `letterGradeEarned` |  | string max 20 | The indicator of student performance as submitted by the instructor. |
| `numericGradeEarned` |  | string max 20 | The indicator of student performance as submitted by the instructor. |

### Items in `sections`

| Field | Required | Type | Description |
|---|---|---|---|
| `sectionReference` | yes | reference; supply `localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName` | This entity represents a setting in which organized instruction of course content is provided, in-person or otherwise, to one or more students for a given peri… |

## Endpoints

- `GET /ed-fi/courseTranscripts`
- `POST /ed-fi/courseTranscripts`
- `GET /ed-fi/courseTranscripts/deletes`
- `GET /ed-fi/courseTranscripts/keyChanges`
- `GET /ed-fi/courseTranscripts/partitions`
- `GET /ed-fi/courseTranscripts/{id}`
- `PUT /ed-fi/courseTranscripts/{id}`
- `DELETE /ed-fi/courseTranscripts/{id}`
