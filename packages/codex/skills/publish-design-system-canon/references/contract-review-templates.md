# Contract, validation, handoff, and parity templates

Use these as proportional Markdown outlines. A material contract should be detailed enough that implementation does not need to invent design meaning. A routine conformance note can be much shorter.

## Design Contract

Author this native contract and its concrete procedures once. The required scope, source authority, status, protected boundaries, freedoms, unresolved choices and implementation handoff meaning remain substantive work. Packet/brief/handoff rendering uses [governed-view assembly](packet-projections.md#governed-view-assembly) without a second authored interpretation.

### Identity and authority

- Title, scope, revision, and status:
- Controlling canon and approved decision references:
- Owner and effectivity authority:
- Supersedes or revoked references:

### Outcome and boundaries

- Commissioned outcome and scope, with authority locators:
- Protected-boundary and implementation-freedom source locators:

These fields organize the approved scope; they do not author new behavioral conditions or exclusions.

### Required experience — source assembly

- Source ID, exact revision, owner, status and accessible full-text locator:
- Complete applicable source units, with definitions and co-applicable dependencies:
- Coverage index: each supplied source unit → included location and relevant acceptance procedure, or evidenced out-of-scope reason:
- Conflicting or unavailable sources and precisely dependent scope:

Carry unchanged text, inline or in included files. Include a complete small source rather than selecting isolated sentences. For larger sources, keep complete applicable sections and dependencies available. A subject index can locate entry, actions, state/recovery, content, permissions, accessibility, responsive/localization and reused patterns; it must not become a rewritten specification or a filter on source applicability.

### Proposals and unresolved choices

For genuinely new material behavior, keep the exact proposed text separate, with origin, scope, alternatives, recommendation, trade-offs, affected existing sources and actual decision/status. A proposal does not override consumed canon. Retain unstructured source evidence unchanged; any normalization requiring a new material interpretation remains proposed. Do not reopen a supplied rule because its implementation or observation is not yet available.

### Acceptance criteria

For each procedure give concrete setup, actions, exact source units supplying expected behavior, and evidence to collect. Include co-applicable sources and relevant contrasting conditions. Do not author another expected-result rule, including in a setup, coverage note or negative assertion. Existing source acceptance rules stay unchanged. Check source → procedure coverage, not just the presence of references; record unavailable observations honestly. Technical implementation remains free unless an authoritative source constrains it.

### Evidence and unknowns

- Source and decision lineage:
- Evidence locators:
- Optional Visual System Projection locator and source revision:
- Approved material Motion Choice Record locators and exact Owner Decision Record IDs/revisions:
- Production-eligible External Asset Candidate Record locators:
- Prototype-only assets and replacement-before-shipping blockers:
- Remaining non-material implementation choices:
- Material gaps that prevent `review-ready` or `effective` status:
- Native handoff: actual implementation authorization or `NOT AUTHORIZED FOR IMPLEMENTATION`, exact pending gate and dependent scope, the separate exact-contract effectivity request when appropriate, return conditions, required parity evidence/environments and relevant asset/motion eligibility from their controlling sources:

## Validation Record

This is native semantic evidence. Findings/verdict/status recommendation and limitations must be actually assessed. Packet rendering copies them; matching bytes or populated fields cannot generate a `pass`.

- Contract identity and revision:
- Sources checked, their authority/status, included full text and source-to-check coverage:
- Result: pass / fail / inconclusive:
- Authority and lineage findings:
- Missing states or contradictions:
- Accessibility, responsive, localization, content, and recovery findings:
- Unsupported, rewritten or non-testable requirements, including hidden conditions in checks, notes, freedoms and gates:
- Material gaps requiring owner decision:
- Proposed corrections and trade-offs:
- Recommended contract status:
- Limitations of validation:

Validation does not approve a direction or silently edit material requirements.

## Implementation Handoff

The following are materialization targets, not a second semantic writing task. Assemble them from the native contract's handoff/source/procedure content, exact governing approvals and observed evidence under [governed-view assembly](packet-projections.md#governed-view-assembly). Preserve every applicable field; an absent source value returns to its native owner, not to invented projection prose.

- Packet identity, revision, freshness, and generated-at date:
- Controlling effective product canon, effective design-system canon, or effective Design Contract reference:
- Approved decision and canon references:
- Evidence package:
- Production-eligible asset locators:
- Motion requirements from the controlling effective source, with requirement references; optional Motion Choice Record evidence locators:
- Prototype-only replacement blockers for dependent shipping scope:
- Acceptance procedures, their expected-behavior source locators and required parity evidence:
- Protected-boundary and implementation-freedom source locators:
- Known non-material evidence notes:
- Source-backed return conditions or actual unresolved material conflict, with dependent scope:

The handoff is the human-readable form of a Coding-Agent Execution Packet. Include the same accessible unchanged source assembly; do not rewrite behavior, exceptions, freedoms or approval rules. Check source coverage and compatibility against the same pinned sources as the Human Decision Brief using [packet projections](packet-projections.md). It creates no design decision or independent normative source.

Include only production-eligible assets in implementation inputs. An unresolved replacement blocks only the shipping scope that depends on that asset. It does not widen implementation freedom or block unrelated work.

## Implementation Parity Record

For each requirement checked:

- controlling requirement reference;
- observed result;
- parity: conforms / differs / not observed / inconclusive;
- evidence locator;
- environment and context;
- observation method or collector;
- capture time;
- limitations;
- user consequence;
- classification (omit for `conforms`): implementation defect / contract gap / inconclusive observation / proposed material delta requiring owner approval;
- responsible next lane.

Conclude with overall coverage, untested states, blocking discrepancies, and the smallest next action. A parity review cannot make an unapproved delta acceptable.

## Reference Alignment Evidence

Use this separate section only when a commissioned reference comparison matters. It does not replace or alter the normative parity result above.

For each comparison:

- Reference Capture Receipt and reference observation:
- Controlling effective product canon, effective design-system canon, or effective Design Contract requirement:
- Implementation observation:
- Alignment: matches reference / intentionally deviates / unintentionally differs / inconclusive:
- Rationale and authority for an intentional deviation:
- Evidence locator, environment, capture time, and limitations:

Reference alignment cannot authorize implementation meaning or hide a contract gap. When a reference and the controlling effective source disagree, follow the controlling effective source. Record the conflict and route any proposed material delta to its owner.
