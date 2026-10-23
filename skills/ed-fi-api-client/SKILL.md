---
name: ed-fi-api-client
description: Guidance for writing, reviewing, auditing, debugging, or fixing any code that acts as an Ed-Fi API client — scripts, CLIs, SDKs, ETL and extract jobs, SIS or data-warehouse integrations. Covers authentication and token handling, the Discovery API, pushing data (POST/PUT/DELETE, dependency order, descriptors), pulling data (paging, change queries, deletes), and diagnosing HTTP errors such as 400, 401, 403, 409, or 412. Targets ODS/API 7.x and Ed-Fi API 8.1+, and also applies when reviewing or upgrading older clients (ODS/API 2.x–6.x). Use whenever a task involves code that calls an Ed-Fi or ODS/API endpoint, or mentions Ed-Fi, ODS/API, edfi, oauth/token, /data/v3, Ed-Fi resources such as students or studentSchoolAssociations, or descriptors.
---

# Ed-Fi API Client

Ed-Fi APIs exchange K-12 education data using resources defined by the Ed-Fi Data Standard. The client
guidance here applies to ODS/API 7.x and Ed-Fi API 8: both expose the same resources and behave the same
way for POST/PUT/DELETE, references, descriptors and errors. Ed-Fi API 8 is a new platform, though, and
has a few breaking changes for clients; see [Ed-Fi API 8 differences](#ed-fi-api-8-differences).
In this skill, **Ed-Fi API 8 means 8.1 and later**; 8.0 is not a target. Examples use ODS/API 7.3 URLs
and Data Standard 5.2.

Do not guess at Ed-Fi behavior from general REST conventions. Several Ed-Fi rules surprise developers:
POST is an upsert, URLs use a server-generated `id` rather than natural keys, and a missing reference
returns `409 Conflict`, not `400` or `404`.

## Step 1: Start every integration from the Discovery API

The API root URL (e.g. `https://api.example.org/v7.3/api`) is the only URL a client should be
configured with. A GET on it returns the version and the URLs for everything else:

```json
{
  "version": "7.3",
  "dataModels": [{ "name": "Ed-Fi", "version": "5.2.0" }],
  "urls": {
    "dependencies": "https://api.example.org/v7.3/api/metadata/data/v3/dependencies",
    "openApiMetadata": "https://api.example.org/v7.3/api/metadata/",
    "oauth": "https://api.example.org/v7.3/api/oauth/token",
    "dataManagementApi": "https://api.example.org/v7.3/api/data/v3/",
    "changeQueries": "https://api.example.org/v7.3/api/changeQueries/v1/"
  }
}
```

- Read `urls.oauth` and `urls.dataManagementApi` from this response instead of hard-coding them.
- Resource paths such as `/ed-fi/students` are relative to `dataManagementApi`. **Make sure it ends in
  `/` before joining paths to it:** ODS/API 7.x returns `.../data/v3/`, but Ed-Fi API 8 returns `.../data`
  with no trailing slash, and URL resolvers (`new URL(path, base)`, `urljoin`) then drop the `data`
  segment. In this skill, `{dataManagementApi}` means that URL with the trailing `/`.
- Check `dataModels` to confirm the Data Standard version before relying on a resource's shape.
- Rule: [DISC-1](references/rules/discovery.md).

### How Ed-Fi URLs are built

Hosts can add segments before the API area, so never build URLs by hand from a guessed pattern:

```text
{root}/[tenant]/[context]/data/v3/{schema}/{resource}     # ODS/API 7.x
{root}/[tenant]/[context]/data/{schema}/{resource}        # Ed-Fi API 8 (no "v3" segment)
```

| Part | Example | Notes |
|---|---|---|
| Tenant (optional) | `.../grandbend/data/v3/...` | Only on multi-tenant hosts |
| Context (optional) | `.../2026/data/v3/...` | Usually a school year, on hosts with one database per year |
| Schema | `ed-fi`, `tx`, `talentMgmt` | `ed-fi` for core resources; extension resources live under their own schema |
| Resource | `students`, `termDescriptors` | camelCase, plural |

- Extensions to a core resource do **not** get a new route: their fields arrive under `_ext` in the
  core resource's body (e.g. `/ed-fi/students` with `"_ext": { "tx": { ... } }`).
- Composites (read-only, denormalized views) use `/composites/v1/{org}/{category}/{resource}`, e.g.
  `/composites/v1/ed-fi/assessment/studentAssessments`. Identity, when enabled, uses `/identity/v2`.
- Ask the developer or the host for the tenant and context segments, then take the rest from the
  Discovery API.

### Ed-Fi API 8 differences

Ed-Fi API 8 keeps the ODS/API resource model, but the release notes say client migration is required:

| Change | What the client must do |
|---|---|
| The `v3` segment is removed from resource URLs | Build resource URLs from the Discovery API (`urls.dataManagementApi`), never from a hard-coded `/data/v3/` path |
| Property names are case-sensitive. A property with the wrong case (`FirstName`) or an unknown name is **silently ignored**, not rejected, so its value is lost | Use the exact camelCase names from the schema (`studentUniqueId`, not `StudentUniqueId`); don't rely on a `400` to catch naming mistakes |
| The token endpoint moved to the Configuration Service (`/connect/token`); `/oauth/token` remains as a compatibility proxy | Take the token URL from `urls.oauth` in the Discovery API |
| No snapshot support | See [references/pull.md](references/pull.md#snapshots-consistent-reads) |
| Cursor paging needs a `pageToken` on every request; `pageSize` alone gets `400` | Get the first token from `/partitions` (see [references/pull.md](references/pull.md#cursor-paging-odsapi-73-and-later)) |

When in doubt, check `version` in the Discovery API response and the host's release notes.

## Step 2: Authenticate with OAuth 2.0 client credentials

POST `grant_type=client_credentials` to `urls.oauth`, sending the key and secret in a Basic
`Authorization` header (form-urlencode each, join with `:`, then base64), then send
`Authorization: Bearer <access_token>` on every request. Cache the token and re-authenticate only when
it is about to expire or a request returns 401. There is no refresh token.

Details, token lifecycle rules, and the client design:
[references/authentication.md](references/authentication.md).
Rules: [AUTH-1 to AUTH-5](references/rules/auth.md).

## Step 3: Ask which kind of integration this is

If the developer has not said, ask:

> Is this a **push** integration (sending data from a source system such as a SIS into Ed-Fi) or a
> **pull** integration (reading data out of Ed-Fi into another system)?

Then load only the guide that applies:

| Integration | Read | Covers |
|---|---|---|
| Push (write) | [references/push.md](references/push.md) | Dependency order, POST as upsert, PUT/DELETE by `id`, references, descriptors, ETags |
| Pull (read) | [references/pull.md](references/pull.md) | Paging, filtering, change queries, `/deletes`, `/keyChanges`, incremental sync |
| Either, when a request fails | [references/errors.md](references/errors.md) | What each status code means in Ed-Fi and how to handle it in code |
| Reviewing existing client code | [references/review.md](references/review.md) | Checking code against the rules and reporting findings by level |

When a developer pastes an error response or asks "what does this 409 mean?", go straight to
[references/errors.md](references/errors.md). When asked to review or audit existing integration code, go
straight to [references/review.md](references/review.md); there is no need to ask push or pull first.

## Finding resources and fields

The OpenAPI specification is several megabytes. Do not load it whole into context.

- If the `ed-fi-api-spec` skill is installed, use it to find the resource for a concept, its required fields,
  references and descriptor types.
- If an Ed-Fi spec lookup tool is available instead (for example the `search_endpoints` and
  `get_schema_details` tools of the original Ed-Fi SDK MCP server), use it.
- Otherwise fetch the specific resource's spec from `urls.openApiMetadata`, or ask the developer which
  resource they are working with.

## Generated SDKs

Instead of hand-writing request and model classes, a client can generate an SDK from the API's
OpenAPI metadata. Suggest it when the developer wants typed models for many resources. See
[references/sdk-generation.md](references/sdk-generation.md).

## Rules

All guidance in this skill follows a single set of numbered rules:
[references/rules.md](references/rules.md). Each rule has a level (*Required*, *Preferred*, *Allowed but
discouraged*), the reason, and how to detect it in code. The guides reference them by ID, e.g. `PUSH-3`.
The rules that apply to every integration:

- **DISC-1:** configure only the API root URL; take every other URL from the Discovery API.
- **AUTH-1 to AUTH-5:** Basic header for credentials, token reuse, one retry on `401`, no secrets in code or
  logs, HTTPS with certificate validation.
- **ERR-1 to ERR-4:** branch on the problem-details `type`, retry only `5xx`/`429`/network errors, log with
  `correlationId`, keep going past single-record failures.
- Push and pull have their own rules (`PUSH-*`, `PULL-*`), applied by the guides below.

When **writing** code, apply every *Required* and *Preferred* rule and never generate an *Allowed but
discouraged* pattern. When **reviewing** code, follow [references/review.md](references/review.md).

## Further reading

- [API Client Developers' Guide](https://docs.ed-fi.org/reference/ed-fi-api/client-developers-guide/)
- [Interacting with an Ed-Fi API tutorial](https://docs.ed-fi.org/reference/data-exchange/tutorial)
