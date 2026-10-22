# SPDX-License-Identifier: Apache-2.0
# Licensed to the Ed-Fi Alliance under one or more agreements.
# The Ed-Fi Alliance licenses this file to you under the Apache License, Version 2.0.
# See the LICENSE and NOTICES files in the project root for more information.

"""Generate a Markdown knowledge graph from Ed-Fi Resources and Descriptors OpenAPI specs.

The output is the reference content of the ed-fi-api-spec skill: an index of resources, an index of
descriptor types, and one file per resource with its natural key, fields, references and endpoints.
It needs only the Python standard library.

Usage:
    python generate.py --resources <file-or-url> --descriptors <file-or-url> --out <dir>
                       [--synonyms synonyms.json] [--label "ODS/API 7.3, Data Standard 5.2"]

Point it at a host's own metadata (e.g. {urls.openApiMetadata}data/v3/resources/swagger.json) to include
that host's extensions.
"""
import argparse
import json
import os
import re
import shutil
import textwrap
import urllib.request

SKIP_FIELDS = {'id', '_etag', '_lastModifiedDate', 'link'}
OPERATIONS = ('get', 'post', 'put', 'delete')
LINE_LENGTH = 110  # .editorconfig max_line_length; tables are exempt
# Index files keep one line per entry, so a line search returns the whole entry.
ONE_LINE_NOTE = ('<!-- One line per entry, so a line search returns the whole entry. -->\n'
                 '<!-- markdownlint-disable MD013 -->')
BLOCK_START = re.compile(r'^([-+*>#|]|\d+[.)])(\s|$)')


def wrap(text):
    """Wrap prose and list-item lines at LINE_LENGTH; leave headings and table rows as they are."""
    out = []
    for line in text.split('\n'):
        if len(line) <= LINE_LENGTH or line.startswith(('|', '#')):
            out.append(line)
            continue
        indent = '  ' if line.startswith('- ') else ''
        lines = textwrap.wrap(line, LINE_LENGTH, subsequent_indent=indent,
                              break_long_words=False, break_on_hyphens=False)
        # A continuation line must not start with something Markdown reads as a block marker.
        for i in range(1, len(lines)):
            while BLOCK_START.match(lines[i].strip()) and ' ' in lines[i - 1].strip():
                head, last = lines[i - 1].rsplit(' ', 1)
                lines[i - 1], lines[i] = head, indent + last + ' ' + lines[i].strip()
        out.extend(lines)
    return '\n'.join(out)


def load(source):
    if re.match(r'https?://', source):
        # Some hosts reject Python's default User-Agent with 403.
        request = urllib.request.Request(source, headers={'User-Agent': 'ed-fi-spec-knowledge-graph'})
        with urllib.request.urlopen(request) as resp:  # noqa: S310 - URL supplied by the person running it
            return json.load(resp)
    with open(source, encoding='utf-8-sig') as fh:
        return json.load(fh)


def first_sentence(text, limit=160):
    text = re.sub(r'\s+', ' ', (text or '').strip())
    match = re.match(r'(.+?[.!?])(\s|$)', text)
    text = match.group(1) if match else text
    return text if len(text) <= limit else text[:limit - 1].rstrip() + '…'


def ref_name(ref):
    return ref.split('/')[-1]


def type_of(prop):
    if '$ref' in prop:
        return ref_name(prop['$ref'])
    if prop.get('type') == 'array':
        items = prop.get('items', {})
        return 'array of ' + (ref_name(items['$ref']) if '$ref' in items else items.get('type', '?'))
    text = prop.get('type', 'object')
    if prop.get('format'):
        text += f" ({prop['format']})"
    if prop.get('maxLength'):
        text += f" max {prop['maxLength']}"
    return text


def is_key(name, prop, required):
    return bool(prop.get('x-Ed-Fi-isIdentity')) or (
        name in required and name.endswith('Reference') and '$ref' in prop)


def field_rows(schema, schemas):
    required = set(schema.get('required', []))
    rows = []
    for name, prop in schema.get('properties', {}).items():
        if name in SKIP_FIELDS:
            continue
        if name.endswith('Descriptor'):
            kind = 'descriptor URI'
        elif name.endswith('Reference') and '$ref' in prop:
            keys = [k for k in schemas.get(ref_name(prop['$ref']), {}).get('properties', {}) if k != 'link']
            kind = 'reference: ' + ', '.join(f'`{k}`' for k in keys)
        else:
            kind = type_of(prop)
        if '$ref' in prop:
            description = schemas.get(ref_name(prop['$ref']), {}).get('description', '')
        else:
            description = prop.get('description', '')
        flag = 'key' if is_key(name, prop, required) else ('yes' if name in required else '')
        rows.append(f'| `{name}` | {flag} | {kind} | {first_sentence(description)} |')
    return rows


def resource_file(tag, description, operations, schemas, synonyms):
    collection = next((p for m, p, _ in operations if m == 'POST'), None) or next(
        (p for _, p, _ in operations if '{' not in p), operations[0][1])
    post = next((op for m, _, op in operations if m == 'POST'), None)
    lines = [f'# {tag}', '', f'`{collection}`', '', re.sub(r'\s+', ' ', description).strip(), '']
    if synonyms:
        lines += ['Also searched as: ' + ', '.join(synonyms) + '.', '']
    if post:
        schema = schemas[ref_name(post['requestBody']['content']['application/json']['schema']['$ref'])]
        required = set(schema.get('required', []))
        keys = [n for n, p in schema.get('properties', {}).items() if is_key(n, p, required)]
        updatable = any(op.get('x-Ed-Fi-isUpdatable') for m, _, op in operations if m == 'PUT')
        key_text = ', '.join(f'`{k}`' for k in keys) or '(none)'
        if updatable:
            key_text += '. The natural key can be changed with PUT (cascading key updates).'
        lines += ['## Natural key', '', key_text, '',
                  '_Derived from the OpenAPI metadata: identity fields plus required references. Reference '
                  'rows below list the key fields inside each reference._', '',
                  '## Fields', '', '`key` = part of the natural key, `yes` = required.', '',
                  '| Field | Required | Type | Description |', '|---|---|---|---|']
        lines += field_rows(schema, schemas)
        lines.append('')
    lines += ['## Endpoints', ''] + sorted({f'- `{m} {p}`' for m, p, _ in operations})
    return collection, wrap('\n'.join(lines)) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n', 1)[0])
    parser.add_argument('--resources', required=True)
    parser.add_argument('--descriptors', required=True)
    parser.add_argument('--out', required=True)
    parser.add_argument('--synonyms', default=os.path.join(os.path.dirname(__file__), 'synonyms.json'))
    parser.add_argument('--label', default='Data Standard 5.2')
    args = parser.parse_args()

    resources, descriptors = load(args.resources), load(args.descriptors)
    synonyms = {}
    if os.path.exists(args.synonyms):
        with open(args.synonyms, encoding='utf-8') as fh:
            for term, targets in json.load(fh).get('synonyms', {}).items():
                for target in targets:
                    synonyms.setdefault(target, []).append(term)

    out_resources = os.path.join(args.out, 'resources')
    if os.path.isdir(out_resources):
        shutil.rmtree(out_resources)
    os.makedirs(out_resources)

    schemas = resources['components']['schemas']
    tag_text = {t['name']: t.get('description', '') for t in resources.get('tags', [])}
    by_tag = {}
    for path, ops in resources['paths'].items():
        for method, op in ops.items():
            if method in OPERATIONS:
                for tag in op.get('tags', []):
                    by_tag.setdefault(tag, []).append((method.upper(), path, op))

    index = [ONE_LINE_NOTE, '', f'# Ed-Fi API resources ({args.label})', '',
             'One line per resource: name, collection path and description. Search this file for the '
             'term you need (try synonyms too), then open the linked file for keys, fields and endpoints. '
             'Descriptor types: [descriptors.md](descriptors.md).', '']
    for tag in sorted(by_tag):
        collection, text = resource_file(tag, tag_text.get(tag, ''), by_tag[tag], schemas, synonyms.get(tag))
        with open(os.path.join(out_resources, f'{tag}.md'), 'w', encoding='utf-8', newline='\n') as fh:
            fh.write(text)
        aka = f" Also: {', '.join(synonyms[tag])}." if tag in synonyms else ''
        index.append(f'- [{tag}](resources/{tag}.md) `{collection}`: '
                     f'{first_sentence(tag_text.get(tag), 140)}{aka}')
    with open(os.path.join(args.out, 'index.md'), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write('\n'.join(index) + '\n')

    descriptor_text = {t['name']: t.get('description', '') for t in descriptors.get('tags', [])}
    lines = [ONE_LINE_NOTE, '', f'# Ed-Fi descriptor types ({args.label})', '',
             'Every descriptor resource has the same shape: `namespace`, `codeValue`, `shortDescription`, '
             '`description` and optional effective dates. Values are data, not part of the spec: read them '
             'from the target API, e.g. `GET {dataManagementApi}ed-fi/gradeLevelDescriptors`.', '']
    for tag in sorted(descriptor_text):
        aka = f" Also: {', '.join(synonyms[tag])}." if tag in synonyms else ''
        lines.append(f'- `{tag}`: {first_sentence(descriptor_text[tag], 140)}{aka}')
    with open(os.path.join(args.out, 'descriptors.md'), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write('\n'.join(lines) + '\n')
    print(f'{len(by_tag)} resources, {len(descriptor_text)} descriptor types -> {args.out}')


if __name__ == '__main__':
    main()
