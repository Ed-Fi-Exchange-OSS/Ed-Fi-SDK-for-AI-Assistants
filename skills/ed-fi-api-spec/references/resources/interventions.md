# interventions

`/ed-fi/interventions`

An implementation of an instructional approach focusing on the specific techniques and materials used to teach
a given subject.

## Natural key

`interventionIdentificationCode`, `educationOrganizationId`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `interventionIdentificationCode` | yes | string max 60 | A unique number or alphanumeric code assigned to an intervention. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
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

### Items in `appropriateGradeLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `gradeLevelDescriptor` | yes | descriptor URI | Grade levels for the intervention. |

### Items in `appropriateSexes`

| Field | Required | Type | Description |
|---|---|---|---|
| `sexDescriptor` | yes | descriptor URI | Sexes for the intervention. |

### Items in `diagnoses`

| Field | Required | Type | Description |
|---|---|---|---|
| `diagnosisDescriptor` | yes | descriptor URI | Targeted purpose of the intervention. |

### Items in `educationContents`

| Field | Required | Type | Description |
|---|---|---|---|
| `educationContentReference` | yes | reference; supply `contentIdentifier` | This entity represents materials for students or teachers that can be used for teaching, learning, research, and more. |

### Items in `interventionPrescriptions`

| Field | Required | Type | Description |
|---|---|---|---|
| `interventionPrescriptionReference` | yes | reference; supply `educationOrganizationId`, `interventionPrescriptionIdentificationCode` | This entity represents a formal prescription of an instructional approach focusing on the specific techniques and materials used to teach a given subject. |

### Items in `learningResourceMetadataURIs`

| Field | Required | Type | Description |
|---|---|---|---|
| `learningResourceMetadataURI` | yes | string max 255 | The URI (typical a URL) pointing to the metadata entry in a LRMI metadata repository, which describes this content item. |

### Items in `meetingTimes`

| Field | Required | Type | Description |
|---|---|---|---|
| `endTime` | yes | string | An indication of the time of day the meeting time ends. |
| `startTime` | yes | string | An indication of the time of day the meeting time begins. |

### Items in `populationServeds`

| Field | Required | Type | Description |
|---|---|---|---|
| `populationServedDescriptor` | yes | descriptor URI | A subset of students that are the focus of the intervention. |

### Items in `staffs`

| Field | Required | Type | Description |
|---|---|---|---|
| `staffReference` | yes | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |

### Items in `uris`

| Field | Required | Type | Description |
|---|---|---|---|
| `uri` | yes | string max 255 | The URI (typical a URL) pointing to an education content item. |

## Endpoints

- `GET /ed-fi/interventions`
- `POST /ed-fi/interventions`
- `GET /ed-fi/interventions/deletes`
- `GET /ed-fi/interventions/keyChanges`
- `GET /ed-fi/interventions/partitions`
- `GET /ed-fi/interventions/{id}`
- `PUT /ed-fi/interventions/{id}`
- `DELETE /ed-fi/interventions/{id}`
