# assessmentItems

`/ed-fi/assessmentItems`

This entity represents one of many single measures that make up an assessment.

## Natural key

`identificationCode`, `assessmentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `identificationCode` | key | string max 60 | A unique number or alphanumeric code assigned to a space, room, site, building, individual, organization, program, or institution by a school, school system, s… |
| `assessmentReference` | key | reference: `assessmentIdentifier`, `namespace` |  |
| `assessmentItemCategoryDescriptor` |  | descriptor URI | Category or type of the assessment item. |
| `assessmentItemURI` |  | string max 255 | The URI (typical a URL) pointing to the entry in an assessment item bank, which describes this content item. |
| `expectedTimeAssessed` |  | string max 30 | The duration allotted for the assessment item expressed in minutes. |
| `itemText` |  | string max 1024 | The text of the item. |
| `learningStandards` |  | array of edFi_assessmentItemLearningStandard | An unordered collection of assessmentItemLearningStandards. |
| `maxRawScore` |  | number (double) | The maximum raw score achievable across all assessment items that are correct and scored at the maximum. |
| `nomenclature` |  | string max 100 | Reflects the specific nomenclature used for assessment item. |
| `possibleResponses` |  | array of edFi_assessmentItemPossibleResponse | An unordered collection of assessmentItemPossibleResponses. |

## Endpoints

- `DELETE /ed-fi/assessmentItems/{id}`
- `GET /ed-fi/assessmentItems/deletes`
- `GET /ed-fi/assessmentItems/keyChanges`
- `GET /ed-fi/assessmentItems/partitions`
- `GET /ed-fi/assessmentItems/{id}`
- `GET /ed-fi/assessmentItems`
- `POST /ed-fi/assessmentItems`
- `PUT /ed-fi/assessmentItems/{id}`
