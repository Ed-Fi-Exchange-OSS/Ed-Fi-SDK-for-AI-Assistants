# staffDirectories

`/ed-fi/staffDirectories`

The contact information associated to a staff member.

Also searched as: address, phone, staff contact.

## Natural key

`educationOrganizationId`, `staffUniqueId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `educationOrganizationReference` | yes | reference; supply `educationOrganizationId` | Reference to educationOrganization. |
| `staffReference` | yes | reference; supply `staffUniqueId` | This entity represents an individual who performs specified activities for any public or private education institution or agency that provides instructional an… |
| `addresses` |  | array of edFi_staffDirectoryAddress | An unordered collection of staffDirectoryAddresses. |
| `electronicMails` |  | array of edFi_staffDirectoryElectronicMail | An unordered collection of staffDirectoryElectronicMails. |
| `internationalAddresses` |  | array of edFi_staffDirectoryInternationalAddress | An unordered collection of staffDirectoryInternationalAddresses. |
| `telephones` |  | array of edFi_staffDirectoryTelephone | An unordered collection of staffDirectoryTelephones. |

### Items in `addresses`

| Field | Required | Type | Description |
|---|---|---|---|
| `addressTypeDescriptor` | yes | descriptor URI | The type of address listed for an individual or organization. |
| `stateAbbreviationDescriptor` | yes | descriptor URI | The abbreviation for the state (within the United States) or outlying area in which an address is located. |
| `city` | yes | string max 30 | The name of the city in which an address is located. |
| `postalCode` | yes | string max 17 | The five or nine digit zip code or overseas postal code portion of an address. |
| `streetNumberName` | yes | string max 150 | The street number and street name or post office box number of an address. |
| `localeDescriptor` |  | descriptor URI | A general geographic indicator that categorizes U.S. |
| `apartmentRoomSuiteNumber` |  | string max 50 | The apartment, room, or suite number of an address. |
| `buildingSiteNumber` |  | string max 20 | The number of the building on the site, if more than one building shares the same address. |
| `congressionalDistrict` |  | string max 30 | The congressional district in which an address is located. |
| `countyFIPSCode` |  | string max 5 | The Federal Information Processing Standards (FIPS) numeric code for the county issued by the National Institute of Standards and Technology (NIST). |
| `doNotPublishIndicator` |  | boolean | An indication that the address should not be published. |
| `latitude` |  | string max 20 | The geographic latitude of the physical address. |
| `longitude` |  | string max 20 | The geographic longitude of the physical address. |
| `nameOfCounty` |  | string max 30 | The name of the county, parish, borough, or comparable unit (within a state) in which an address is located. |
| `characteristics` |  | array of edFi_staffDirectoryAddressCharacteristic | An unordered collection of staffDirectoryAddressCharacteristics. |
| `periods` |  | array of edFi_staffDirectoryAddressPeriod | An unordered collection of staffDirectoryAddressPeriods. |

### Items in `electronicMails`

| Field | Required | Type | Description |
|---|---|---|---|
| `electronicMailTypeDescriptor` | yes | descriptor URI | The type of email listed for an individual or organization. |
| `electronicMailAddress` | yes | string max 128 | The electronic mail (e-mail) address listed for an individual or organization. |
| `doNotPublishIndicator` |  | boolean | An indication that the electronic email address should not be published. |
| `primaryEmailAddressIndicator` |  | boolean | An indication that the electronic mail address should be used as the principal electronic mail address for an individual or organization. |

### Items in `internationalAddresses`

| Field | Required | Type | Description |
|---|---|---|---|
| `addressTypeDescriptor` | yes | descriptor URI | The type of address listed for an individual or organization. |
| `countryDescriptor` | yes | descriptor URI | The name of the country. |
| `addressLine1` | yes | string max 150 | The first line of the address. |
| `addressLine2` |  | string max 150 | The second line of the address. |
| `addressLine3` |  | string max 150 | The third line of the address. |
| `addressLine4` |  | string max 150 | The fourth line of the address. |
| `beginDate` |  | string (date) | The first date the address is valid. |
| `endDate` |  | string (date) | The last date the address is valid. |
| `latitude` |  | string max 20 | The geographic latitude of the physical address. |
| `longitude` |  | string max 20 | The geographic longitude of the physical address. |

### Items in `telephones`

| Field | Required | Type | Description |
|---|---|---|---|
| `telephoneNumberTypeDescriptor` | yes | descriptor URI | The type of communication number listed for an individual or organization. |
| `telephoneNumber` | yes | string max 24 | The telephone number including the area code, and extension, if applicable. |
| `doNotPublishIndicator` |  | boolean | An indication that the telephone number should not be published. |
| `orderOfPriority` |  | integer (int32) | The order of priority assigned to telephone numbers to define which number to attempt first, second, etc. |
| `textMessageCapabilityIndicator` |  | boolean | An indication that the telephone number is technically capable of sending and receiving Short Message Service (SMS) text messages. |

## Endpoints

- `GET /ed-fi/staffDirectories`
- `POST /ed-fi/staffDirectories`
- `GET /ed-fi/staffDirectories/deletes`
- `GET /ed-fi/staffDirectories/keyChanges`
- `GET /ed-fi/staffDirectories/partitions`
- `GET /ed-fi/staffDirectories/{id}`
- `PUT /ed-fi/staffDirectories/{id}`
- `DELETE /ed-fi/staffDirectories/{id}`
