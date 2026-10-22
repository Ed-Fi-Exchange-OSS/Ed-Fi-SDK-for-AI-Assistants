# descriptorMappings

`/ed-fi/descriptorMappings`

A mapping of a descriptor value in one namespace to a descriptor value in another namespace. This can be used to exchange known contextual mappings of enumeration values.

## Natural key

`mappedNamespace`, `mappedValue`, `namespace`, `value`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `mappedNamespace` | key | string max 255 | The namespace of the descriptor value to which the from descriptor value is mapped to. |
| `mappedValue` | key | string max 50 | The descriptor value to which the from descriptor value is being mapped to. |
| `namespace` | key | string max 255 | The namespace of the descriptor value that is being mapped to another value. |
| `value` | key | string max 50 | The descriptor value that is being mapped to another value. |
| `modelEntities` |  | array of edFi_descriptorMappingModelEntity | An unordered collection of descriptorMappingModelEntities. |

## Endpoints

- `DELETE /ed-fi/descriptorMappings/{id}`
- `GET /ed-fi/descriptorMappings/deletes`
- `GET /ed-fi/descriptorMappings/keyChanges`
- `GET /ed-fi/descriptorMappings/partitions`
- `GET /ed-fi/descriptorMappings/{id}`
- `GET /ed-fi/descriptorMappings`
- `POST /ed-fi/descriptorMappings`
- `PUT /ed-fi/descriptorMappings/{id}`
