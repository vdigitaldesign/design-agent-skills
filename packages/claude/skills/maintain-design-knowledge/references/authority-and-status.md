# Authority, materiality, and status

Read this reference whenever a skill may classify design work, propose a direction, record a decision, write a contract, or judge parity. It is the shared authority rule for this repository.

## Separate kinds of truth

- **Source authority / primary claim** owns what a product or policy says is true: for example, an approved product decision, a platform requirement, or an authoritative design-system rule.
- **Observed evidence snapshot** owns what was observed, where, when, by which method, and with which limitations. Observation is not approval.
- **Product canon** owns effective product facts and decisions within its stated scope.
- **Effective design-system canon** owns approved system relationships, tokens, component or pattern rules, documentation, and lifecycle within its consumer scope.
- **Approved design decision** records a human-authorized material choice and its scope. It is normative for that choice but may still need specification.
- **Effective Design Contract** owns the testable design requirements for its stated scope.
- **Lineage metadata** owns relationships among sources, observations, decisions, contracts, and verification records. It does not own the underlying facts.

Keep one normative owner for each fact. Preserve source and revision lineage. A self-contained contract or handoff may concisely restate an approved fact when the restatement cites that owner and cannot conflict with it. The restatement does not become a second owner. A render, prototype, recommendation, audit, validation result, or parity record is governed evidence, not canon.

## Authority interface

Before treating a material choice as approved, identify:

- the authority source and scope;
- which decisions the current human or policy may approve;
- protected boundaries that must not change silently;
- current product/design-system canon and Design Contract references, with their effectivity statuses;
- the destination for conflicts or missing authority.

The universal skills do not assume particular organizational roles. Consumer policy determines who owns product, brand, regulatory, information-architecture, analytics, or other decisions and how conflicts are resolved.

Always follow stricter consumer policy. When no stricter policy is supplied, an explicit scoped instruction or selection from the user commissioning the current task is valid authority for that scope. Silence, reactions, vague approval, and an agent’s own preference are not authority.

## Outside-design pre-route

Pass purely engineering work to engineering without design ceremony. Examples include internal refactoring, build configuration, dependency maintenance, or performance work with no design consequence. Re-enter design routing when the work changes or may change product/UI behavior, accessibility, interaction states, content meaning, visual or system rules, or an effective Design Contract.

## Observation does not activate operation

Reading an API, data model, database contract, implementation file, or operational record as permitted design evidence does not by itself activate an API, database, engineering, migration, or operational-diagnosis workflow. Activate those workflows only for an authorized mutation or implementation, an operational diagnosis, or an explicit consumer-policy requirement for that operational specialist. Record observed operational sources and their revisions in design lineage while keeping the operational workflow inactive.

Never weaken a consumer repository's more specific routing or permission rule. When its policy requires an operational review for a particular observation or proposed design change, that stronger rule controls.

## Materiality

A decision is **material** when changing it could alter user outcomes, task flow, information architecture, routes, terminology or meaning, data or fields, permissions, destructive or recovery behavior, accessibility expectations, responsive behavior that changes meaning, product identity, design-system posture, or the choice between materially different solutions.

A change is **routine conformance** when all three conditions hold:

- effective product canon, effective design-system canon, or an effective Design Contract already determines the result;
- evidence shows no new product meaning or interaction choice;
- the work only restores or applies that rule.

Record the scope, controlling reference, evidence, and why no new material decision exists. Do not create a new contract or effectivity gate solely for routine work. Do not require a wall of empty sections.

When uncertain, state which consequence makes the classification uncertain. Classify materiality by scope. One unresolved decision blocks only dependent work.

Use the evidence ladder in [packet projections](packet-projections.md): routine, bounded material, or high-impact. Escalate depth for cross-surface reach, irreversibility, consequential uncertainty, system migration, or multiple authorities. Do not calculate a universal risk score.

## Insufficient context is not a generic refusal

Before escalating, inspect all permitted, relevant sources and finish independent work that does not depend on the missing fact. If a material gap remains, return:

1. findings already established;
2. the irreducible missing fact or authority;
3. viable options, when evidence supports them;
4. a recommendation and trade-offs, when a recommendation is supportable;
5. the smallest question that lets work resume.

Do not invent a direction to avoid abstaining. Do not stop merely because some input is imperfect.

## Continuation invariant

Execute the entire safe, relevant workflow chain in the same turn. Routing notes, Task Frames, Design Reads, audits, reuse assessments, explorations, validations, and other process records are intermediate results, not default stopping points.

Stop only when the next dependent step genuinely requires:

- an irreducible human-owned fact, material selection, or effectivity decision;
- evidence or a tool that is unavailable after permitted alternatives are exhausted; or
- an external action that the current authority does not allow.

Use only the workflows the task needs. Do not invoke every skill mechanically, repeat the same intake in multiple skills, or perform design ceremony for engineering-only work.

## Controlled finding vocabulary

Classify each design-surface finding as exactly one of: `implementation discrepancy`, `contract gap`, `design debt`, `product question`, or `inconclusive observation`.

Classify each implementation-parity difference as exactly one of: `implementation defect`, `contract gap`, `inconclusive observation`, or `proposed material delta requiring owner approval`.

Do not shorten these labels or substitute synonyms in an audit, handoff verification plan, or parity record.

## Minimal statuses

Use status vocabularies by record type instead of one universal lifecycle.

### Design decision

- `proposed` — a candidate with no decision authority;
- `approved` — authorized for the recorded scope;
- `rejected` — explicitly not selected;
- `superseded` — replaced by a later approved decision;
- `revoked` — authority withdrawn without a replacement.

### Design Contract

- `draft` — incomplete or still resolving material questions;
- `review-ready` — internally validated, awaiting effectivity authority;
- `effective` — approved for implementation in the recorded scope;
- `superseded` — replaced by a later effective contract;
- `revoked` — no longer authorized for implementation.

Validation may recommend `review-ready`. It cannot make a contract `effective`. Implementation requires an effective contract when material design decisions are in scope.

### Design-system canon revision

- `proposed` — drafted content without exact effectivity approval;
- `review-ready` — internally checked exact revision awaiting authority;
- `effective` — explicitly approved and published in the consumer-owned canonical destination;
- `superseded` — historical revision replaced for new work by a named effective revision;
- `revoked` — authority withdrawn, with the safe fallback or absence of one recorded.

Posture approval authorizes change drafting. It does not make the resulting canon revision effective. Publication requires explicit approval of the exact revision. Preserve history and supersession lineage when you publish.

## Decision gates

- **Entry gate:** classify scope and materiality, then continue the accessible design work. The gate routes work. It is not the product.
- **Selection gate:** before specification becomes normative, a human with the required authority selects, combines, rejects, or requests another material direction.
- **Effectivity gate:** an authorized human makes an exact validated Design Contract or design-system canon revision effective. Approval of one does not silently approve the other.
- **Parity gate:** implementation review reports conformance or discrepancy. It cannot rewrite the contract or excuse a material delta.

The agent does not need approval for every research, audit, comparison, or drafting action already inside its authorized scope.

## Conflicts

Prefer the most specific, current, authoritative source within its scope. Do not silently resolve conflicts between product canon, an approved decision, and observed implementation. Record the conflicting claims, their authority and recency, the dependent work, and the smallest decision needed.
