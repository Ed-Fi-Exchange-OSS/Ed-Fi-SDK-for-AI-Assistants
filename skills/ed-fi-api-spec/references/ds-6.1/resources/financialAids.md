# financialAids

`/ed-fi/financialAids`

This entity represents the financial aid a person is awarded.

## Natural key

`aidTypeDescriptor`, `beginDate`, `studentUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `aidTypeDescriptor` | yes | descriptor URI | The classification of financial aid awarded to a person for the academic term/year. |
| `beginDate` | yes | string (date) | The date the award was designated. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `aidAmount` |  | number (double) | The amount of financial aid awarded to a person for the term/year. |
| `aidConditionDescription` |  | string max 1024 | The description of the condition under which the aid was given. |
| `endDate` |  | string (date) | The date the award was removed. |
| `pellGrantRecipient` |  | boolean | Indicates a person who receives Pell Grant aid. |

## Endpoints

- `GET /ed-fi/financialAids`
- `POST /ed-fi/financialAids`
- `GET /ed-fi/financialAids/deletes`
- `GET /ed-fi/financialAids/keyChanges`
- `GET /ed-fi/financialAids/partitions`
- `GET /ed-fi/financialAids/{id}`
- `PUT /ed-fi/financialAids/{id}`
- `DELETE /ed-fi/financialAids/{id}`
