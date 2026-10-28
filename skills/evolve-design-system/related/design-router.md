---
name: design-router
description: Orchestrate a request that touches UI/UX when no specialist design skill is explicit or the work spans multiple design workflows. Pass engineering-only work through without design ceremony; do not use this router as an automatic duplicate intake or to implement frontend code.
---

# Design Router

Turn the request into useful design work. Choose the smallest correct route. Use the decision gate to start the work; do not treat it as the deliverable.

Read [authority and status](../references/authority-and-status.md) before you classify the task. If material or uncertain work will cross more than one design workflow, create one compact [Design Work Packet](../references/packet-projections.md#design-work-packet) before the first downstream step. Do not load the Task Frame or Design Read templates just to route the task. Use [task and context templates](../references/task-context-templates.md) only when one of those durable outputs is required.

## Route by current state

Inspect all permitted, relevant sources before you report insufficient context. Identify:

- the requested outcome;
- the available authority;
- current product canon, design-system canon, and Design Contract references, with their effectivity statuses;
- observed evidence;
- whether any new material decision exists.

First, check whether the work is outside design scope. Pass purely engineering work to the engineering agent immediately. Re-enter this router if the change affects product/UI behavior, accessibility, states, content meaning, visual or system rules, or a Design Contract.

Use an existing API, data, database, implementation, or operational contract as design evidence when it establishes permitted product facts. Observation alone does not activate an API, database, engineering, migration, or operational-diagnosis workflow. Activate such a workflow only for authorized mutation or implementation, operational diagnosis, or an explicit consumer-policy requirement. Always follow a consumer repository's stronger routing rule.

| Current state | Route |
| --- | --- |
| Effective product canon, effective design-system canon, or an effective Design Contract already determines the exact result | Produce a light routine handoff from the controlling source. Pass it to engineering and plan [verify-design-implementation](verify-design-implementation.md). Do not create a new contract or effectivity gate. |
| Scope, materiality, or authority is ambiguous, or the user explicitly asks for a brief | Use [frame-design-task](frame-design-task.md), then continue the required workflow chain. |
| A material outcome or interaction is undecided | Reconstruct context. Audit or assess reuse as needed. Explore directions, obtain a human decision, write and validate a contract, then hand off. Frame first only when its specific trigger applies. |
| Material context or authority may be missing | Use [reconstruct-design-context](reconstruct-design-context.md). Continue independent research and audit before you escalate an irreducible gap. |
| The question concerns the quality or behavior of an existing interface | Use [audit-design-surface](audit-design-surface.md). |
| The question concerns design-system health, coverage, or change posture | Use [audit-design-system](audit-design-system.md). Continue evidence-backed `consume` under effective canon. Route approved change postures to [evolve-design-system](../SKILL.md). |
| The choice between existing, official, trusted, or custom solutions remains open | Use [assess-design-reuse](assess-design-reuse.md). |
| Design knowledge useful across tasks needs retrieval, freshness review, capture, rejection/non-fit, or supersession | Use [maintain-design-knowledge](maintain-design-knowledge.md). Do not create an entry for every task. |
| A material choice needs alternatives | Use [explore-design-directions](explore-design-directions.md). |
| Visual language, composition, or polish is a material question | Use [develop-visual-direction](develop-visual-direction.md). Include tangible comparison when selection remains open. |
| The user explicitly asks for a prototype, mockup, or design lab, or tangible interaction evidence is required | Use [prototype-design-directions](prototype-design-directions.md). |
| A human has selected, combined, or rejected directions | Use [record-design-decision](record-design-decision.md). |
| An approved direction needs testable specification and handoff | Use [write-design-contract](write-design-contract.md). |
| A draft or review-ready contract needs pre-build review | Use [validate-design-contract](validate-design-contract.md). |
| An exact design-system proposal has explicit effectivity approval and needs durable publication/adoption lineage | Use [publish-design-system-canon](publish-design-system-canon.md). |
| An implementation exists and must be checked against design authority | Use [verify-design-implementation](verify-design-implementation.md). |

A request may need several workflows in sequence. Carry findings and lineage into each step. Do not make the user restate evidence. Continue every safe, relevant step in the same turn. Stop only at a genuine blocker defined by the shared continuation invariant.

## Retrieval discipline

Prefer exact known decision, page, artifact, or record IDs and path-scoped searches. Before you expand a search for an ambiguous noun, inspect the bounded match count and identifiers.

Limit connected-source fields, excerpts, records, and date range. Broaden the search only when the bounded result is insufficient. Record the prior scope, count, insufficiency, and expansion in the packet. Use a focused-context target to diagnose cost; never use it as permission to omit material evidence.

## Required behavior

- For **routine conformance**, use the exact six-field compact shape in [packet projections](../references/packet-projections.md): controlling revision, observed delta, exact correction, protected boundaries, concise acceptance/parity request, and return-to-design condition. Do not duplicate routing, finding, source, or freshness sections. Do not write a full future parity procedure before implementation evidence exists. Do not force framing, a manifest, decision brief, new contract, effectivity gate, exploration, or owner selection.
- For **material work**, perform accessible research, audit, reuse assessment, and interaction and visual craft. Include alternatives or prototypes when useful. Give a recommendation. Use a bounded material or high-impact evidence packet. Make it proportional to reach, reversibility, uncertainty, and authority. Stop for human selection before you make the direction normative.
- For **insufficient context**, report findings, viable options, trade-offs, and the irreducible missing fact. Include a recommendation when supportable. Never return a generic refusal.
- When the design system is missing or deficient, route to a scoped consume / extend / repair / constrain / establish / replace-migrate assessment. Continue authorized `consume` directly. Use [evolve-design-system](../SKILL.md) for approved change postures. Publish only exact approved canon through [publish-design-system-canon](publish-design-system-canon.md). Do not silently invent a system.
- If the request mixes design and implementation, complete the design work in scope. Give the coding agent an effective handoff. Do not write code from this skill.

## Router output

For a material or uncertain multi-skill route, carry one Design Work Packet. Do not add a separate routing note and repeated intake artifacts. Keep these fields in the packet:

- ID and revision;
- requested outcome and scope;
- authority and materiality;
- facts, inferences, unknowns, and conflicts;
- protected boundaries;
- exact source locators and revisions;
- active sequence;
- explicitly inactive workflows or workflow groups, with their absent triggers;
- completed findings to preserve;
- next gate or scoped stop.

Downstream steps update the same packet and preserve its lineage.

When the chain stops for one missing human-owned fact, return the decision-relevant findings, supported options, recommendation and trade-offs, material unknowns, protected boundaries, and one bounded question.

Keep packet administration and workflow bookkeeping in the carried context. Include them in the reply only when requested or needed to understand the evidence, authority, or next decision. You do not need a separate document just to ask the question. Return the complete packet when it is the requested deliverable or required for a handoff. In either form, preserve the applicable audit vocabulary and evidence limitations.

Do not create a packet for engineering pass-through, a single clear specialist invocation, or routine conformance. Use the smallest native output for those paths.

Execute the full safe workflow chain in the same turn when authorized and feasible. Do not treat routing or another intermediate artifact as the product.

After an audit, Design Lab, visual direction, contract, or parity task, route to knowledge maintenance only when both conditions hold: the evidence is likely to improve a later task across scopes, and an authorized durable index exists. Keep incidental or product-private learning in the task packet.
