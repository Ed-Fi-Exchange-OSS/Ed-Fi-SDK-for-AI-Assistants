# financialAids

`/tpdm/financialAids`

This entity represents the financial aid a person is awarded.

## Natural key

`aidTypeDescriptor`, `beginDate`, `studentUniqueId`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `aidTypeDescriptor` | yes | descriptor URI | The classification of financial aid awarded to a person for the academic term/year. |
| `beginDate` | yes | string (date) | The date the award was designated. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `aidAmount` |  | number (double) | The amount of financial aid awarded to a person for the term/year. |
| `aidConditionDescription` |  | string max 1024 | The description of the condition (e.g., placement in a high need school) under which the aid was given. |
| `endDate` |  | string (date) | The date the award was removed. |
| `pellGrantRecipient` |  | boolean | Indicates a person who receives Pell Grant aid. |

## Endpoints

- `GET /tpdm/financialAids`
- `POST /tpdm/financialAids`
- `GET /tpdm/financialAids/deletes`
- `GET /tpdm/financialAids/keyChanges`
- `GET /tpdm/financialAids/partitions`
- `GET /tpdm/financialAids/{id}`
- `PUT /tpdm/financialAids/{id}`
- `DELETE /tpdm/financialAids/{id}`
