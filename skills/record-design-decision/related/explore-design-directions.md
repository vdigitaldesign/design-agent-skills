---
name: explore-design-directions
description: Develop and compare materially different UI/UX directions, choose the smallest decision-useful artifact, and present a recommendation for human selection. Use when a material design choice remains open; route explicit prototype, mockup, or design-lab work to prototype-design-directions.
---

# Explore Design Directions

Produce a bounded choice that helps the human decide. Cosmetic variants alone are not enough.

## Packet mode

- **Carried:** use and update the supplied valid Design Work Packet. Do not reconstruct its intake or reread pinned authority merely to confirm it.
- **Direct single-skill:** when an Exploration Set is the complete requested outcome, return it without creating a packet.
- **Direct expansion:** when direct exploration becomes a material or uncertain multi-skill chain, create exactly one [Design Work Packet](../references/packet-projections.md#design-work-packet) before the first downstream handoff.

Refresh a carried packet only when a required field is missing, a source is stale or conflicting, scope or authority changes, or genuinely new evidence appears.

Without a valid packet, read [authority and status](../references/authority-and-status.md). Load the [Exploration Set template](../references/audit-exploration-templates.md) only for a durable exploration record. Load [practical design checklists](../references/quality-checklists.md) only when the needed lenses are not already carried or the impact needs deeper coverage.

When material external references influence directions, create or use the canonical [Reference Capture Receipt](../references/product-profile-and-tools.md#reference-capture-receipt) before using those references. Reuse a valid receipt if its source, intent, scope, freshness, permissions, and limitations still match. Otherwise, perform the canonical [preflight and lowest-sufficient-evidence fallback](../references/product-profile-and-tools.md#normalized-limitations-and-fallbacks) and create a receipt. Direct invocation remains valid and does not require unrelated framing.

## Before exploring

Confirm the material question, supplied facts, inferences, unknowns, protected boundaries, reuse assessment, and decision authority. Inspect permitted sources and finish any safe context or audit work first.

If an irreducible fact prevents responsible directions, abstain before you generate them. Return findings, trade-offs, and the smallest question needed. Include viable interpretations when evidence supports them and a recommendation if possible.

## Create meaningful directions

When a real material choice exists, usually create two or three directions. Vary interaction structure, information hierarchy, state or recovery model, density, composition, or another axis relevant to the decision. Do not relabel minor visual variations as alternatives.

For each direction:

- explain the user flow and information structure;
- show how it handles important states, permissions, failure, and recovery;
- identify reuse versus custom work;
- preserve protected boundaries;
- state evidence, assumptions, unknowns, accessibility and responsive implications;
- name strengths, costs, risks, and conditions where it fits.

When visual character or composition is a material axis, use [develop-visual-direction](develop-visual-direction.md). Make the variants resolve hierarchy, rhythm, optical balance, typography, color relationships, density, imagery, affordance, coherence, distinctiveness, and polish. Do not rely on adjectives alone.

Avoid universal pseudo-precise scores. Compare trade-offs in terms of the product outcome and evidence.

## Produce decision-useful evidence

Choose the smallest artifact that resolves the material choice:

- Use [prototype-design-directions](prototype-design-directions.md) when a prototype, mockup, or design lab is explicitly requested, or when interaction timing, motion, spatial behavior, state transitions, or visual comparison must be experienced.
- Produce an annotated wireframe or static mock when hierarchy, layout, density, or visual composition is the material question.
- Use prose only when it genuinely makes the alternatives and trade-offs decidable without hiding spatial or interaction uncertainty.

A low-fidelity comparison does not require the full Design Lab protocol. Load that protocol only through prototype work when controlled tangible variants, interaction scripts, media locators, or comparable rendered states are necessary.

Record what the artifact demonstrates and what it does not. Prototypes, wireframes, mocks, and renders are evidence. They never become canon by themselves.

## Recommend and hand off to the human

Make a recommendation when the evidence supports one. State why, the trade-offs the owner accepts, and what new evidence would change the recommendation.

Ask the authorized human to select, combine, reject, or request another round. Do not begin specification from an unrecorded material preference. Once the human responds, use [record-design-decision](../SKILL.md). Continue the safe chain in the same turn when the selection is already explicit.

In carried or direct-expansion mode, update the packet with:

- the current step;
- the Exploration Set and artifact locators and revisions;
- the recommendation;
- findings to preserve;
- the unresolved choice;
- the selection gate;
- the next step and stop.

In direct single-skill mode, return the native exploration without a Design Work Packet.

An observed API or data contract constrains directions. It does not activate an operational workflow unless a stronger consumer rule or actual operational task requires it.
