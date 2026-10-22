# studentSpecialEducationProgramAssociations

`/ed-fi/studentSpecialEducationProgramAssociations`

This association represents the special education program(s) that a student participates in or receives services from. The association is a subclass of the GeneralStudentProgramAssociation specifically designed for special education programs.

## Natural key

`beginDate`, `educationOrganizationReference`, `programReference`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | key | string (date) | The earliest date the student is involved with the program. |
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `programReference` | key | reference: `educationOrganizationId`, `programName`, `programTypeDescriptor` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
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

## Endpoints

- `DELETE /ed-fi/studentSpecialEducationProgramAssociations/{id}`
- `GET /ed-fi/studentSpecialEducationProgramAssociations/deletes`
- `GET /ed-fi/studentSpecialEducationProgramAssociations/keyChanges`
- `GET /ed-fi/studentSpecialEducationProgramAssociations/partitions`
- `GET /ed-fi/studentSpecialEducationProgramAssociations/{id}`
- `GET /ed-fi/studentSpecialEducationProgramAssociations`
- `POST /ed-fi/studentSpecialEducationProgramAssociations`
- `PUT /ed-fi/studentSpecialEducationProgramAssociations/{id}`
