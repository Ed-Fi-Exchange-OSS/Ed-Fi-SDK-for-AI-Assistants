# descriptorMappings

`/ed-fi/descriptorMappings`

A mapping of a descriptor value in one namespace to a descriptor value in another namespace. This can be used
to exchange known contextual mappings of enumeration values.

## Natural key

`mappedNamespace`, `mappedValue`, `namespace`, `value`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `mappedNamespace` | yes | string max 255 | The namespace of the descriptor value to which the from descriptor value is mapped to. |
| `mappedValue` | yes | string max 50 | The descriptor value to which the from descriptor value is being mapped to. |
| `namespace` | yes | string max 255 | The namespace of the descriptor value that is being mapped to another value. |
| `value` | yes | string max 50 | The descriptor value that is being mapped to another value. |
| `modelEntities` |  | array of edFi_descriptorMappingModelEntity | An unordered collection of descriptorMappingModelEntities. |

### Items in `modelEntities`

| Field | Required | Type | Description |
|---|---|---|---|
| `modelEntityDescriptor` | yes | descriptor URI | The resources for which the descriptor mapping applies. |

## Endpoints

- `GET /ed-fi/descriptorMappings`
- `POST /ed-fi/descriptorMappings`
- `GET /ed-fi/descriptorMappings/deletes`
- `GET /ed-fi/descriptorMappings/keyChanges`
- `GET /ed-fi/descriptorMappings/partitions`
- `GET /ed-fi/descriptorMappings/{id}`
- `PUT /ed-fi/descriptorMappings/{id}`
- `DELETE /ed-fi/descriptorMappings/{id}`
