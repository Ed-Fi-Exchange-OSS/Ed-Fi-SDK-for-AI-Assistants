# Spec knowledge graph generator

Generates the reference content of the [`ed-fi-api-spec`](../../skills/ed-fi-api-spec/SKILL.md) skill from
the Ed-Fi Resources and Descriptors OpenAPI specifications: `index.md`, `descriptors.md` and one Markdown file
per resource. This is approach B in [ADR 0001](../../docs/adr/0001-api-spec-similarity-search.md) and the
[spec lookup analysis](../../docs/spec-lookup-analysis.md).

Requires Python 3.9 or later; standard library only.

## Regenerate the skill content

```bash
python eng/spec-knowledge-graph/generate.py \
  --resources https://api.ed-fi.org/v7.3/api/metadata/data/v3/resources/swagger.json \
  --descriptors https://api.ed-fi.org/v7.3/api/metadata/data/v3/descriptors/swagger.json \
  --out skills/ed-fi-api-spec/references \
  --label "ODS/API 7.3, Data Standard 5.2"
```

`--resources` and `--descriptors` accept an `https` URL or a local file. The output folder's `resources/`
directory is replaced on each run.

Each resource file lists the natural key, the fields with their required flags, the fields to supply in each
reference, and the fields of nested collections (one level). The natural key comes from the collection GET's
query parameters marked `x-Ed-Fi-isIdentity`, which flatten references into their fields. The request schemas
can't be used for this: they mark identity on scalar fields only, so a required reference may or may not be
part of a record's identity.

Resource files are wrapped at 110 characters, like the rest of the repository. `index.md` and `descriptors.md`
keep one line per entry, so searching them for a term returns the whole entry; they turn off the line-length
lint rule for that reason.

## Test the generator

`test_generate.py` runs the generator on a small fixture specification, with no network access:

```bash
python -m unittest discover -s eng/spec-knowledge-graph
```

## Include a host's extensions

Extensions only appear in the metadata of the host that has them. Point the generator at that host's metadata
(listed by `GET {urls.openApiMetadata}?sdk=true`) and write the output to the developer's own copy of the skill:

```bash
python eng/spec-knowledge-graph/generate.py \
  --resources https://<host>/<path>/metadata/data/v3/resources/swagger.json \
  --descriptors https://<host>/<path>/metadata/data/v3/descriptors/swagger.json \
  --out <installed skill folder>/references \
  --label "<host name>, Data Standard 5.2 with extensions"
```

## Synonyms

[`synonyms.json`](synonyms.json) maps common developer terms that don't appear in Ed-Fi resource names or
descriptions (for example "enrollment" or "parent") to the resources they should lead to. The generator adds
them to the index lines ("Also: …") and to each resource file. Add an entry when a lookup test shows a miss.
