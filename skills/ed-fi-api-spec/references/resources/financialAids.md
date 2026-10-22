# financialAids

`/tpdm/financialAids`

This entity represents the financial aid a person is awarded.

## Natural key

`aidTypeDescriptor`, `beginDate`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `aidTypeDescriptor` | key | descriptor URI | The classification of financial aid awarded to a person for the academic term/year. |
| `beginDate` | key | string (date) | The date the award was designated. |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `aidAmount` |  | number (double) | The amount of financial aid awarded to a person for the term/year. |
| `aidConditionDescription` |  | string max 1024 | The description of the condition (e.g., placement in a high need school) under which the aid was given. |
| `endDate` |  | string (date) | The date the award was removed. |
| `pellGrantRecipient` |  | boolean | Indicates a person who receives Pell Grant aid. |

## Endpoints

- `DELETE /tpdm/financialAids/{id}`
- `GET /tpdm/financialAids/deletes`
- `GET /tpdm/financialAids/keyChanges`
- `GET /tpdm/financialAids/partitions`
- `GET /tpdm/financialAids/{id}`
- `GET /tpdm/financialAids`
- `POST /tpdm/financialAids`
- `PUT /tpdm/financialAids/{id}`
