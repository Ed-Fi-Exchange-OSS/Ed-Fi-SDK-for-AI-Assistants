# Spec lookup analysis: options for similarity search over the Ed-Fi API specifications

- **Status:** Draft v0.2, for review
- **Author:** Rafael Ceballos (Simpat Tech)
- **Addresses:** PRD FR-SPEC-2 and Q-1 (issue #43, DEVOPS-144); FR-SPEC-3 and Q-2 (issue #44, DEVOPS-145)
- **Feeds:** [ADR 0001](adr/0001-api-spec-similarity-search.md) (similarity search over the Ed-Fi API specs)
- **Data:** ODS/API 7.3 public sandbox, Data Standard 5.2, Resources and Descriptors specs (Oct 20, 2026)

This analysis evaluates the options in ADR 0001 with measured data and a working prototype of option B, and
proposes the experiment that will settle the decision. It uses the ADR's option names and evaluation
criteria.

## 1. Problem size

Loading the specifications into an assistant's context is not an option:

| Spec | Size | Approx. tokens | Paths | Operations | Schemas |
|---|---|---|---|---|---|
| Resources | 4.9 MB | ~1.22 M | 763 | 1,222 | 989 |
| Descriptors | 6.1 MB | ~1.52 M | 1,145 | 1,832 | 917 |
| **Total** | **11.0 MB** | **~2.7 M** | | | |

Token counts use the usual ~4 characters per token approximation. The corpus that matters for lookup is
much smaller: **153 resources** and **229 descriptor types**, with a few thousand properties. As the ADR
notes, scale is not a driver.

## 2. Options (from ADR 0001)

| Option | Summary |
|---|---|
| **A** | Local embeddings, vector index in SQLite (`sqlite-vec`) |
| **A2** | Local embeddings, brute-force cosine similarity over a plain file |
| **A3** | Embeddings precomputed at build time and shipped in the repo (combined with A or A2 for queries) |
| **B** | Markdown knowledge graph (`index.md` plus linked files), delivered as an Agent Skill |
| **C** | Hybrid: B for navigation, plus an optional embedding search (A or A2) for harder queries |
| **D** | Something else |
| *Rejected* | Full-text keyword search (SQLite FTS5 with BM25, archived PR #30); kept only as a baseline |

## 3. Evidence

### 3.1 Prototype of option B

A small converter (about 100 lines of Python, no dependencies) generated a knowledge graph from the two
specs:

| Output | Content | Approx. tokens |
|---|---|---|
| `index.md` | 153 resources, one line each: name, path, first sentence of its description | ~7.8 K |
| `descriptors.md` | 229 descriptor types, one line each, plus how to read their values | ~7.0 K |
| `resources/*.md` | 153 files: natural key, fields (type, required, reference keys, descriptor), endpoints | ~78 K total; median ~450, max ~1.5 K per file |

A typical lookup reads the index plus one or two resource files, about **8–10 K tokens**, compared with
~2.7 M for the raw specs.

Spot checks on the generated content:

- **Natural keys** are derived from the spec's `x-Ed-Fi-isIdentity` fields plus required references. For
  example, `studentSchoolAssociations` → `entryDate`, `schoolReference`, `studentReference`.
- **Cascading key updates** are read from `x-Ed-Fi-isUpdatable` on PUT. The prototype flags exactly the 8
  resources that the Ed-Fi documentation lists (Class Period, Grade, GradebookEntry, Location, Section,
  Session, Student School Association, Student Section Association).
- **References** show the key fields of the referenced resource (e.g. `schoolReference: schoolId`).

### 3.2 Lookups that failed with keyword search

Queries that returned nothing, or the wrong results, with the FTS5 baseline or the earlier substring search,
run as a plain text search (grep) over the B index:

| Query | FTS5 (PR #30) | Substring search | B: `index.md` (grep) |
|---|---|---|---|
| attendance | 0 | 40 | 5 attendance event resources |
| enroll (student in school) | 0 | 0 | `studentSchoolAssociations` ("…the school in which a student is enrolled") |
| school association | 0 | 0 | `studentSchoolAssociations`, `staffSchoolAssociations`, `feederSchoolAssociations` |
| graduation plan | 0 | 0 | `graduationPlans` |
| staff assignment | 0 | 0 | `staffEducationOrganizationAssignmentAssociations` |
| grade level descriptor | 0 | 0 | `gradeLevelDescriptors` (in `descriptors.md`) |

The index works because it holds the **human-readable descriptions**, and because an assistant can try
several wordings and read the results. B delegates similarity to the assistant's own language
understanding, as the ADR describes. These results are from a single text search per query, not yet from an
assistant navigating the index; the experiment (section 6) measures the real behavior.

### 3.3 What the embedding options (A, A2, A3) would require

Not built, per FR-SPEC-2. Common to all three:

- **Query-time embedding.** Every lookup must embed the developer's question with the same model, so the
  developer's machine needs the model (tens of MB) and a runtime (Node.js or Python). A3 removes
  document-side embedding, but not this.
- **An entry point the assistant can call.** This could be a script bundled with a skill (Agent Skills can
  ship scripts) or an MCP server. Either way, the harness must be allowed to run it, unlike B's static files.
- **Identifier word-splitting** before embedding (`studentSchoolAssociation` → "student school
  association"), as the ADR notes.
- **A build step per spec version**, and per host to include extensions.

Differences between them:

- **A** adds the `sqlite-vec` native extension (one binary per OS and architecture).
- **A2** drops it. By estimate (not measured), about 400 documents × 384 dimensions is roughly 0.6 MB of
  vectors, small enough that a full scan should take milliseconds. Given the corpus size, A is not
  expected to offer an advantage over A2.
- **A3** precomputes those vectors and ships them in the repo. It is useful with A2, but it adds binary
  artifacts that must be regenerated when the spec changes.

## 4. Evaluation against the ADR criteria

| ADR criterion | A | A2 | A3 (+A2) | B | C (B + A2) |
|---|---|---|---|---|---|
| **Correctness on exact names** | Good | Good | Good | Good: whole resource in one file | Good |
| **Correctness on natural-language queries** | Strong by design | Strong by design | Strong by design | Good when descriptions match the wording (3.2); depends on the assistant trying synonyms | Strong |
| **Correctness on fields and descriptors** | Depends on chunking; fields can be split across chunks | Same as A | Same as A | Key, fields, references and endpoints together | Good |
| **Token usage** | Low: top-k chunks | Low | Low | Moderate: ~8–10 K per lookup | Low to moderate |
| **Steps per lookup** | Few | Few | Few | More: index, then file(s) | Few to more |
| **Setup burden and runtime dependencies** | High: model, runtime, native extension | Medium: model and runtime | Medium: model and runtime; faster setup | **None** | Medium (embeddings optional) |
| **Maintenance when the spec changes** | Re-embed, rebuild index | Re-embed | Re-embed, re-commit binaries | Re-run the converter; human-readable diffs | Both |
| **Fit with Agent Skills and portability** | Needs script or MCP support | Needs script or MCP support | Needs script or MCP support | **Native**: works wherever skills work | B is native; embeddings need script support |
| **Transparency and review (NFR-ACC-1)** | Opaque ranking | Opaque ranking | Opaque ranking | Plain Markdown, reviewable in a PR | Mixed |

**Risks for B to validate in the experiment:**

- **Index size:** ~7.8 K tokens is fine for one lookup but adds up in long sessions. If needed, the index
  can be split by domain.
- **Wording mismatch:** a developer's term may not appear in any description (e.g. "parent" vs. `contacts`
  in Data Standard 5). Mitigations: word-split names and synonyms in the index. Only the experiment shows
  how often this matters.
- **Derived natural keys:** inferred from the OpenAPI metadata; spot-check them against the Ed-Fi data model
  before release.

## 5. Recommendation (Q-1)

> _Draft, to be confirmed after review._

1. **Build B first**, as part of the Agent Skills release. It meets the PRD constraints (local, no hosted
   service, harness-neutral, reviewable) with no runtime dependency, and the prototype already resolves the
   lookups that failed with keyword search.
2. **If the experiment shows a natural-language gap, move to C with A2:** add an optional embedding search
   to B, using brute-force similarity (A2) rather than `sqlite-vec` (A), since the corpus is small. Consider
   A3 (shipped vectors) only if setup time becomes an issue.
3. **Do not build A** (`sqlite-vec`) for this release: at this corpus size it adds a native dependency
   without an expected benefit over A2. This is based on the corpus size (section 3.3), not on a
   measured comparison; neither A nor A2 has been built.
4. Record the outcome in ADR 0001 after the experiment.

## 6. Experiment design (Q-2)

### 6.1 Conditions

| ID | Condition | What the assistant has |
|---|---|---|
| C0 | No help | The API Client skill only, no spec access beyond fetching it |
| C1 | Keyword baseline | FTS5 search from archived PR #30 (via the original MCP server) |
| C2 | Option B | The Markdown knowledge graph as a skill |
| C3 | Option A2 (or C) | Embedding search, only if built after the first results |

### 6.2 Tasks

Eighteen lookup tasks with a known correct answer, verified against the spec:

| # | Kind | Task (prompt to the assistant) | Expected answer |
|---|---|---|---|
| 1 | Exact name | What is the natural key of `studentSchoolAssociations`? | `entryDate`, `schoolReference`, `studentReference` |
| 2 | Exact name | Which fields are required to POST a `student`? | `studentUniqueId`, `firstName`, `lastSurname`, `birthDate` |
| 3 | Exact name | What is the natural key of `sections`? | `sectionIdentifier`, `courseOfferingReference` |
| 4 | Exact name | Can the natural key of `sessions` be changed with PUT? | Yes (cascading key updates) |
| 5 | Natural language | Which resource records that a student is enrolled in a school? | `studentSchoolAssociations` |
| 6 | Natural language | Where do I record daily school attendance for a student? | `studentSchoolAttendanceEvents` |
| 7 | Natural language | Where do I record which teacher teaches a section? | `staffSectionAssociations` |
| 8 | Natural language | Where are a student's standardized test results stored? | `studentAssessments` |
| 9 | Natural language | How do I link a student to a parent or guardian? | `studentContactAssociations` (DS 5 uses "contact") |
| 10 | Natural language | Where do I record a student's final course grade for a grading period? | `grades` |
| 11 | Natural language | Where is a course on a student's transcript stored? | `courseTranscripts` |
| 12 | Natural language | Where do I record a student's participation in special education? | `studentSpecialEducationProgramAssociations` |
| 13 | Natural language | Where do I record a student's behavior in a discipline incident? | `studentDisciplineIncidentBehaviorAssociations` |
| 14 | Natural language | Where do I record a staff member's assignment to a district? | `staffEducationOrganizationAssignmentAssociations` |
| 15 | Field mapping | Our SIS has `sch_id`. Which Ed-Fi field does it map to on a school? | `schoolId` |
| 16 | Descriptor | Which descriptor type lists grade levels, and how do I get its values? | `gradeLevelDescriptors`; read values from the API |
| 17 | Descriptor | Which descriptor does `entryTypeDescriptor` on a studentSchoolAssociation use? | `entryTypeDescriptors` |
| 18 | Reference | What keys do I need to reference a calendar? | `calendarCode`, `schoolId`, `schoolYear` |

### 6.3 Scoring rubric

| Measure | How | ADR criterion |
|---|---|---|
| **Correctness** | 2 = correct and complete; 1 = partially correct (e.g. right resource, incomplete key); 0 = wrong or no answer | Correctness and completeness |
| **Hallucination** | Count of invented resources, fields or descriptors in the answer | Correctness and completeness |
| **Context cost** | Input tokens used for the task, from the harness or API usage report | Token usage |
| **Steps** | Number of tool calls or files read | Number of steps |

Primary result: the total correctness score per condition, split by task kind (exact name, natural
language, field mapping, descriptor, reference).

### 6.4 Models and procedure

1. Run every condition in **Claude Code** and **GitHub Copilot** (FR-REL-1), with the default model of each
   harness, and record the model and version.
2. Run each task in a fresh session, so earlier tasks don't leak context.
3. Run each task-condition pair twice. If the two runs disagree, run a third and take the majority score.
4. Record results in a table: task, condition, harness, model, scores, notes.
5. Two reviewers score correctness independently for any answer that does not match the expected answer
   exactly.

### 6.5 Decision rule

- If **C2 (B)** scores at least as well as C0 and C1 overall, and reaches at least 80 % of the maximum on the
  natural-language tasks: **adopt B** and record it in ADR 0001.
- If C2 falls short mainly on natural-language tasks: first improve the index (word-split names, synonyms,
  domain grouping) and re-run. If it still falls short, **build C with A2** and compare C3 against C2.

## 7. Next steps

1. Review this analysis and agree on the recommendation (Q-1) and the experiment design (Q-2).
2. Add the converter to the repo (e.g. `tools/`) and generate the knowledge graph as a skill (issue #45).
3. Run the experiment (issue #47) and publish the results here and in ADR 0001.
