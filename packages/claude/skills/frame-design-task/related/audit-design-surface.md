---
name: audit-design-surface
description: Audit an existing interface or journey for usability, interaction states, accessibility, responsive behavior, content, coherence, and contract gaps. Use for evidence-backed design critique; do not modify implementation or silently redesign the product.
---

# Audit Design Surface

Explain how the current surface behaves, where it helps or harms the user, and which next action each finding requires.

## Packet mode

- **Carried:** use and update the supplied valid Design Work Packet. Do not reconstruct its intake or reread pinned authority merely to confirm it.
- **Direct single-skill:** when a surface audit is the complete requested outcome, return the native audit without creating a packet.
- **Direct expansion:** when direct audit work becomes a material or uncertain multi-skill chain, create exactly one [Design Work Packet](../references/packet-projections.md#design-work-packet) before the first downstream handoff.

Refresh a carried packet only when a required field is missing, a source is stale or conflicting, scope or authority changes, or genuinely new evidence appears.

Without a valid packet, read [authority and status](../references/authority-and-status.md). Load the [Design Surface Audit template](../references/audit-exploration-templates.md) only when a durable audit record is required. Use [practical design checklists](../references/quality-checklists.md) only when the requested lenses are not already established or the impact warrants deeper coverage.

When visual quality or identity is in scope, load [visual-direction craft](../references/visual-craft.md). Load the whole [product profile and tools](../references/product-profile-and-tools.md) reference only when evidence depends on capture, state exercise, accessibility tooling, external references, consumer mappings, or connected retrieval.

If external reference evidence is part of the commission, create or use the canonical [Reference Capture Receipt](../references/product-profile-and-tools.md#reference-capture-receipt) before comparison. Reuse a valid receipt if its source, intent, scope, freshness, permissions, and limitations still match. If none exists, perform the canonical [preflight and lowest-sufficient-evidence fallback](../references/product-profile-and-tools.md#normalized-limitations-and-fallbacks), then create the receipt. Direct invocation does not require unrelated framing. Report commissioned reference comparison with the central [Reference Alignment Evidence](../references/contract-review-templates.md#reference-alignment-evidence) template. Keep it separate from canon-backed findings and implementation parity.

## Audit procedure

1. Bound the user outcome, surface, paths, states, environments, viewports, and evidence method.
2. Inspect the accessible current experience before proposing changes. Include representative happy, edge, failure, permission, recovery, keyboard, narrow-layout, localization, and RTL conditions when relevant.
3. Compare observations with effective product canon, effective design-system canon, or an effective Design Contract when one exists. Do not use personal taste as the expected source.
4. Record strengths worth preserving. Record findings with evidence, user consequence, scope, confidence, and affected states. For visual findings, identify the broken relationship, such as hierarchy, rhythm, optical balance, typography, density, affordance, coherence, or polish. Do not substitute taste adjectives for that relationship.
5. Classify each finding as an implementation discrepancy, contract gap, design debt, product question, or inconclusive observation.
6. Cluster repeated symptoms into underlying causes without overstating certainty.
7. Continue into the smallest next workflow: routine implementation correction, context reconstruction, reuse assessment, material exploration, system assessment, or contract repair. Stop only at a genuine blocker in the shared continuation invariant.

An observed API, data, or database contract may support a finding without activating its operational workflow. Keep that workflow explicitly inactive unless mutation, implementation, operational diagnosis, or stronger consumer policy requires it.

In carried or direct-expansion mode, update the packet with:

- the current step;
- the Surface Audit locator and revision;
- findings to preserve and new findings;
- source evidence;
- the active/inactive route;
- resolved and new gates;
- the next step and stop.

In direct single-skill mode, return the native audit without a Design Work Packet.

## Severity and recommendations

Base priority on user consequence, frequency or reach when known, reversibility, safety, accessibility, and dependency. Do not use aesthetic intensity to set priority. Distinguish evidence from inference.

For material problems, provide viable options, a recommendation, and trade-offs. Preserve the owner selection gate. For routine discrepancies, cite the controlling requirement and do not manufacture a redesign exercise.

## Boundaries

- Do not edit code or present a mockup as canon.
- Do not infer that inconsistent implementation proves the design system should be replaced.
- Do not call unobserved states correct or broken. Mark them unobserved.
- Do not promote observed reference motion into a recommendation without a user/product job, applicable constraints, and authority.
- Maker self-review is supporting evidence, not final proof.

Use [audit-design-system](audit-design-system.md) when the evidence indicates a system-level coverage or governance problem.

When repeated cross-task evidence establishes a reusable failure pattern or known non-fit, route that bounded learning to [maintain-design-knowledge](maintain-design-knowledge.md). Keep product-specific findings in the audit.
