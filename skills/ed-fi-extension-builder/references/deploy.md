# Deploying an extension to a local Ed-Fi API

How to load a built extension (`ApiSchema-EXTENSION.json`) into the local Ed-Fi API 8.1 stack from the
[Data Management Service](https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service) repository. It follows
Steps 4 to 6 of the how-to guides; claims are in [security.md](security.md) and the checks in
[verify.md](verify.md). Tested on 2026-11-23 with the repository's `main` branch (8.1 line), PowerShell 7 and
Docker Desktop.

A host that doesn't run the local stack (a hosted or packaged Ed-Fi API) loads the same two inputs, the
staged schemas and a claims fragment, through its own deployment. Ask the developer how their host is
deployed before giving these commands.

## Before you start

- The stack has been started once with `./bootstrap-local-dms.ps1` (Getting Started), so the core schemas are
  staged in the repository checkout.
- The extension builds without errors ([build.md](build.md)).
- The .NET 10 SDK is installed. The staging script builds the `api-schema-tools` CLI if it can't find it.
- Every command runs from `eng/docker-compose/` in the repository checkout.

**Ports.** The stack publishes the API on `8080` (`DMS_HTTP_PORTS`), the Configuration Service on `8081` and
PostgreSQL on `5435` (`POSTGRES_PORT`), all set in `eng/docker-compose/.env`. If another Ed-Fi API already
uses a port, change the value in `.env` before the first start and use the new port in every URL. The stack's
Compose project is `dms-local`, so its teardown removes only its own containers and volumes.

## Step 1: Gather the schemas

Put each schema in its own folder under one directory. The staging script finds every `ApiSchema*.json` in
it:

```text
my-schemas/
  Ed-Fi/ApiSchema.json, discovery-spec.json, xsd/     <- core, copied from the staged workspace
  TPDM/ApiSchema.json, xsd/                           <- Data Standard 5.2 only
  SampleStudentTranscript/ApiSchema-EXTENSION.json    <- the MetaEd output, as is
```

Copy the core schemas that the first start staged (the guide's Step 4a, PowerShell):

```powershell
$schemaRoot = "C:\path\to\my-schemas"
foreach ($project in Get-ChildItem ".bootstrap\ApiSchema\schemas" -Directory) {
  $target = Join-Path $schemaRoot $project.Name
  New-Item -ItemType Directory -Force $target | Out-Null
  Copy-Item (Join-Path $project.FullName "ApiSchema.json") $target
  $content = Join-Path ".bootstrap\ApiSchema\content" $project.Name
  if (Test-Path $content) { Copy-Item (Join-Path $content "*") $target -Recurse }
}
```

Then copy `MetaEdOutput/<ProjectName>/ApiSchema/ApiSchema-EXTENSION.json` into its own folder. More than one
extension can be loaded at once: give each its own folder.

## Step 2: Reset the stack (deletes data)

The schema creates the database tables when the stack starts, so a new or changed extension needs an empty
database. **This step deletes the stack's databases**: every record, and every API client and vendor in the
Configuration Service. Tell the developer and wait for a yes before running it:

```powershell
./bootstrap-local-dms.ps1 -d -v
```

It also removes the `.bootstrap/` workspace, so run it before staging, never after.

## Step 3: Stage the schemas

```powershell
./prepare-dms-schema.ps1 -ApiSchemaPath "C:\path\to\my-schemas"
```

It prints `Prepared ApiSchema workspace` and the effective schema hash. According to the guide, staging a
schema set that differs from an existing `.bootstrap/` workspace fails with `Existing staged bootstrap
workspace differs from requested inputs`: run Step 2 first.

## Step 4: Stage the claims

Write the claims fragment ([security.md](security.md)) and stage it:

```powershell
./prepare-dms-claims.ps1 -ClaimsDirectoryPath "C:\path\to\my-claims"
```

It prints `Claims mode: Hybrid`. Without `-ClaimsDirectoryPath` it fails with `ClaimsDirectoryPath is required
for unmapped extension project(s)`. An extension that only adds properties to core resources still needs the
parameter if no other fragment is staged; one fragment for any extension in the set is enough.

## Step 5: Start

```powershell
./bootstrap-local-dms.ps1
```

The start creates the tables from the staged schemas, loads the claims into the Configuration Service and
checks them (`Claims gate PASSED`), then starts the API (`DMS service is healthy`).

If it stops with `api-schema-tools ddl provision failed ... with exit code 1`, the table generation rejected the
schema set. The script doesn't show why; run the generation without a database to see the error, from the
repository root:

```powershell
src/dms/clis/EdFi.DataManagementService.SchemaTools/bin/Release/net10.0/api-schema-tools ddl emit `
  -s my-schemas/Ed-Fi/ApiSchema.json -s my-schemas/TPDM/ApiSchema.json `
  -s my-schemas/SampleStudentTranscript/ApiSchema-EXTENSION.json -o ddl-check -d pgsql
```

The first `-s` is the core schema and the rest are extensions. Adding one extension at a time shows which one
fails. A known case is in [Known issues](#known-issues).

## Changing an installed extension

The running stack can't reload a schema or claims. After any change to the `.metaed` files or the fragment:
build, then Steps 2 to 5 again. The data is lost, so reload it through the API afterwards.

## Known issues

- **Extending a common inside a core resource (Ed-Fi API 8.1.0).** The Student Transcript example extends
  the `ClassRanking` common of `StudentAcademicRecord`, which is a single object (not a collection). The
  `common extension EdFi.ClassRanking` property fails on its own, with or without other additions to the
  resource: the start fails with `ddl provision failed`, and `ddl emit` shows `An item with the same key has
  already been added. Key: samplestudenttranscript.StudentAcademicRecordExtension`. Without that property,
  `Common EdFi.ClassRanking additions` builds and deploys but changes nothing: `classRanking` gets no `_ext`,
  and MetaEd gives no warning. Until the Ed-Fi API fixes it, tell the developer, and put the new properties on
  the resource instead of the common if the extension must deploy now. Commons that are collections weren't
  tested.
