# studentSchoolAssociations

`/ed-fi/studentSchoolAssociations`

This association represents the school in which a student is enrolled. The semantics of enrollment may differ
slightly by state. Non-enrollment relationships between a student and an education organization may be
described using the StudentEducationOrganizationAssociation.

Also searched as: enrollment.

## Natural key

`entryDate`, `schoolId`, `studentUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `entryDate` | yes | string (date) | The month, day, and year on which an individual enters and begins to receive instructional services in a school for each school year. |
| `calendarReference` |  | reference; supply `calendarCode`, `schoolId`, `schoolYear` | A set of dates associated with an organization. |
| `classOfSchoolYearTypeReference` |  | reference; supply `schoolYear` | Identifier for a school year. |
| `graduationPlanReference` |  | reference; supply `educationOrganizationId`, `graduationPlanTypeDescriptor`, `graduationSchoolYear` | This entity is a plan outlining the required credits, credits by subject, credits by course, and other criteria required for graduation. |
| `nextYearSchoolReference` |  | reference; supply `schoolId` | This entity represents an educational organization that includes staff and students who participate in classes and educational activity groups. |
| `schoolReference` | yes | reference; supply `schoolId` | This entity represents an educational organization that includes staff and students who participate in classes and educational activity groups. |
| `schoolYearTypeReference` |  | reference; supply `schoolYear` | Identifier for a school year. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `alternativeGraduationPlans` |  | array of edFi_studentSchoolAssociationAlternativeGraduationPlan | An unordered collection of studentSchoolAssociationAlternativeGraduationPlans. |
| `educationPlans` |  | array of edFi_studentSchoolAssociationEducationPlan | An unordered collection of studentSchoolAssociationEducationPlans. |
| `employedWhileEnrolled` |  | boolean | An individual who is a paid employee or works in his or her own business, profession, or farm and at the same time is enrolled in secondary, postsecondary, or… |
| `enrollmentTypeDescriptor` |  | descriptor URI | The type of enrollment reflected by the StudentSchoolAssociation. |
| `entryGradeLevelDescriptor` | yes | descriptor URI | The grade level or primary instructional level at which a student enters and receives services in a school or an educational institution during a given academi… |
| `entryGradeLevelReasonDescriptor` |  | descriptor URI | The primary reason as to why a staff member determined that a student should be promoted or not (or be demoted) at the end of a given school term. |
| `entryTypeDescriptor` |  | descriptor URI | The process by which a student enters a school during a given academic session. |
| `exitWithdrawDate` |  | string (date) | The recorded exit or withdraw date for the student. |
| `exitWithdrawTypeDescriptor` |  | descriptor URI | The circumstances under which the student exited from membership in an educational institution. |
| `fullTimeEquivalency` |  | number (double) | The full-time equivalent ratio for the student s assignment to a school for services or instruction. |
| `nextYearGradeLevelDescriptor` |  | descriptor URI | The anticipated grade level for the student for the next school year. |
| `primarySchool` |  | boolean | Indicates if a given enrollment record should be considered the primary record for a student. |
| `repeatGradeIndicator` |  | boolean | An indicator of whether the student is enrolling to repeat a grade level, either by failure or an agreement to hold the student back. |
| `residencyStatusDescriptor` |  | descriptor URI | An indication of the location of a persons legal residence relative to (within or outside of) the boundaries of the public school attended and its administrati… |
| `schoolChoice` |  | boolean | An indication of whether the student enrolled in this school under the provisions for public school choice |
| `schoolChoiceBasisDescriptor` |  | descriptor URI | The legal basis for the school choice enrollment according to local, state or federal policy or regulation. |
| `schoolChoiceTransfer` |  | boolean | An indication of whether students transferred in or out of the school did so during the school year under the provisions for public school choice in accordance… |
| `termCompletionIndicator` |  | boolean | Idicates whether or not a student completed the most recent school term. |

### Items in `alternativeGraduationPlans`

| Field | Required | Type | Description |
|---|---|---|---|
| `alternativeGraduationPlanReference` | yes | reference; supply `educationOrganizationId`, `graduationPlanTypeDescriptor`, `graduationSchoolYear` | This entity is a plan outlining the required credits, credits by subject, credits by course, and other criteria required for graduation. |

### Items in `educationPlans`

| Field | Required | Type | Description |
|---|---|---|---|
| `educationPlanDescriptor` | yes | descriptor URI | The type of education plan(s) the student is following, if appropriate. |

## Endpoints

- `GET /ed-fi/studentSchoolAssociations`
- `POST /ed-fi/studentSchoolAssociations`
- `GET /ed-fi/studentSchoolAssociations/deletes`
- `GET /ed-fi/studentSchoolAssociations/keyChanges`
- `GET /ed-fi/studentSchoolAssociations/partitions`
- `GET /ed-fi/studentSchoolAssociations/{id}`
- `PUT /ed-fi/studentSchoolAssociations/{id}`
- `DELETE /ed-fi/studentSchoolAssociations/{id}`

`PUT` can change this resource's identifying values; the API cascades the change to records that reference it
(cascading key updates, `x-Ed-Fi-isUpdatable` in the specification).
