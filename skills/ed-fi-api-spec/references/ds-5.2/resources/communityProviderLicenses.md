# communityProviderLicenses

`/ed-fi/communityProviderLicenses`

The legal document held by the community provider that authorizes the holder to perform certain functions and
or services.

## Natural key

`licenseIdentifier`, `licensingOrganization`, `communityProviderId`

## Fields

`yes` = required.

| Field | Required | Type | Description |
|---|---|---|---|
| `licenseIdentifier` | yes | string max 36 | The unique identifier issued by the licensing organization. |
| `licensingOrganization` | yes | string max 75 | The organization issuing the license. |
| `communityProviderReference` | yes | reference; supply `communityProviderId` | This entity represents an educational organization that includes staff and students who participate in classes and educational activity groups. |
| `authorizedFacilityCapacity` |  | integer (int32) | The maximum number that can be contained or accommodated which a provider is authorized or licensed to serve. |
| `licenseEffectiveDate` | yes | string (date) | The month, day, and year on which a license is active or becomes effective. |
| `licenseExpirationDate` |  | string (date) | The month, day, and year on which a license will expire. |
| `licenseIssueDate` |  | string (date) | The month, day, and year on which an active license was issued. |
| `licenseStatusDescriptor` |  | descriptor URI | An indication of the status of the license. |
| `licenseTypeDescriptor` | yes | descriptor URI | An indication of the category of the license. |
| `oldestAgeAuthorizedToServe` |  | integer (int32) | The oldest age of children a provider is authorized or licensed to serve. |
| `youngestAgeAuthorizedToServe` |  | integer (int32) | The youngest age of children a provider is authorized or licensed to serve. |

## Endpoints

- `GET /ed-fi/communityProviderLicenses`
- `POST /ed-fi/communityProviderLicenses`
- `GET /ed-fi/communityProviderLicenses/deletes`
- `GET /ed-fi/communityProviderLicenses/keyChanges`
- `GET /ed-fi/communityProviderLicenses/partitions`
- `GET /ed-fi/communityProviderLicenses/{id}`
- `PUT /ed-fi/communityProviderLicenses/{id}`
- `DELETE /ed-fi/communityProviderLicenses/{id}`
