# studentAssessments

`/ed-fi/studentAssessments`

This entity represents the analysis or scoring of a student's response on an assessment. The analysis results
in a value that represents a student's performance on a set of items on a test.

Also searched as: test results, test scores.

## Natural key

`studentAssessmentIdentifier`, `assessmentIdentifier`, `namespace`, `studentUniqueId`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `studentAssessmentIdentifier` | yes | string max 60 | A unique number or alphanumeric code assigned to an assessment administered to a student. |
| `assessmentReference` | yes | reference; supply `assessmentIdentifier`, `namespace` | This entity represents a tool, instrument, process, or exhibition composed of a systematic sampling of behavior for measuring a student's competence, knowledge… |
| `reportedSchoolReference` |  | reference; supply `schoolId` | This entity represents an educational organization that includes staff and students who participate in classes and educational activity groups. |
| `schoolYearTypeReference` |  | reference; supply `schoolYear` | Identifier for a school year. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `accommodations` |  | array of edFi_studentAssessmentAccommodation | An unordered collection of studentAssessmentAccommodations. |
| `administrationDate` |  | string (date-time) | The date and time an assessment was completed by the student. |
| `administrationEndDate` |  | string (date-time) | The date and time an assessment administration ended. |
| `administrationEnvironmentDescriptor` |  | descriptor URI | The environment in which the test was administered. |
| `administrationLanguageDescriptor` |  | descriptor URI | The language in which an assessment is written and/or administered. |
| `assessedMinutes` |  | integer (int32) | Reported time student was assessed in minutes. |
| `eventCircumstanceDescriptor` |  | descriptor URI | An unusual event occurred during the administration of the assessment. |
| `eventDescription` |  | string max 1024 | Describes special events that occur before during or after the assessment session that may impact use of results. |
| `items` |  | array of edFi_studentAssessmentItem | An unordered collection of studentAssessmentItems. |
| `performanceLevels` |  | array of edFi_studentAssessmentPerformanceLevel | An unordered collection of studentAssessmentPerformanceLevels. |
| `period` |  | edFi_studentAssessmentPeriod |  |
| `platformTypeDescriptor` |  | descriptor URI | The platform with which the assessment was delivered to the student during the assessment session. |
| `reasonNotTestedDescriptor` |  | descriptor URI | The primary reason student is not tested. |
| `reportedSchoolIdentifier` |  | string max 60 | A reported school identifier for the school the enrollment at the time of the assessment used when the assigned SchoolId is not known by the assessment vendor. |
| `retestIndicatorDescriptor` |  | descriptor URI | Indicator if the test was a retake. |
| `scoreResults` |  | array of edFi_studentAssessmentScoreResult | An unordered collection of studentAssessmentScoreResults. |
| `serialNumber` |  | string max 60 | The unique number for the assessment form or answer document. |
| `studentObjectiveAssessments` |  | array of edFi_studentAssessmentStudentObjectiveAssessment | An unordered collection of studentAssessmentStudentObjectiveAssessments. |
| `whenAssessedGradeLevelDescriptor` |  | descriptor URI | The grade level of a student when assessed. |

### Items in `accommodations`

| Field | Required | Type | Description |
|---|---|---|---|
| `accommodationDescriptor` | yes | descriptor URI | The specific type of special variation used in how an examination is presented, how it is administered, or how the test taker is allowed to respond. |

### Items in `items`

| Field | Required | Type | Description |
|---|---|---|---|
| `assessmentItemResultDescriptor` | yes | descriptor URI | The analyzed result of a student's response to an assessment item. |
| `responseIndicatorDescriptor` |  | descriptor URI | Indicator of the response. |
| `assessmentResponse` |  | string max 255 | A student's response to a stimulus on a test. |
| `descriptiveFeedback` |  | string max 1024 | The formative descriptive feedback that was given to a student in response to the results from a scored/evaluated assessment item. |
| `itemNumber` |  | integer (int32) | The test question number for this student's test item. |
| `rawScoreResult` |  | number (double) | A meaningful raw score of the performance of a student on an assessment item. |
| `timeAssessed` |  | string max 30 | The overall time that a student actually spent on the assessment item expressed in minutes. |
| `assessmentItemReference` | yes | reference; supply `assessmentIdentifier`, `identificationCode`, `namespace` | This entity represents one of many single measures that make up an assessment. |

### Items in `performanceLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `assessmentReportingMethodDescriptor` | yes | descriptor URI | The method that the instructor of the class uses to report the performance and achievement. |
| `performanceLevelDescriptor` | yes | descriptor URI | A specification of which performance level value describes the student proficiency. |
| `performanceLevelIndicatorName` |  | string max 60 | The name of the indicator being measured for a collection of performance level values. |

### Items in `scoreResults`

| Field | Required | Type | Description |
|---|---|---|---|
| `assessmentReportingMethodDescriptor` | yes | descriptor URI | The method that the administrator of the assessment uses to report the performance and achievement of all students. |
| `resultDatatypeTypeDescriptor` | yes | descriptor URI | The datatype of the result. |
| `result` | yes | string max 35 | The value of a meaningful raw score or statistical expression of the performance of an individual. |

### Items in `studentObjectiveAssessments`

| Field | Required | Type | Description |
|---|---|---|---|
| `administrationDate` |  | string (date-time) | The date and time an assessment was completed by the student. |
| `administrationEndDate` |  | string (date-time) | The date and time an assessment administration ended. |
| `assessedMinutes` |  | integer (int32) | Reported time student was assessed in minutes. |
| `objectiveAssessmentReference` | yes | reference; supply `assessmentIdentifier`, `identificationCode`, `namespace` | This entity represents subtests that assess specific learning objectives. |
| `performanceLevels` |  | array of edFi_studentAssessmentStudentObjectiveAssessmentPerformanceLevel | An unordered collection of studentAssessmentStudentObjectiveAssessmentPerformanceLevels. |
| `scoreResults` |  | array of edFi_studentAssessmentStudentObjectiveAssessmentScoreResult | An unordered collection of studentAssessmentStudentObjectiveAssessmentScoreResults. |

## Endpoints

- `GET /ed-fi/studentAssessments`
- `POST /ed-fi/studentAssessments`
- `GET /ed-fi/studentAssessments/deletes`
- `GET /ed-fi/studentAssessments/keyChanges`
- `GET /ed-fi/studentAssessments/partitions`
- `GET /ed-fi/studentAssessments/{id}`
- `PUT /ed-fi/studentAssessments/{id}`
- `DELETE /ed-fi/studentAssessments/{id}`
