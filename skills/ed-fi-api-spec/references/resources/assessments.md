# assessments

`/ed-fi/assessments`

This entity represents a tool, instrument, process, or exhibition composed of a systematic sampling of
behavior for measuring a student's competence, knowledge, skills, or behavior. An assessment can be used to
measure differences in individuals or groups and changes in performance from one occasion to the next.

## Natural key

`assessmentIdentifier`, `namespace`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `academicSubjects` | yes | array of edFi_assessmentAcademicSubject | An unordered collection of assessmentAcademicSubjects. |
| `assessmentIdentifier` | key | string max 60 | A unique number or alphanumeric code assigned to an assessment. |
| `namespace` | key | string max 255 | Namespace for the assessment. |
| `educationOrganizationReference` |  | reference: `educationOrganizationId` |  |
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

## Endpoints

- `DELETE /ed-fi/assessments/{id}`
- `GET /ed-fi/assessments/deletes`
- `GET /ed-fi/assessments/keyChanges`
- `GET /ed-fi/assessments/partitions`
- `GET /ed-fi/assessments/{id}`
- `GET /ed-fi/assessments`
- `POST /ed-fi/assessments`
- `PUT /ed-fi/assessments/{id}`
