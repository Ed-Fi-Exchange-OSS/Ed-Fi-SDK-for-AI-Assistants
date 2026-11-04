---
name: ed-fi-oneroster-client
description: Guidance for writing, reviewing, or debugging code that reads rostering data from the Ed-Fi OneRoster API (edfi-oneroster), the service that serves 1EdTech OneRoster 1.2 Rostering from an Ed-Fi ODS. Covers getting a token from the ODS/API, OneRoster scopes, Discovery, paging and rate limits, the imsx error format, data freshness (scheduled refresh), and how OneRoster records map back to the Ed-Fi ODS/API to explain missing, empty, or duplicated results. Use whenever a task mentions OneRoster together with Ed-Fi or the ODS/API, /ims/oneroster/rostering/v1p2, roster.readonly scopes, or a rostering sync from an Ed-Fi ODS/API host.
---

# Ed-Fi OneRoster API Client

The [Ed-Fi OneRoster API](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) serves 1EdTech
**OneRoster 1.2 Rostering** from the data in an Ed-Fi ODS. It is a separate service next to the ODS/API
(7.3.2 and later), and it reads from views over the ODS (Data Standard 4.0, 5.1 and 5.2, and 6.1 in
recent pre-releases).

This skill covers how the **Ed-Fi OneRoster service** behaves. It does not teach the OneRoster standard;
follow the [OneRoster 1.2 specification](https://www.imsglobal.org/spec/oneroster/v1p2) for field meanings.
This skill targets the service running next to ODS/API 7.3.2 and later; OneRoster support for Ed-Fi API 8
has not been announced.

Several things differ from both a generic OneRoster provider and the ODS/API:

- Tokens come from the **ODS/API**, with the same key and secret. There is no separate OneRoster credential.
- It is **read-only Rostering**: no Gradebook, no Resources, no CSV, no POST/PUT/DELETE.
- Data is **refreshed on a schedule** the host sets (from every 15 minutes to once a day), not live.
- Errors use the OneRoster `imsx_*` body, not the ODS/API problem details.
- Users are **school-scoped**: a student at two schools appears twice.

## Step 1: Start from Discovery

Configure only the OneRoster root URL. A GET on it (no token needed) returns:

```json
{
  "version": "1.0.0",
  "urls": {
    "openApiMetadata": "https://oneroster.example.org/swagger.json",
    "swaggerUI": "https://oneroster.example.org/docs",
    "oauth": "https://api.example.org/v7.3/api/oauth/token",
    "dataManagementApi": "https://oneroster.example.org/ims/oneroster/rostering/v1p2/"
  }
}
```

- `urls.oauth` is the **ODS/API** token endpoint, built from the host's settings. On multi-tenant or
  multi-year hosts, check it against the ODS/API Discovery response
  ([references/authentication.md](references/authentication.md#getting-a-token)).
- `urls.dataManagementApi` is the base for every resource path (`users`, `classes`...).
- On multi-tenant or multi-year hosts, the root includes the tenant and context segments
  (`https://oneroster.example.org/grandbend/2026/`). Ask the host for them. Without them, Discovery returns
  URLs with placeholders; an unknown tenant or context returns `404`.
- `version` is a fixed string. Don't use it to detect features or the Data Standard version.

## Step 2: Authenticate through the ODS/API

Request a token from `urls.oauth` with the client credentials grant and the ODS/API key and secret, then send
`Authorization: Bearer <token>` to the OneRoster service. **Include a `scope` parameter** with the OneRoster
scope URIs the client needs, separated by spaces: a token requested without it carries no OneRoster scopes,
and every request gets `403`. This works only when the host has set the ODS/API
to issue JWT tokens for the OneRoster service; tell the developer so, since a `401` from OneRoster with a
token that works on the ODS/API is a host setting, not a client bug. The token rules of `ed-fi-api-client`
apply as written (AUTH-1 to AUTH-5): Basic header, reuse until near expiry, one retry on `401`, no secrets in
code.

Scopes, host setup that causes `401`/`403`, and empty results:
[references/authentication.md](references/authentication.md).

## Route to the right reference

| Situation | Read |
|---|---|
| Token, scopes, `401`, `403`, or `200` with empty collections | [references/authentication.md](references/authentication.md) |
| Listing resources, paging a full sync, filters, `429`, any error body | [references/requests-and-paging.md](references/requests-and-paging.md) |
| "I wrote it to the ODS/API, why isn't it here?", refresh schedule, incremental sync, deleting local records | [references/data-freshness.md](references/data-freshness.md) |
| Duplicated, missing or changed records; empty fields; which ODS/API data a record comes from | [references/mapping-to-ed-fi.md](references/mapping-to-ed-fi.md) |

## When to use `ed-fi-api-client` instead

Use the ODS/API (and the `ed-fi-api-client` skill, if installed) to **write** data, including grades and
attendance, or to read ODS/API data that OneRoster doesn't expose. Never generate requests to
`/ims/oneroster/gradebook/...` or `/ims/oneroster/resources/...` for this service; they don't exist.

## Rules for every OneRoster client

1. Take the token URL and the API base from Discovery; never hard-code `/oauth/token` on the OneRoster host.
2. Page until an **empty** page; don't rely on a total count or on the requested `limit` being honored.
3. Back off on `429` and keep one token for the whole run.
4. Read errors from `imsx_codeMajor` / `imsx_codeMinor` / `imsx_description`.
5. Never delete local records only because they are missing from one sync run.
6. Never put real keys, secrets or tokens in code, logs or examples.

## Further reading

- [OneRoster API (ODS/API 7.3 feature)](https://docs.ed-fi.org/reference/ods-api/platform-dev-guide/features/oneroster)
- [How To: Enable OneRoster with the Ed-Fi ODS/API](https://docs.ed-fi.org/reference/ed-fi-api/how-to-guides/how-to-oneroster-with-the-ed-fi-ods-api)
- [OneRoster data model (mapping from the ODS/API)](https://docs.ed-fi.org/reference/oneroster/data-model/)
