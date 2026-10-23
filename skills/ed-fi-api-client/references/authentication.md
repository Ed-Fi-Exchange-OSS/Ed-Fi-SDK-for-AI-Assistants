# Authentication and token handling

## What the client needs

The API host provides:

- **Client key** (`client_id`) and **client secret** (`client_secret`). Store both in environment
  variables or a secret store, never in source code.
- **API root URL**, e.g. `https://api.example.org/v7.3/api`. Everything else comes from the
  [Discovery API](../SKILL.md#step-1-start-every-integration-from-the-discovery-api).

The key/secret pair is tied to a claim set and to one or more education organizations (or
namespaces). Those decide which resources and which records the client may read or write. A valid
token can still get `403` for data outside that scope. See [errors.md](errors.md#403-forbidden).

## Requesting a token

Rule: [AUTH-1](rules/auth.md).

Send the key and secret in an HTTP **Basic** `Authorization` header. This is the preferred method:

```http
POST {urls.oauth}
Authorization: Basic BASE64( urlencode(KEY) + ":" + urlencode(SECRET) )
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials
```

Build the header in this order (RFC 6749 §2.3.1):

1. **Form-urlencode** the key and the secret separately (`application/x-www-form-urlencoded` rules).
2. Join them with a colon: `encodedKey:encodedSecret`.
3. **Base64-encode** the result and send `Authorization: Basic <base64>`.

Many HTTP libraries' built-in "basic auth" helpers skip step 1. That works until a secret contains a
special character, then the token request fails with `401`. Ed-Fi API 8 secrets must contain at least
one special character, so do not skip the encoding, even if your current secret happens to be
alphanumeric.

### Credentials in the request body (allowed, not recommended)

ODS/API 7.x and Ed-Fi API 8.1 also accept the key and secret as form fields in the body
(`grant_type=client_credentials&client_id=…&client_secret=…`), for compatibility with older clients
and documentation examples. **Prefer the Basic header in new code:**

- Request bodies are more likely to be logged by proxies, gateways or debugging tools, which would
  expose the secret.
- The Basic header works on every version. Ed-Fi API 8.0 and early 8.1 pre-releases (such as
  `8.1.0-beta1`) reject body credentials with `400` "Malformed Authorization header".

When reviewing existing code, flag this pattern as a recommended change, not a defect.

A successful response:

```json
{ "access_token": "…", "expires_in": 1800, "token_type": "bearer" }
```

Then send the token on every request:

```http
GET {urls.dataManagementApi}ed-fi/students
Authorization: Bearer ACCESS_TOKEN
```

## Token lifecycle rules

Rules: [AUTH-2, AUTH-3](rules/auth.md).

1. **Reuse the token.** Request a new one only when the current one is about to expire. Requesting a
   token per call is slow and can trip host rate limits.
2. **Use `expires_in` from the response.** Do not assume a fixed lifetime; it is configured by the
   host. Renew a little early to avoid in-flight expiry, with a margin bounded by the lifetime
   (e.g. 60 seconds, or a tenth of `expires_in` if that is shorter), so short-lived tokens are still
   reused.
3. **There is no refresh token.** "Refreshing" means repeating the client-credentials request.
4. **On `401`, re-authenticate once and retry the request once.** If it fails again, stop: the
   credentials are wrong, revoked, or for a different API instance.
5. **Share one token across concurrent workers** in the same process, and make sure only one worker
   renews it at a time.

## Designing the client

Whatever the language, a well-behaved Ed-Fi client wraps every call in the same logic:

```text
discover():
    if urls are cached: return them
    GET rootUrl
    fail clearly if urls.oauth or urls.dataManagementApi is missing
    make urls.dataManagementApi end in "/"                           # Ed-Fi API 8 omits it
    cache urls

authenticate():
    if a renewal is already in progress: wait for it and return     # one renewal at a time
    basic = base64(urlencode(key) + ":" + urlencode(secret))
    POST urls.oauth with header Authorization: Basic <basic>
         and form body grant_type=client_credentials
    on failure: raise an error that includes error_description from the response
    token     = access_token
    expiresAt = now + expires_in - min(60 seconds, expires_in / 10) # renew early

request(method, path, body, headers, query):
    discover()
    if no token or now >= expiresAt: authenticate()
    send method to urls.dataManagementApi + path (without its leading "/")
         with Authorization: Bearer <token>, Content-Type: application/json
    if status is 401:
        authenticate()                                              # once
        send again
    return the full response (status, headers, body)
```

- Return the full response, not just the body: callers need headers such as `Location`, `ETag`,
  `Total-Count` and `Next-Page-Token`.
- Read the root URL, key and secret from configuration (environment variables or a secret store).
- Reuse one HTTP connection pool / client instance for all requests.
- Put retries for 5xx, 429 and network errors around `request()`; see
  [errors.md](errors.md#retry-policy).

Write this in the developer's language and HTTP library. A JavaScript example of this design is in
[examples/javascript-client.md](examples/javascript-client.md).

## Troubleshooting authentication

| Symptom | Likely cause |
|---|---|
| `400`/`401` from the token endpoint with `invalid_client` | Wrong key or secret; credentials created for a different API instance or tenant; or, with a Basic header, the key and secret were not form-urlencoded before base64 encoding (check: did you urlencode? did you base64-encode the joined `key:secret`?) |
| Token works, every resource call returns `401` | Token sent to a different API instance than the one that issued it, or header not formatted `Bearer <token>` |
| Token works, some calls return `403` | Claim set or education organization scope; see [errors.md](errors.md#403-forbidden) |
| TLS or certificate errors | Fix certificate trust (e.g. trust a local self-signed certificate). Only for local testing, switch validation off behind an explicit, off-by-default setting; never permanently ([AUTH-5](rules/auth.md)) |
