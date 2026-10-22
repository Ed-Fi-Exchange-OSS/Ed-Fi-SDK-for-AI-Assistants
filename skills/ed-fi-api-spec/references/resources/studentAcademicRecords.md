# studentAcademicRecords

`/ed-fi/studentAcademicRecords`

This educational entity represents the cumulative record of academic achievement for a student.

## Natural key

`termDescriptor`, `educationOrganizationReference`, `schoolYearTypeReference`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `termDescriptor` | key | descriptor URI | The term for the session during the school year. |
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `schoolYearTypeReference` | key | reference: `schoolYear` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `academicHonors` |  | array of edFi_studentAcademicRecordAcademicHonor | An unordered collection of studentAcademicRecordAcademicHonors. |
| `classRanking` |  | edFi_studentAcademicRecordClassRanking |  |
| `cumulativeAttemptedCreditConversion` |  | number (double) | Conversion factor that when multiplied by the number of credits is equivalent to Carnegie units. |
| `cumulativeAttemptedCredits` |  | number (double) | The value of credits or units of value awarded for the completion of a course. |
| `cumulativeAttemptedCreditTypeDescriptor` |  | descriptor URI | The type of credits or units of value awarded for the completion of a course. |
| `cumulativeEarnedCreditConversion` |  | number (double) | Conversion factor that when multiplied by the number of credits is equivalent to Carnegie units. |
| `cumulativeEarnedCredits` |  | number (double) | The value of credits or units of value awarded for the completion of a course. |
| `cumulativeEarnedCreditTypeDescriptor` |  | descriptor URI | The type of credits or units of value awarded for the completion of a course. |
| `diplomas` |  | array of edFi_studentAcademicRecordDiploma | An unordered collection of studentAcademicRecordDiplomas. |
| `gradePointAverages` |  | array of edFi_studentAcademicRecordGradePointAverage | An unordered collection of studentAcademicRecordGradePointAverages. |
| `projectedGraduationDate` |  | string (date) | The month and year the student is projected to graduate. |
| `recognitions` |  | array of edFi_studentAcademicRecordRecognition | An unordered collection of studentAcademicRecordRecognitions. |
| `reportCards` |  | array of edFi_studentAcademicRecordReportCard | An unordered collection of studentAcademicRecordReportCards. |
| `sessionAttemptedCreditConversion` |  | number (double) | Conversion factor that when multiplied by the number of credits is equivalent to Carnegie units. |
| `sessionAttemptedCredits` |  | number (double) | The value of credits or units of value awarded for the completion of a course. |
| `sessionAttemptedCreditTypeDescriptor` |  | descriptor URI | The type of credits or units of value awarded for the completion of a course. |
| `sessionEarnedCreditConversion` |  | number (double) | Conversion factor that when multiplied by the number of credits is equivalent to Carnegie units. |
| `sessionEarnedCredits` |  | number (double) | The value of credits or units of value awarded for the completion of a course. |
| `sessionEarnedCreditTypeDescriptor` |  | descriptor URI | The type of credits or units of value awarded for the completion of a course. |

## Endpoints

- `DELETE /ed-fi/studentAcademicRecords/{id}`
- `GET /ed-fi/studentAcademicRecords/deletes`
- `GET /ed-fi/studentAcademicRecords/keyChanges`
- `GET /ed-fi/studentAcademicRecords/partitions`
- `GET /ed-fi/studentAcademicRecords/{id}`
- `GET /ed-fi/studentAcademicRecords`
- `POST /ed-fi/studentAcademicRecords`
- `PUT /ed-fi/studentAcademicRecords/{id}`
