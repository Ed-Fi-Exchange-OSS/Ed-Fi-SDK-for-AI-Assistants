# PRD: Ed-Fi Agent Skills for API Client Integrations

- **Status:** Draft v0.1
- **Owner:** Stephen Fuqua (Ed-Fi Alliance)
- **Repository:** Ed-Fi-Exchange-OSS/Ed-Fi-SDK-for-AI-Assistants

## 1. Product overview

Developers who are new to working with the Ed-Fi Data Standard often overlook critical development guidelines
around authentication, descriptors, paging, and conflict responses, and are forced to infer dependency order
from raw OpenAPI specifications. AI coding agents can help overcome these problems, but they need to be
grounded in authoritative context.

This product is a library of **Agent Skills**: text-based skill packages that load into AI coding harnesses
(at minimum Claude Code and GitHub Copilot) and give them normative guidance straight from the Ed-Fi Alliance.

The first release targets **API client integrations** (push and pull). It effectively packages the Ed-Fi
Client Developers' Guide, plus the content already present in an earlier MCP server, as Agent Skills. A plain
Agent Skill is preferred over an MCP server because no remote server is required and the guidance is static
knowledge, not data.

### 1.1 Strategic alignment

- The Alliance provides frameworks and proofs of concept, not production-grade or prescriptive solutions.
- Agent Skills supersede the knowledge-delivery role of the existing MCP server, which predates Agent Skills.
- Skills guide developers building integrations. The separate semantic layer / data MCP initiative guides AI
  systems accessing data at runtime. The two efforts should share vocabulary so a skill can direct a developer
  to an API-spec lookup capability.

### 1.2 Target users and personas

- **Integration developer (primary).** Builds push (e.g., SIS to Ed-Fi) or pull (e.g., analytics or downstream
  system) clients. Uses an AI coding assistant. Pain: hallucinated Ed-Fi API integration patterns, opaque
  error responses, time lost researching. Success: working, correct client code with fewer iterations.
- **Integration reviewer / troubleshooter.** Debugs failing integrations. Pain: cryptic responses such as 409
  or 401. Success: accurate explanation and fix.
- **Skill maintainer / contributor.** Ed-Fi Alliance staff and community. Success: easy to update, review, and
  validate skills.

### 1.3 Jobs to be done

- When I build an Ed-Fi API client, I want my assistant to apply correct authentication and token handling, so
  that I do not debug OAuth mistakes.
- When I build a push integration, I want guidance on dependency ordering, descriptor resolution and
  idempotent writes, so that loads succeed in the right order.
- When I build a pull integration, I want guidance on paging, change queries and incremental sync, so that I
  synchronize efficiently and correctly.
- When I receive an unexpected API response, I want my assistant to explain what it means (e.g., "what does
  this 409 mean?") and how to handle it in code.
- When I need to find an endpoint or property, I want to avoid loading the entire OpenAPI spec into context
  (see FR-SPEC; experimental).

## 2. System context

- Skills are static files in a Git repository, consumed locally by AI coding harnesses. No hosted service.
- Target API: Ed-Fi ODS/API 7 and Ed-Fi API 8. Client guidance is largely the same for both; version-specific
  differences (e.g., URL paths, property-name casing, token endpoint, snapshots) are called out where they
  matter (see NFR-COMP-1). Data Standard 5.2 is the baseline.
- Development environment: Ed-Fi API 8 with Data Standard 5.2, started using the Ed-Fi Alliance pilot test
  kit.

## 3. Functional requirements

### 3.1 Client skill foundation (Priority 1)

- **FR-BASE-1:** The product SHALL provide an API Client base skill covering authentication, token handling
  and acquisition, authorization, and metadata discovery.
- **FR-BASE-2:** The base skill SHALL use progressive disclosure; for example, it SHALL determine whether the
  developer is building a push or pull integration and direct the assistant to the corresponding detailed
  guidance, without loading both into context.
- **FR-BASE-3:** The base skill SHALL cover error handling in code, including retry, backoff and token-expiry
  handling.
- **FR-BASE-4:** The base skill SHALL provide guidance for diagnosing specific API responses, including at
  least 400, 401, 403, 404, 409, 412, 429 and 5xx, with the cause and recommended handling for each.
- **FR-BASE-5:** The skill content SHALL carry over relevant knowledge from the existing `sdk-as-mcp` server
  and the Client Developers' Guide, and SHALL be reorganized rather than copied verbatim where structure
  conflicts with progressive disclosure.

### 3.2 Push guidance

- **FR-PUSH-1:** The push skill SHALL cover resource dependency ordering for loads.
- **FR-PUSH-2:** The push skill SHALL cover descriptor resolution.
- **FR-PUSH-3:** The push skill SHALL cover POST/PUT semantics, natural-key identity, conflict (409) handling
  and deletes.
- **FR-PUSH-4:** The push skill SHALL explicitly discourage deleting and re-posting records to update them,
  and explain POST-as-upsert and PUT by resource id instead.

### 3.3 Pull guidance

- **FR-PULL-1:** The pull skill SHALL cover paging strategies, including offset paging and, where supported,
  cursor paging and partitions for parallel extraction.
- **FR-PULL-2:** The pull skill SHALL cover change queries and incremental synchronization.
- **FR-PULL-3:** The pull skill SHOULD cover descriptor and reference resolution when reading.

### 3.4 Worked domain example

- **FR-DOM-1:** If a domain-specific example is included, it SHALL be performance evaluations from the IIA
  project.
- **FR-DOM-2:** Generic client guidance (FR-BASE, FR-PUSH, FR-PULL) SHALL take priority over any domain
  content.

### 3.5 API specification knowledge (experimental)

- **FR-SPEC-1:** The team SHOULD evaluate two approaches to giving an assistant targeted access to the
  Resources and Descriptors OpenAPI specifications without loading the full spec: (A) a local SQLite vector
  search (to be built with true embeddings; the keyword search in open PR #30 uses SQLite FTS5 with BM25 and
  can serve as a keyword-search baseline); (B) a Markdown "wiki" knowledge graph, with `index.md` as table of
  contents linking to detailed files, delivered as an Agent Skill.
- **FR-SPEC-2:** An analysis of approach B versus A SHALL be provided at project start, before approach A is
  built.
- **FR-SPEC-3:** Both approaches SHOULD be implemented if time permits, along with a documented experiment
  design for comparing output quality.
- **FR-SPEC-4:** Composite and extension specifications SHALL NOT be indexed in this release.
- **FR-SPEC-5:** If embeddings are used, a local embedding option SHOULD be used when a simple path exists.

### 3.6 Code Review skill (stretch)

- **FR-REV-1:** The product MAY provide a Code Review skill that evaluates integration code against Ed-Fi API
  integration best practices and flags anti-patterns.
- **FR-REV-2:** Integration rules SHOULD be defined once and shared by the build guidance and the Code Review
  skill, so that both stay consistent.

### 3.7 Validation and release

- **FR-REL-1:** Each skill SHALL be verified to work in at least Claude Code and GitHub Copilot before it is
  considered done.
- **FR-REL-2:** Each skill SHALL have a documented set of test prompts with expected outcomes, used to verify
  it in each required harness.
- **FR-REL-3:** The release SHALL be a tagged release of the repository.
- **FR-REL-4:** The repository SHOULD document how to install and use each skill in supported harnesses.

## 4. Non-functional requirements

- **NFR-ACC-1:** Guidance SHALL be consistent with normative Ed-Fi Alliance documentation. Where the source is
  ambiguous, the skill SHALL say so rather than guess.
- **NFR-TOK-1:** Skills SHALL minimize context use: concise entry files, with detail in separately loaded
  files.
- **NFR-COMP-1:** Skills SHALL apply to ODS/API 7 and Ed-Fi API 8, with Data Standard 5.2 as the baseline.
  Version-specific differences SHALL be called out explicitly.
- **NFR-PORT-1:** Skills SHOULD be harness-neutral, following the Agent Skills format, and SHOULD work in
  other harnesses (e.g., Codex, Cursor) without modification.
- **NFR-SEC-1:** Skills and examples SHALL NOT contain real credentials. Guidance SHALL recommend secure
  storage and handling of client secrets and tokens.
- **NFR-MNT-1:** Content SHOULD be organized so that individual topics can be updated independently when the
  standard changes.

## 5. System architecture

| Component | Description | Notes |
| --- | --- | --- |
| API Client base skill | Entry point: auth, tokens, authorization, metadata discovery, push/pull routing, error handling | Priority 1 |
| Push guidance files | Dependency order, descriptors, conflicts, loading | Loaded on demand |
| Pull guidance files | Paging, change queries, incremental sync | Loaded on demand |
| Response troubleshooting reference | HTTP status and Ed-Fi error explanations | Part of base or linked file |
| Code Review skill | Anti-pattern review of existing integration code | Stretch |
| API spec lookup, approach A | Local SQLite vector index of Resources and Descriptors specs | Experimental |
| API spec lookup, approach B | Markdown knowledge graph (`index.md` plus linked files) as a skill | Experimental |
| Test harnesses | Claude Code, GitHub Copilot | Required validation targets |

Runtime: local files loaded by the harness. Data ownership: skill content is owned by the Alliance repo; no
user data is processed.

## 6. Out of scope and known limitations

- API Customization and skills (claim sets, authorization, profiles): these belong in a separate product for
  API host providers.
- Domain-specific overlays (assessments, gradebook): deferred to 2027.
- Composite and extension specifications in spec lookup.
- Data Standard Extension Builder skills: belong in a separate product for API host providers.
- Semantic layer / data MCP server: belongs in a separate product.
- Community contribution and governance process (target Q1 2027).
- Remote or hosted servers.
- Skills cannot replace developers' understanding of their own source system's semantics.

## 7. Open questions

- **Q-1:** Which spec lookup approach (A or B) will be built first? Pending the analysis in FR-SPEC-2.
- **Q-2:** How will the quality comparison between the vector search and Markdown knowledge graph approaches
  be measured (tasks, rubric, models)? Left open.
- **Q-3:** Skill discovery, vetting and maintenance model for community contributions.

## 8. Glossary

- **Agent Skill:** A packaged set of instructions and resources an AI coding harness loads on demand.
- **Progressive disclosure:** Loading a short base skill first, and detailed files only as needed.
- **MCP:** Model Context Protocol, a server-based mechanism for giving AI tools context or data.
- **Descriptor:** Ed-Fi Data Standard code-list type resolved by URI.
- **Change queries:** ODS/API mechanism for retrieving changes since a version.
- **AMT:** Analytics Middle Tier, views that flatten Ed-Fi data for analytics.
- **IIA:** Texas's _Insight to Impact Application_ project from which the performance evaluation domain
  example is drawn.
- **Semantic layer:** Governed data abstraction for AI access at runtime (separate effort).
