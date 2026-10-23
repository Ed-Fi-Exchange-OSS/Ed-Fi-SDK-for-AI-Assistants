# candidateEducatorPreparationProgramAssociations

`/tpdm/candidateEducatorPreparationProgramAssociations`

Information about the association between the Teacher Candidate and the EducatorPreparationProgram

## Fields

`yes` = required. The OpenAPI specification does not say which fields identify a record; for natural keys, see
the Data Standard documentation.

| Field | Required | Type | Description |
|---|---|---|---|
| `beginDate` | yes | string (date) | The begin date for the association. |
| `candidateReference` | yes | reference; supply `candidateIdentifier` | A candidate is both a person enrolled in a educator preparation program and a candidate to become an educator. |
| `educatorPreparationProgramReference` | yes | reference; supply `educationOrganizationId`, `programName`, `programTypeDescriptor` | The Educator Preparation Program is designed to prepare students to become licensed educators. |
| `cohortYears` |  | array of tpdm_candidateEducatorPreparationProgramAssociationCohortYear | An unordered collection of candidateEducatorPreparationProgramAssociationCohortYears. |
| `degreeSpecializations` |  | array of tpdm_candidateEducatorPreparationProgramAssociationDegreeSpecialization | An unordered collection of candidateEducatorPreparationProgramAssociationDegreeSpecializations. |
| `endDate` |  | string (date) | The end date for the association. |
| `eppProgramPathwayDescriptor` |  | descriptor URI | The program pathway the candidate is following; for example: Residency, Internship, Traditional |
| `reasonExitedDescriptor` |  | descriptor URI | Reason exited for the association. |

### Items in `cohortYears`

| Field | Required | Type | Description |
|---|---|---|---|
| `cohortYearTypeDescriptor` | yes | descriptor URI | The type of cohort year (9th grade, graduation). |
| `termDescriptor` |  | descriptor URI | The term associated with the cohort year; for example, the intended term of graduation. |
| `schoolYearTypeReference` | yes | reference; supply `schoolYear` | Identifier for a school year. |

### Items in `degreeSpecializations`

| Field | Required | Type | Description |
|---|---|---|---|
| `majorSpecialization` | yes | string max 255 | The major area for a degree or area of specialization for a certificate. |
| `endDate` |  | string (date) | The month, day, and year on which the Teacher Candidate exited the declared specialization. |
| `minorSpecialization` |  | string max 255 | The minor area for a degree or area of specialization for a certificate. |

## Endpoints

- `GET /tpdm/candidateEducatorPreparationProgramAssociations`
- `POST /tpdm/candidateEducatorPreparationProgramAssociations`
- `GET /tpdm/candidateEducatorPreparationProgramAssociations/deletes`
- `GET /tpdm/candidateEducatorPreparationProgramAssociations/keyChanges`
- `GET /tpdm/candidateEducatorPreparationProgramAssociations/partitions`
- `GET /tpdm/candidateEducatorPreparationProgramAssociations/{id}`
- `PUT /tpdm/candidateEducatorPreparationProgramAssociations/{id}`
- `DELETE /tpdm/candidateEducatorPreparationProgramAssociations/{id}`
