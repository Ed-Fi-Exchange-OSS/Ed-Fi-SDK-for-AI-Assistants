# SPDX-License-Identifier: Apache-2.0
# Licensed to the Ed-Fi Alliance under one or more agreements.
# The Ed-Fi Alliance licenses this file to you under the Apache License, Version 2.0.
# See the LICENSE and NOTICES files in the project root for more information.

"""Run the spec lookup comparison tasks in Claude Code or the GitHub Copilot CLI, headless.

Conditions (design in docs/spec-lookup-analysis.md, section 6):
  C0  ed-fi-api-client skill only
  C1  C0 + the keyword-search MCP server from archived PR #30 (FTS5), built locally (see README)
  C2  C0 + the ed-fi-api-spec skill (option B)

Usage:
    python run_ab.py --out <dir> [--assistant claude|copilot] [--conditions C0,C1,C2] [--tasks Q01,H3,...]
                     [--runs 2] [--first-run 1] [--skill-ref HEAD] [--mcp-server <path to dist/index.js>]

Each run is a fresh session in a work folder that holds only the condition's skills. Results go to
<out>/<condition>/<task>-r<n>.md and <out>/runs.jsonl (one line per run, appended), with the answer, tool
calls, files read, and, for Claude Code, tokens and cost.
"""
import argparse
import concurrent.futures as cf
import io
import json
import os
import shutil
import subprocess
import sys
import tarfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
PREFIX = 'Ed-Fi API, Data Standard 5.2: '
MCP_NAME = 'ed-fi-data-standard'
SKILLS = {'C0': ['ed-fi-api-client'], 'C1': ['ed-fi-api-client'], 'C2': ['ed-fi-api-client', 'ed-fi-api-spec']}
SKILLS_DIR = {'claude': '.claude', 'copilot': '.github'}
CLAUDE_DENIED = ['Write', 'Edit', 'Bash', 'PowerShell', 'NotebookEdit', 'WebSearch']
COPILOT_DENIED = ['shell', 'write']
COPILOT_HIDDEN = {'report_intent', 'skill'}  # bookkeeping tools, not lookup steps


def extract_skills(ref, names, dest, assistant):
    """Copy skills/<name> from a git ref into dest/<.claude|.github>/skills/<name>."""
    data = subprocess.run(['git', '-C', REPO, 'archive', ref] + [f'skills/{n}' for n in names],
                          capture_output=True, check=True).stdout
    with tarfile.open(fileobj=io.BytesIO(data)) as tar:
        tar.extractall(os.path.join(dest, SKILLS_DIR[assistant]), filter='data')


def setup(cond, args):
    work = os.path.join(args.out, 'work', cond)
    if os.path.exists(work):
        shutil.rmtree(work)
    os.makedirs(work)
    extract_skills(args.skill_ref, SKILLS[cond], work, args.assistant)
    mcp = None
    if cond == 'C1':
        if not args.mcp_server:
            sys.exit('C1 needs --mcp-server (the built dist/index.js of archived PR #30; see README)')
        mcp = os.path.join(work, 'mcp.json')
        with open(mcp, 'w', encoding='utf-8') as fh:
            json.dump({'mcpServers': {MCP_NAME: {'command': 'node', 'args': [os.path.abspath(args.mcp_server)]}}}, fh)
    return work, mcp


def run_claude(task, work, mcp):
    cmd = [shutil.which('claude') or 'claude', '-p', PREFIX + task['prompt'], '--output-format', 'stream-json',
           '--verbose', '--no-session-persistence', '--disallowedTools'] + CLAUDE_DENIED + ['--strict-mcp-config']
    if mcp:
        cmd += ['--mcp-config', mcp, '--allowedTools', f'mcp__{MCP_NAME}']
    p = subprocess.run(cmd, cwd=work, capture_output=True, text=True, encoding='utf-8', timeout=1200)
    tools, files, answer, usage, cost = [], [], '', {}, 0
    for line in p.stdout.splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if ev.get('type') == 'assistant':
            for c in ev['message'].get('content', []):
                if c.get('type') == 'tool_use':
                    tools.append(c['name'])
                    if c.get('input', {}).get('file_path'):
                        files.append(os.path.basename(c['input']['file_path']))
        if ev.get('type') == 'result':
            answer, usage, cost = ev.get('result', ''), ev.get('usage', {}), ev.get('total_cost_usd', 0)
    tokens = sum(usage.get(k, 0) for k in ('input_tokens', 'cache_creation_input_tokens', 'cache_read_input_tokens'))
    return tools, files, answer, p.returncode, {'input_tokens': tokens, 'output_tokens': usage.get('output_tokens', 0),
                                                'cost_usd': cost}


def run_copilot(task, work, mcp):
    """Copilot CLI, JSONL output. The CLI doesn't report tokens or cost."""
    cmd = [shutil.which('copilot') or 'copilot', '-p', PREFIX + task['prompt'], '--output-format', 'json',
           '--no-ask-user', '--allow-all-tools', '--disable-builtin-mcps', '--no-auto-update'] + [
        f'--deny-tool={t}' for t in COPILOT_DENIED]
    if mcp:
        cmd += ['--additional-mcp-config', '@' + mcp]
    p = subprocess.run(cmd, cwd=work, capture_output=True, text=True, encoding='utf-8', timeout=1200)
    tools, files, answer, used, model = [], [], '', [], ''
    for line in p.stdout.splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        data = ev.get('data', {})
        if ev.get('type') == 'tool.execution_start':
            name, inp = data.get('toolName', ''), data.get('arguments') or {}
            if name == 'skill':
                used.append(inp.get('skill', ''))
            if name not in COPILOT_HIDDEN:
                tools.append(name)
                if inp.get('path'):
                    files.append(os.path.basename(inp['path']))
        if ev.get('type') == 'assistant.message' and data.get('content'):
            answer, model = data['content'], data.get('model', model)
    return tools, files, answer, p.returncode, {'skills_used': used, 'model': model}


def run(job):
    cond, task, n, work, mcp, args = job
    runner = run_copilot if args.assistant == 'copilot' else run_claude
    tools, files, answer, rc, extra = runner(task, work, mcp)
    rec = {'assistant': args.assistant, 'condition': cond, 'task': task['id'], 'group': task['group'],
           'kind': task['kind'], 'run': n, 'prompt': task['prompt'], 'expected': task['expected'], 'answer': answer,
           'tools': tools, 'steps': len(tools), 'files': files, 'exit_code': rc} | extra
    d = os.path.join(args.out, cond)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, f"{task['id']}-r{n}.md"), 'w', encoding='utf-8') as fh:
        fh.write(f"# {task['id']} · {cond} · run {n}\n\n**Prompt:** {task['prompt']}\n\n"
                 f"**Expected:** {task['expected']}\n\n**Tools ({len(tools)}):** {', '.join(tools) or 'none'}  \n"
                 f"**Files:** {', '.join(files) or 'none'}\n\n## Answer\n\n{answer}\n")
    return rec


def main():
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n', 1)[0])
    parser.add_argument('--out', required=True)
    parser.add_argument('--assistant', choices=['claude', 'copilot'], default='claude')
    parser.add_argument('--conditions', default='C0,C1,C2')
    parser.add_argument('--tasks', default='', help='comma-separated task IDs; all tasks if empty')
    parser.add_argument('--runs', type=int, default=2)
    parser.add_argument('--first-run', type=int, default=1, help='number of the first run, e.g. 3 for third runs')
    parser.add_argument('--skill-ref', default='HEAD', help='git ref to take the skills from')
    parser.add_argument('--mcp-server', help='path to the built FTS5 MCP server (dist/index.js), for C1')
    parser.add_argument('--workers', type=int, default=4)
    args = parser.parse_args()
    args.out = os.path.abspath(args.out)  # the MCP config path is read by a process running in the work folder
    sys.stdout.reconfigure(encoding='utf-8')

    with open(os.path.join(HERE, 'tasks.json'), encoding='utf-8') as fh:
        tasks = json.load(fh)
    if args.tasks:
        tasks = [t for t in tasks if t['id'] in args.tasks.split(',')]
    jobs = []
    for cond in args.conditions.split(','):
        work, mcp = setup(cond, args)
        jobs += [(cond, t, n, work, mcp, args) for t in tasks
                 for n in range(args.first_run, args.first_run + args.runs)]
    with open(os.path.join(args.out, 'runs.jsonl'), 'a', encoding='utf-8') as log, \
            cf.ThreadPoolExecutor(args.workers) as ex:
        for rec in ex.map(run, jobs):
            log.write(json.dumps(rec, ensure_ascii=False) + '\n')
            log.flush()
            print(f"{rec['condition']} {rec['task']:4} r{rec['run']} steps={rec['steps']:2} rc={rec['exit_code']}",
                  flush=True)


if __name__ == '__main__':
    main()
