# studentIEPs

`/ed-fi/studentIEPs`

EARLY ACCESS: This entity represents an Individualized Education Program (IEP) for a student receiving special
education services. The IEP is a legally required document that outlines a student's special education
services.

## Natural key

`iepFinalizedDate`, `studentIEPIdentifier`, `educationOrganizationId`, `studentUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `iepFinalizedDate` | yes | string (date) | The date the IEP was finalized. |
| `studentIEPIdentifier` | yes | string max 120 | A unique identifier assigned by the provider or source system of IEP services. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `accommodations` |  | array of edFi_studentIEPAccommodation | An unordered collection of studentIEPAccommodations. |
| `disabilities` |  | array of edFi_studentIEPDisability | An unordered collection of studentIEPDisabilities. |
| `ideaEvents` |  | array of edFi_studentIEPIDEAEvent | An unordered collection of studentIEPIDEAEvents. |
| `iepAmendedDate` |  | string (date) | The date when the IEP was last amended, if any. |
| `iepBeginDate` | yes | string (date) | The projected date for the beginning of special education and related services. |
| `iepEndDate` | yes | string (date) | The effective end date of the IEP. |
| `iepStatusDescriptor` | yes | descriptor URI | The current status of the IEP. |
| `medicallyFragile` |  | boolean | Indicates whether the student receiving special education and related services is: 1) in the age range of birth to 22 years, and 2) has a serious, ongoing illn… |
| `multiplyDisabled` |  | boolean | Indicates whether the student receiving special education and related services has been designated as multiply disabled by the admission, review, and dismissal… |
| `reasonExitedDescriptor` |  | descriptor URI | The reason why a person stops receiving special education services. |
| `schoolHoursPerWeek` |  | number (double) | Indicate the total number of hours of instructional time per week for the school that the student attends. |
| `specialEducationHoursPerWeek` |  | number (double) | Indicates the total number of hours of time per week specific to special education related services. |
| `specialEducationSettingDescriptor` |  | descriptor URI | The major instructional setting (more than 50 percent of a student's special education program). |

### Items in `accommodations`

| Field | Required | Type | Description |
|---|---|---|---|
| `accommodationDescriptor` | yes | descriptor URI | The special variation(s) to be used in how various services (in general) are presented, how they are administered, or how the student is allowed to respond. |

### Items in `disabilities`

| Field | Required | Type | Description |
|---|---|---|---|
| `disabilityDescriptor` | yes | descriptor URI | A disability category that describes a individual's impairment. |
| `disabilityDeterminationSourceTypeDescriptor` |  | descriptor URI | The source that provided the disability determination. |
| `disabilityDiagnosis` |  | string max 80 | A description of the disability diagnosis. |
| `orderOfDisability` |  | integer (int32) | The order by severity of individual's disabilities: 1- Primary, 2 - Secondary, 3 - Tertiary, etc. |
| `designations` |  | array of edFi_studentIEPDisabilityDesignation | An unordered collection of studentIEPDisabilityDesignations. |

### Items in `ideaEvents`

| Field | Required | Type | Description |
|---|---|---|---|
| `ideaEventReference` | yes | reference; supply `educationOrganizationId`, `ideaEventIdentifier`, `ideaEventTypeDescriptor`, `studentUniqueId` | EARLY ACCESS: An IDEA related student event describing status, dates and narrative. |

## Endpoints

- `GET /ed-fi/studentIEPs`
- `POST /ed-fi/studentIEPs`
- `GET /ed-fi/studentIEPs/deletes`
- `GET /ed-fi/studentIEPs/keyChanges`
- `GET /ed-fi/studentIEPs/partitions`
- `GET /ed-fi/studentIEPs/{id}`
- `PUT /ed-fi/studentIEPs/{id}`
- `DELETE /ed-fi/studentIEPs/{id}`
