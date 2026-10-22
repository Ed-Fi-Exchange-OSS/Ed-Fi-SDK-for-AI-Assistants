# studentAssessments

`/ed-fi/studentAssessments`

This entity represents the analysis or scoring of a student's response on an assessment. The analysis results in a value that represents a student's performance on a set of items on a test.

Also searched as: test results, test scores.

## Natural key

`studentAssessmentIdentifier`, `assessmentReference`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `studentAssessmentIdentifier` | key | string max 60 | A unique number or alphanumeric code assigned to an assessment administered to a student. |
| `assessmentReference` | key | reference: `assessmentIdentifier`, `namespace` |  |
| `reportedSchoolReference` |  | reference: `schoolId` |  |
| `schoolYearTypeReference` |  | reference: `schoolYear` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
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

## Endpoints

- `DELETE /ed-fi/studentAssessments/{id}`
- `GET /ed-fi/studentAssessments/deletes`
- `GET /ed-fi/studentAssessments/keyChanges`
- `GET /ed-fi/studentAssessments/partitions`
- `GET /ed-fi/studentAssessments/{id}`
- `GET /ed-fi/studentAssessments`
- `POST /ed-fi/studentAssessments`
- `PUT /ed-fi/studentAssessments/{id}`
