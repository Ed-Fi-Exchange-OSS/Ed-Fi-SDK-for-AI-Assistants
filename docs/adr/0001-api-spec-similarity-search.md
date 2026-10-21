# ADR 0001: Delivering similarity search over the Ed-Fi API specifications

- **Status:** Proposed (draft; decision deferred to implementation)
- **Date:** 2026-10-20
- **Related:** PRD FR-SPEC-1 through FR-SPEC-5, Q-1, Q-2

## Context

Assistants need targeted access to the Ed-Fi Resources and Descriptors OpenAPI specifications without loading the full specification into context (PRD §3.5). A developer often does not know the exact resource name: they may ask to "enroll a student in a school" and need `studentSchoolAssociation`. Lookup therefore needs to support _similarity_ (meaning-based matching), not only exact or substring matches.

Constraints from the PRD:

- No hosted service; everything runs locally from files in a Git repository (§2).
- Composite and extension specifications are not indexed in this release (FR-SPEC-4).
- If embeddings are used, a local embedding option SHOULD be used when a simple path exists (FR-SPEC-5).
- Ed-Fi Data Standard identifiers are single camelCase tokens (e.g., `studentSchoolAssociation`), which embedding models and tokenizers handle poorly unless split into words first.
- The corpus is small (hundreds of resources, a few thousand properties), so scale is not a driver.

## Decision

**Not yet decided.** The options below are candidates. The team will select one, or propose a different approach, during implementation, guided by the FR-SPEC-2 analysis and the Q-2 experiment (a fixed set of real lookup tasks scored on correctness, token usage and number of steps, in Claude Code and GitHub Copilot). This ADR will be updated with the outcome.

## Options considered

### Option A: Local embeddings with a vector index (SQLite)

Generate embeddings for resources, properties and descriptors using a local model (for example, Transformers.js with a small ONNX model such as `all-MiniLM-L6-v2` or `bge-small-en-v1.5`, or `fastembed`). Store them in SQLite with the `sqlite-vec` extension and query by nearest neighbor.

- Pros: true semantic similarity; supports natural-language queries; no external API calls.
- Cons: requires a runtime (Node.js or Python) plus native binaries; model download (about 30 MB or more); query-time embedding requires loading the model (about a second of startup); must be built, since nothing exists yet; identifiers need word-splitting before embedding.

### Option A2: Local embeddings with brute-force cosine similarity

Same embedding approach as A, but store vectors in a plain JSON or binary file and compare the query vector with every stored vector (a dot product over normalized vectors). At this corpus size the scan takes milliseconds, and the results are exact.

- Pros: removes the SQLite and `sqlite-vec` dependency; simplest data format; easy to inspect and diff.
- Cons: still needs a local embedding model and runtime for query-time embedding; would need revisiting only if the corpus grew by orders of magnitude.

### Option A3: Precomputed embeddings shipped in the repository

Compute document embeddings at build time and commit them with the release, so developers do not need to embed the spec themselves.

- Pros: faster setup; reproducible per release.
- Cons: query-time embedding is still required, so the model and runtime are still needed unless combined with another approach; adds binary artifacts to the repository and must be regenerated when the spec changes.

### Option B: Markdown knowledge graph ("wiki") delivered as an Agent Skill

Generate Markdown files describing resources, descriptors and their relationships, with `index.md` as a table of contents linking to detailed files. The assistant navigates by reading the index and following links, using its own language understanding for similarity.

- Pros: no runtime, model or native dependencies; works in any harness that supports Agent Skills; fits progressive disclosure; human-reviewable and easy to version.
- Cons: relies on the assistant to navigate well; index size consumes context and may grow large; more steps per lookup; must be regenerated when the spec changes.

### Option C: Hybrid

Combine approaches, for example a Markdown index (B) for navigation with an optional local embedding search (A or A2) over word-split identifiers and descriptions for harder queries.

- Pros: covers both known-name and natural-language lookups; embeddings remain optional.
- Cons: highest implementation and maintenance cost; two paths to keep consistent.

### Option D: Something else

Other approaches (for example, a locally hosted embedding runtime, or a different retrieval design) may be proposed during implementation and recorded here.

## Rejected alternatives

### Full-text index with keyword search (SQLite FTS5 with BM25)

Prototyped in archived PR #30. Rejected as the similarity-search solution because it matches on tokens, not meaning:

- Natural-language queries return nothing, because there is no semantic matching.
- Ed-Fi API paths are single camelCase tokens, so partial or conceptual terms miss them (for example, "attendance" returned 0 results versus 40 for the earlier substring search).
- It requires Node.js on the developer machine.

It may still serve as a keyword-search baseline in the Q-2 comparison, and keyword matching over word-split identifiers could be a component of a hybrid (Option C).

## Evaluation criteria

- Correctness and completeness on lookups: exact names, natural-language queries, fields and descriptors.
- Token usage and number of steps per lookup.
- Setup burden and runtime dependencies (including Node.js or Python availability).
- Maintenance effort when the specification changes.
- Fit with the Agent Skills format and portability across harnesses.

## Consequences

To be completed when a decision is made. Whichever option is chosen, identifier word-splitting should be considered for any matching approach, and the selected design must satisfy FR-SPEC-4 (no composite or extension specs) and FR-SPEC-5 (local embeddings where a simple path exists).
