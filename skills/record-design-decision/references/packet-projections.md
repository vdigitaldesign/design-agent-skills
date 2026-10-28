# Evidence ladder, design packets, and shared-canon projections

Use the lightest packet that makes the work safe and useful. Tiers add depth to the evidence. They do not create a numeric risk score or require empty `N/A` sections.

## Evidence ladder

### Routine packet

Use this packet when effective product canon, effective design-system canon, or an effective Design Contract already determines the exact result, and the work introduces no new design meaning.

Include:

- **Controlling revision:** effective product canon, effective design-system canon, or an effective Design Contract.
- **Observed delta:** current evidence versus that exact requirement.
- **Exact correction:** one bounded observable change already determined by the controlling revision.
- **Protected boundaries:** conforming behavior, content, states, accessibility, and out-of-scope consumers that must not change.
- **Acceptance and parity request:** the smallest implementation evidence needed to check the correction and protected boundaries.
- **Return to design:** only a canon conflict, material delta, unresolved applicability, or necessary scope expansion.

Use those six labels as the complete default routine-handoff shape. Keep each concise. Do not duplicate them as routing, finding, source, or freshness sections. Before implementation evidence exists, request the evidence. Do not yet write a full future parity procedure or environment matrix.

Do not create a Design Work Packet, Task Frame, Design Read, Human Decision Brief, review Finding/Repair/Falsifier sections, exploration, new contract, selection, or effectivity gate merely to complete this packet. Do not turn routine work into ceremony by applying completeness requirements from higher tiers. Use the controlling source text or its precise locator for existing behavior; the six labels must not introduce replacement conditions, freedoms or approval rules.

### Compact routine-handoff shape

```markdown
## Routine handoff

- Controlling revision:
- Observed delta:
- Exact correction:
- Protected boundaries:
- Acceptance and parity request:
- Return to design:
```

### Bounded material packet

Use for a scoped, reasonably reversible material choice with contained consumers.

Add as relevant:

- Task Frame and Design Read;
- protected boundaries and authority;
- reuse/system assessment;
- materially different directions and the smallest decision-useful artifact;
- recommendation and human selection;
- Design Contract, validation, effectivity decision, execution packet, and parity plan.

### High-impact packet

Use when work is cross-surface, difficult to reverse, destructive or safety-sensitive, system-wide, high-uncertainty, or dependent on several authorities.

Deepen the bounded packet with the evidence that the actual risk requires:

- multiple journeys, consumer surfaces, environments, platforms, or cohorts;
- stronger research and contradictory-source treatment;
- full system posture, compatibility, adoption, migration, rollback, and exception analysis;
- additional authority resolution and protected-boundary review;
- broader accessibility, localization, RTL, privacy, content, and failure/recovery evidence;
- independent visual, interaction/accessibility, system, and parity critique where useful.

Move to a higher tier when new evidence reveals larger reach, lower reversibility, authority conflict, or consequential unknowns. Do not use a high-impact label to justify irrelevant bureaucracy.

## Governed-view assembly

Separate semantic authorship from rendering throughout a commissioned chain. Native decision/proposal/contract/acceptance/validation records own the judgments; the packet and human/coding projections locate or reproduce those same values. Author a scope, classification, choice, unknown, gate or verdict only at its native owner. Uniquely owned routing/gate decisions and actual workflow events still belong to the packet; they are recorded once and then carried unchanged, not inferred by a renderer.

1. Finish the native semantic content needed for the current step, including alternatives/trade-offs, actual authority/status, unresolved choices, concrete procedures and handoff/parity meaning. Keep the original authoritative sources available. Required record identities and outcomes do not disappear.
2. Materialize the commissioned views with ordinary authorized file operations: copy exact already-owned values/blocks, insert exact accessible source locators, or include the complete scoped native record. Use tool-backed copying for reproduced text rather than composing another summary. A tool-written file containing newly authored projection prose is not mechanical assembly; preserve the exact copied source blocks/locators and their readback evidence. Where records share a file, use their exact existing sections/locators without exporting unrelated scope.
3. Presentation labels, file names and observed revision/hash/time metadata may be formatted. Behavior, scope, freedoms, risks, unknowns, approval questions and verdicts are copied/located from their native owners; no new prose interpreting them is supplied by assembly. Read back reproduced blocks and their source revisions. Resolve links within the actual delivered unit.
4. If a required value is not available, return that content requirement to its existing native author in the same bounded workflow. A missing recording field is not itself evidence of a missing product fact or a new approval gate. Preserve any real unresolved material blocker and its dependent scope; do not manufacture a complete/ready handoff.
5. After a native correction or a real authority event, regenerate only affected views and their revision/lineage metadata. Preserve all real freshness/equivalence checks below. A validation verdict applies only to its exact native revisions; re-check affected semantic content after a native change before presenting a ready result. Never silently repair meaning inside a projection. A failed or unavailable assembly/readback remains explicit incomplete evidence, not qualification. No new model call, external write or deployment is authorized by this step.

| Materialized target | Exact value owner / supplied evidence |
|---|---|
| Packet task, context, authority, source inventory, record revisions and preserved findings | Original commissioning sources and current native decision/proposal/contract/validation, plus the packet's uniquely owned route/gate facts and actual events; no second source classification |
| Human brief choice, options, recommendation/trade-offs, protected boundaries, risks/unknowns and exact question | Current native proposal/decision, contract/validation constraints and their controlling evidence; each exact requested decision is authored at its native owner |
| Coding packet scope, sources, procedures, boundaries/freedoms, return conditions, parity and implementation authorization | Native contract/handoff and actual separate approval/publication records; draft authorization wording is carried unchanged |
| Approval/publication/adoption receipt metadata | Actual scoped human response and observed authorized write/readback/adoption; no simulated event |

This is literal assembly, not a behavior compiler, source-selection manifest, new semantic model or verdict engine. It neither chooses applicable source units nor proves the native content correct. Use the existing file tools; when they cannot produce/verify the requested usable unit, report that actual scoped blocker and retain native work. A mechanically exact unit with bad AC, an omitted applicable case or an ambiguous proposal still fails substantive validation. Routine conformance remains the six-label native handoff with no extra packet/assembly ceremony.

## Design Work Packet

Use one compact Design Work Packet when a material or uncertain request crosses more than one design workflow. `design-router` creates it before the first downstream skill. A directly invoked specialist creates it before its first downstream handoff only when the direct task expands into such a chain.

Carry the same packet ID through the chain. Revise it only as new evidence or scope requires. Materialize its repeated fields through [governed-view assembly](#governed-view-assembly), preserving its uniquely owned route/gate decisions and actual events. The packet is a governed assembly and lineage record. It is not normative canon and does not replace the specialist outputs it links.

Every directly invoked specialist chooses exactly one entry mode:

- consume and update a supplied valid packet;
- return its native output without a packet when the direct task genuinely ends with that skill; or
- when direct work expands into a material or uncertain multi-skill chain, create exactly one packet before the first downstream handoff.

Do not create a packet retroactively for a completed single-skill task. Do not create a separate packet for each specialist.

### Identity and task

- Packet ID, revision, evidence tier, created/updated time, and current custodian:
- Requested outcome, in-scope and out-of-scope surfaces/users/moments, and deliverable:
- Authority source/scope, materiality and reason, permissions, and unresolved authority:

### Carried context

- Facts, inferences, unknowns, and conflicts, each with exact owner/evidence locator and revision when one exists; for an unknown, record the inspected evidence boundary:
- Protected boundaries:
- Exact source locators, revisions/statuses, observed-at or verified-at dates, freshness, and limitations:
- Included governed records with IDs/revisions/statuses and locators:

### Route and stop

- Active workflow sequence, current step, and why each active workflow is required:
- Explicitly inactive workflows or unambiguous workflow groups, with the absent trigger or boundary—including operational domains observed only as evidence:
- Work completed and findings that later steps must preserve:
- Next human gate or irreducible stop condition, its authority, and the dependent scope it blocks:
- Projection revisions issued from this packet, when any:

Name inactive workflows concisely. Do not list every installed capability when a clear group and absent trigger are unambiguous.

### Validity and refresh

A carried packet is valid when all of these conditions hold:

- its task scope still matches;
- every field required by the downstream step is present or explicitly unknown;
- source statuses/freshness remain usable;
- conflicts are visible;
- the active sequence and next gate are current.

Downstream skills use a valid packet. They do not reconstruct the same context or reread authority and source material merely to confirm it. Refresh the same packet ID only when:

- a required field is missing rather than explicitly unknown;
- a required source is stale, unavailable, or conflicts with another governing source;
- the requested scope or authority changes; or
- the downstream task genuinely requires new evidence.

Record the changed fields, reason, new evidence locator, and packet revision. Do not create a fresh packet for each skill. Keep the exact owner/revision with each concise summary. Summaries locate source meaning and gain no independent authority; execution uses the unchanged controlling source text.

## Human Decision Brief

This non-normative projection focuses on a decision and derives from a pinned packet revision. Materialize the fields below from the exact native decision/proposal through [governed-view assembly](#governed-view-assembly). They are required content, not independent summary-writing assignments.

- Decision and why it is material:
- Authority and protected boundaries:
- Facts, inferences, unknowns, and evidence limitations:
- Comparable options with artifact/media locators:
- Recommendation, trade-offs, risks, and falsifying evidence:
- Exact selection or effectivity question:
- Source packet ID/revision and generated-at date:

It reproduces the native decision/proposal values or their exact accessible owner/revision locators through governed-view assembly. Do not omit a material unknown merely to simplify the decision.

## Coding-Agent Execution Packet

This is a non-normative implementation projection from effective sources. It contains no new design decision. Materialize the fields below from the native contract/handoff, exact sources and actual authority/evidence records through [governed-view assembly](#governed-view-assembly). Do not independently compose their meaning.

- Target outcome and implementation scope:
- Controlling effective product canon, effective design-system canon, or effective Design Contract IDs/revisions, as applicable:
- Approved decisions and effectivity references:
- Accessible unchanged source assembly and requirement locators:
- Source coverage for relevant state, content, accessibility, responsive, localization, RTL and theme scope:
- Acceptance procedures, expected-behavior source locators and evidence to collect:
- Source locators for protected boundaries, forbidden changes and implementation freedoms:
- Evidence/artifact locators and their non-canonical limitations:
- Required parity evidence and verification environments:
- Source-backed return conditions or actual unresolved material conflict and its dependent scope:
- Source packet ID/revision and generated-at date:

This packet carries the same normative source units as the contract; headings, procedures, notes and boundaries cannot supply a second version of their behavior. Make the full controlling text accessible to the receiver, not just IDs or summaries. Start material implementation only when every required normative source is effective. A draft execution packet must say `NOT AUTHORIZED FOR IMPLEMENTATION` and identify the exact missing gate.

## Visual System Projection

This optional, non-normative projection makes approved visual meaning easier for humans or agents to retrieve. It is not a Design Contract or design-system canon. It does not become a second owner of facts.

Record the projection ID and revision, exact source IDs and revisions, generated-at date, and limitations. Then cover these nine sections:

1. **Identity, scope, authority, and source revisions.**
2. **Visual premise and hierarchy.**
3. **Semantic color, typography, spacing, shape, and depth.**
4. **Component and state expression.**
5. **Layout and responsive behavior.**
6. **Motion and feedback purpose, including reduced- or non-motion fallback.**
7. **Imagery and icon provenance, including fallbacks.**
8. **Required, allowed, forbidden, and known non-fit choices.**
9. **Unresolved items and return-to-design conditions.**

A Visual System Projection derives only from an exact approved decision, effective canon, or an effective Design Contract. If its source is an approved decision that is not yet effective, the projection may support contract drafting. In that case, it must state `NOT AUTHORIZED FOR IMPLEMENTATION`. A Coding-Agent Execution Packet may rely only on effective sources.

The projection cannot add behavior or authority, close an unknown, turn a proposal into an approval, or make a source effective. Regenerate or revise the projection when its source changes. Never edit the projection as if it were canon.

## Freshness and equivalence check

Before using any projection—including a Human Decision Brief, Coding-Agent Execution Packet, or Visual System Projection:

1. Resolve every referenced source and confirm its revision/status is still current for the scope.
2. Compare the projection’s requirements, options, boundaries, unknowns, and effectivity state with its pinned sources.
3. Confirm summaries preserve meaning and cite the single normative owner. In a contract or execution packet, check that existing normative text is unchanged and available, applicable sources are covered, and procedures/proposals do not add or suppress source behavior.
4. Flag missing, added, stale, or contradictory content. Do not silently repair material meaning inside a projection.
5. Regenerate the projection from its current native sources through governed-view assembly, recording the new projection revision. Correct semantic meaning at its native owner; presentation-only edits must preserve the exact owned values.

Equivalence means no material addition, omission, contradiction, or authority change. Summaries and presentation may differ; normative source units in a contract or execution packet remain unchanged. Neither identical bytes nor compiler-generated output proves correct applicability, completeness or proposal compatibility.

## Worked handoff example

Illustrative consumer task, not product canon or an additional required packet. The source already specifies the behavior; engineering chooses its technical implementation.

- **Source:** effective `DC-LIB r2`, requirement `R-4`: after a definitive archive rejection, keep the selection and show the supplied rejection reason. A transport timeout is an unknown outcome, not a rejection; preserve the selection while reading status for that same operation.
- **Authority:** the recorded owner decision makes this exact revision effective and explicitly authorizes local implementation. The consumer also records that this decision satisfies its specification-approval gate. Deployment remains outside scope.
- **Acceptance procedure `AC-4`, checking `R-4`:** provide controlled definitive-rejection and transport-timeout responses in separate setups. Initiate archive and capture selected IDs, supplied service outcome/reason, visible status, request log and original operation ID. Use the complete unchanged `R-4` above for expectations; do not author a second rule in this procedure. Record unavailable observations rather than claiming a result.
- **Execution packet:** cite `DC-LIB r2/R-4`, its effectivity decision and `AC-4`; request the selection, displayed outcome and operation-ID evidence. Preserve other effective requirements by reference. The packet adds no rule or approval.
- **Engineering task:** implement and test rejection/unknown handling against `R-4/AC-4`; choose the state representation and status-read mechanism within the contract's freedoms. Return a proposed behavior change to design; continue unrelated authorized work.

An invalid projection says “ask the owner again before this already authorized local implementation” or “a timeout is a failed archive.” The first invents a gate; the second changes the source outcome. If consumer policy instead leaves a required technical approval outstanding, name that real gate and its dependent scope. Effective design authority does not silently waive it.

