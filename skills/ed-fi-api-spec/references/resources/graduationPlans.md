# graduationPlans

`/ed-fi/graduationPlans`

This entity is a plan outlining the required credits, credits by subject, credits by course, and other criteria required for graduation. A graduation plan may be one or more standard plans defined by an education organization and/or individual plans for some or all students.

## Natural key

`graduationPlanTypeDescriptor`, `educationOrganizationReference`, `graduationSchoolYearTypeReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `graduationPlanTypeDescriptor` | key | descriptor URI | The type of academic plan the student is following for graduation. |
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `graduationSchoolYearTypeReference` | key | reference: `schoolYear` |  |
| `creditsByCourses` |  | array of edFi_graduationPlanCreditsByCourse | An unordered collection of graduationPlanCreditsByCourses. |
| `creditsByCreditCategories` |  | array of edFi_graduationPlanCreditsByCreditCategory | An unordered collection of graduationPlanCreditsByCreditCategories. |
| `creditsBySubjects` |  | array of edFi_graduationPlanCreditsBySubject | An unordered collection of graduationPlanCreditsBySubjects. |
| `individualPlan` |  | boolean | An indicator of whether the graduation plan is tailored for an individual. |
| `requiredAssessments` |  | array of edFi_graduationPlanRequiredAssessment | An unordered collection of graduationPlanRequiredAssessments. |
| `totalRequiredCreditConversion` |  | number (double) | Conversion factor that when multiplied by the number of credits is equivalent to Carnegie units. |
| `totalRequiredCredits` | yes | number (double) | The value of credits or units of value awarded for the completion of a course. |
| `totalRequiredCreditTypeDescriptor` |  | descriptor URI | The type of credits or units of value awarded for the completion of a course. |

## Endpoints

- `DELETE /ed-fi/graduationPlans/{id}`
- `GET /ed-fi/graduationPlans/deletes`
- `GET /ed-fi/graduationPlans/keyChanges`
- `GET /ed-fi/graduationPlans/partitions`
- `GET /ed-fi/graduationPlans/{id}`
- `GET /ed-fi/graduationPlans`
- `POST /ed-fi/graduationPlans`
- `PUT /ed-fi/graduationPlans/{id}`
