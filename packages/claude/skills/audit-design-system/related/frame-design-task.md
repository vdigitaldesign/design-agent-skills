---
name: frame-design-task
description: Turn an explicit design brief or ambiguous UI/UX scope, materiality, or authority into a bounded Task Frame. Use when those intake questions genuinely need resolution; do not invoke it automatically when a specialist request is already clear.
---

# Frame Design Task

Produce a bounded Task Frame that lets design work advance without hiding authority or duplicating a clear specialist intake. Continue into the next safe workflow in the same turn.

## Packet mode

- **Carried:** use and update the supplied valid Design Work Packet. Do not reconstruct its intake or reread pinned authority merely to confirm it.
- **Direct single-skill:** when framing is the complete requested outcome, return the Task Frame without creating a packet.
- **Direct expansion:** when direct work becomes a material or uncertain multi-skill chain, create exactly one [Design Work Packet](../references/packet-projections.md#design-work-packet) before the first downstream handoff.

Refresh a carried packet only when a required field is missing, a source is stale or conflicting, scope or authority changes, or genuinely new evidence appears.

Without a valid packet, read [authority and status](../references/authority-and-status.md). Use the proportional [Task Frame template](../references/task-context-templates.md) only when the user requested a durable brief or the ambiguity requires one. Use [packet projections](../references/packet-projections.md) when selecting a tier or creating the expanding-direct packet.

When the request supplies or asks to collect an external reference, also read [product profile and tools](../references/product-profile-and-tools.md). Record the source class separately from the commissioned intent: inspiration, benchmark, or explicit reproduction. Confirm permitted influence, collection boundaries, and reproduction/brand-rights authority before routing. `Explicit reproduction` changes comparison scope. It grants no product, brand, asset, or implementation authority.

## Workflow

1. Restate the user or product outcome, not only the requested artifact or UI element.
2. Bound the users, surfaces, moments, deliverable, and explicit exclusions.
3. Identify effective product canon, effective design-system canon, or effective Design Contract references, available decision authority, and protected boundaries.
4. Inspect the permitted evidence needed to classify materiality. Do not decide from wording alone.
5. Classify the task as routine conformance, material, or uncertain and name the consequence that determines the classification.
6. Select routine, bounded material, or high-impact packet depth without a numeric score. Name the reach, reversibility, uncertainty, system, or authority reason for escalation.
7. List material decisions without choosing them. Separate design decisions from downstream code choices.
8. Record work that can proceed now, the next workflow, the human gate, and the smallest scoped stop condition.

## Materiality checks

Treat a choice as material when it may alter user outcomes, flow, information architecture, meaning, fields, permissions, destructive or recovery behavior, accessibility expectations, responsive meaning, identity, system posture, or the choice between materially different solutions.

Treat work as routine only when an effective source determines the result and evidence shows no new product or interaction meaning. A routine frame needs only scope, the controlling reference, evidence, and the reason no new material decision exists.

## Insufficient inputs

Do not stop at “need more context.” Inspect permitted sources and complete independent scoping first. If the remaining gap is material, return established findings, viable interpretations or options, trade-offs, and one bounded question. Include a recommendation if supportable.

## Handoff

- Route missing facts or source conflicts to [reconstruct-design-context](reconstruct-design-context.md).
- Route existing-surface evidence to [audit-design-surface](audit-design-surface.md).
- Route design-system uncertainty to [audit-design-system](../SKILL.md).
- Route open solution choices to [assess-design-reuse](assess-design-reuse.md) or [explore-design-directions](explore-design-directions.md).

The Task Frame does not approve a direction, create product facts, or replace the downstream design work. Do not stop after framing unless the shared continuation invariant identifies a genuine blocker.

In carried or direct-expansion mode, update the packet with:

- the current step;
- the Task Frame locator and revision;
- scope, authority, and materiality;
- findings to preserve;
- the active sequence;
- the next gate and stop.

Do not create a second packet for framing. In direct single-skill mode, return the native Task Frame without a Design Work Packet.
