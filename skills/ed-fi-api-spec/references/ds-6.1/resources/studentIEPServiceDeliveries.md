# studentIEPServiceDeliveries

`/ed-fi/studentIEPServiceDeliveries`

EARLY ACCESS: Services delivered to a student as prescribed by their Individual Education Program (IEP).

## Natural key

`serviceDeliveryDescriptor`, `iepServiceDeliveryIdentifier`, `serviceDeliveryDate`, `educationOrganizationId`,
`iepFinalizedDate`, `studentIEPIdentifier`, `studentUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `iepServiceDeliveryIdentifier` | yes | string max 120 | A unique identifier assigned by the provider of IEP services for the delivery record. |
| `serviceDeliveryDate` | yes | string (date) | The date when prescribed services were delivered for a student. |
| `serviceDeliveryDescriptor` | yes | descriptor URI | The type of services delivered to the student. |
| `studentIEPReference` | yes | reference; supply `educationOrganizationId`, `iepFinalizedDate`, `studentIEPIdentifier`, `studentUniqueId` | EARLY ACCESS: This entity represents an Individualized Education Program (IEP) for a student receiving special education services. |
| `studentIEPServicePrescriptionReference` |  | reference; supply `educationOrganizationId`, `iepFinalizedDate`, `servicePrescriptionDate`, `servicePrescriptionDescriptor`, `studentIEPIdentifier`, `studentUniqueId` | EARLY ACCESS: The service prescribed to a student as part of their Individual Education Program (IEP). |
| `ideaEvents` |  | array of edFi_studentIEPServiceDeliveryIDEAEvent | An unordered collection of studentIEPServiceDeliveryIDEAEvents. |
| `providers` |  | array of edFi_studentIEPServiceDeliveryProvider | An unordered collection of studentIEPServiceDeliveryProviders. |

### Items in `ideaEvents`

| Field | Required | Type | Description |
|---|---|---|---|
| `ideaEventReference` | yes | reference; supply `educationOrganizationId`, `ideaEventIdentifier`, `ideaEventTypeDescriptor`, `studentUniqueId` | EARLY ACCESS: An IDEA related student event describing status, dates and narrative. |

### Items in `providers`

| Field | Required | Type | Description |
|---|---|---|---|
| `firstName` | yes | string max 75 | A name given to an individual at birth, baptism, or during another naming ceremony, or through legal change. |
| `lastSurname` | yes | string max 75 | The name borne in common by members of a family. |
| `serviceProviderTypeDescriptor` |  | descriptor URI | Indicates service provider type, including specialist, internal staff, external staff, etc. |
| `middleName` |  | string max 75 | A secondary name given to an individual at birth, baptism, or during another naming ceremony. |
| `primaryProvider` |  | boolean | Indicates that this provider was the Primary Service Provider. |
| `providerCode` |  | string max 16 | A code assigned to the service provider. |
| `staffReference` |  | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |

## Endpoints

- `GET /ed-fi/studentIEPServiceDeliveries`
- `POST /ed-fi/studentIEPServiceDeliveries`
- `GET /ed-fi/studentIEPServiceDeliveries/deletes`
- `GET /ed-fi/studentIEPServiceDeliveries/keyChanges`
- `GET /ed-fi/studentIEPServiceDeliveries/partitions`
- `GET /ed-fi/studentIEPServiceDeliveries/{id}`
- `PUT /ed-fi/studentIEPServiceDeliveries/{id}`
- `DELETE /ed-fi/studentIEPServiceDeliveries/{id}`
