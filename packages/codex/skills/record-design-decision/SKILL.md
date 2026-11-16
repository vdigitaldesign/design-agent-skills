---
name: record-design-decision
description: Turn an authorized human selection, combination, rejection, or request for another round into a scoped design decision record. Use after material alternatives are presented; do not infer approval or fill details the human did not decide.
---

# Record Design Decision

Preserve the human’s material choice precisely enough that later specification cannot substitute the agent’s preference.

## Packet mode

- **Carried:** use and update the supplied valid Design Work Packet. Do not reconstruct its intake or reread pinned authority merely to confirm it.
- **Direct single-skill:** when recording the decision is the complete requested outcome, return the Owner Decision Record without creating a packet.
- **Direct expansion:** when direct decision recording becomes a material or uncertain multi-skill chain, create exactly one [Design Work Packet](references/packet-projections.md#design-work-packet) before the first downstream handoff, using the [governed-view assembly](references/packet-projections.md#governed-view-assembly) from the existing sources and native records.

Refresh a carried packet only when a required field is missing, a source is stale or conflicting, scope or authority changes, or genuinely new evidence appears.

Without a valid packet, read [authority and status](references/authority-and-status.md). Use the [Owner Decision Record template](references/audit-exploration-templates.md) for the native decision. Materialize a commissioned non-normative [Human Decision Brief](references/packet-projections.md#governed-view-assembly) from that exact decision and its evidence; do not independently author its interpretation. When a packet exists, pin the brief to the same source packet revision. For a direct single-skill output, pin it to the exact native evidence/decision revisions.

## Workflow

Author the decision meaning once in the Owner Decision Record: actual response, selection/modifications, scope, unresolved material questions and authority. Reuse supplied exact decision text where it already governs. Keep semantic classification here; the assembly step copies its values and locators into the required packet/brief without making another choice.

1. Verify the decision scope, authority source, options presented, and the exact human response. Follow stricter consumer policy. Otherwise, an explicit scoped selection from the user commissioning the current task is valid authority for that scope.
2. Record whether the human selected one direction, combined named parts, rejected directions, or requested another round.
3. Capture explicit modifications, rationale, accepted trade-offs, protected boundaries, and facts that remain unchanged.
4. Preserve the exact human response, selected artifact/revision and explicit modifications, with evidence and authority scope. Include the selected normative text unchanged when self-contained delivery is needed. A concise rationale or summary is navigation, not a replacement rule. An ambiguous combination or modification remains a scoped question rather than a silently authored source. Preserve the single normative owner; do not request a new approval for an already exact, authorized selection.
5. Mark the decision `approved`, `rejected`, or still `proposed` according to the actual response.
6. Identify unresolved details and decide whether each is material or a downstream implementation freedom.
7. Check that the Human Decision Brief and decision record cite the same option/artifact revisions and have no material addition or omission.

## Ambiguous selections

Do not convert “looks good,” a reaction, silence, vague approval, or an agent ranking into approval when the material scope is unclear. Explain the ambiguity and ask the smallest bounded question. Include the current findings, viable interpretations, recommendation, and trade-offs so the human can decide efficiently.

Do not fill missing interaction, content, state, or system decisions while recording a selection. If combining directions creates a new material direction, return it for explicit approval. Do not treat it as selected.

## Next step

An approved decision authorizes its recorded material choice, not an entire architecture or implementation. Send it with lineage to [write-design-contract](related/write-design-contract.md) and continue the safe chain in the same turn. If the human requests another round, return to [explore-design-directions](related/explore-design-directions.md) with the feedback preserved.

In carried or direct-expansion mode, materialize the following packet updates from this native decision and actual workflow events. Preserve the packet's uniquely owned route/gate facts; do not rewrite its source context or create another decision interpretation:


- the current step;
- Owner Decision Record and Human Decision Brief locators and revisions;
- selected/rejected evidence;
- findings and trade-offs to preserve;
- the resolved selection gate;
- any new gate;
- the active sequence;
- the next step and stop.

In direct single-skill mode, return the native decision output without a Design Work Packet.
