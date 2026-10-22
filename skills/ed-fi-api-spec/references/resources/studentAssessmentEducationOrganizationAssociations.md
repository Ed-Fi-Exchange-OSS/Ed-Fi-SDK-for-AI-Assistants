# studentAssessmentEducationOrganizationAssociations

`/ed-fi/studentAssessmentEducationOrganizationAssociations`

The association of individual StudentAssessments with EducationOrganizations indicating administration,
enrollment, or attribution.

## Natural key

`educationOrganizationAssociationTypeDescriptor`, `educationOrganizationReference`,
`studentAssessmentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationAssociationTypeDescriptor` | key | descriptor URI | The type of association being represented. |
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `schoolYearTypeReference` |  | reference: `schoolYear` |  |
| `studentAssessmentReference` | key | reference: `assessmentIdentifier`, `namespace`, `studentAssessmentIdentifier`, `studentUniqueId` |  |

## Endpoints

- `DELETE /ed-fi/studentAssessmentEducationOrganizationAssociations/{id}`
- `GET /ed-fi/studentAssessmentEducationOrganizationAssociations/deletes`
- `GET /ed-fi/studentAssessmentEducationOrganizationAssociations/keyChanges`
- `GET /ed-fi/studentAssessmentEducationOrganizationAssociations/partitions`
- `GET /ed-fi/studentAssessmentEducationOrganizationAssociations/{id}`
- `GET /ed-fi/studentAssessmentEducationOrganizationAssociations`
- `POST /ed-fi/studentAssessmentEducationOrganizationAssociations`
- `PUT /ed-fi/studentAssessmentEducationOrganizationAssociations/{id}`
