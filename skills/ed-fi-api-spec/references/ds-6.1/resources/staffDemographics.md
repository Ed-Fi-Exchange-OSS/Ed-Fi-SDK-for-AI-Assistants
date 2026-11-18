# staffDemographics

`/ed-fi/staffDemographics`

The demographic information associated to a Staff member

Also searched as: race.

## Natural key

`educationOrganizationId`, `staffUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `staffReference` | yes | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |
| `ancestryEthnicOrigins` |  | array of edFi_staffDemographicAncestryEthnicOrigin | An unordered collection of staffDemographicAncestryEthnicOrigins. |
| `citizenshipStatusDescriptor` |  | descriptor URI | An indicator of whether or not the person is a U.S. |
| `genderIdentity` |  | string max 60 | The Staff's gender as last reported to the education organization. |
| `hispanicLatinoEthnicity` |  | boolean | An indication that the individual traces his or her origin or descent to Mexico, Puerto Rico, Cuba, Central, and South America, and other Spanish cultures, reg… |
| `identificationDocuments` |  | array of edFi_staffDemographicIdentificationDocument | An unordered collection of staffDemographicIdentificationDocuments. |
| `languages` |  | array of edFi_staffDemographicLanguage | An unordered collection of staffDemographicLanguages. |
| `races` |  | array of edFi_staffDemographicRace | An unordered collection of staffDemographicRaces. |
| `sexDescriptor` |  | descriptor URI | The Staff's birth sex as reported to the education organization. |
| `tribalAffiliations` |  | array of edFi_staffDemographicTribalAffiliation | An unordered collection of staffDemographicTribalAffiliations. |
| `visas` |  | array of edFi_staffDemographicVisa | An unordered collection of staffDemographicVisas. |

### Items in `ancestryEthnicOrigins`

| Field | Required | Type | Description |
|---|---|---|---|
| `ancestryEthnicOriginDescriptor` | yes | descriptor URI | The original peoples or cultures with which the individual identifies. |

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
| `uses` |  | array of edFi_staffDemographicLanguageUse | An unordered collection of staffDemographicLanguageUses. |

### Items in `races`

| Field | Required | Type | Description |
|---|---|---|---|
| `raceDescriptor` | yes | descriptor URI | The general racial category which most clearly reflects the individual's recognition of his or her community or with the which the individual most identifies a… |

### Items in `tribalAffiliations`

| Field | Required | Type | Description |
|---|---|---|---|
| `tribalAffiliationDescriptor` | yes | descriptor URI | An American Indian tribe with which the Staff is affiliated as last reported to the education organization. |

### Items in `visas`

| Field | Required | Type | Description |
|---|---|---|---|
| `visaDescriptor` | yes | descriptor URI | An indicator of a non-US citizen's Visa type. |

## Endpoints

- `GET /ed-fi/staffDemographics`
- `POST /ed-fi/staffDemographics`
- `GET /ed-fi/staffDemographics/deletes`
- `GET /ed-fi/staffDemographics/keyChanges`
- `GET /ed-fi/staffDemographics/partitions`
- `GET /ed-fi/staffDemographics/{id}`
- `PUT /ed-fi/staffDemographics/{id}`
- `DELETE /ed-fi/staffDemographics/{id}`
