# Audit, reuse, exploration, and decision templates

These are output shapes, not schemas. Adapt depth to the decision risk.

## Design Surface Audit

### Scope and evidence

- User outcome and surface:
- States, viewports, inputs, and paths inspected:
- Evidence locators, environment, capture time, and limitations:
- Reference Capture Receipt IDs/revisions and commissioned intent, when applicable:

### Findings

For each finding:

- observed behavior;
- expected source, when one exists;
- user consequence;
- affected states and users;
- confidence;
- classification: implementation discrepancy / contract gap / design debt / product question / inconclusive observation;
- recommended next action and required authority.

### Coherence summary

- Strengths worth preserving:
- Repeated failure patterns:
- Protected boundaries:
- Material decisions exposed:

When the commission includes reference comparison, record the comparison using the central [Reference Alignment Evidence](contract-review-templates.md#reference-alignment-evidence) shape. Keep it separate from canon-backed audit findings and implementation parity.

Repeated token or style frequency is observed evidence only. It may support a hypothesis, but it does not by itself establish a semantic role, design-system health, or canon.

## Design-System Assessment

### Observed state

- Scope assessed:
- Sources and implemented evidence:
- Foundation/token/theme relationships and drift:
- Component and pattern specification coverage:
- Behavior, content, state, accessibility, and responsive contracts:
- Documentation, ownership, adoption, exception, and maintenance signals:
- Agent-ready retrieval context and evaluation fixtures:
- Maturity by scope: healthy / partial / absent / harmful, with evidence:

### Proposed operating posture

- Posture and exact scope:
- Evidence and rationale:
- What remains unchanged:
- Debt or exceptions accepted:
- Alternatives considered:
- Owner decision required:
- Continuation: consume under effective canon / approved evolution path / bounded owner question:

## Reuse Assessment

### Need

- Required behavior and constraints:
- Effective product or system references:

### Candidates

For each candidate:

- source and authority;
- functional and interaction fit;
- state and accessibility coverage;
- customization or integration cost relevant to design;
- provenance or license concern relevant to reuse;
- material gaps and risks.

### Recommendation

- reuse / adapt / custom;
- rationale and trade-offs;
- residual design decisions;
- fallback if the recommendation cannot be used.

## Exploration Set

### Decision to explore

- Material question:
- Evidence, constraints, and protected boundaries:
- Axes that may vary:

### Directions

For each materially different direction:

- interaction and information structure;
- state and recovery model;
- reuse posture;
- accessibility and responsive implications;
- assumptions and unknowns;
- strengths, costs, and risks;
- evidence or prototype locator, if used.

### Comparison and recommendation

- Meaningful differences:
- Recommendation and why:
- Conditions that would change the recommendation:
- Trade-offs the owner must accept:

## Owner Decision Record

This is the native owner of the interpretation of the human response. Author its semantic content once. Packet and brief fields copy these values or point to this exact accessible revision under [governed-view assembly](packet-projections.md#governed-view-assembly); no second rationale, choice, gap or authority interpretation is written there.

- Decision scope:
- Authority source:
- Options presented:
- Exact human response and selected artifact/revision/text, combination, rejection, or request for another round:
- Explicit modifications:
- Rationale and accepted trade-offs:
- Protected boundaries and unchanged facts:
- Unresolved questions:
- Status and date:
- Inputs and lineage references:

Retain selected normative text unchanged, inline or through an accessible exact revision. Rationale and summaries do not replace it. Do not fill missing details while recording a selection. Return ambiguities that could change the chosen direction to the owner.

## Design-System Change Proposal

This native proposal contains the actual alternatives/recommendation/trade-offs and exact decision request as well as the proposed text. Keep the contract and proposal identities/authority separate. Required projections copy or locate this same material through [governed-view assembly](packet-projections.md#governed-view-assembly).

### Authority and posture

- Approved operating posture and scope:
- Authority source and stricter consumer policy, if any:
- Current effective canon and observed evidence:
- Protected boundaries:

### Smallest scoped change

Include only what the approved posture requires:

- token decisions and relationships;
- component or pattern contract;
- interaction and accessibility states;
- behavior, content, responsive, localization, theme, and platform rules;
- usage/avoid/known-non-fit documentation and retrieval terms;
- agent-ready context and evaluation fixtures;
- approved exceptions, constraints, or debt;
- compatibility, adoption, drift detection, migration, deprecation, and rollback plan where relevant.

### Impact and verification

- Surfaces and consumers affected:
- Preserved behavior:
- Acceptance criteria:
- Migration or adoption sequence:
- Canon destination, revision/supersession plan, and adoption receipt requirements:
- Evidence and validation plan:
- Risks and unresolved material questions:
- Exact requested human choice/effectivity decision, including the proposal ID/revision and its dependent scope:

### Status

- proposed / review-ready / effective / superseded / revoked:
- Effectivity authority and decision reference:

Drafting an approved change posture does not make the proposal effective canon.
