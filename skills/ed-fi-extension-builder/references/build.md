# Building with the MetaEd command line

The MetaEd build checks the `.metaed` files and generates `ApiSchema-EXTENSION.json`. The how-to guides use
the Build button of the MetaEd IDE in VS Code; the same build runs from the command line with
`@edfi/metaed-console`, which lets the assistant run it and read the errors. Source:
[MetaEd for Continuous Integration](https://docs.ed-fi.org/reference/metaed/metaed-for-continuous-integration).
Tested with MetaEd 4.9.0, the Data Standard 5.2 model package 3.0.1 and Node.js 22.

## Set up once

Use a folder of its own for the build tools (here `metaed-build/`), not the extension project. It needs
Node.js and npm. The packages come from the Ed-Fi package feed, which needs no credentials. Create
`metaed-build/.npmrc` with:

```text
@edfi:registry=https://pkgs.dev.azure.com/ed-fi-alliance/Ed-Fi-Alliance-OSS/_packaging/EdFi/npm/registry/
```

Then, in `metaed-build/`:

```bash
npm init -y
npm install --save-exact @edfi/metaed-console@4.9.0 @edfi/ed-fi-model-5.2@3.0.1
```

`@edfi/ed-fi-model-5.2` is the core Data Standard 5.2 model the extension builds on. If the feed isn't
reachable (a proxy, an offline machine), say so and fall back to the Build button in the MetaEd IDE.

## The config file

Create `metaed-build/metaed-config.json`. Replace the extension's path and `projectName`:

```json
{
  "metaEdConfiguration": {
    "artifactDirectory": "./MetaEdOutput",
    "deployDirectory": "",
    "pluginTechVersion": {},
    "projects": [
      { "namespaceName": "EdFi", "projectName": "Ed-Fi", "projectVersion": "5.2.0",
        "projectExtension": "", "description": "The Ed-Fi Data Model 5.2" },
      { "namespaceName": "SampleStudentTranscript", "projectName": "SampleStudentTranscript",
        "projectVersion": "1.0.0", "projectExtension": "EXTENSION", "description": "" }
    ],
    "projectPaths": [ "./node_modules/@edfi/ed-fi-model-5.2", "../StudentTranscript" ],
    "pluginConfigDirectories": [],
    "defaultPluginTechVersion": "7.3.0",
    "allianceMode": false,
    "suppressPrereleaseVersion": true
  }
}
```

- List the core model first and the extension second, in `projects` and in `projectPaths`, in the same order.
- `namespaceName` and `projectName` of the extension are its `projectName` from `package.json`;
  `projectVersion` matches too.
- A relative `artifactDirectory` is resolved against the extension's folder, not the current folder, so
  `./MetaEdOutput` puts the output in the extension project, where the IDE puts it.
- `defaultPluginTechVersion` doesn't change `ApiSchema-EXTENSION.json`: in testing, the file was byte for byte
  the same with `7.3.0` and `8.1.0`. It only affects artifacts for ODS/API 7.x.
- Keep `allianceMode` `false`.

## Run the build

`-a` accepts the
[Ed-Fi License Agreement](https://docs.ed-fi.org/reference/metaed/getting-started-with-metaed-ide/installation/ed-fi-license-agreement).
Ask the developer to accept it before the first run; don't accept it on their behalf. From `metaed-build/`
(the same command in Bash and PowerShell):

```bash
node node_modules/@edfi/metaed-console/dist/index.js -a -c metaed-config.json
```

A build takes a few seconds. The **exit code** is `0` when the build succeeds and `1` when there are errors.

## Read the output

The build writes one JSON line per message to standard output:

```text
{"level":"error","message":"  Descriptor property AlternativeEducationEligibilityReasn does not match any declared descriptor in namespace SampleAlternativeEducationProgram.  C:\\...\\Association\\StudentAlternativeEducationProgramAssociation.metaed (3:16)"}
```

- Only `"level":"error"` lines fail the build. Each ends with the file and `(line:column)`.
- One `warn` line about `LearningStandardEquivalenceAssociation` in the core `Assessment.metaed` is expected with
  this model package; it isn't about the extension.
- Read every other warning. `X named Y already exists in project Ed-Fi` means the extension declares a new
  entity with a core name instead of extending the core one (rule CORE-1 in [rules.md](rules.md)); the build
  succeeds, but the API gets a second, unrelated resource. MetaEd reports these warnings only when the build
  has no errors.
- Node.js deprecation warnings on standard error are noise.

## Common errors

These messages came from real builds with MetaEd 4.9.0:

| Message (abbreviated) | Cause | Fix |
|---|---|---|
| `Descriptor property X does not match any declared descriptor in namespace Y` (also for domain entities, commons) | Misspelled name, or a core name without `EdFi.` | Fix the name, or add `EdFi.` |
| `Domain Entity X does not have an identity specified` | No `is part of identity` property | Mark the properties that identify the record |
| `'is part of identity' is invalid for property P on Domain Entity Extension X` | Identity in `additions` or a subclass | Use `is required` or `is optional` |
| `no viable alternative at input 'Domain EntityX...'` | Missing `documentation` after the entity name | Add the documentation line |
| `mismatched input '<EOF>' expecting 'max length'` | `string` without `max length` | Add `max length` |
| `mismatched input 'b' expecting ID` | A name that starts in lowercase | Start names with an uppercase letter |
| `mismatched input 'c' expecting {<EOF>, 'association', 'bool', ...}` | A misspelled keyword (here `colection`) at the line shown | Fix the keyword |

When the build fails, explain each error in terms of the `.metaed` line it points to, propose the change, apply
it only after the developer agrees, and build again. Parse errors can hide later errors, so rebuild after each
fix.

## The output

`MetaEdOutput/<projectName>/ApiSchema/ApiSchema-EXTENSION.json` is the only file Ed-Fi API 8.1 needs. The other
folders (`Database`, `Interchange`, `ApiMetadata`) are for ODS/API 7.x; the `XSD` folder is needed only for the
XML bulk load client. Check the result before deploying, from the extension project's folder:

```bash
node -e "const p=require('./MetaEdOutput/SampleStudentTranscript/ApiSchema/ApiSchema-EXTENSION.json').projectSchema; console.log(p.projectEndpointName, Object.keys(p.resourceSchemas))"
```

It should print the URL segment of the extension and every new resource, plus each core resource that has
`additions` (for example `studentAcademicRecords`).
