---
name: prototype-design-directions
description: Create decision-useful UI/UX prototypes, annotated wireframes, static mocks, or design-lab comparisons for material directions. Use when tangible exploration is explicitly requested or interaction, timing, spatial behavior, hierarchy, or visual composition must be experienced; do not produce production frontend code or canon.
---

# Prototype Design Directions

Produce the smallest tangible evidence that lets the authorized human compare or validate a material direction.

## Packet mode

- **Carried:** use and update the supplied valid Design Work Packet. Do not reconstruct its intake or reread pinned authority merely to confirm it.
- **Direct single-skill:** when the prototype, mock, wireframe, or Design Lab is the complete requested outcome, return it without creating a packet.
- **Direct expansion:** when direct prototype work becomes a material or uncertain multi-skill chain, create exactly one [Design Work Packet](../references/packet-projections.md#design-work-packet) before the first downstream handoff.

Refresh a carried packet only when a required field is missing, a source is stale or conflicting, scope or authority changes, or genuinely new prototype evidence appears.

Without a valid packet, read [authority and status](../references/authority-and-status.md). Use the [Exploration Set template](../references/audit-exploration-templates.md) for an annotated wireframe, static mock, or other low-fidelity comparison. Load the [Design Lab protocol](../references/design-lab-protocol.md) only when interactive behavior or controlled multi-variant comparison needs its full protocol. Use [practical design checklists](../references/quality-checklists.md) when coverage is not already carried or the impact warrants it. Load [visual-direction craft](../references/visual-craft.md) when motion or external assets affect the comparison.

Keep operational workflows declared in the packet inactive when API, data, implementation, or operational material is only observed evidence. Re-route only for an actual mutation, implementation, diagnosis trigger, or a stronger consumer-policy requirement.

When material external references influence prototype evidence, create or use the canonical [Reference Capture Receipt](../references/product-profile-and-tools.md#reference-capture-receipt) before using those references. Reuse a valid receipt if its source, intent, scope, freshness, permissions, and limitations still match. Otherwise, perform the canonical [preflight and lowest-sufficient-evidence fallback](../references/product-profile-and-tools.md#normalized-limitations-and-fallbacks) and create a receipt. Direct invocation remains valid and does not require unrelated framing.

## Establish the decision

Reuse the current Task Frame, Design Read, audits, reuse assessment, protected boundaries, and exploration work. Do not repeat intake that is already clear. If a material fact is missing, finish every safe artifact decision first. Then return the bounded gap with findings, viable options, recommendation, and trade-offs.

## Choose the artifact

- Create an interactive prototype when timing, transition, motion, spatial behavior, input handling, or state changes must be experienced.
- Create an annotated wireframe or static mock when hierarchy, layout, density, content structure, or visual composition is the material question.
- Use a Design Lab when two or three controlled directions need side-by-side comparison. Preserve fixed facts and name the variable axes. Use comparable frames, states, viewports, and content. Supply a repeatable interaction script. Record artifact/media locators, revision, limitations, recommendation, and selection lineage.

If the direction is not selected, keep materially different variants comparable. Use the same product facts, content, constraints, and evaluation conditions. If a direction is already approved, prototype only the unresolved behavior. Do not reopen settled decisions.

## Required evidence

Show the relevant entry, primary flow, key states, permissions, failure or recovery, accessibility behavior, and responsive condition.

When motion is part of an interactive brief, choose purposeful transitions for meaningful state changes across the artifact. Include relevant disclosure, selection, feedback, and dismissal. A first-screen entrance does not demonstrate these relationships. Keep steady content still when motion adds no value.

For a chosen transition, make both directions and interruption or rapid reversal usable. Preserve keyboard/touch behavior, focus, and a reduced- or non-motion equivalent. For example, inspect an accordion's content and surrounding layout while opening and closing, not just its indicator or final open state. Demonstrate the chosen behavior in the prototype. In its existing evidence summary, distinguish observed motion from unverified intent. Do not add a motion quota or a separate reporting ritual.

For each artifact record:

- direction and material question;
- artifact locator or embedded representation;
- what is interactive or annotated;
- evidence, assumptions, and protected boundaries;
- what the artifact demonstrates and does not demonstrate;
- accessibility, state, responsive, localization, and RTL limitations;
- comparison findings, recommendation, and trade-offs.

Use available design or prototyping tools when authorized. Disposable sandbox prototype code is allowed when it is the smallest useful interaction evidence. Keep that code isolated, record its limitations and revision, and mark it forbidden for production reuse. Do not write production frontend code merely to make a prototype.

Carry central motion and asset record IDs and revisions into the Lab. Do not copy their fields. A remote or reference-site asset remains prototype-only unless the central record establishes production eligibility. It must never enter a production handoff merely because it appeared in a selected prototype.

## Authority and continuation

A prototype, wireframe, mock, or render is evidence, never canon. Ask the authorized human to select, combine, reject, or request another round when a material choice remains. If an explicit scoped selection is already available, record it and continue toward the draft Design Contract in the same turn. Stop only at a genuine selection, effectivity, evidence/tool, or authorization blocker.

If comparison evidence establishes a reusable mechanism or known non-fit beyond the current product decision, route only that bounded learning to [maintain-design-knowledge](../SKILL.md). The Lab itself and its product facts remain in their governed task records and, when packet mode applies, are linked from the packet.

In carried or direct-expansion mode, update the packet with:

- the current step;
- artifact and media locators and revisions;
- limitations;
- comparison findings;
- the recommendation;
- findings to preserve;
- the selection gate/lineage;
- the next step and stop.

In direct single-skill mode, return the native prototype evidence without a Design Work Packet. Never create a packet per artifact or variant.
