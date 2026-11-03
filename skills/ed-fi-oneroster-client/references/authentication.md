# Authentication and authorization

How a client gets access to the Ed-Fi OneRoster API, and what to check when access fails. Part of the
[ed-fi-oneroster-client](../SKILL.md) skill.

## Getting a token

The OneRoster service doesn't issue tokens. It accepts **JWT access tokens issued by the ODS/API**:

1. Take the token URL from `urls.oauth` in the OneRoster Discovery response. The service builds it from the
   issuer URL the host configured, so on multi-tenant or multi-year hosts compare it with `urls.oauth` in the
   ODS/API Discovery response; if they differ, use the ODS/API one.
2. POST `grant_type=client_credentials` with the ODS/API key and secret in a Basic `Authorization` header
   (form-urlencode each, join with `:`, base64). If `ed-fi-api-client` is installed, follow its
   [authentication guide](https://github.com/Ed-Fi-Exchange-OSS/Ed-Fi-SDK-for-AI-Assistants/blob/main/skills/ed-fi-api-client/references/authentication.md);
   the rules are the same.
3. Send `Authorization: Bearer <access_token>` on every OneRoster request. Reuse the token until it is about to
   expire (`expires_in`); there is no refresh token.

```http
POST https://api.example.org/v7.3/api/oauth/token
Authorization: Basic BASE64(urlencode(YOUR_KEY):urlencode(YOUR_SECRET))
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials
```

### Don't post credentials to the OneRoster host

The OneRoster service answers `/oauth/token` with a `307` redirect to the issuer's `/oauth/token`, always
without the tenant or school-year segments. Some HTTP clients drop the POST body or the `Authorization` header
when they follow a redirect to another host, and on multi-tenant or multi-year hosts the redirect can point to
the wrong token endpoint. Call the ODS/API token URL directly.

## Host setup the client depends on

These are set by the API host, not in client code. When they are wrong, the client can't fix them; tell the
developer what to ask the host.

| Symptom | Likely cause on the host |
|---|---|
| `401` "Invalid or expired token" on every request, but the same token works on the ODS/API | The ODS/API issues GUID tokens instead of JWT (`Security:AccessTokenType` must be `jwt`); or the JWT's audience, issuer or signing key doesn't match the OneRoster service's settings |
| `401` "Not authorized to access the requested resource" on a multi-tenant or multi-year host | The URL's tenant or school year isn't one the token is for. Check the segments in the URL; the token carries its tenant and ODS instances |
| `403` with "Insufficient scope" | The API client's permissions don't include the OneRoster scope for that endpoint |
| `403` with `imsx_codeMinor` `forbidden` | Internal authorization error in the service; report it to the host with the URL and time |
| `404` "The specified data could not be found" on every data endpoint | The token has no ODS instance the service can resolve; ask the host to check the API client's ODS instance |
| `200` with empty arrays on every collection | The API client has no education organizations associated |
| `431`, `400` or a dropped connection for a client with access to many education organizations | The token is very large (thousands of education organization IDs) and exceeds header size limits |

A `401` with "Missing or invalid Authorization header" means the request itself has no `Bearer` token; that is
a client bug.

## Scopes

The service checks OneRoster 1.2 scopes in the token's `scope` claim. Each scope is a full URI:

| Endpoints | Scope required (any one) |
|---|---|
| Every rostering endpoint except demographics | `https://purl.imsglobal.org/spec/or/v1p2/scope/roster.readonly` or `https://purl.imsglobal.org/spec/or/v1p2/scope/roster-core.readonly` |
| `/demographics` | `https://purl.imsglobal.org/spec/or/v1p2/scope/roster-demographics.readonly` |

- `roster.readonly` does **not** include demographics, by design in OneRoster 1.2. A token with only
  `roster.readonly` gets `403` on `/demographics` and `200` everywhere else.
- A missing scope is a permissions problem. Retrying or getting a new token doesn't help.
- How a client gets the scopes into its token depends on the host's ODS/API configuration. Ask the host
  whether the token request must include a `scope` parameter; the Ed-Fi documentation doesn't say.

## Empty or partial results with a valid token

The service filters every query by the **education organization IDs in the token**. A token with none
returns `200` with empty collections, not an error, and `404` for single records. When "the token works but
everything is empty":

1. Ask the host to associate the API client with the right education organizations in the ODS/API.
2. If the host was just deployed or the data was just loaded, wait for the next refresh
   ([data-freshness.md](data-freshness.md)).
3. Check the tenant and context segments in the URL; a wrong school year points to another ODS.

With a school-level token, the school's own `orgs` record is visible but its district and state are not, so
following a school's `parent` reference can return `404`. Some records can also be missing for scoped tokens
when the host's descriptor mapping is incomplete ([mapping-to-ed-fi.md](mapping-to-ed-fi.md)).
