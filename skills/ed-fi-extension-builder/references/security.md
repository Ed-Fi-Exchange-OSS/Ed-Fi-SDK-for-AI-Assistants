# Claims for extension resources

The Ed-Fi API denies access to a resource that isn't in the claims hierarchy. Every **new resource and
descriptor** an extension adds needs a resource claim in a **claims fragment**; the fragment is staged before
the start ([deploy.md](deploy.md), Step 4). Source: Steps 5d and 7 of the how-to guides and
[How To: Create and Manage API Security Metadata](https://docs.ed-fi.org/reference/ed-fi-api/8/how-to-guides/how-to-create-and-manage-api-security-metadata).

## What needs a claim

| Extension element | Claim |
|---|---|
| New descriptor | A child of `domains/systemDescriptors` |
| New association or entity about students, staff or education organizations | A child of `domains/relationshipBasedData` (or another existing domain that fits) |
| New entity with no relationship to education organizations, students or staff | A new domain with its own default strategy and claim set grants |
| `additions` to a core resource or common type | None: the core resource's claim covers its `_ext` properties |

## Claim names

`http://ed-fi.org/identity/claims/{projectEndpointName}/{resourceName}`, with both values from the generated
`ApiSchema-EXTENSION.json`: `projectEndpointName` is the kebab-case project name (`sample-student-transcript`),
and `resourceName` is the entity name as authored (`PostSecondaryOrganization`,
`InstitutionLevelDescriptor`). Ed-Fi API 8 names have no `/ods/` segment, unlike ODS/API 7.x. Matching is
case-insensitive.

## The fragment

One JSON file per extension in a folder of its own, named `NNN-<name>-claims.json`. Under an existing domain,
the new claims inherit that domain's grants (for example, `SISVendor` has Read on `systemDescriptors` and full
access on `relationshipBasedData`):

```json
{
  "name": "SampleAlternativeEducationProgramClaims",
  "resourceClaims": [
    {
      "isParent": true,
      "name": "domains/systemDescriptors",
      "children": [
        { "name": "http://ed-fi.org/identity/claims/sample-alternative-education-program/AlternativeEducationEligibilityReasonDescriptor" }
      ]
    },
    {
      "isParent": true,
      "name": "domains/relationshipBasedData",
      "children": [
        { "name": "http://ed-fi.org/identity/claims/sample-alternative-education-program/StudentAlternativeEducationProgramAssociation" }
      ]
    }
  ]
}
```

The guide notes that a `claimSets` list on an existing domain is ignored. To grant access to a resource
with no natural parent, or to only some claim sets, create a new domain with a default strategy and explicit
grants, as the Student Transcript example does for `postSecondaryOrganizations`:

```json
{
  "isParent": true,
  "name": "http://ed-fi.org/identity/claims/domains/sample-student-transcript",
  "_defaultAuthorizationStrategiesForCrud": [
    { "actionName": "Create", "authorizationStrategies": [{ "name": "NoFurtherAuthorizationRequired" }] },
    { "actionName": "Read", "authorizationStrategies": [{ "name": "NoFurtherAuthorizationRequired" }] },
    { "actionName": "Update", "authorizationStrategies": [{ "name": "NoFurtherAuthorizationRequired" }] },
    { "actionName": "Delete", "authorizationStrategies": [{ "name": "NoFurtherAuthorizationRequired" }] },
    { "actionName": "ReadChanges", "authorizationStrategies": [{ "name": "NoFurtherAuthorizationRequired" }] }
  ],
  "children": [
    { "name": "http://ed-fi.org/identity/claims/sample-student-transcript/PostSecondaryOrganization" }
  ],
  "claimSets": [
    { "name": "SISVendor", "actions": [{ "name": "Create" }, { "name": "Read" }, { "name": "Update" }, { "name": "Delete" }, { "name": "ReadChanges" }] },
    { "name": "EdFiSandbox", "actions": [{ "name": "Create" }, { "name": "Read" }, { "name": "Update" }, { "name": "Delete" }, { "name": "ReadChanges" }] }
  ]
}
```

Only the claim sets listed get access: on the test stack, an `AssessmentVendor` client got `403` on
`postSecondaryOrganizations` and `200` on the extension's descriptors, which inherit from
`systemDescriptors`.

## Checks before staging

- One claim for every new resource and descriptor in `ApiSchema-EXTENSION.json`, and none for resources that
  only have `additions`.
- `projectEndpointName` in every URI matches the schema.
- Ask the developer which claim sets need access, and choose `NoFurtherAuthorizationRequired` only for data
  that isn't about students, staff or education organizations. Say what each choice exposes.

## Descriptor namespaces

Writes to descriptors are authorized by **namespace prefix**: the `namespace` of each value must start with a
prefix assigned to the client's vendor. On the test stack, `uri://sample.org/...` returned `403` with `The
'Namespace' value of the data does not start with any of the caller's associated namespace prefixes`, and
`uri://sample.ed-fi.org/...` worked. Use a namespace the developer's vendor already has, or ask the host
administrator to add one.
