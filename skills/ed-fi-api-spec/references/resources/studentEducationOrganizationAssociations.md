# studentEducationOrganizationAssociations

`/ed-fi/studentEducationOrganizationAssociations`

This association represents student information as reported in the context of the student's relationship to
the education organization. Enrollment relationship semantics are covered by StudentSchoolAssociation.

## Natural key

`educationOrganizationReference`, `studentReference`

_Derived from the OpenAPI metadata: identity fields plus required references. Reference rows below list the
key fields inside each reference._

## Fields

`key` = part of the natural key, `yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationReference` | key | reference: `educationOrganizationId` |  |
| `studentReference` | key | reference: `studentUniqueId` |  |
| `addresses` |  | array of edFi_studentEducationOrganizationAssociationAddress | An unordered collection of studentEducationOrganizationAssociationAddresses. |
| `ancestryEthnicOrigins` |  | array of edFi_studentEducationOrganizationAssociationAncestryEthnicOrigin | An unordered collection of studentEducationOrganizationAssociationAncestryEthnicOrigins. |
| `barrierToInternetAccessInResidenceDescriptor` |  | descriptor URI | An indication of the barrier to having internet access in the student s primary place of residence. |
| `cohortYears` |  | array of edFi_studentEducationOrganizationAssociationCohortYear | An unordered collection of studentEducationOrganizationAssociationCohortYears. |
| `disabilities` |  | array of edFi_studentEducationOrganizationAssociationDisability | An unordered collection of studentEducationOrganizationAssociationDisabilities. |
| `displacedStudents` |  | array of edFi_studentEducationOrganizationAssociationDisplacedStudent | An unordered collection of studentEducationOrganizationAssociationDisplacedStudents. |
| `electronicMails` |  | array of edFi_studentEducationOrganizationAssociationElectronicMail | An unordered collection of studentEducationOrganizationAssociationElectronicMails. |
| `genderIdentity` |  | string max 60 | The student's gender as last reported to the education organization. |
| `hispanicLatinoEthnicity` |  | boolean | An indication that the individual traces his or her origin or descent to Mexico, Puerto Rico, Cuba, Central, and South America, and other Spanish cultures, reg… |
| `internationalAddresses` |  | array of edFi_studentEducationOrganizationAssociationInternationalAddress | An unordered collection of studentEducationOrganizationAssociationInternationalAddresses. |
| `internetAccessInResidence` |  | boolean | An indication of whether the student is able to access the internet in their primary place of residence. |
| `internetAccessTypeInResidenceDescriptor` |  | descriptor URI | The primary type of internet service used in the student s primary place of residence. |
| `internetPerformanceInResidenceDescriptor` |  | descriptor URI | An indication of whether the student can complete the full range of learning activities, including video streaming and assignment upload, without interruptions… |
| `languages` |  | array of edFi_studentEducationOrganizationAssociationLanguage | An unordered collection of studentEducationOrganizationAssociationLanguages. |
| `limitedEnglishProficiencyDescriptor` |  | descriptor URI | An indication that the student has been identified as limited English proficient by the Language Proficiency Assessment Committee (LPAC), or English proficient. |
| `loginId` |  | string max 60 | The login ID for the user; used for security access control interface. |
| `primaryLearningDeviceAccessDescriptor` |  | descriptor URI | An indication of whether the primary learning device is shared or not shared with another individual. |
| `primaryLearningDeviceAwayFromSchoolDescriptor` |  | descriptor URI | The type of device the student uses most often to complete learning activities away from school. |
| `primaryLearningDeviceProviderDescriptor` |  | descriptor URI | The provider of the primary learning device. |
| `profileThumbnail` |  | string max 255 | Locator reference for the student photo. |
| `races` |  | array of edFi_studentEducationOrganizationAssociationRace | An unordered collection of studentEducationOrganizationAssociationRaces. |
| `sexDescriptor` |  | descriptor URI | The student's birth sex as reported to the education organization. |
| `studentCharacteristics` |  | array of edFi_studentEducationOrganizationAssociationStudentCharacteristic | An unordered collection of studentEducationOrganizationAssociationStudentCharacteristics. |
| `studentIdentificationCodes` |  | array of edFi_studentEducationOrganizationAssociationStudentIdentificationCode | An unordered collection of studentEducationOrganizationAssociationStudentIdentificationCodes. |
| `studentIndicators` |  | array of edFi_studentEducationOrganizationAssociationStudentIndicator | An unordered collection of studentEducationOrganizationAssociationStudentIndicators. |
| `supporterMilitaryConnectionDescriptor` |  | descriptor URI | Military connection of the person/people whom the student is a dependent of. |
| `telephones` |  | array of edFi_studentEducationOrganizationAssociationTelephone | An unordered collection of studentEducationOrganizationAssociationTelephones. |
| `tribalAffiliations` |  | array of edFi_studentEducationOrganizationAssociationTribalAffiliation | An unordered collection of studentEducationOrganizationAssociationTribalAffiliations. |

## Endpoints

- `DELETE /ed-fi/studentEducationOrganizationAssociations/{id}`
- `GET /ed-fi/studentEducationOrganizationAssociations/deletes`
- `GET /ed-fi/studentEducationOrganizationAssociations/keyChanges`
- `GET /ed-fi/studentEducationOrganizationAssociations/partitions`
- `GET /ed-fi/studentEducationOrganizationAssociations/{id}`
- `GET /ed-fi/studentEducationOrganizationAssociations`
- `POST /ed-fi/studentEducationOrganizationAssociations`
- `PUT /ed-fi/studentEducationOrganizationAssociations/{id}`
