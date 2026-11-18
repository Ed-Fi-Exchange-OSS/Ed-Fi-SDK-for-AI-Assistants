# studentSpecialEducationProgramEligibilityAssociations

`/ed-fi/studentSpecialEducationProgramEligibilityAssociations`

Captures details regarding the evaluation process for eligibility of students for special education services
under IDEA Part C or Part B.

## Natural key

`consentToEvaluationReceivedDate`, `educationOrganizationId`, `programEducationOrganizationId`, `programName`,
`programTypeDescriptor`, `studentUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `consentToEvaluationReceivedDate` | yes | string (date) | Indicates the date on which the local education agency received written consent for the evaluation from the student's parent or guardian. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `programReference` | yes | reference; supply `educationOrganizationId`, `programName`, `programTypeDescriptor` | This entity represents any program designed to work in conjunction with, or as a supplement to, the main academic program. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `consentToEvaluationDate` |  | string (date) | The date on which the student's parent gave a consent (Parent Consent Date). |
| `eligibilityConferenceDate` |  | string (date) | The month, day, and year when the eligibility conference is held between the parent(s)/guardian(s) and the educational organization responsible staff member(s)… |
| `eligibilityDelayReasonDescriptor` |  | descriptor URI | The reason why the eligibility determination was completed beyond the required timeframe. |
| `eligibilityDeterminationDate` |  | string (date) | Indicates the month, day, and year the local education agency (LEA) held the admission, review, and dismissal committee meeting regarding the child's eligibili… |
| `eligibilityEvaluationDate` |  | string (date) | Indicates the month, day, and year when the written individual evaluation report was completed. |
| `eligibilityEvaluationTypeDescriptor` |  | descriptor URI | Indicates if this is an initial evaluation or a reevaluation. |
| `evaluationCompleteIndicator` |  | boolean | Indicates the evaluation completed status. |
| `evaluationDelayDays` |  | integer (int32) | Indicates the number of student absences, if any, beginning the first instructional day following the date on which the local education agency (LEA) received w… |
| `evaluationDelayReasonDescriptor` |  | descriptor URI | Refers to the justification as to why the evaluation report was completed beyond the state-established timeframe. |
| `evaluationLateReason` |  | string max 255 | Refers to additional information for delay in doing the evaluation. |
| `ideaIndicator` |  | boolean | Indicates whether or not the student was determined eligible as a result of an evaluation. |
| `ideaPartDescriptor` | yes | descriptor URI | Indicates if the evaluation is done under Part B IDEA or Part C IDEA. |
| `originalECIServicesDate` |  | string (date) | The month, date, and year when an infant or toddler, from birth through age 2, began participating in the early childhood intervention (ECI) program. |
| `transitionConferenceDate` |  | string (date) | Indicates the month, day, and year when the transition conference was held (for a child receiving early childhood intervention (ECI) services) among the lead a… |
| `transitionNotificationDate` |  | string (date) | Indicates the month, day, and year the LEA Notification of Potentially Eligible for Special Education Services was sent by the early childhood intervention (EC… |

## Endpoints

- `GET /ed-fi/studentSpecialEducationProgramEligibilityAssociations`
- `POST /ed-fi/studentSpecialEducationProgramEligibilityAssociations`
- `GET /ed-fi/studentSpecialEducationProgramEligibilityAssociations/deletes`
- `GET /ed-fi/studentSpecialEducationProgramEligibilityAssociations/keyChanges`
- `GET /ed-fi/studentSpecialEducationProgramEligibilityAssociations/partitions`
- `GET /ed-fi/studentSpecialEducationProgramEligibilityAssociations/{id}`
- `PUT /ed-fi/studentSpecialEducationProgramEligibilityAssociations/{id}`
- `DELETE /ed-fi/studentSpecialEducationProgramEligibilityAssociations/{id}`
