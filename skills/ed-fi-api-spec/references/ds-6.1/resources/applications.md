# applications

`/ed-fi/applications`

An application for employment or acceptance.

## Natural key

`applicationIdentifier`, `applicantProfileIdentifier`, `educationOrganizationId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `applicationIdentifier` | yes | string max 20 | Identifier assigned to the application for a candidate or open staff position. |
| `applicantProfileReference` | yes | reference; supply `applicantProfileIdentifier` | The profile of the person making an application. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `openStaffPositionReference` |  | reference; supply `educationOrganizationId`, `requisitionNumber` | This entity represents an open staff position that the education organization is seeking to fill. |
| `academicSubjectDescriptor` |  | descriptor URI | The academic subject for which the application is made. |
| `acceptedDate` |  | string (date) | The date of acceptance, if offered. |
| `applicationDate` | yes | string (date) | The month, day, and year the application was submitted. |
| `applicationSourceDescriptor` |  | descriptor URI | Specifies the source for the application. |
| `applicationStatusDescriptor` | yes | descriptor URI | Indicates the current status of the application. |
| `currentEmployee` |  | boolean | Indicator as to whether the applicant is a current employee of the school district. |
| `firstContactDate` |  | string (date) | Date applicant was first contacted after submitting application. |
| `highNeedsAcademicSubjectDescriptor` |  | descriptor URI | The high need academic subject for the application, if any. |
| `hireStatusDescriptor` |  | descriptor URI | Indicates the current status of the application for hire. |
| `hiringSourceDescriptor` |  | descriptor URI | The source for the application. |
| `recruitmentEventAttendances` |  | array of edFi_applicationRecruitmentEventAttendance | An unordered collection of applicationRecruitmentEventAttendances. |
| `scoreResults` |  | array of edFi_applicationScoreResult | An unordered collection of applicationScoreResults. |
| `terms` |  | array of edFi_applicationTerm | An unordered collection of applicationTerms. |
| `withdrawDate` |  | string (date) | The date the application was withdrawn by the applicant. |
| `withdrawReasonDescriptor` |  | descriptor URI | Reason applicant withdrew application. |

### Items in `recruitmentEventAttendances`

| Field | Required | Type | Description |
|---|---|---|---|
| `recruitmentEventAttendanceReference` | yes | reference; supply `educationOrganizationId`, `eventDate`, `eventTitle`, `recruitmentEventAttendeeIdentifier` | A prospect for employment or acceptance that has not yet made a formal application but has attended a recruitment event, such as a job fair or university recru… |

### Items in `scoreResults`

| Field | Required | Type | Description |
|---|---|---|---|
| `assessmentReportingMethodDescriptor` | yes | descriptor URI | The method that the administrator of the assessment uses to report the performance and achievement of all students. |
| `resultDatatypeTypeDescriptor` | yes | descriptor URI | The datatype of the result. |
| `result` | yes | string max 35 | The value of a meaningful raw score or statistical expression of the performance of an individual. |

### Items in `terms`

| Field | Required | Type | Description |
|---|---|---|---|
| `termDescriptor` | yes | descriptor URI | The intended term of enrollment for which the application is being submitted. |

## Endpoints

- `GET /ed-fi/applications`
- `POST /ed-fi/applications`
- `GET /ed-fi/applications/deletes`
- `GET /ed-fi/applications/keyChanges`
- `GET /ed-fi/applications/partitions`
- `GET /ed-fi/applications/{id}`
- `PUT /ed-fi/applications/{id}`
- `DELETE /ed-fi/applications/{id}`
