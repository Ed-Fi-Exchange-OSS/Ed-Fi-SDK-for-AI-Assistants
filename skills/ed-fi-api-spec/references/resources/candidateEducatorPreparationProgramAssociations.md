# candidateEducatorPreparationProgramAssociations

`/tpdm/candidateEducatorPreparationProgramAssociations`

Information about the association between the Teacher Candidate and the EducatorPreparationProgram

## Natural key

`beginDate`, `candidateReference`, `educatorPreparationProgramReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | key | string (date) | The begin date for the association. |
| `candidateReference` | key | reference: `candidateIdentifier` |  |
| `educatorPreparationProgramReference` | key | reference: `educationOrganizationId`, `programName`, `programTypeDescriptor` |  |
| `cohortYears` |  | array of tpdm_candidateEducatorPreparationProgramAssociationCohortYear | An unordered collection of candidateEducatorPreparationProgramAssociationCohortYears. |
| `degreeSpecializations` |  | array of tpdm_candidateEducatorPreparationProgramAssociationDegreeSpecialization | An unordered collection of candidateEducatorPreparationProgramAssociationDegreeSpecializations. |
| `endDate` |  | string (date) | The end date for the association. |
| `eppProgramPathwayDescriptor` |  | descriptor URI | The program pathway the candidate is following; for example: Residency, Internship, Traditional |
| `reasonExitedDescriptor` |  | descriptor URI | Reason exited for the association. |

## Endpoints

- `DELETE /tpdm/candidateEducatorPreparationProgramAssociations/{id}`
- `GET /tpdm/candidateEducatorPreparationProgramAssociations/deletes`
- `GET /tpdm/candidateEducatorPreparationProgramAssociations/keyChanges`
- `GET /tpdm/candidateEducatorPreparationProgramAssociations/partitions`
- `GET /tpdm/candidateEducatorPreparationProgramAssociations/{id}`
- `GET /tpdm/candidateEducatorPreparationProgramAssociations`
- `POST /tpdm/candidateEducatorPreparationProgramAssociations`
- `PUT /tpdm/candidateEducatorPreparationProgramAssociations/{id}`
