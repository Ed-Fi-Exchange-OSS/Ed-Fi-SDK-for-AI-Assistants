# Licensed to the Ed-Fi Alliance under one or more agreements.
# The Ed-Fi Alliance licenses this file to you under the Apache License, Version 2.0.
# See the LICENSE and NOTICES files in the project root for more information.

<#
.SYNOPSIS
    Runs test prompts T12, T13 and T14 from docs/skills/api-client-test-prompts.md
    through Claude Code, one fresh session per prompt.

.DESCRIPTION
    Each prompt is passed to `claude -p` with an instruction to write its answer to
    {Prefix}-{T__}.md (for example, with-skill-T12.md). Run it once with the skill
    installed and once without, using a different prefix each time, then score the
    output files against the expected outcomes in the test prompts document.

.PARAMETER Prefix
    Prefix for the output file names, e.g. "with-skill" or "baseline".

.PARAMETER OutputDirectory
    Directory for the output files. Defaults to the current directory.

.EXAMPLE
    ./Invoke-UpgradeTestPrompts.ps1 -Prefix with-skill
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [ValidateNotNullOrEmpty()]
    [string] $Prefix,

    [string] $OutputDirectory = (Get-Location).Path
)

$ErrorActionPreference = 'Stop'

$prompts = [ordered]@{
    'T12' = 'We''re upgrading our Ed-Fi integration from Data Standard 4.0 to 5.0. What do we have to change in the records we send?'
    'T13' = 'We''re moving from Data Standard 5.0 to 5.1. Will our existing integration break, and what is new?'
    'T14' = 'Our SIS needs to report dual credit courses and assessment registrations. We are on Data Standard 5.1. What does 5.2 add, and does upgrading break anything?'
}

if (-not (Get-Command claude -ErrorAction SilentlyContinue)) {
    throw 'The claude CLI was not found on the PATH.'
}

if (-not (Test-Path $OutputDirectory)) {
    New-Item -ItemType Directory -Path $OutputDirectory | Out-Null
}
$OutputDirectory = (Resolve-Path $OutputDirectory).Path

foreach ($id in $prompts.Keys) {
    $outFile = Join-Path $OutputDirectory "$Prefix-$id.md"

    $fullPrompt = @"
$($prompts[$id])

Write your complete answer to the file '$outFile' in Markdown format. Do not write anything else to disk.
"@

    Write-Host "Running $id -> $outFile"

    # -p runs a single non-interactive session; acceptEdits lets it write the output file.
    & claude -p $fullPrompt --permission-mode acceptEdits
    if ($LASTEXITCODE -ne 0) {
        Write-Warning "claude exited with code $LASTEXITCODE for $id"
        continue
    }

    if (Test-Path $outFile) {
        Write-Host "  wrote $outFile"
    }
    else {
        Write-Warning "  $outFile was not created"
    }
}
