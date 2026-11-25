# SPDX-License-Identifier: Apache-2.0
# Licensed to the Ed-Fi Alliance under one or more agreements.
# The Ed-Fi Alliance licenses this file to you under the Apache License, Version 2.0.
# See the LICENSE and NOTICES files in the project root for more information.

"""Run the Extension Builder test prompts in Claude Code or the GitHub Copilot CLI, headless.

The prompts are read from docs/skills/extension-builder-test-prompts.md. Each run is a fresh, read-only
session in a work folder that holds the fixtures and, for the "with" condition, the ed-fi-extension-builder
skill taken from a git ref.

Usage:
    python run_prompts.py --out <dir> [--assistant claude|copilot] [--conditions with,without]
                          [--tasks T1,T2] [--skill-ref HEAD] [--model <name>] [--parallel 4]

Answers go to <out>/<assistant>/<condition>/<task>.md, and one line per run to <out>/runs.jsonl.
"""
import argparse
import concurrent.futures as cf
import io
import json
import os
import re
import shutil
import subprocess
import tarfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
PROMPTS = os.path.join(REPO, 'docs', 'skills', 'extension-builder-test-prompts.md')
FIXTURES = os.path.join(HERE, 'fixtures')
SKILL = 'ed-fi-extension-builder'
SKILLS_DIR = {'claude': '.claude', 'copilot': '.github'}
CLAUDE_DENIED = ['Write', 'Edit', 'Bash', 'PowerShell', 'NotebookEdit', 'WebSearch', 'WebFetch']
COPILOT_DENIED = ['shell', 'write']
COPILOT_EXCLUDED = ['web_fetch', 'web_search', 'semantic_code_search']
COPILOT_HIDDEN = {'report_intent', 'skill'}


def read_prompts(path=PROMPTS):
    """Return [{'id', 'title', 'prompt'}] from the '## Tn · title' sections and their '> ' prompt lines."""
    tasks, current, in_prompt, lines = [], None, False, []
    with open(path, encoding='utf-8') as fh:
        for raw in fh:
            line = raw.rstrip('\n')
            m = re.match(r'^## (T\d+) · (.+)$', line)
            if m:
                current = {'id': m.group(1), 'title': m.group(2)}
                tasks.append(current)
                in_prompt, lines = False, []
                continue
            if current is None:
                continue
            if line == '**Prompt:**':
                in_prompt = True
                continue
            if in_prompt:
                if line.startswith('>'):
                    lines.append(line[2:] if line.startswith('> ') else line[1:])
                elif lines:
                    current['prompt'] = '\n'.join(lines).strip()
                    in_prompt = False
    missing = [t['id'] for t in tasks if 'prompt' not in t]
    if missing:
        raise SystemExit(f'No prompt found for {", ".join(missing)} in {path}')
    return tasks


def setup(assistant, cond, args):
    work = os.path.join(args.out, 'work', f'{assistant}-{cond}')
    if os.path.exists(work):
        shutil.rmtree(work)
    shutil.copytree(FIXTURES, work)
    if cond == 'with':
        data = subprocess.run(['git', '-C', REPO, 'archive', args.skill_ref, f'skills/{SKILL}'],
                              capture_output=True, check=True).stdout
        with tarfile.open(fileobj=io.BytesIO(data)) as tar:
            tar.extractall(os.path.join(work, SKILLS_DIR[assistant]), filter='data')
    return work


def run_claude(prompt, work, model):
    cmd = [shutil.which('claude') or 'claude', '-p', prompt, '--output-format', 'stream-json', '--verbose',
           '--no-session-persistence', '--strict-mcp-config', '--disallowedTools'] + CLAUDE_DENIED
    if model:
        cmd += ['--model', model]
    p = subprocess.run(cmd, cwd=work, capture_output=True, text=True, encoding='utf-8', timeout=1200)
    tools, files, skills, answer, usage, used_model = [], [], [], '', {}, ''
    for line in p.stdout.splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if ev.get('type') == 'assistant':
            used_model = ev['message'].get('model', used_model)
            for c in ev['message'].get('content', []):
                if c.get('type') == 'tool_use':
                    tools.append(c['name'])
                    inp = c.get('input', {})
                    if c['name'] == 'Skill':
                        skills.append(inp.get('skill', ''))
                    if inp.get('file_path'):
                        files.append(os.path.relpath(inp['file_path'], work))
        if ev.get('type') == 'result':
            answer, usage = ev.get('result', ''), ev.get('usage', {})
    return {'tools': tools, 'files': files, 'skills_used': skills, 'answer': answer, 'exit_code': p.returncode,
            'model': used_model, 'output_tokens': usage.get('output_tokens', 0)}


def run_copilot(prompt, work, model):
    """Copilot CLI, JSONL output. The CLI doesn't report tokens."""
    cmd = [shutil.which('copilot') or 'copilot', '-p', prompt, '--output-format', 'json', '--no-ask-user',
           '--allow-all-tools', '--disable-builtin-mcps', '--no-auto-update'] + [
        f'--deny-tool={t}' for t in COPILOT_DENIED] + ['--excluded-tools'] + COPILOT_EXCLUDED
    if model:
        cmd += ['--model', model]
    p = subprocess.run(cmd, cwd=work, capture_output=True, text=True, encoding='utf-8', timeout=1200)
    tools, files, skills, answers, used_model = [], [], [], [], ''
    for line in p.stdout.splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        data = ev.get('data', {})
        if ev.get('type') == 'tool.execution_start':
            name, inp = data.get('toolName', ''), data.get('arguments') or {}
            if name == 'skill':
                skills.append(inp.get('skill', ''))
            if name not in COPILOT_HIDDEN:
                tools.append(name)
                if inp.get('path'):
                    files.append(os.path.relpath(inp['path'], work) if os.path.isabs(inp['path']) else inp['path'])
        if ev.get('type') == 'assistant.message' and data.get('content'):
            answers.append(data['content'])
            used_model = data.get('model', used_model)
    return {'tools': tools, 'files': files, 'skills_used': skills, 'answer': answers[-1] if answers else '',
            'exit_code': p.returncode, 'model': used_model}


def run(job):
    assistant, cond, task, work, args = job
    runner = run_copilot if assistant == 'copilot' else run_claude
    rec = {'assistant': assistant, 'condition': cond, 'task': task['id'], 'title': task['title'],
           'prompt': task['prompt']} | runner(task['prompt'], work, args.model)
    d = os.path.join(args.out, assistant, cond)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, f"{task['id']}.md"), 'w', encoding='utf-8') as fh:
        fh.write(f"# {task['id']} · {task['title']} · {assistant} · {cond} skill\n\n"
                 f"**Model:** {rec['model'] or 'default'}  \n"
                 f"**Skills used:** {', '.join(rec['skills_used']) or 'none'}  \n"
                 f"**Tools ({len(rec['tools'])}):** {', '.join(rec['tools']) or 'none'}  \n"
                 f"**Files:** {', '.join(rec['files']) or 'none'}\n\n## Answer\n\n{rec['answer']}\n")
    return rec


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--out', required=True)
    ap.add_argument('--assistant', choices=['claude', 'copilot'], default='claude')
    ap.add_argument('--conditions', default='with,without')
    ap.add_argument('--tasks', default='')
    ap.add_argument('--skill-ref', default='HEAD')
    ap.add_argument('--model', default='')
    ap.add_argument('--parallel', type=int, default=4)
    args = ap.parse_args()
    args.out = os.path.abspath(args.out)

    tasks = read_prompts()
    if args.tasks:
        wanted = set(args.tasks.split(','))
        tasks = [t for t in tasks if t['id'] in wanted]
    conds = args.conditions.split(',')
    jobs = []
    for cond in conds:
        work = setup(args.assistant, cond, args)
        jobs += [(args.assistant, cond, t, work, args) for t in tasks]

    with cf.ThreadPoolExecutor(max_workers=args.parallel) as pool, \
            open(os.path.join(args.out, 'runs.jsonl'), 'a', encoding='utf-8') as log:
        for rec in pool.map(run, jobs):
            log.write(json.dumps(rec, ensure_ascii=False) + '\n')
            log.flush()
            print(f"{rec['assistant']} {rec['condition']:7} {rec['task']:4} exit {rec['exit_code']} "
                  f"skills={','.join(rec['skills_used']) or '-'} tools={len(rec['tools'])}")


if __name__ == '__main__':
    main()
