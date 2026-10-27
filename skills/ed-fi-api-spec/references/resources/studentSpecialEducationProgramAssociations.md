# studentSpecialEducationProgramAssociations

`/ed-fi/studentSpecialEducationProgramAssociations`

This association represents the special education program(s) that a student participates in or receives
services from. The association is a subclass of the GeneralStudentProgramAssociation specifically designed for
special education programs.

## Natural key

`beginDate`, `educationOrganizationId`, `programEducationOrganizationId`, `programName`,
`programTypeDescriptor`, `studentUniqueId`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | yes | string (date) | The earliest date the student is involved with the program. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `programReference` | yes | reference; supply `educationOrganizationId`, `programName`, `programTypeDescriptor` | This entity represents any program designed to work in conjunction with, or as a supplement to, the main academic program. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `disabilities` |  | array of edFi_studentSpecialEducationProgramAssociationDisability | An unordered collection of studentSpecialEducationProgramAssociationDisabilities. |
| `endDate` |  | string (date) | The month, day, and year on which the student exited the program or stopped receiving services. |
| `ideaEligibility` |  | boolean | Indicator of the eligibility of the student to receive special education services according to the Individuals with Disabilities Education Act (IDEA). |
| `iepBeginDate` |  | string (date) | The effective date of the most recent IEP. |
| `iepEndDate` |  | string (date) | The end date of the most recent IEP. |
| `iepReviewDate` |  | string (date) | The date of the last IEP review. |
| `lastEvaluationDate` |  | string (date) | The date of the last special education evaluation. |
| `medicallyFragile` |  | boolean | Indicates whether the student receiving special education and related services is: 1) in the age range of birth to 22 years, and 2) has a serious, ongoing illn… |
| `multiplyDisabled` |  | boolean | Indicates whether the student receiving special education and related services has been designated as multiply disabled by the admission, review, and dismissal… |
| `programParticipationStatuses` |  | array of edFi_generalStudentProgramAssociationProgramParticipationStatus | An unordered collection of generalStudentProgramAssociationProgramParticipationStatuses. |
| `reasonExitedDescriptor` |  | descriptor URI | The reason the student left the program within a school or district. |
| `reductionInHoursPerWeekComparedToPeers` |  | number (double) | Records the number of hours reduced for the shortened school day for the IEP student as compared to peers in regular education. |
| `schoolHoursPerWeek` |  | number (double) | Indicate the total number of hours of instructional time per week for the school that the student attends. |
| `servedOutsideOfRegularSession` |  | boolean | Indicates whether the student received services during the summer session or between sessions. |
| `serviceProviders` |  | array of edFi_studentSpecialEducationProgramAssociationServiceProvider | An unordered collection of studentSpecialEducationProgramAssociationServiceProviders. |
| `shortenedSchoolDayIndicator` |  | boolean | Indicator that the student's IEP requires a shortened school day. |
| `specialEducationExitDate` |  | string (date) | The month, day and year on which a person stops receiving special education services. |
| `specialEducationExitExplained` |  | string max 1024 | Explanation on why a person stops receiving special education services. |
| `specialEducationExitReasonDescriptor` |  | descriptor URI | The reason why a person stops receiving special education services. |
| `specialEducationHoursPerWeek` |  | number (double) | The number of hours per week for special education instruction and therapy. |
| `specialEducationProgramServices` |  | array of edFi_studentSpecialEducationProgramAssociationSpecialEducationProgramService | An unordered collection of studentSpecialEducationProgramAssociationSpecialEducationProgramServices. |
| `specialEducationSettingDescriptor` |  | descriptor URI | The major instructional setting (more than 50 percent of a student's special education program). |

### Items in `disabilities`

| Field | Required | Type | Description |
|---|---|---|---|
| `disabilityDescriptor` | yes | descriptor URI | A disability category that describes a individual's impairment. |
| `disabilityDeterminationSourceTypeDescriptor` |  | descriptor URI | The source that provided the disability determination. |
| `disabilityDiagnosis` |  | string max 80 | A description of the disability diagnosis. |
| `orderOfDisability` |  | integer (int32) | The order by severity of individual's disabilities: 1- Primary, 2 - Secondary, 3 - Tertiary, etc. |
| `designations` |  | array of edFi_studentSpecialEducationProgramAssociationDisabilityDesignation | An unordered collection of studentSpecialEducationProgramAssociationDisabilityDesignations. |

### Items in `programParticipationStatuses`

| Field | Required | Type | Description |
|---|---|---|---|
| `participationStatusDescriptor` | yes | descriptor URI | The student's program participation status. |
| `statusBeginDate` | yes | string (date) | The date the student's program participation status began. |
| `designatedBy` |  | string max 60 | The person, organization, or department that designated the participation status. |
| `statusEndDate` |  | string (date) | The date the student's program participation status ended. |

### Items in `serviceProviders`

| Field | Required | Type | Description |
|---|---|---|---|
| `primaryProvider` |  | boolean | Primary ServiceProvider. |
| `staffReference` | yes | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |

### Items in `specialEducationProgramServices`

| Field | Required | Type | Description |
|---|---|---|---|
| `specialEducationProgramServiceDescriptor` | yes | descriptor URI | Indicates the service being provided to the student by the special education program. |
| `primaryIndicator` |  | boolean | True if service is a primary service. |
| `serviceBeginDate` |  | string (date) | First date the student was in this option for the current school year. |
| `serviceEndDate` |  | string (date) | Last date the student was in this option for the current school year. |
| `providers` |  | array of edFi_studentSpecialEducationProgramAssociationSpecialEducationProgramServiceProvider | An unordered collection of studentSpecialEducationProgramAssociationSpecialEducationProgramServiceProviders. |

## Endpoints

- `GET /ed-fi/studentSpecialEducationProgramAssociations`
- `POST /ed-fi/studentSpecialEducationProgramAssociations`
- `GET /ed-fi/studentSpecialEducationProgramAssociations/deletes`
- `GET /ed-fi/studentSpecialEducationProgramAssociations/keyChanges`
- `GET /ed-fi/studentSpecialEducationProgramAssociations/partitions`
- `GET /ed-fi/studentSpecialEducationProgramAssociations/{id}`
- `PUT /ed-fi/studentSpecialEducationProgramAssociations/{id}`
- `DELETE /ed-fi/studentSpecialEducationProgramAssociations/{id}`
