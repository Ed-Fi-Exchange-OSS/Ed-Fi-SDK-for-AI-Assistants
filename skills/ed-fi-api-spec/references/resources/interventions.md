# interventions

`/ed-fi/interventions`

An implementation of an instructional approach focusing on the specific techniques and materials used to teach a given subject.

## Natural key

`interventionIdentificationCode`, `educationOrganizationReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `interventionIdentificationCode` | key | string max 60 | A unique number or alphanumeric code assigned to an intervention. |
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `appropriateGradeLevels` |  | array of edFi_interventionAppropriateGradeLevel | An unordered collection of interventionAppropriateGradeLevels. |
| `appropriateSexes` |  | array of edFi_interventionAppropriateSex | An unordered collection of interventionAppropriateSexes. |
| `beginDate` | yes | string (date) | The start date for the intervention implementation. |
| `deliveryMethodDescriptor` | yes | descriptor URI | The way in which an intervention was implemented. |
| `diagnoses` |  | array of edFi_interventionDiagnosis | An unordered collection of interventionDiagnoses. |
| `educationContents` |  | array of edFi_interventionEducationContent | An unordered collection of interventionEducationContents. |
| `endDate` |  | string (date) | The end date for the intervention implementation. |
| `interventionClassDescriptor` | yes | descriptor URI | The way in which an intervention is used: curriculum, supplement, or practice. |
| `interventionPrescriptions` |  | array of edFi_interventionInterventionPrescription | An unordered collection of interventionInterventionPrescriptions. |
| `learningResourceMetadataURIs` |  | array of edFi_interventionLearningResourceMetadataURI | An unordered collection of interventionLearningResourceMetadataURIs. |
| `maxDosage` |  | integer (int32) | The maximum duration of time in minutes that may be assigned for the intervention. |
| `meetingTimes` |  | array of edFi_interventionMeetingTime | An unordered collection of interventionMeetingTimes. |
| `minDosage` |  | integer (int32) | The minimum duration of time in minutes that may be assigned for the intervention. |
| `namespace` |  | string max 255 | Namespace for the intervention. |
| `populationServeds` |  | array of edFi_interventionPopulationServed | An unordered collection of interventionPopulationServeds. |
| `staffs` |  | array of edFi_interventionStaff | An unordered collection of interventionStaffs. |
| `uris` |  | array of edFi_interventionURI | An unordered collection of interventionURIs. |

## Endpoints

- `DELETE /ed-fi/interventions/{id}`
- `GET /ed-fi/interventions/deletes`
- `GET /ed-fi/interventions/keyChanges`
- `GET /ed-fi/interventions/partitions`
- `GET /ed-fi/interventions/{id}`
- `GET /ed-fi/interventions`
- `POST /ed-fi/interventions`
- `PUT /ed-fi/interventions/{id}`
