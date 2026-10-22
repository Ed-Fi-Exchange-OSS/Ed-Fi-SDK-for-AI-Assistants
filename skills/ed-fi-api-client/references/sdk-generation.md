# Generating a client SDK from the OpenAPI metadata

Ed-Fi APIs publish OpenAPI documents, so a client can generate typed models and request classes
instead of writing them by hand. The Ed-Fi documentation uses
[OpenAPI Generator](https://openapi-generator.tech/), which supports C#, Java, Python, TypeScript and
many other languages.

## When to suggest it

- **Good fit:** the integration touches many resources, the team wants typed models, or the
  language has strong typing (C#, Java, TypeScript).
- **Not needed:** a script that reads or writes a few resources. Plain HTTP with the client design in
  [authentication.md](authentication.md#designing-the-client) is simpler.

## Which metadata document to generate from

Take the metadata base URL from `urls.openApiMetadata` in the Discovery API response. List the
available documents with:

```http
GET {urls.openApiMetadata}?sdk=true
```

| Document (relative to the metadata URL) | Contains |
|---|---|
| `data/v3/swagger.json` | Everything: core resources, descriptors and the host's extensions, in one package |
| `data/v3/ed-fi/swagger.json` | Core Ed-Fi resources and descriptors only |
| `data/v3/resources/swagger.json` | Resources only |
| `data/v3/descriptors/swagger.json` | Descriptors only |
| `composites/v1/ed-fi/enrollment/swagger.json` | Enrollment composites |
| `identity/v2/swagger.json` | Identity API, when the host enables it |

- The paths above are from ODS/API 7.3. On Ed-Fi API 8 the `v3` segment is removed from resource
  URLs, so list the documents with `?sdk=true` instead of assuming these paths.
- The documents are OpenAPI 3.0 by default. Append `?version=2` if the generator needs OpenAPI 2.0.
- Generate from **the host's own API**, not a public sandbox, when the host has extensions:
  extensions only appear in that host's metadata. Regenerate when the host adds or changes extensions.

## Command pattern

```text
openapi-generator-cli generate
    -g <language>                      # csharp, java, python, typescript-axios, ...
    -i <metadata URL of the document>
    -o <output folder>
    --api-package <namespace for API classes>
    --model-package <namespace for model classes>
    --skip-validate-spec
    --global-property modelTests=false,apiTests=false
```

- The Ed-Fi walkthrough generates C# (`-g csharp`) with OpenAPI Generator CLI 7.x, which needs Java
  (JDK 11 or later) to run. Use the generator's own options for package names in other languages.
- It skips spec validation (`--skip-validate-spec`) and the generated tests.
- When generating from several documents (resources, descriptors, composites), give each a different
  API and model package so names do not collide.

## What the generated SDK does not do

Generated code handles request building and serialization. It does **not** apply Ed-Fi rules, so
wrap it with the same logic as a hand-written client:

- Discovery, token reuse and the 401 retry: [authentication.md](authentication.md#designing-the-client).
  Check how the generated code accepts an access token and plug the token logic in there.
- Retries for 5xx and 429: [errors.md](errors.md#retry-policy).
- Reading `Location`, `ETag`, `Total-Count` and `Next-Page-Token`: make sure the generated call
  exposes response headers, not only the body.
- Dependency order, descriptors, paging and change queries: [push.md](push.md) and [pull.md](pull.md).

If the host assigns Profiles, check that the generator produced the Profile-specific content types;
otherwise requests fail with 403 (see [errors.md](errors.md#403-forbidden)).
