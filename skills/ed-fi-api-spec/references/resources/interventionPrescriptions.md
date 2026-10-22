# interventionPrescriptions

`/ed-fi/interventionPrescriptions`

This entity represents a formal prescription of an instructional approach focusing on the specific techniques and materials used to teach a given subject. This can be prescribed by academic research, an interventions vendor, or another entity.

## Natural key

`interventionPrescriptionIdentificationCode`, `educationOrganizationReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `interventionPrescriptionIdentificationCode` | key | string max 60 | A unique number or alphanumeric code assigned to an intervention prescription. |
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `appropriateGradeLevels` |  | array of edFi_interventionPrescriptionAppropriateGradeLevel | An unordered collection of interventionPrescriptionAppropriateGradeLevels. |
| `appropriateSexes` |  | array of edFi_interventionPrescriptionAppropriateSex | An unordered collection of interventionPrescriptionAppropriateSexes. |
| `deliveryMethodDescriptor` | yes | descriptor URI | The way in which an intervention was implemented: individual, small group, whole class, or whole school. |
| `diagnoses` |  | array of edFi_interventionPrescriptionDiagnosis | An unordered collection of interventionPrescriptionDiagnoses. |
| `educationContents` |  | array of edFi_interventionPrescriptionEducationContent | An unordered collection of interventionPrescriptionEducationContents. |
| `interventionClassDescriptor` | yes | descriptor URI | The way in which an intervention is used: curriculum, supplement, or practice. |
| `learningResourceMetadataURIs` |  | array of edFi_interventionPrescriptionLearningResourceMetadataURI | An unordered collection of interventionPrescriptionLearningResourceMetadataURIs. |
| `maxDosage` |  | integer (int32) | The maximum duration of time in minutes that is recommended for the intervention. |
| `minDosage` |  | integer (int32) | The minimum duration of time in minutes that is recommended for the intervention. |
| `namespace` |  | string max 255 | Namespace for the intervention. |
| `populationServeds` |  | array of edFi_interventionPrescriptionPopulationServed | An unordered collection of interventionPrescriptionPopulationServeds. |
| `uris` |  | array of edFi_interventionPrescriptionURI | An unordered collection of interventionPrescriptionURIs. |

## Endpoints

- `DELETE /ed-fi/interventionPrescriptions/{id}`
- `GET /ed-fi/interventionPrescriptions/deletes`
- `GET /ed-fi/interventionPrescriptions/keyChanges`
- `GET /ed-fi/interventionPrescriptions/partitions`
- `GET /ed-fi/interventionPrescriptions/{id}`
- `GET /ed-fi/interventionPrescriptions`
- `POST /ed-fi/interventionPrescriptions`
- `PUT /ed-fi/interventionPrescriptions/{id}`
