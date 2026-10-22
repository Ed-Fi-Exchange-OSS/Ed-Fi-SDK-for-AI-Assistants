# interventionStudies

`/ed-fi/interventionStudies`

An experimental or quasi-experimental study of an intervention technique.

## Natural key

`interventionStudyIdentificationCode`, `educationOrganizationReference`, `interventionPrescriptionReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `interventionStudyIdentificationCode` | key | string max 60 | A unique number or alphanumeric code assigned to an intervention study. |
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `interventionPrescriptionReference` | key | reference: `educationOrganizationId`, `interventionPrescriptionIdentificationCode` |  |
| `appropriateGradeLevels` |  | array of edFi_interventionStudyAppropriateGradeLevel | An unordered collection of interventionStudyAppropriateGradeLevels. |
| `appropriateSexes` |  | array of edFi_interventionStudyAppropriateSex | An unordered collection of interventionStudyAppropriateSexes. |
| `deliveryMethodDescriptor` | yes | descriptor URI | The way in which an intervention was implemented: individual, small group, whole class, or whole school. |
| `educationContents` |  | array of edFi_interventionStudyEducationContent | An unordered collection of interventionStudyEducationContents. |
| `interventionClassDescriptor` | yes | descriptor URI | The way in which an intervention is used: curriculum, supplement, or practice. |
| `interventionEffectivenesses` |  | array of edFi_interventionStudyInterventionEffectiveness | An unordered collection of interventionStudyInterventionEffectivenesses. |
| `learningResourceMetadataURIs` |  | array of edFi_interventionStudyLearningResourceMetadataURI | An unordered collection of interventionStudyLearningResourceMetadataURIs. |
| `participants` | yes | integer (int32) | The number of participants observed in the study. |
| `populationServeds` |  | array of edFi_interventionStudyPopulationServed | An unordered collection of interventionStudyPopulationServeds. |
| `stateAbbreviations` |  | array of edFi_interventionStudyStateAbbreviation | An unordered collection of interventionStudyStateAbbreviations. |
| `uris` |  | array of edFi_interventionStudyURI | An unordered collection of interventionStudyURIs. |

## Endpoints

- `DELETE /ed-fi/interventionStudies/{id}`
- `GET /ed-fi/interventionStudies/deletes`
- `GET /ed-fi/interventionStudies/keyChanges`
- `GET /ed-fi/interventionStudies/partitions`
- `GET /ed-fi/interventionStudies/{id}`
- `GET /ed-fi/interventionStudies`
- `POST /ed-fi/interventionStudies`
- `PUT /ed-fi/interventionStudies/{id}`
