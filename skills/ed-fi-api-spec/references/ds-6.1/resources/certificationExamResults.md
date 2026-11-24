# certificationExamResults

`/ed-fi/certificationExamResults`

The person's result from taking a certification exam.

## Natural key

`certificationExamDate`, `certificationExamIdentifier`, `namespace`, `personId`, `sourceSystemDescriptor`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `certificationExamDate` | yes | string (date) | The month, day, and year on which the certification exam is taken. |
| `certificationExamReference` | yes | reference; supply `certificationExamIdentifier`, `namespace` | An examination required by one or more certifications. |
| `certificationExamStudentAssessmentReference` |  | reference; supply `assessmentIdentifier`, `namespace`, `studentAssessmentIdentifier`, `studentUniqueId` | This entity represents the analysis or scoring of a student's response on an assessment. |
| `personReference` | yes | reference; supply `personId`, `sourceSystemDescriptor` | Reference to person. |
| `attemptNumber` |  | integer (int32) | The number of the person's attempt for the certification exam. |
| `certificationExamPassIndicator` |  | boolean | Indicator that the person passed the certification exam. |
| `certificationExamScore` |  | number (double) | The score result for the certification exam attempt. |
| `certificationExamStatusDescriptor` |  | descriptor URI | The status of the certification exam attempt. |

## Endpoints

- `GET /ed-fi/certificationExamResults`
- `POST /ed-fi/certificationExamResults`
- `GET /ed-fi/certificationExamResults/deletes`
- `GET /ed-fi/certificationExamResults/keyChanges`
- `GET /ed-fi/certificationExamResults/partitions`
- `GET /ed-fi/certificationExamResults/{id}`
- `PUT /ed-fi/certificationExamResults/{id}`
- `DELETE /ed-fi/certificationExamResults/{id}`
