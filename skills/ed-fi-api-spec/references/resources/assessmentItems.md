# assessmentItems

`/ed-fi/assessmentItems`

This entity represents one of many single measures that make up an assessment.

## Natural key

`identificationCode`, `assessmentIdentifier`, `namespace`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `identificationCode` | yes | string max 60 | A unique number or alphanumeric code assigned to a space, room, site, building, individual, organization, program, or institution by a school, school system, s… |
| `assessmentReference` | yes | reference; supply `assessmentIdentifier`, `namespace` | This entity represents a tool, instrument, process, or exhibition composed of a systematic sampling of behavior for measuring a student's competence, knowledge… |
| `assessmentItemCategoryDescriptor` |  | descriptor URI | Category or type of the assessment item. |
| `assessmentItemURI` |  | string max 255 | The URI (typical a URL) pointing to the entry in an assessment item bank, which describes this content item. |
| `expectedTimeAssessed` |  | string max 30 | The duration allotted for the assessment item expressed in minutes. |
| `itemText` |  | string max 1024 | The text of the item. |
| `learningStandards` |  | array of edFi_assessmentItemLearningStandard | An unordered collection of assessmentItemLearningStandards. |
| `maxRawScore` |  | number (double) | The maximum raw score achievable across all assessment items that are correct and scored at the maximum. |
| `nomenclature` |  | string max 100 | Reflects the specific nomenclature used for assessment item. |
| `possibleResponses` |  | array of edFi_assessmentItemPossibleResponse | An unordered collection of assessmentItemPossibleResponses. |

### Items in `learningStandards`

| Field | Required | Type | Description |
|---|---|---|---|
| `learningStandardReference` | yes | reference; supply `learningStandardId` | A statement that describes a specific competency or academic standard. |

### Items in `possibleResponses`

| Field | Required | Type | Description |
|---|---|---|---|
| `responseValue` | yes | string max 60 | The response value, often an option number or code value (e.g., 1, 2, A, B, true, false). |
| `correctResponse` |  | boolean | Indicates the response is correct. |
| `responseDescription` |  | string max 1024 | Additional text provided to define the response value. |

## Endpoints

- `GET /ed-fi/assessmentItems`
- `POST /ed-fi/assessmentItems`
- `GET /ed-fi/assessmentItems/deletes`
- `GET /ed-fi/assessmentItems/keyChanges`
- `GET /ed-fi/assessmentItems/partitions`
- `GET /ed-fi/assessmentItems/{id}`
- `PUT /ed-fi/assessmentItems/{id}`
- `DELETE /ed-fi/assessmentItems/{id}`
