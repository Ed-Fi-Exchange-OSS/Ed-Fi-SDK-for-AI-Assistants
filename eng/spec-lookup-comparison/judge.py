# SPDX-License-Identifier: Apache-2.0
# Licensed to the Ed-Fi Alliance under one or more agreements.
# The Ed-Fi Alliance licenses this file to you under the Apache License, Version 2.0.
# See the LICENSE and NOTICES files in the project root for more information.

"""First-pass scoring of the comparison runs with the correctness rubric, using Claude Code headless.

Usage:
    python judge.py <results-dir>

Writes <results-dir>/scores.jsonl, one line per run. This is a first pass only: review every score below 2 and
every open-ended task by hand, and record the final score as correctness_final in scores_final.json.
"""
import concurrent.futures as cf
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

RUBRIC = """You are scoring an answer from an AI coding assistant to an Ed-Fi API (Data Standard 5.2) lookup question.

Question: {prompt}
Expected answer (verified against the Ed-Fi specification): {expected}

Assistant's answer:
<<<
{answer}
>>>

Score it:
- correctness: 2 = correct and complete (names the expected resource(s)/fields; extra correct detail is fine);
  1 = partially correct (right resource but incomplete or partly wrong key/fields, or the right answer buried
  among wrong alternatives); 0 = wrong, missing, or only "I don't know".
- note: one short sentence explaining the score.

Reply with only a JSON object: {{"correctness": 0|1|2, "note": "<text>"}}"""


def judge(rec):
    prompt = RUBRIC.format(prompt=rec['prompt'], expected=rec['expected'], answer=rec['answer'][:12000])
    p = subprocess.run([shutil.which('claude') or 'claude', '-p', prompt, '--output-format', 'json',
                        '--no-session-persistence', '--strict-mcp-config', '--disallowedTools', 'Write', 'Edit', 'Bash',
                        'PowerShell', 'Read', 'Glob', 'Grep', 'WebFetch', 'WebSearch', 'Skill'],
                       cwd=tempfile.gettempdir(), capture_output=True, text=True, encoding='utf-8', timeout=600)
    text = json.loads(p.stdout).get('result', '') if p.stdout.strip().startswith('{') else p.stdout
    m = re.search(r'\{.*\}', text, re.S)
    score = json.loads(m.group(0)) if m else {'correctness': None, 'note': text[:200]}
    return {k: rec[k] for k in ('condition', 'task', 'group', 'kind', 'run')} | score


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    results = sys.argv[1]
    with open(os.path.join(results, 'runs.jsonl'), encoding='utf-8') as fh:
        runs = [json.loads(line) for line in fh]
    with open(os.path.join(results, 'scores.jsonl'), 'w', encoding='utf-8') as out, cf.ThreadPoolExecutor(6) as ex:
        for score in ex.map(judge, runs):
            out.write(json.dumps(score, ensure_ascii=False) + '\n')
            out.flush()
    print('scored', len(runs))


if __name__ == '__main__':
    main()
