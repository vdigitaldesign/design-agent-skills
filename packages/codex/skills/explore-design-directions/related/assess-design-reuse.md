---
name: assess-design-reuse
description: Compare existing product patterns, official platform solutions, trusted libraries, and custom design before choosing a UI/UX approach. Use when reuse versus adaptation or custom work is open; do not let popularity or availability substitute for product fit.
---

# Assess Design Reuse

Find the strongest suitable existing solution before you start custom design. Allow custom work when evidence shows that reuse is insufficient.

## Packet mode

- **Carried:** use and update the supplied valid Design Work Packet. Do not reconstruct its intake or reread pinned authority merely to confirm it.
- **Direct single-skill:** when a Reuse Assessment is the complete requested outcome, return it without creating a packet.
- **Direct expansion:** when direct reuse work becomes a material or uncertain multi-skill chain, create exactly one [Design Work Packet](../references/packet-projections.md#design-work-packet) before the first downstream handoff.

Refresh a carried packet only when a required field is missing, a source is stale or conflicting, scope or authority changes, or genuinely new candidate evidence appears.

Without a valid packet, read [authority and status](../references/authority-and-status.md). Use the [Reuse Assessment template](../references/audit-exploration-templates.md) only for a durable or complex comparison. Query or update the [Design Knowledge Index](../references/design-knowledge-index.md) only when candidates or findings should be reusable across tasks. Do not load it or create a permanent entry for incidental research.

## Workflow

1. State the required behavior, material states, constraints, protected boundaries, and current system posture.
2. Inspect relevant candidates in this order when available: effective product pattern, approved design-system primitive, official platform solution, trusted library or established pattern, then custom design.
3. Verify candidates against authoritative or primary sources when practical. Record provenance, freshness, known non-fit, supersession, and any license concern relevant to actual reuse. Do not build a registry for a one-off assessment.
4. Compare functional fit, interaction model, full state coverage, accessibility, responsive and localization behavior, design-system compatibility, customization cost relevant to design, and material gaps.
5. Recommend reuse, bounded adaptation, or custom design. State evidence, trade-offs, residual decisions, and a fallback.

## Decision rules

- Reuse is preferred only when the candidate fits the product outcome and constraints.
- An existing solution is not necessarily correct. Apply the approved design-system posture.
- Popularity, screenshots, or keyword similarity are not design authority.
- Do not adapt a candidate so extensively that custom design would be clearer and safer.
- Custom work is allowed when no candidate fits, but it must receive the same exploration, state design, accessibility, validation, and owner decision as any other material direction.

If evidence is incomplete, complete the comparison that the evidence permits. Return viable options, trade-offs, and the irreducible missing fact. Include a recommendation when supportable. Send open material choices to [explore-design-directions](../SKILL.md).

In carried or direct-expansion mode, update the packet with:

- the current step;
- the Reuse Assessment locator and revision;
- candidate evidence;
- the recommendation;
- residual decisions;
- findings to preserve;
- the active sequence;
- the next gate and stop.

In direct single-skill mode, return the native assessment without a Design Work Packet.

An implementation, API, or data contract inspected for candidate fit remains evidence. It does not activate an operational workflow without mutation, implementation, diagnosis, or a stronger consumer rule.

If the assessment establishes provenance, known non-fit, rejection, or supersession evidence useful across tasks, send only that reusable learning to [maintain-design-knowledge](maintain-design-knowledge.md). Do not create an index entry for ordinary candidate comparison.
