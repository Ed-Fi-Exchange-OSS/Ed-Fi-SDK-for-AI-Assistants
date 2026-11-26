# Deploying an extension to a host

How to load an extension into an Ed-Fi API 8.1 host that doesn't run the local stack from
[deploy.md](deploy.md): a server, containers from the published images, or a cloud deployment. The host loads
the same inputs as the local stack (the core and extension schemas and a claims fragment), with the host's
own settings and tools. Sources: [Extending API DataModel](https://docs.ed-fi.org/reference/ed-fi-api/8/platform-dev-guide/extensibility-customization/extending-api-datamodel),
[Database Provisioning](https://docs.ed-fi.org/reference/ed-fi-api/8/platform-dev-guide/utilities/database-provisioning),
[How To: Create and Manage API Security Metadata](https://docs.ed-fi.org/reference/ed-fi-api/8/how-to-guides/how-to-create-and-manage-api-security-metadata),
and `docs/CONFIGURATION.md` and `docs/CLAIMS-LOADING-GUIDE.md` in the
[Data Management Service](https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service) repository.

Ask the developer how their host is deployed (containers, a server, which database engine) and who manages it
before giving these steps. Hosting choices, such as how a secret or a mount is set, are theirs.

## What changes on a host

An extension changes the database tables and the claims hierarchy, and neither can change in place:

- **The database must be new.** Provisioning creates tables only; it can't add an extension to a database
  that already has a schema. Adding, changing or removing an extension means a new database and reloading the
  data through the API.
- **Claims load only into an empty Configuration Service database.** On a later start the service logs
  `Claims data already exists, skipping initial load` and ignores changed files. The documented production path
  for new resource claims is a new Configuration Service database, which means recreating vendors,
  applications, credentials and data stores.

Say both before the developer plans a change to a host in use. Plan an extension before the host goes live
when possible.

## Step 1: Stage the schema workspace

The API loads schemas from a directory with a manifest, `bootstrap-api-schema-manifest.json`. Loose
`ApiSchema*.json` files without it aren't loaded. The simplest way to get a valid directory is to stage it
with the local scripts ([deploy.md](deploy.md), Steps 1 and 3) and copy `.bootstrap/ApiSchema/` to the host.
Or write the manifest by hand:

```json
{
  "version": 1,
  "projects": [
    { "projectName": "Ed-Fi", "projectEndpointName": "ed-fi", "isExtensionProject": false,
      "schemaPath": "schemas/Ed-Fi/ApiSchema.json", "discoverySpecPath": "content/Ed-Fi/discovery-spec.json",
      "xsdDirectory": "content/Ed-Fi/xsd" },
    { "projectName": "SampleStudentTranscript", "projectEndpointName": "sample-student-transcript",
      "isExtensionProject": true, "schemaPath": "schemas/SampleStudentTranscript/ApiSchema.json" }
  ]
}
```

- Exactly one project is the core (`isExtensionProject: false`). Paths are relative to the manifest, without
  `..`.
- Without the core `discoverySpecPath`, the discovery specification endpoint fails. `xsdDirectory` is needed
  only for the XML bulk load client.
- If the manifest or a file it lists is missing or invalid, the API doesn't start.

Point the API at the directory:

| Setting | Docker Compose variable | Value |
|---|---|---|
| `AppSettings__ApiSchema__UseCustomPath` | `USE_API_SCHEMA_PATH` | `true` |
| `AppSettings__ApiSchema__Path` | `API_SCHEMA_PATH` | The directory, for example `/app/ApiSchema` |

Leave `SCHEMA_PACKAGES` empty: when it's set, the container downloads those packages at startup and rewrites
the manifest, which drops a staged extension.

## Step 2: Provision a new database

Use `api-schema-tools` (the .NET tool `EdFi.Api.SchemaTools` from the Ed-Fi package feed, or a build from the
repository) with the same schema files, core first, in the manifest's order:

```bash
api-schema-tools ddl provision \
  -s schemas/Ed-Fi/ApiSchema.json \
  -s schemas/SampleStudentTranscript/ApiSchema.json \
  -c "<connection string>" -d pgsql --create-database
```

- `-d` is `pgsql` or `mssql`. The API doesn't create or migrate tables when it starts.
- The output ends with `Provisioning complete` and the **effective schema hash**. `api-schema-tools hash` with
  the same files prints the same hash without a database.
- Running it again with the same files changes nothing. With a different set of schemas, it stops with
  `dms.EffectiveSchema validation failed: EffectiveSchemaHash: stored=..., expected=...`: the database belongs
  to the old set, so provision a new one.
- Keep the connection string out of logs and shared files; ask the developer to supply it.

Then register the new database as a data store in the Configuration Service, as for any data store.

## Step 3: Load the claims

Set the Configuration Service to compose the built-in claims with the fragments from [security.md](security.md):

| Setting | Value |
|---|---|
| `CONFIGURATION_SERVICE_CLAIMS_SOURCE` (`ClaimsOptions__ClaimsSource`) | `Hybrid` |
| `CONFIGURATION_SERVICE_CLAIMS_DIRECTORY` (`ClaimsOptions__ClaimsDirectory`) | The folder with the `*-claims.json` fragments |
| `ClaimsOptions__DataStandardVersion` | `6.1` on a Data Standard 6.1 host; `5.2` is the default |

Start the service against an empty Configuration Service database, with database deployment on startup
enabled, so it seeds the claims. Fragment names must end in lowercase `-claims.json`; if a fragment isn't valid
JSON, the service loads the built-in claims without the fragments.

`Filesystem` mode (one complete `Claims.json`) and the management endpoints that reload or upload claims also
exist. The endpoints are off by default, and the repository's guide says not to turn them on in production, so
don't suggest them.

## Step 4: Restart and verify

Restart the API after changing the schema workspace; it loads schemas only at startup. Then follow
[verify.md](verify.md) with the host's URLs.

If requests return `503` while Discovery works, the database and the loaded schemas don't match (a different
effective schema hash) or the database wasn't provisioned. Compare the hash of the provisioned database with
`api-schema-tools hash` on the API's schema files.

## What was tested

On 2026-11-26, `ddl provision` and `hash` with the Data Standard 6.1 core and three extensions, against a new
PostgreSQL database: the results described in Step 2. The rest of this page comes from the sources above and
wasn't run on a host.
