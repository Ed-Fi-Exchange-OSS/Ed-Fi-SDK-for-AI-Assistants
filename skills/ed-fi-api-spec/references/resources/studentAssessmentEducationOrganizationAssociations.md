# studentAssessmentEducationOrganizationAssociations

`/ed-fi/studentAssessmentEducationOrganizationAssociations`

The association of individual StudentAssessments with EducationOrganizations indicating administration,
enrollment, or attribution.

## Natural key

`educationOrganizationAssociationTypeDescriptor`, `educationOrganizationId`, `assessmentIdentifier`,
`namespace`, `studentAssessmentIdentifier`, `studentUniqueId`

Field names from the GET query parameters marked `x-Ed-Fi-isIdentity`; fields of a reference appear without it
(e.g. `schoolId` for `schoolReference`).

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationAssociationTypeDescriptor` | yes | descriptor URI | The type of association being represented. |
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `schoolYearTypeReference` |  | reference; supply `schoolYear` | Identifier for a school year. |
| `studentAssessmentReference` | yes | reference; supply `assessmentIdentifier`, `namespace`, `studentAssessmentIdentifier`, `studentUniqueId` | This entity represents the analysis or scoring of a student's response on an assessment. |

## Endpoints

- `GET /ed-fi/studentAssessmentEducationOrganizationAssociations`
- `POST /ed-fi/studentAssessmentEducationOrganizationAssociations`
- `GET /ed-fi/studentAssessmentEducationOrganizationAssociations/deletes`
- `GET /ed-fi/studentAssessmentEducationOrganizationAssociations/keyChanges`
- `GET /ed-fi/studentAssessmentEducationOrganizationAssociations/partitions`
- `GET /ed-fi/studentAssessmentEducationOrganizationAssociations/{id}`
- `PUT /ed-fi/studentAssessmentEducationOrganizationAssociations/{id}`
- `DELETE /ed-fi/studentAssessmentEducationOrganizationAssociations/{id}`
