# interventionPrescriptions

`/ed-fi/interventionPrescriptions`

This entity represents a formal prescription of an instructional approach focusing on the specific techniques
and materials used to teach a given subject. This can be prescribed by academic research, an interventions
vendor, or another entity.

## Natural key

`interventionPrescriptionIdentificationCode`, `educationOrganizationId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `interventionPrescriptionIdentificationCode` | yes | string max 60 | A unique number or alphanumeric code assigned to an intervention prescription. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
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

### Items in `appropriateGradeLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `gradeLevelDescriptor` | yes | descriptor URI | Grade levels for the prescribed intervention. |

### Items in `appropriateSexes`

| Field | Required | Type | Description |
|---|---|---|---|
| `sexDescriptor` | yes | descriptor URI | Sexes for the intervention prescription. |

### Items in `diagnoses`

| Field | Required | Type | Description |
|---|---|---|---|
| `diagnosisDescriptor` | yes | descriptor URI | Targeted purpose of the intervention prescription. |

### Items in `educationContents`

| Field | Required | Type | Description |
|---|---|---|---|
| `educationContentReference` | yes | reference; supply `contentIdentifier` | This entity represents materials for students or teachers that can be used for teaching, learning, research, and more. |

### Items in `learningResourceMetadataURIs`

| Field | Required | Type | Description |
|---|---|---|---|
| `learningResourceMetadataURI` | yes | string max 255 | The URI (typical a URL) pointing to the metadata entry in a LRMI metadata repository, which describes this content item. |

### Items in `populationServeds`

| Field | Required | Type | Description |
|---|---|---|---|
| `populationServedDescriptor` | yes | descriptor URI | A subset of students that are the focus of the intervention prescription. |

### Items in `uris`

| Field | Required | Type | Description |
|---|---|---|---|
| `uri` | yes | string max 255 | The URI (typical a URL) pointing to an education content item. |

## Endpoints

- `GET /ed-fi/interventionPrescriptions`
- `POST /ed-fi/interventionPrescriptions`
- `GET /ed-fi/interventionPrescriptions/deletes`
- `GET /ed-fi/interventionPrescriptions/keyChanges`
- `GET /ed-fi/interventionPrescriptions/partitions`
- `GET /ed-fi/interventionPrescriptions/{id}`
- `PUT /ed-fi/interventionPrescriptions/{id}`
- `DELETE /ed-fi/interventionPrescriptions/{id}`
