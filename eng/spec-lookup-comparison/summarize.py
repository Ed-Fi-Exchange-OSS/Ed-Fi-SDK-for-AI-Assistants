# SPDX-License-Identifier: Apache-2.0
# Licensed to the Ed-Fi Alliance under one or more agreements.
# The Ed-Fi Alliance licenses this file to you under the Apache License, Version 2.0.
# See the LICENSE and NOTICES files in the project root for more information.

"""Print the result tables of the spec lookup comparison as Markdown.

Usage:
    python summarize.py <results-dir>

Reads from <results-dir>:
  scores_final.json             one entry per run with correctness_final (after the manual review)
  third-runs/scores_final.json  optional; the third runs for task-condition pairs whose two runs disagree
  runs.jsonl                    steps and tokens
  unknown_names.json            optional; from verify_names.py

The score per task and condition follows the design: the two runs' score if they agree, otherwise the majority
of three runs (the middle score, which is also the result when all three differ).
"""
import collections
import json
import os
import sys

CONDITIONS = ('C0', 'C1', 'C2')
GROUPS = [
    ('All tasks', lambda t: True),
    ('Original', lambda t: t['group'] == 'original'),
    ('Original, natural language', lambda t: t['group'] == 'original' and t['kind'] == 'Natural language'),
    ('Held-out', lambda t: t['group'] == 'held-out'),
    ('Synonym sensitivity', lambda t: t['group'] == 'synonym'),
]


def load(path, default=None):
    if not os.path.exists(path):
        return default
    with open(path, encoding='utf-8') as fh:
        if path.endswith('.jsonl'):
            return [json.loads(line) for line in fh]
        return json.load(fh)


def table(header, rows):
    lines = ['| ' + ' | '.join(header) + ' |', '|' + '---|' * len(header)]
    return '\n'.join(lines + ['| ' + ' | '.join(str(c) for c in row) + ' |' for row in rows])


def ratio(got, best):
    return f'{got}/{best} ({100 * got / best:.0f}%)' if best else '-'


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    results = sys.argv[1]
    scores = load(os.path.join(results, 'scores_final.json'))
    third = {(s['condition'], s['task']): s['correctness_final']
             for s in load(os.path.join(results, 'third-runs', 'scores_final.json'), [])}
    runs = load(os.path.join(results, 'runs.jsonl'))
    unknown = load(os.path.join(results, 'unknown_names.json'), [])

    by_pair = collections.defaultdict(list)
    for s in scores:
        by_pair[(s['condition'], s['task'])].append(s)
    pairs = {}
    for key, entries in by_pair.items():
        values = [e['correctness_final'] for e in entries]
        if len(set(values)) > 1:
            if key not in third:
                sys.exit(f'{key[0]} {key[1]}: runs disagree ({values}) and there is no third run')
            values.append(third[key])
        pairs[key] = {'task': entries[0], 'score': sorted(values)[len(values) // 2]}

    print('## Correctness per task (majority rule)\n')
    rows = []
    for name, keep in GROUPS:
        cells = []
        for c in CONDITIONS:
            chosen = [p for (cond, _), p in pairs.items() if cond == c and keep(p['task'])]
            cells.append(ratio(sum(p['score'] for p in chosen), 2 * len(chosen)))
        rows.append([name] + cells)
    print(table(['Group'] + list(CONDITIONS), rows))

    print('\n## Correctness per answer\n')
    rows = []
    for name, keep in GROUPS:
        cells = []
        for c in CONDITIONS:
            chosen = [s for s in scores if s['condition'] == c and keep(s)]
            cells.append(ratio(sum(s['correctness_final'] for s in chosen), 2 * len(chosen)))
        rows.append([name] + cells)
    print(table(['Group'] + list(CONDITIONS), rows))

    print('\n## Invented names, cost and steps\n')
    per = {c: [r for r in runs if r['condition'] == c] for c in CONDITIONS}
    rows = []
    if unknown:
        rows.append(['Unknown identifiers'] + [
            f"{sum(len(u['unknown']) for u in unknown if u['condition'] == c)} of "
            f"{sum(u['checked'] for u in unknown if u['condition'] == c)}" for c in CONDITIONS])
        rows.append(['Runs with any'] + [
            f"{sum(bool(u['unknown']) for u in unknown if u['condition'] == c)}/{len(per[c])}" for c in CONDITIONS])
    rows.append(['Runs that used a tool'] + [f"{sum(r['steps'] > 0 for r in per[c])}/{len(per[c])}"
                                             for c in CONDITIONS])
    rows.append(['Steps per task (average)'] + [f"{sum(r['steps'] for r in per[c]) / len(per[c]):.1f}"
                                                for c in CONDITIONS])
    if any(r.get('input_tokens') for r in runs):
        rows.append(['Input tokens per task (average)'] + [
            f"~{sum(r.get('input_tokens', 0) for r in per[c]) / len(per[c]) / 1000:.0f} K" for c in CONDITIONS])
    print(table(['', *CONDITIONS], rows))


if __name__ == '__main__':
    main()
