# assessments

`/ed-fi/assessments`

This entity represents a tool, instrument, process, or exhibition composed of a systematic sampling of
behavior for measuring a student's competence, knowledge, skills, or behavior. An assessment can be used to
measure differences in individuals or groups and changes in performance from one occasion to the next.

## Natural key

`assessmentIdentifier`, `namespace`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `academicSubjects` | yes | array of edFi_assessmentAcademicSubject | An unordered collection of assessmentAcademicSubjects. |
| `assessmentIdentifier` | yes | string max 60 | A unique number or alphanumeric code assigned to an assessment. |
| `namespace` | yes | string max 255 | Namespace for the assessment. |
| `educationOrganizationReference` |  | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `adaptiveAssessment` |  | boolean | Indicates that the assessment is adaptive. |
| `assessedGradeLevels` |  | array of edFi_assessmentAssessedGradeLevel | An unordered collection of assessmentAssessedGradeLevels. |
| `assessmentCategoryDescriptor` |  | descriptor URI | The category of an assessment based on format and content. |
| `assessmentFamily` |  | string max 60 | The assessment family this assessment is a member of. |
| `assessmentForm` |  | string max 60 | Identifies the form of the assessment, for example a regular versus makeup form, multiple choice versus constructed response, etc. |
| `assessmentTitle` | yes | string max 255 | The title or name of the assessment. |
| `assessmentVersion` |  | integer (int32) | The version identifier for the assessment. |
| `contentStandard` |  | edFi_assessmentContentStandard |  |
| `identificationCodes` |  | array of edFi_assessmentIdentificationCode | An unordered collection of assessmentIdentificationCodes. |
| `languages` |  | array of edFi_assessmentLanguage | An unordered collection of assessmentLanguages. |
| `maxRawScore` |  | number (double) | The maximum raw score achievable across all assessment items that are correct and scored at the maximum. |
| `nomenclature` |  | string max 100 | Reflects the specific nomenclature used for assessment. |
| `performanceLevels` |  | array of edFi_assessmentPerformanceLevel | An unordered collection of assessmentPerformanceLevels. |
| `periods` |  | array of edFi_assessmentPeriod | An unordered collection of assessmentPeriods. |
| `platformTypes` |  | array of edFi_assessmentPlatformType | An unordered collection of assessmentPlatformTypes. |
| `programs` |  | array of edFi_assessmentProgram | An unordered collection of assessmentPrograms. |
| `revisionDate` |  | string (date) | The month, day, and year that the conceptual design for the assessment was most recently revised substantially. |
| `scores` |  | array of edFi_assessmentScore | An unordered collection of assessmentScores. |
| `sections` |  | array of edFi_assessmentSection | An unordered collection of assessmentSections. |

### Items in `academicSubjects`

| Field | Required | Type | Description |
|---|---|---|---|
| `academicSubjectDescriptor` | yes | descriptor URI | The description of the content or subject area (e.g., arts, mathematics, reading, stenography, or a foreign language) of an assessment. |

### Items in `assessedGradeLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `gradeLevelDescriptor` | yes | descriptor URI | The grade level(s) for which an assessment is designed. |

### Items in `identificationCodes`

| Field | Required | Type | Description |
|---|---|---|---|
| `assessmentIdentificationSystemDescriptor` | yes | descriptor URI | A coding scheme that is used for identification and record-keeping purposes by schools, social services, or other agencies to refer to an assessment. |
| `assigningOrganizationIdentificationCode` |  | string max 60 | The organization code or name assigning the assessment identification code. |
| `identificationCode` | yes | string max 60 | A unique number or alphanumeric code assigned to an assessment by a school, school system, state, or other agency or entity. |

### Items in `languages`

| Field | Required | Type | Description |
|---|---|---|---|
| `languageDescriptor` | yes | descriptor URI | An indication of the languages in which the assessment is designed. |

### Items in `performanceLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `assessmentReportingMethodDescriptor` | yes | descriptor URI | The method that the instructor of the class uses to report the performance and achievement of all students. |
| `performanceLevelDescriptor` | yes | descriptor URI | The performance level(s) defined for the assessment. |
| `resultDatatypeTypeDescriptor` |  | descriptor URI | The datatype of the result. |
| `maximumScore` |  | string max 35 | The maximum score to make the indicated level of performance. |
| `minimumScore` |  | string max 35 | The minimum score required to make the indicated level of performance. |
| `performanceLevelIndicatorName` |  | string max 60 | The name of the indicator being measured for a collection of performance level values. |

### Items in `periods`

| Field | Required | Type | Description |
|---|---|---|---|
| `assessmentPeriodDescriptor` | yes | descriptor URI | The period of time in which an assessment is supposed to be administered (e.g., Beginning of Year, Middle of Year, End of Year). |
| `beginDate` |  | string (date) | The first date the assessment is to be administered. |
| `endDate` |  | string (date) | The last date the assessment is to be administered. |

### Items in `platformTypes`

| Field | Required | Type | Description |
|---|---|---|---|
| `platformTypeDescriptor` | yes | descriptor URI | The platforms with which the assessment may be delivered. |

### Items in `programs`

| Field | Required | Type | Description |
|---|---|---|---|
| `programReference` | yes | reference; supply `educationOrganizationId`, `programName`, `programTypeDescriptor` | This entity represents any program designed to work in conjunction with, or as a supplement to, the main academic program. |

### Items in `scores`

| Field | Required | Type | Description |
|---|---|---|---|
| `assessmentReportingMethodDescriptor` | yes | descriptor URI | The method that the administrator of the assessment uses to report the performance and achievement of all students. |
| `resultDatatypeTypeDescriptor` |  | descriptor URI | The datatype of the result. |
| `maximumScore` |  | string max 35 | The maximum score possible on the assessment. |
| `minimumScore` |  | string max 35 | The minimum score possible on the assessment. |

### Items in `sections`

| Field | Required | Type | Description |
|---|---|---|---|
| `sectionReference` | yes | reference; supply `localCourseCode`, `schoolId`, `schoolYear`, `sectionIdentifier`, `sessionName` | This entity represents a setting in which organized instruction of course content is provided, in-person or otherwise, to one or more students for a given peri… |

## Endpoints

- `GET /ed-fi/assessments`
- `POST /ed-fi/assessments`
- `GET /ed-fi/assessments/deletes`
- `GET /ed-fi/assessments/keyChanges`
- `GET /ed-fi/assessments/partitions`
- `GET /ed-fi/assessments/{id}`
- `PUT /ed-fi/assessments/{id}`
- `DELETE /ed-fi/assessments/{id}`
