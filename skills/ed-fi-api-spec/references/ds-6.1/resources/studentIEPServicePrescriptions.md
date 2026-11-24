# studentIEPServicePrescriptions

`/ed-fi/studentIEPServicePrescriptions`

EARLY ACCESS: The service prescribed to a student as part of their Individual Education Program (IEP).

## Natural key

`servicePrescriptionDescriptor`, `servicePrescriptionDate`, `educationOrganizationId`, `iepFinalizedDate`,
`studentIEPIdentifier`, `studentUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `servicePrescriptionDate` | yes | string (date) | The date the service was prescribed. |
| `servicePrescriptionDescriptor` | yes | descriptor URI | The type of service prescribed. |
| `studentIEPReference` | yes | reference; supply `educationOrganizationId`, `iepFinalizedDate`, `studentIEPIdentifier`, `studentUniqueId` | EARLY ACCESS: This entity represents an Individualized Education Program (IEP) for a student receiving special education services. |
| `beginDate` | yes | string (date) | The effective date when service is to begin. |
| `duration` | yes | integer (int32) | The length of time for the prescribed service in minutes. |
| `durationIntervalDescriptor` | yes | descriptor URI | How often the prescribed service is to be provided within the specified duration period. |
| `endDate` |  | string (date) | The effective date when the prescribed service ended. |
| `frequency` | yes | number (double) | The number of times the prescribed service is to be provided within the specified duration period. |
| `frequencyIntervalDescriptor` | yes | descriptor URI | How often the frequency should repeat for the prescribed service. |
| `ideaEvents` |  | array of edFi_studentIEPServicePrescriptionIDEAEvent | An unordered collection of studentIEPServicePrescriptionIDEAEvents. |
| `serviceLocationTypeDescriptor` | yes | descriptor URI | The type of location where the prescribed service is to be provided. |
| `staffs` |  | array of edFi_studentIEPServicePrescriptionStaff | An unordered collection of studentIEPServicePrescriptionStaffs. |

### Items in `ideaEvents`

| Field | Required | Type | Description |
|---|---|---|---|
| `ideaEventReference` | yes | reference; supply `educationOrganizationId`, `ideaEventIdentifier`, `ideaEventTypeDescriptor`, `studentUniqueId` | EARLY ACCESS: An IDEA related student event describing status, dates and narrative. |

### Items in `staffs`

| Field | Required | Type | Description |
|---|---|---|---|
| `staffReference` | yes | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |

## Endpoints

- `GET /ed-fi/studentIEPServicePrescriptions`
- `POST /ed-fi/studentIEPServicePrescriptions`
- `GET /ed-fi/studentIEPServicePrescriptions/deletes`
- `GET /ed-fi/studentIEPServicePrescriptions/keyChanges`
- `GET /ed-fi/studentIEPServicePrescriptions/partitions`
- `GET /ed-fi/studentIEPServicePrescriptions/{id}`
- `PUT /ed-fi/studentIEPServicePrescriptions/{id}`
- `DELETE /ed-fi/studentIEPServicePrescriptions/{id}`
