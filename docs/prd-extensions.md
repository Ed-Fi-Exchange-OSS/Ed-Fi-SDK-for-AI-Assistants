# PRD: Ed-Fi Agent Skills for Data Standard Extensions

- **Status:** Draft v0.1
- **Owner:** Stephen Fuqua (Ed-Fi Alliance)
- **Repository:** Ed-Fi-Exchange-OSS/Ed-Fi-SDK-for-AI-Assistants
- **Sources:**
  - [How To: Extend the Ed-Fi API - Alternative Education Program
    Example](https://docs.ed-fi.org/reference/ed-fi-api/8/how-to-guides/how-to-extend-the-ed-fi-ods-api-alternative-education-program-example/)
    (Ed-Fi API 8.1)
  - [How To: Extend the Ed-Fi API - Student Transcript
    Example](https://docs.ed-fi.org/reference/ed-fi-api/8/how-to-guides/how-to-extend-the-ed-fi-ods-api-student-transcript-example/)
    (Ed-Fi API 8.1)
  - [MetaEd documentation](https://docs.ed-fi.org/reference/metaed), including the Cookbook, the Language
    Specification and [MetaEd for Continuous
    Integration](https://docs.ed-fi.org/reference/metaed/metaed-for-continuous-integration)
  - [Ed-Fi Data Standard Extension Framework Best
    Practices](https://docs.ed-fi.org/reference/data-exchange/extensions-framework/)
  - The `review-model-pr` skill in
    [AI-Tools-for-Ed-Fi-SDLC](https://github.com/Ed-Fi-Alliance-OSS/AI-Tools-for-Ed-Fi-SDLC)
  - The client skills PRD in this repository ([prd.md](prd.md)); the extension skills are a separate product,
    for API hosts, in the same repository

## 1. Product overview

States, districts and vendors that run an Ed-Fi API extend the Data Standard when they need data the core
model does not hold. Building an extension takes several tools and steps that are easy to get wrong: modeling
in MetaEd, building the API schema, staging it with the core schema, adding the new resources to the claims
hierarchy, and restarting with a clean database. A mistake in any step leaves a resource that does not appear
or that no client can access, and changing an installed extension means reloading data.

This product is a set of **Agent Skills** that help an AI coding assistant guide an implementer through that
process for **Ed-Fi API 8.1 and later**, and review MetaEd extension source against Ed-Fi modeling rules. The
skills run the MetaEd build from the command line and offer to fix build errors, so the implementer gets a
model that builds before any deployment step.

The first release is based on the two official how-to guides for Ed-Fi API 8.1, which together show the two
kinds of extension: a new resource and descriptor (Alternative Education Program) and properties added to an
existing core resource (Student Transcript).

### 1.1 Strategic alignment and success criteria

- The Alliance provides frameworks and proofs of concept, not production-grade or prescriptive solutions.
- Ed-Fi API 8 is the target for new implementations. Its extension workflow differs from ODS/API 7.3 (no C#
  project, no SQL claims scripts), so guidance written for 7.3 misleads assistants and implementers.
- The extension skills complement the client skills: client skills already explain how clients read and write
  extension resources and `_ext` properties.
- **Success criteria:**
  - Both how-to examples can be modeled, built, deployed and verified end to end from an assistant's output
    using the skills, in Claude Code and GitHub Copilot.
  - On the test prompts, answers with the skills meet more expected outcomes than answers without them.
  - The review skill finds the known defects planted in the review test cases.

### 1.2 Target users and personas

- **Extension author (primary).** An implementer at a state, district or vendor who models and deploys an
  extension on an Ed-Fi API 8.1 host. Knows their data; may be new to MetaEd and to the Ed-Fi API 8 tooling.
  Pain: unfamiliar modeling language, build errors, resources that deploy but are not accessible. Success: a
  working extension, verified with API calls, with fewer iterations.
- **Extension reviewer.** Reviews MetaEd extension source before it is deployed or shared. Pain: modeling
  rules that live in several places. Success: consistent findings, separated into blocking issues and
  suggestions.
- **Skill maintainer / contributor.** Ed-Fi Alliance staff and community. Success: easy to update when MetaEd
  or Ed-Fi API tooling changes, and easy to validate.

### 1.3 Jobs to be done

- When my data does not fit the core model, I want my assistant to tell me whether I need an extension at all
  or whether an existing entity or descriptor already covers it.
- When I need a new resource, I want my assistant to model it in MetaEd (association, domain entity,
  descriptor, common type) with correct identity, naming and references to core entities.
- When I need to add properties to a core resource, I want my assistant to extend that resource rather than
  copy or modify it.
- When the MetaEd build fails, I want my assistant to run the build, explain the errors and offer fixes.
- When the extension builds, I want my assistant to take me through staging the schema, writing the claims
  fragment and restarting the API, and warn me before any step that deletes data.
- When the API restarts, I want my assistant to verify that the extension appears in Discovery and that a
  client can call the new endpoints.
- When I review extension source, I want my assistant to check it against Ed-Fi modeling rules and report
  blocking issues separately from suggestions.

## 2. System context

- Skills are static files in this repository, consumed locally by AI coding harnesses. No hosted service.
- **Target platform:** Ed-Fi API 8.1 and later, with Data Standard 5.2. ODS/API 7.3 may be added later (see
  section 6).
- **Modeling and build:** MetaEd 4.9 or later, which produces `ApiSchema-EXTENSION.json`. The skills run the
  MetaEd build through its command-line package (`@edfi/metaed-console`), which requires Node.js and access
  to the Ed-Fi package feed.
- **Deployment:** the how-to guides use the local Ed-Fi API stack from the Data Management Service
  repository: `prepare-dms-schema.ps1` stages the core and extension schemas, `prepare-dms-claims.ps1` stages
  the claims fragment, and `bootstrap-local-dms.ps1` provisions a clean database and seeds the Configuration
  Service. The schema and claims load only into empty databases, so any change to an installed extension
  needs a teardown that deletes data.
- **Security:** new resources are added to the claims hierarchy through a claims fragment, with claim URIs of
  the form `http://ed-fi.org/identity/claims/{projectEndpointName}/{resourceName}`. Placement in the
  hierarchy decides which claim sets inherit access.
- **Development environment:** Ed-Fi API 8.1 with Data Standard 5.2, running locally as in the how-to guides.

## 3. Functional requirements

### 3.1 Extension skill foundation

- **FR-EXT-1:** The product SHALL provide an extension skill whose entry file covers when to extend, the
  end-to-end flow (design, model, build, stage, secure, start, verify) and routing to detailed guidance.
- **FR-EXT-2:** The skill SHALL first check whether the need can be met by existing core entities,
  descriptors or descriptor values, and say so when an extension is not needed.
- **FR-EXT-3:** The skill SHALL use progressive disclosure, loading modeling, build, deployment, security and
  verification guidance only when the task needs it.

### 3.2 Modeling

- **FR-MODEL-1:** The skill SHALL guide creation of a MetaEd extension project: folder layout, `package.json`
  (`projectName`, `projectVersion` following SemVer) and naming rules for the project name.
- **FR-MODEL-2:** The skill SHALL cover the entity kinds used in the two examples: a new association based on
  a core association, a new domain entity, new descriptors, extension of a core resource, extension of a core
  common type, and references to core entities.
- **FR-MODEL-3:** The skill SHALL cover identity (`is identity`), required and optional properties,
  collections, and documentation strings, following the Ed-Fi modeling rules in FR-REVIEW.
- **FR-MODEL-4:** The skill SHALL NOT modify core Data Standard entities, and SHALL NOT enable MetaEd Alliance
  Mode.
- **FR-MODEL-5:** The skill SHOULD point to the matching MetaEd Cookbook recipe for each modeling task.

### 3.3 Build

- **FR-BUILD-1:** The skill SHALL run the MetaEd build from the command line, targeting Ed-Fi API 8.1 and Data
  Standard 5.2, and SHALL report whether it succeeded.
- **FR-BUILD-2:** When the build fails, the skill SHALL explain each error in terms of the `.metaed` source and
  offer a fix. It SHALL apply a fix only after the user agrees, and SHALL rebuild after each fix.
- **FR-BUILD-3:** The skill SHALL ask the user to accept the Ed-Fi license before running the build, rather
  than accepting it on the user's behalf.
- **FR-BUILD-4:** The skill SHALL cover installing the MetaEd command-line package and the Data Standard model
  package it needs, and SHALL say what to do when the package feed is not reachable.

### 3.4 Deployment

- **FR-DEPLOY-1:** The skill SHALL guide gathering the core and extension schema files in the layout the
  staging script expects.
- **FR-DEPLOY-2:** The skill SHALL guide staging the schema, starting the stack and confirming that the
  extension was provisioned.
- **FR-DEPLOY-3:** The skill SHALL warn before any step that deletes databases or staged files, and SHALL
  state that changing an installed extension requires a clean database and reloading data through the API.
- **FR-DEPLOY-4:** The skill SHOULD state which steps are specific to the local development stack, so that a
  host can map them to its own deployment.

### 3.5 Security

- **FR-SEC-1:** The skill SHALL guide writing a claims fragment for every new resource and descriptor, with
  claim URIs that match the generated schema's `projectEndpointName` and resource names.
- **FR-SEC-2:** The skill SHALL explain the two access patterns in the how-to guides: inheriting access by
  placing claims under existing domains, and restricting access with a new domain that names its claim sets.
- **FR-SEC-3:** The skill SHALL state that an extension resource is not accessible until it is in the claims
  hierarchy and granted to a claim set.

### 3.6 Verification

- **FR-VERIFY-1:** The skill SHALL verify the deployed extension by checking that Discovery lists the
  extension under `dataModels`, obtaining a token, and calling a new endpoint.
- **FR-VERIFY-2:** For an extension of a core resource, the skill SHALL verify that the new properties are
  accepted and returned under `_ext`.
- **FR-VERIFY-3:** The skill SHALL explain the likely cause when verification fails: the extension missing
  from Discovery, a 403 from a missing claim, or a 404 from a wrong project endpoint.

### 3.7 Review

- **FR-REVIEW-1:** The product SHALL provide review guidance for MetaEd extension source (`.metaed` files and
  the project `package.json`). It SHALL NOT review the generated `ApiSchema-EXTENSION.json`.
- **FR-REVIEW-2:** The review guidance SHALL adapt the `review-model-pr` checklist to extensions: build
  validity, typos and grammar, documentation completeness, identity, naming, deprecation, shared types and
  slowly changing dimensions. Items specific to the Ed-Fi-Model repository (for example the `DATASTD-` PR
  title) SHALL be left out.
- **FR-REVIEW-3:** The review guidance SHALL add extension-specific checks: no changes to core entities,
  consistent project name and namespace, references to core entities that exist in the target Data Standard,
  and a claims fragment entry for every new resource.
- **FR-REVIEW-4:** The review SHALL run the MetaEd build when possible, and SHALL report findings with file
  and line, separated into blocking issues and suggestions.
- **FR-REVIEW-5:** Modeling rules SHOULD be defined once and shared by the build guidance and the review
  guidance.

### 3.8 Validation and release

- **FR-REL-1:** Each skill SHALL be verified in at least Claude Code and GitHub Copilot before it is
  considered done.
- **FR-REL-2:** Each skill SHALL have a documented set of test prompts with expected outcomes, run with and
  without the skill.
- **FR-REL-3:** Both how-to examples SHALL be built with the MetaEd command line, deployed to a local Ed-Fi
  API 8.1 and verified with API calls, following the assistant's output.
- **FR-REL-4:** The review guidance SHALL be tested against extension source with planted defects, with the
  expected findings documented.
- **FR-REL-5:** The repository SHOULD document how to install and use the extension skills.

## 4. Non-functional requirements

- **NFR-ACC-1:** Guidance SHALL be consistent with the Ed-Fi API 8.1 how-to guides and the MetaEd
  documentation. Where they are ambiguous or silent, the skill SHALL say so rather than guess.
- **NFR-COMP-1:** Skills SHALL target Ed-Fi API 8.1 and later with MetaEd 4.9 or later. Guidance SHALL NOT
  describe ODS/API 7.3 steps (C# extension project, SQL claims scripts, `initdev`) as applying to Ed-Fi API 8.
- **NFR-SAFE-1:** The skill SHALL ask before running commands that delete data, change the core model or
  accept a license.
- **NFR-SEC-1:** Skills and examples SHALL NOT contain real credentials. Verification steps SHALL use
  credentials the user creates for the local stack and SHALL NOT print secrets.
- **NFR-TOK-1:** Skills SHALL minimize context use: a concise entry file, with detail in separately loaded
  files.
- **NFR-PORT-1:** Skills SHOULD follow the Agent Skills format and work in other harnesses without
  modification. Commands SHOULD be given for both PowerShell and Bash where the underlying tools allow it.
- **NFR-MNT-1:** Content SHOULD be organized so that MetaEd, staging and claims guidance can be updated
  independently when the tooling changes.

## 5. System architecture

| Component | Description | Notes |
| --- | --- | --- |
| Extension skill entry file | When to extend, end-to-end flow, routing | Loaded first |
| Modeling guidance | MetaEd project, entity kinds, identity, naming | Shared rules with review |
| Build guidance | MetaEd command line: install, configure, run, fix errors | Runs the build |
| Deployment guidance | Gather, stage, start, reset | Local stack as in the how-to guides |
| Security guidance | Claims fragments, claim URIs, inherited and restricted access | |
| Verification guidance | Discovery, token, endpoint calls, `_ext` | |
| Review guidance | Checklist for `.metaed` source | Adapted from `review-model-pr` |
| Worked examples | Alternative Education Program, Student Transcript | From the API 8.1 how-to guides |
| Test harnesses | Claude Code, GitHub Copilot | Required validation targets |

Runtime: local files loaded by the harness, plus the MetaEd command line and the local Ed-Fi API stack on the
user's machine. Data ownership: skill content is owned by the Alliance repository; the extension source and
data belong to the user.

## 6. Out of scope and known limitations

- ODS/API 7.3 build, deployment and security. May be added in a later release.
- Review of the generated `ApiSchema-EXTENSION.json`; it is generated from the `.metaed` source.
- Data Standard governance and the community extension review process.
- Migrating data between versions of an installed extension, beyond the rule that changes need a clean
  database and a data reload.
- Data Standard 6, until Ed-Fi API 8 targets it.
- Indexing extension specifications in the `ed-fi-api-spec` lookup.
- Skills cannot decide what a host's data means; the implementer remains responsible for the design.

## 7. Open questions

- **Q-1:** The how-to guides deploy to the local development stack. Should the skills also guide deployment to
  a host's own environment (for example, setting `ApiSchemaPath` and provisioning with `api-schema-tools`
  directly), or only the local stack in the first release?
- **Q-2:** One skill for building and reviewing, or a separate review skill, as with `review-model-pr`?
- **Q-3:** Should extension examples beyond the two how-to guides (for example, a state extension) be part of
  the test set?

## 8. Glossary

- **Agent Skill:** A packaged set of instructions and resources an AI coding harness loads on demand.
- **Extension:** Additions to the Ed-Fi Data Standard (new entities, descriptors or properties on core
  entities) defined in a separate MetaEd project.
- **MetaEd:** The Ed-Fi modeling language and tooling that generate API artifacts from `.metaed` source.
- **ApiSchema:** The JSON schema files that Ed-Fi API 8 loads at runtime; `ApiSchema-EXTENSION.json` is the
  extension's file.
- **Claims fragment:** A JSON file that adds resources to the claims hierarchy of the Configuration Service.
- **Claim set:** A named set of permissions assigned to API clients.
- **`_ext`:** The property under which extension properties of a core resource appear in API payloads.
- **Discovery:** The API root endpoint that lists the data models the API serves.
