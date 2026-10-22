# API Client skill: draft review notes

Working notes for the first draft of `skills/ed-fi-api-client`. Not part of the skill itself.

## Repository changes (2026-10-20)

Stephen moved the original MCP server to `sdk-as-mcp/` (tag `original-sdk-as-mcp-server`) and added
`.editorconfig` (4-space indent, max line length 110; Markdown keeps trailing whitespace). The PRD draft
(`docs/prd.md`, branch `PRD`) defines the scope; this skill maps to FR-BASE, FR-PUSH and FR-PULL.

## Sources

- MCP prompts in `sdk-as-mcp/src/index.ts`: `getAuthenticationGuideContent()`, `getQuickStartGuideContent()` and
  `getDataValidationGuideContent()`. `getHelpAndUsageGuideContent()` is about the MCP server and was not used.
- Ed-Fi API Client Developers' Guide (to be cross-checked during normative review).

## Structure

| File | Content |
|---|---|
| `SKILL.md` | Discovery API, URL structure (tenant/context/schema, `_ext`, composites), auth summary, push/pull routing question, generated SDKs, rules for every integration (incl. dates), spec lookup guidance |
| `references/authentication.md` | Token request, token lifecycle rules, language-neutral client design, auth troubleshooting |
| `references/push.md` | Dependency order, POST upsert, PUT/DELETE by `id`, references, descriptors, ETags, throughput |
| `references/pull.md` | Paging, filtering, change queries, `/deletes`, `/keyChanges`, snapshots, sync algorithm |
| `references/errors.md` | Problem details format, status code table, 400/401/403/404/409/412 explained, retry policy |
| `references/sdk-generation.md` | Generating a client SDK with OpenAPI Generator: which metadata document, command pattern, what the SDK does not handle |
| `references/examples/javascript-client.md` | Optional JavaScript illustration of the client design, retry wrapper and failure logging |

## Corrections made to the MCP prompt content

| MCP content | Problem | Skill |
|---|---|---|
| PUT/DELETE examples use `/ed-fi/students/12345` (`sdk-as-mcp/src/index.ts:1014`, `:1033`) | Natural key in the URL; must be the resource `id` | Uses `{id}`, explains how to get it, flags the mistake under 404 |
| "409: Conflict (duplicate key)" (`sdk-as-mcp/src/index.ts:1098`) | POST of an existing key is an upsert (200). 409 is a missing reference, existing dependents, or a uniqueness conflict | Dedicated 409 section in `errors.md` |
| "Access tokens typically expire in 1 hour, implement refresh logic" (`:800`) | Lifetime is host-configured; there is no refresh token | Use `expires_in`, renew early, re-authenticate |
| "Rate limiting… typically 100 requests/minute" (`:941`) | No basis in the API | Removed; 429 handled generically with `Retry-After` |
| Hard-coded descriptor allow-list (`:1191`) | Descriptor values vary by state/district namespace | Read values from descriptor endpoints |
| 401 retry not guarded against concurrent renewal | Token stampede under parallel load | Reference client collapses concurrent renewals |
| "Get students with filtering: `?schoolId=123`" (`:980`) | `students` has no `schoolId` property | Filtering example uses `studentSchoolAssociations` |

## New content not in the MCP

Change queries, `/deletes`, `/keyChanges`, snapshots, `Total-Count`, POST-as-upsert, ETag / `If-Match` / 412,
403 claim set vs. education organization vs. namespace, 404 / 405 / 413 / 429, sync algorithm,
failure logging.

## Former [VERIFY] items: resolved from the Ed-Fi documentation (2026-10-19)

| Item | Resolution | Source |
|---|---|---|
| Resources that allow natural-key changes via PUT | As shipped in ODS/API 7.x: Class Period, Grade, GradebookEntry, Location, Section, Session, Student School Association, Student Section Association. Hosts can enable more (source install). | [Cascading Key Updates](https://docs.ed-fi.org/reference/ed-fi-api/technical-articles/cascading-key-updates-on-ods-api-resources) |
| Cursor paging | ODS/API 7.3+: `pageSize`/`pageToken`, `Next-Page-Token` header, `/partitions?number=` (default up to 10). Not combinable with `limit`/`offset` or `totalCount`. | [Partitioned Cursor Paging](https://docs.ed-fi.org/reference/ed-fi-api/client-developers-guide/improve-paging-performance-cursor-paging) |
| Snapshot header and detection | ODS/API 7.x: `Use-Snapshot: true`; `404 Snapshot Not Found` if not configured. Ed-Fi API 8.0: no snapshot support. | [Changed Record Queries (7.3)](https://docs.ed-fi.org/reference/ed-fi-api/client-developers-guide/using-the-changed-record-queries), [Changed Record Queries (v8)](https://docs.ed-fi.org/reference/ed-fi-api/8/platform-dev-guide/features/changed-record-queries) |
| 409 `type` URNs | `urn:ed-fi:api:data-conflict:unresolved-reference`, `...:dependent-item-exists`, `...:non-unique-identity`. Also documented: 412 `urn:ed-fi:api:optimistic-lock-failed` and the 403 sub-types. | [Error Response Knowledge Base](https://docs.ed-fi.org/reference/ed-fi-api/client-developers-guide/error-response-knowledge-base) |

Corrections made while resolving them:

- Sync algorithm now processes **key changes first**, then changes, then deletes (reverse order), per the guide.
- ETag / `If-Match` / 412 described as depending on the host enabling the ETag feature.
- 403 section rewritten around the documented `type` sub-types.

## Token request: Basic header preferred (Stephen, Slack 2026-10-20)

- **Basic `Authorization` header is the only method the skill encourages.** Credentials in the body are accepted by
  Ed-Fi API 8 (recently added for ODS/API compatibility, allowed by OAuth 2.0), but bodies are more likely to be logged.
  Build guidance: Basic only. Review guidance: body is allowed, but flag it as a recommended change. This is the first
  concrete case of "build" and "review" applying the same rule differently (see the rules + two interfaces design).
- **RFC 6749 §2.3.1:** form-urlencode `client_id` and `client_secret` before joining with `:` and base64-encoding.
  Covered for build (authentication.md), review (same section) and debugging (errors.md 401, auth troubleshooting).
- **Do Ed-Fi secrets contain special characters?** Checked in source code:
  - ODS/API (`Ed-Fi-ODS`, `EdFi.Admin.DataAccess/Models/ApiClient.cs`, main and v7.3): generated secrets are 24 characters
    of base64 with `+` and `/` rejected and no padding, so **alphanumeric only**. Encoding is a no-op for generated
    secrets, but secrets can also be set manually in `EdFi_Admin`.
  - Ed-Fi API 8 / DMS Configuration Service (`ClientSecretValidation`): secrets **must** include a special character
    from `!@#$%^&*()-_=+[]{}:;,.?`. Generated secrets exclude `+ % = & space` ("transport unsafe") but can include
    `: ; , ? [ ] { } ( ) ! @ # $ ^ *`. User-supplied secrets may include all of them.
  - Conclusion: encoding matters for Ed-Fi API 8 and for any manually set secret, so the skill always requires it.

## Coverage against the Client Developers' Guide (2026-10-19)

Scope = the Client Developers' Guide (Stephen: "bundling up the Client Developers' Guide as Agent Skills").
Sections added after comparing with its index:

- **API Routes** → `SKILL.md` "How Ed-Fi URLs are built" ([source](https://docs.ed-fi.org/reference/ed-fi-api/client-developers-guide/api-routes))
- **Date & DateTime Elements** → `push.md` §6, `pull.md` §5, rule 6 in `SKILL.md` ([source](https://docs.ed-fi.org/reference/ed-fi-api/client-developers-guide/date-datetime-elements))
- **Using Code Generation to Create an SDK** → `references/sdk-generation.md` ([source](https://docs.ed-fi.org/reference/ed-fi-api/client-developers-guide/using-code-generation-to-create-an-sdk))

Not covered on purpose: Profiles and bulk loading tools (not in the guide; the skill only covers the Profile 403 and
points to bulk tools), and "Using the Sandbox Administration Portal" (sandbox-specific). "Basics" and "Using the
Online Documentation" are covered only partially; review them before the release.

## Confirmed on Ed-Fi API 8 (pilot test kit, 2026-10-22)

Checked against the Ed-Fi API v8 pilot test kit (Discovery reports `8.1.0-beta1`, Data Standard 5.2); details in
[api-client-test-results.md](api-client-test-results.md#ed-fi-api-8-verification--pilot-test-kit--2026-10-22).

1. **Cursor paging:** supported, but every request needs a `pageToken`; `pageSize` alone gets `400`. `/partitions`
   works. Fixed in `pull.md` and PULL-2.
2. **Cascading key updates:** work (StudentSchoolAssociation `entryDate`); Student returns `400`
   `key-change-not-supported`. Fixed in `push.md` and `SKILL.md`.
3. **`/deletes` and `/keyChanges`:** same fields as ODS/API 7.x; offset paging only; need `ReadChanges`. Added to `pull.md`.
4. **Discovery `urls`:** `dependencies`, `openApiMetadata`, `oauth`, `tokenInfo`, `dataManagementApi`, `changeQueries`,
   `xsdMetadata`; no `v3` segment. Confirmed.
5. **Error `type` values:** 409 `unresolved-reference` / `dependent-item-exists`, 403 `access-denied:action` and
   relationship `security:authorization`, 412 `optimistic-lock-failed` match. Confirmed.
6. **Not verified:** tenant and context segments (the kit runs single-tenant) and the `?sdk=true` metadata listing.
7. **Found during the check:** body credentials are rejected (`400` "Malformed Authorization header"), and
   wrong-case or unknown properties are silently ignored rather than rejected. Both added to `SKILL.md`,
   `authentication.md` and AUTH-1.

> Note: Stephen said client guidance is "the same for ODS/API 7 and Ed-Fi API 8"; the v8 release notes say
> "client migration is required". The resource behavior is the same, but URLs, casing and token endpoint differ.
> Worth mentioning in the PR description.

## Open questions

- **Code languages (decided 2026-10-19):** the skill is language-neutral. Rules, HTTP examples and
  pseudocode let the assistant write correct code in the developer's own language. The JavaScript
  client from the MCP was kept as an optional example in `references/examples/`, so it does not bias
  the assistant toward JavaScript. Raise in the PR description in case the Alliance wants
  per-language examples (US005/US010 in `sdk-as-mcp/docs/requirements/user-stories.md`).
- **Where skills live:** `skills/` at the repo root for now. Does the Alliance want a different layout or a
  plugin/marketplace manifest?
- **Domain overlay:** performance evaluations (IIA) as the first domain-specific add-on, after the generic skill.

## Testing plan

1. Load the skill in Claude Code and in Codex.
2. Run the same prompts with and without the skill and compare, e.g.:
   - "Write a Node script that loads students and their school enrollments into Ed-Fi."
   - "Write a nightly job that syncs Ed-Fi sections into our warehouse."
   - "I got this 409 when posting a studentSchoolAssociation: `<body>`. What's wrong?"
   - "Update student 604822's last name."  (should look up the `id`, not PUT to `/students/604822`)
3. Run the generated code against a local Ed-Fi API 8 + Data Standard 5.2 instance (pilot test kit).
