# interventionStudies

`/ed-fi/interventionStudies`

An experimental or quasi-experimental study of an intervention technique.

## Natural key

`interventionStudyIdentificationCode`, `educationOrganizationId`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `interventionStudyIdentificationCode` | yes | string max 60 | A unique number or alphanumeric code assigned to an intervention study. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `interventionPrescriptionReference` | yes | reference; supply `educationOrganizationId`, `interventionPrescriptionIdentificationCode` | This entity represents a formal prescription of an instructional approach focusing on the specific techniques and materials used to teach a given subject. |
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

### Items in `appropriateGradeLevels`

| Field | Required | Type | Description |
|---|---|---|---|
| `gradeLevelDescriptor` | yes | descriptor URI | Grade levels participating in this study. |

### Items in `appropriateSexes`

| Field | Required | Type | Description |
|---|---|---|---|
| `sexDescriptor` | yes | descriptor URI | Sexes participating in this study. |

### Items in `educationContents`

| Field | Required | Type | Description |
|---|---|---|---|
| `educationContentReference` | yes | reference; supply `contentIdentifier` | This entity represents materials for students or teachers that can be used for teaching, learning, research, and more. |

### Items in `interventionEffectivenesses`

| Field | Required | Type | Description |
|---|---|---|---|
| `diagnosisDescriptor` | yes | descriptor URI | Targeted purpose of the intervention (e.g., attendance issue, dropout risk) for which the effectiveness is measured. |
| `gradeLevelDescriptor` | yes | descriptor URI | Grade level for which effectiveness is measured. |
| `populationServedDescriptor` | yes | descriptor URI | Population for which effectiveness is measured. |
| `interventionEffectivenessRatingDescriptor` | yes | descriptor URI | An intervention demonstrates effectiveness if the research has shown that the program caused an improvement in outcomes. |
| `improvementIndex` |  | integer (int32) | Along a percentile distribution of students, the improvement index represents the change in an average student's percentile rank that is considered to be due t… |

### Items in `learningResourceMetadataURIs`

| Field | Required | Type | Description |
|---|---|---|---|
| `learningResourceMetadataURI` | yes | string max 255 | The URI (typical a URL) pointing to the metadata entry in a LRMI metadata repository, which describes this content item. |

### Items in `populationServeds`

| Field | Required | Type | Description |
|---|---|---|---|
| `populationServedDescriptor` | yes | descriptor URI | A subset of students that are the focus of the intervention study. |

### Items in `stateAbbreviations`

| Field | Required | Type | Description |
|---|---|---|---|
| `stateAbbreviationDescriptor` | yes | descriptor URI | The abbreviation for the state (within the United States) or outlying area, the school system of which the participants of the study are considered to be a par… |

### Items in `uris`

| Field | Required | Type | Description |
|---|---|---|---|
| `uri` | yes | string max 255 | The URI (typical a URL) pointing to an education content item. |

## Endpoints

- `GET /ed-fi/interventionStudies`
- `POST /ed-fi/interventionStudies`
- `GET /ed-fi/interventionStudies/deletes`
- `GET /ed-fi/interventionStudies/keyChanges`
- `GET /ed-fi/interventionStudies/partitions`
- `GET /ed-fi/interventionStudies/{id}`
- `PUT /ed-fi/interventionStudies/{id}`
- `DELETE /ed-fi/interventionStudies/{id}`
