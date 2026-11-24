# graduationPlans

`/ed-fi/graduationPlans`

This entity is a plan outlining the required credits, credits by subject, credits by course, and other
criteria required for graduation. A graduation plan may be one or more standard plans defined by an education
organization and/or individual plans for some or all students.

## Natural key

`graduationPlanTypeDescriptor`, `educationOrganizationId`, `graduationSchoolYear`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `graduationPlanTypeDescriptor` | yes | descriptor URI | The type of academic plan the student is following for graduation. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `graduationSchoolYearTypeReference` | yes | reference; supply `schoolYear` | Identifier for a school year. |
| `creditsByCourses` |  | array of edFi_graduationPlanCreditsByCourse | An unordered collection of graduationPlanCreditsByCourses. |
| `creditsByCreditCategories` |  | array of edFi_graduationPlanCreditsByCreditCategory | An unordered collection of graduationPlanCreditsByCreditCategories. |
| `creditsBySubjects` |  | array of edFi_graduationPlanCreditsBySubject | An unordered collection of graduationPlanCreditsBySubjects. |
| `individualPlan` |  | boolean | An indicator of whether the graduation plan is tailored for an individual. |
| `requiredAssessments` |  | array of edFi_graduationPlanRequiredAssessment | An unordered collection of graduationPlanRequiredAssessments. |
| `totalRequiredCreditConversion` |  | number (double) | Conversion factor that when multiplied by the number of credits is equivalent to Carnegie units. |
| `totalRequiredCredits` | yes | number (double) | The value of credits or units of value awarded for the completion of a course. |
| `totalRequiredCreditTypeDescriptor` |  | descriptor URI | The type of credits or units of value awarded for the completion of a course. |

### Items in `creditsByCourses`

| Field | Required | Type | Description |
|---|---|---|---|
| `courseSetName` | yes | string max 120 | Identifying name given to a collection of courses. |
| `creditTypeDescriptor` |  | descriptor URI | The type of credits or units of value awarded for the completion of a course. |
| `whenTakenGradeLevelDescriptor` |  | descriptor URI | The grade level when the student is planned to take the course. |
| `creditConversion` |  | number (double) | Conversion factor that when multiplied by the number of credits is equivalent to Carnegie units. |
| `credits` | yes | number (double) | The value of credits or units of value awarded for the completion of a course. |
| `courses` | yes | array of edFi_graduationPlanCreditsByCourseCourse | An unordered collection of graduationPlanCreditsByCourseCourses. |

### Items in `creditsByCreditCategories`

| Field | Required | Type | Description |
|---|---|---|---|
| `creditCategoryDescriptor` | yes | descriptor URI | A categorization for the course transcript credits awarded in the course transcript. |
| `creditTypeDescriptor` |  | descriptor URI | The type of credits or units of value awarded for the completion of a course. |
| `creditConversion` |  | number (double) | Conversion factor that when multiplied by the number of credits is equivalent to Carnegie units. |
| `credits` | yes | number (double) | The value of credits or units of value awarded for the completion of a course. |

### Items in `creditsBySubjects`

| Field | Required | Type | Description |
|---|---|---|---|
| `academicSubjectDescriptor` | yes | descriptor URI | The intended major subject area of the graduation requirement. |
| `creditTypeDescriptor` |  | descriptor URI | The type of credits or units of value awarded for the completion of a course. |
| `creditConversion` |  | number (double) | Conversion factor that when multiplied by the number of credits is equivalent to Carnegie units. |
| `credits` | yes | number (double) | The value of credits or units of value awarded for the completion of a course. |

### Items in `requiredAssessments`

| Field | Required | Type | Description |
|---|---|---|---|
| `assessmentReference` | yes | reference; supply `assessmentIdentifier`, `namespace` | This entity represents a tool, instrument, process, or exhibition composed of a systematic sampling of behavior for measuring a student's competence, knowledge… |
| `scores` |  | array of edFi_graduationPlanRequiredAssessmentScore | An unordered collection of graduationPlanRequiredAssessmentScores. |
| `performanceLevel` |  | edFi_graduationPlanRequiredAssessmentPerformanceLevel |  |

## Endpoints

- `GET /ed-fi/graduationPlans`
- `POST /ed-fi/graduationPlans`
- `GET /ed-fi/graduationPlans/deletes`
- `GET /ed-fi/graduationPlans/keyChanges`
- `GET /ed-fi/graduationPlans/partitions`
- `GET /ed-fi/graduationPlans/{id}`
- `PUT /ed-fi/graduationPlans/{id}`
- `DELETE /ed-fi/graduationPlans/{id}`
