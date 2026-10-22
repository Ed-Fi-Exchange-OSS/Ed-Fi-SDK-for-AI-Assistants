# courseTranscripts

`/ed-fi/courseTranscripts`

This entity is the final record of a student's performance in their courses at the end of a semester or school
year.

## Natural key

`courseAttemptResultDescriptor`, `courseReference`, `studentAcademicRecordReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `courseAttemptResultDescriptor` | key | descriptor URI | The result from the student's attempt to take the course. |
| `courseReference` | key | reference: `courseCode`, `educationOrganizationId` |  |
| `externalEducationOrganizationReference` |  | reference: `educationOrganizationId` |  |
| `responsibleTeacherStaffReference` |  | reference: `staffUniqueId` |  |
| `studentAcademicRecordReference` | key | reference: `educationOrganizationId`, `schoolYear`, `studentUniqueId`, `termDescriptor` |  |
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

## Endpoints

- `DELETE /ed-fi/courseTranscripts/{id}`
- `GET /ed-fi/courseTranscripts/deletes`
- `GET /ed-fi/courseTranscripts/keyChanges`
- `GET /ed-fi/courseTranscripts/partitions`
- `GET /ed-fi/courseTranscripts/{id}`
- `GET /ed-fi/courseTranscripts`
- `POST /ed-fi/courseTranscripts`
- `PUT /ed-fi/courseTranscripts/{id}`
