# studentDemographics

`/ed-fi/studentDemographics`

The demographic information associated to a student.

Also searched as: race, disability, student characteristic, English proficiency.

## Natural key

`educationOrganizationId`, `studentUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `studentReference` | yes | reference; supply `studentUniqueId` | This entity represents an individual for whom instruction, services, and/or care are provided in an early childhood, elementary, or secondary educational progr… |
| `ancestryEthnicOrigins` |  | array of edFi_studentDemographicAncestryEthnicOrigin | An unordered collection of studentDemographicAncestryEthnicOrigins. |
| `citizenshipStatusDescriptor` |  | descriptor URI | An indicator of whether or not the person is a U.S. |
| `disabilities` |  | array of edFi_studentDemographicDisability | An unordered collection of studentDemographicDisabilities. |
| `economicDisadvantageDescriptor` |  | descriptor URI | The indication of an inadequate financial condition of an individual's family, as determined by family income, number of family members/dependents, participati… |
| `genderIdentity` |  | string max 60 | The student's gender as last reported to the education organization. |
| `hispanicLatinoEthnicity` |  | boolean | An indication that the individual traces his or her origin or descent to Mexico, Puerto Rico, Cuba, Central, and South America, and other Spanish cultures, reg… |
| `identificationDocuments` |  | array of edFi_studentDemographicIdentificationDocument | An unordered collection of studentDemographicIdentificationDocuments. |
| `languages` |  | array of edFi_studentDemographicLanguage | An unordered collection of studentDemographicLanguages. |
| `limitedEnglishProficiencyDescriptor` |  | descriptor URI | An indication that the student has been identified as limited English proficient by the Language Proficiency Assessment Committee (LPAC), or English proficient. |
| `races` |  | array of edFi_studentDemographicRace | An unordered collection of studentDemographicRaces. |
| `sexDescriptor` |  | descriptor URI | The student's birth sex as reported to the education organization. |
| `studentCharacteristics` |  | array of edFi_studentDemographicStudentCharacteristic | An unordered collection of studentDemographicStudentCharacteristics. |
| `supporterMilitaryConnectionDescriptor` |  | descriptor URI | Military connection of the person/people whom the student is a dependent of. |
| `tribalAffiliations` |  | array of edFi_studentDemographicTribalAffiliation | An unordered collection of studentDemographicTribalAffiliations. |
| `visas` |  | array of edFi_studentDemographicVisa | An unordered collection of studentDemographicVisas. |

### Items in `ancestryEthnicOrigins`

| Field | Required | Type | Description |
|---|---|---|---|
| `ancestryEthnicOriginDescriptor` | yes | descriptor URI | The original peoples or cultures with which the individual identifies. |

### Items in `disabilities`

| Field | Required | Type | Description |
|---|---|---|---|
| `disabilityDescriptor` | yes | descriptor URI | A disability category that describes a individual's impairment. |
| `disabilityDeterminationSourceTypeDescriptor` |  | descriptor URI | The source that provided the disability determination. |
| `disabilityDiagnosis` |  | string max 80 | A description of the disability diagnosis. |
| `orderOfDisability` |  | integer (int32) | The order by severity of individual's disabilities: 1- Primary, 2 - Secondary, 3 - Tertiary, etc. |
| `designations` |  | array of edFi_studentDemographicDisabilityDesignation | An unordered collection of studentDemographicDisabilityDesignations. |

### Items in `identificationDocuments`

| Field | Required | Type | Description |
|---|---|---|---|
| `identificationDocumentUseDescriptor` | yes | descriptor URI | The primary function of the document used for establishing identity. |
| `personalInformationVerificationDescriptor` | yes | descriptor URI | The category of the document relative to its purpose. |
| `issuerCountryDescriptor` |  | descriptor URI | Country of origin of the document. |
| `documentExpirationDate` |  | string (date) | The day when the document expires, if null then never expires. |
| `documentTitle` |  | string max 60 | The title of the document given by the issuer. |
| `issuerDocumentIdentificationCode` |  | string max 120 | The unique identifier on the issuer's identification system. |
| `issuerName` |  | string max 150 | Name of the entity or institution that issued the document. |

### Items in `languages`

| Field | Required | Type | Description |
|---|---|---|---|
| `languageDescriptor` | yes | descriptor URI | A specification of which written or spoken communication is being used. |
| `uses` |  | array of edFi_studentDemographicLanguageUse | An unordered collection of studentDemographicLanguageUses. |

### Items in `races`

| Field | Required | Type | Description |
|---|---|---|---|
| `raceDescriptor` | yes | descriptor URI | The general racial category which most clearly reflects the individual's recognition of his or her community or with the which the individual most identifies a… |

### Items in `studentCharacteristics`

| Field | Required | Type | Description |
|---|---|---|---|
| `studentCharacteristicDescriptor` | yes | descriptor URI | The characteristic designated for the student. |
| `designatedBy` |  | string max 60 | The person, organization, or department that designated the characteristic. |
| `periods` |  | array of edFi_studentDemographicStudentCharacteristicPeriod | An unordered collection of studentDemographicStudentCharacteristicPeriods. |

### Items in `tribalAffiliations`

| Field | Required | Type | Description |
|---|---|---|---|
| `tribalAffiliationDescriptor` | yes | descriptor URI | An American Indian tribe with which the student is affiliated as last reported to the education organization. |

### Items in `visas`

| Field | Required | Type | Description |
|---|---|---|---|
| `visaDescriptor` | yes | descriptor URI | An indicator of a non-US citizen's Visa type. |

## Endpoints

- `GET /ed-fi/studentDemographics`
- `POST /ed-fi/studentDemographics`
- `GET /ed-fi/studentDemographics/deletes`
- `GET /ed-fi/studentDemographics/keyChanges`
- `GET /ed-fi/studentDemographics/partitions`
- `GET /ed-fi/studentDemographics/{id}`
- `PUT /ed-fi/studentDemographics/{id}`
- `DELETE /ed-fi/studentDemographics/{id}`
