# SPDX-License-Identifier: Apache-2.0
# Licensed to the Ed-Fi Alliance under one or more agreements.
# The Ed-Fi Alliance licenses this file to you under the Apache License, Version 2.0.
# See the LICENSE and NOTICES files in the project root for more information.

"""Count Ed-Fi-style identifiers in the answers that don't exist in the Resources and Descriptors specs.

Usage:
    python verify_names.py --resources <file> --descriptors <file> <results-dir>

Writes <results-dir>/unknown_names.json. Only camelCase identifiers in backticks are checked, so the count is an
upper bound: it includes older Data Standard names that an answer flags as such, and a few false positives.
"""
import argparse
import collections
import json
import os
import re
import sys

IDENTIFIER = re.compile(r'`([A-Za-z][A-Za-z0-9]*(?:/[A-Za-z][A-Za-z0-9]*)*)`')
GENERIC = {'id', 'limit', 'offset', 'true', 'false', 'null', 'link', 'data', 'json', 'namespace', 'codeValue',
           'shortDescription', 'description', 'pageToken', 'pageSize', 'totalCount', 'minChangeVersion',
           'maxChangeVersion', 'deletes', 'keyChanges', 'partitions', 'etag'}


def spec_names(paths):
    names = set()
    for path in paths:
        with open(path, encoding='utf-8') as fh:
            spec = json.load(fh)
        for route, ops in spec['paths'].items():
            names.update(seg for seg in route.split('/') if seg and not seg.startswith('{'))
            for op in ops.values():
                if isinstance(op, dict):
                    names.update(prm.get('name', '') for prm in op.get('parameters', []))
        names.update(t['name'] for t in spec.get('tags', []))
        components = spec.get('components', {})
        for schema_name, schema in components.get('schemas', {}).items():
            names.add(schema_name.split('_', 1)[-1])
            names.update(schema.get('properties', {}).keys())
        names.update(prm.get('name', '') for prm in components.get('parameters', {}).values())
    return {n.lower() for n in names if n}


def known(token, names):
    t = token.lower()
    candidates = {t, t + 's', t.rstrip('s'), t + 'es', t[:-3] + 'y' if t.endswith('ies') else t}
    if t.endswith('reference'):
        candidates.add(t[:-len('reference')])
    return any(c in names for c in candidates)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n', 1)[0])
    parser.add_argument('--resources', required=True)
    parser.add_argument('--descriptors', required=True)
    parser.add_argument('results')
    args = parser.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    names = spec_names([args.resources, args.descriptors])

    out = []
    with open(os.path.join(args.results, 'runs.jsonl'), encoding='utf-8') as fh:
        for line in fh:
            run = json.loads(line)
            tokens = {part for m in IDENTIFIER.findall(run['answer']) for part in m.split('/')
                      if len(part) > 4 and part not in GENERIC and part[0].islower()
                      and re.search(r'[a-z][A-Z]|^[a-z]+$', part)}
            unknown = sorted(t for t in tokens if not known(t, names))
            out.append({'condition': run['condition'], 'task': run['task'], 'run': run['run'], 'unknown': unknown,
                        'checked': len(tokens)})
    with open(os.path.join(args.results, 'unknown_names.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1)

    totals = collections.defaultdict(lambda: [0, 0, 0, 0])
    for o in out:
        t = totals[o['condition']]
        t[0] += len(o['unknown'])
        t[1] += o['checked']
        t[2] += bool(o['unknown'])
        t[3] += 1
    for cond, (unknown, checked, with_any, runs) in sorted(totals.items()):
        print(f'{cond}: {unknown} unknown of {checked} checked; runs with any: {with_any}/{runs}')


if __name__ == '__main__':
    main()
