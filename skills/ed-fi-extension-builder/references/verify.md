# Verifying a deployed extension

After the start ([deploy.md](deploy.md)), check that the API serves the extension and that a client can use
it. Source: Step 8 of the how-to guides. The URLs below use the local stack's default ports (API `8080`,
Configuration Service `8081`); use the ports from the developer's `.env`.

## 1. Discovery lists the extension

```powershell
Invoke-RestMethod http://localhost:8080/api
```

`dataModels` lists each extension by `projectName`, with its version, next to `Ed-Fi` (and `TPDM` on Data
Standard 5.2). If it's missing, the schema wasn't staged before the start.

## 2. Create an API client

The reset deleted every client. From `eng/docker-compose/`:

```powershell
Import-Module ../smoke_test/modules/SmokeTest.psm1 -Force
$cred = Get-SmokeTestCredential -ConfigServiceUrl "http://localhost:8081"
```

- The client uses the `EdFiSandbox` claim set; `-ClaimSetName` picks another.
- A second call needs a new `-VendorName` and `-ApplicationName`; reusing the defaults fails with `400`.
- `-EducationOrganizationIds` sets the education organizations the client is associated with. Relationship
  based reads and writes only reach data linked to them.
- Don't print the key and secret in shared logs; keep them in variables.

Get a token:

```powershell
$auth = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes("$($cred.Key):$($cred.Secret)"))
$token = (Invoke-RestMethod -Method Post -Uri "http://localhost:8081/connect/token" `
  -Headers @{ Authorization = "Basic $auth" } -ContentType "application/x-www-form-urlencoded" `
  -Body @{ grant_type = "client_credentials" }).access_token
```

## 3. Call the new resources

New resources are under `/data/{projectEndpointName}/`, in camelCase plural:

```powershell
Invoke-RestMethod -Uri "http://localhost:8080/api/data/sample-student-transcript/postSecondaryOrganizations" `
  -Headers @{ Authorization = "Bearer $token" }
```

`200` with an empty list means the resource exists and the claim set can read it. Then write one record of
each new descriptor and resource, and read it back. Descriptors first, since resources refer to them.

## 4. Check additions to core resources

Additions travel under `_ext.{projectName in lowercase}` in the payload of the core resource, at
`/data/ed-fi/...`:

```json
{
  "studentReference": { "studentUniqueId": "604822" },
  "educationOrganizationReference": { "educationOrganizationId": 255901001 },
  "schoolYearTypeReference": { "schoolYear": 2026 },
  "termDescriptor": "uri://ed-fi.org/TermDescriptor#Fall Semester",
  "_ext": {
    "samplestudenttranscript": {
      "postSecondaryOrganizationReference": { "nameOfInstitution": "Sample State University" },
      "submissionCertificationDescriptor": "uri://sample.ed-fi.org/SampleStudentTranscript/SubmissionCertificationDescriptor#Official"
    }
  }
}
```

A `200` on the core resource alone doesn't prove the extension is loaded. Write a record with `_ext` and read
it back, or look for the `_ext` node in the resource's schema in the OpenAPI document
(`/api/metadata/specifications`).

## Reading the results

| Response | Meaning | Fix |
|---|---|---|
| `404` on `/data/{projectEndpointName}/...` | The extension isn't loaded, or the URL segment is wrong | Check Discovery and `projectEndpointName` |
| `403` `access-denied:action`, naming the resource claim | The claim set has no grant for this action | Add or fix the claim in the fragment ([security.md](security.md)); redeploy |
| `403` `namespace-mismatch` on a descriptor | The descriptor's `namespace` doesn't start with one of the vendor's prefixes | Use a namespace the vendor has ([security.md](security.md#descriptor-namespaces)) |
| `403` with `No relationships have been established` | Relationship-based authorization: the record isn't linked to the client's education organizations | Create the linking record first (for a student, a `studentSchoolAssociation`) |
| `400` `... does not exist` on a descriptor | The descriptor value hasn't been loaded | POST the descriptor value first |
| `409` `unresolved-reference` | A referenced record doesn't exist, including references inside `_ext` | Create the referenced record first |
| `GET` returns `[]` after a `201` | The client can write but not read through its relationships | Link the record to the client's education organizations, then read again |

## What the API enforces for additions

Tested on Ed-Fi API 8.1 (2026-11-23), with `is required` on a property added to the core `Staff`:

- A `POST /data/ed-fi/staffs` **without `_ext`** returned `201`, and so did one with an empty
  `_ext.{project}` object; the record was stored without the property.
- A wrong type inside `_ext` returned `400` (`isTenured Value is "string" but should be "boolean"`).
- Values sent under `_ext` came back on `GET`.

So a required addition doesn't make clients send it. Model additions as optional (rule CORE-5 in
[rules.md](rules.md)) and validate in the client if the value is needed.
