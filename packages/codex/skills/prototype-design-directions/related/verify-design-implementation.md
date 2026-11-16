---
name: verify-design-implementation
description: Compare an implemented interface with controlling effective product canon, effective design-system canon, or an effective Design Contract and report evidence-backed parity, gaps, and untested states. Use after or during implementation; do not edit code, rewrite authority, or approve an unselected delta.
---

# Verify Design Implementation

Determine whether the implemented experience preserves the controlling effective design requirements across meaningful states and environments.

## Select the requested outcome

Return the [compact routine handoff](../references/packet-projections.md#compact-routine-handoff-shape) when both conditions hold:

- supplied evidence identifies a bounded discrepancy already determined by effective canon;
- the requested next step is engineering correction followed by later verification.

Request the smallest post-change evidence needed to check the correction and protected boundaries, then stop. This path does not require a new Implementation Parity Record or the full review procedure below merely to prepare future verification.

When verification of the current implementation is itself requested, continue with the parity workflow below, including its relevant coverage and evidence requirements.

## Packet mode

- **Carried:** use and update the supplied valid Design Work Packet. Do not reconstruct its intake or reread pinned authority merely to confirm it.
- **Direct single-skill:** when implementation parity is the complete requested outcome, return the Implementation Parity Record without creating a packet.
- **Direct expansion:** when direct parity work opens a material or uncertain multi-skill chain, create exactly one [Design Work Packet](../references/packet-projections.md#design-work-packet) before the first downstream handoff.

Refresh a carried packet only when a required field is missing, a source is stale or conflicting, scope or authority changes, or genuinely new implementation evidence appears.

Without a valid packet, read [authority and status](../references/authority-and-status.md). Load the [Implementation Parity Record template](../references/contract-review-templates.md). Load [practical design checklists](../references/quality-checklists.md) for applicable parity lenses. Load the whole tool-neutral evidence/limitation contract in [product profile and tools](../references/product-profile-and-tools.md) when evidence collection or consumer verification constraints require it.

## Preconditions and evidence

Identify:

- the controlling effective product canon, effective design-system canon, or effective Design Contract;
- its revision and acceptance criteria;
- approved deltas;
- protected boundaries;
- target environments;
- accessible implementation evidence.

Routine parity does not require a new Design Contract. A draft or review-ready Design Contract cannot authorize implementation or normative parity. Concrete browser, platform, or framework collectors are downstream choices. Record whichever observation method is used.

For each requirement checked, capture:

- controlling requirement reference;
- observed result and parity status;
- evidence locator;
- environment and context;
- observation method or collector;
- capture time and limitations.

Do not claim parity for an unobserved state.

## Review procedure

1. Map acceptance criteria to observable paths, states, viewports, input methods, localization or RTL conditions, and assistive-technology checks relevant to the contract.
2. Exercise the full relevant state cycle, including failure, permissions, partial success, cancellation, retry, undo, and recovery.
3. Compare behavior, content, hierarchy, accessibility, responsive behavior, system usage, and motivated motion with the controlling effective source.
4. Record differences with user consequence and confidence. Tie each claimed consequence to observed evidence or an explicit source rule. Label inferred risks as potential; absence of a stated safeguard or recovery path is not evidence that it does not exist.
5. Classify each difference as an implementation defect, contract gap, inconclusive observation, or proposed material delta requiring owner approval.
6. Report overall coverage, blocking discrepancies, untested states, and the smallest next action.

Complete normative contract parity first. When a commissioned reference comparison also exists, add the separate Reference Alignment Evidence section from the shared template. Classify intentional deviation only when its rationale and authority are recorded. A reference match cannot override a contract gap, and an intentional reference deviation cannot rewrite the controlling requirement.

For motion parity, compare the requirements in the controlling effective source: user/product purpose, triggers, affected states, timing relationships, keyboard/touch/no-hover behavior, reduced- or non-motion fallback, and performance/lifecycle constraint. A Motion Choice Record may supply decision evidence and lineage but cannot supply implementation authority. Verify the effective relationship. Do not imitate reference motion or enforce a motion quota.

## Boundaries

- Do not edit code or instruct the implementation to diverge from the controlling effective source.
- Do not call a defect a design improvement without returning it to the design and owner lane.
- If the contract is ambiguous or incomplete, report a contract gap. Do not invent expected behavior.
- An implementation can expose new evidence but cannot silently rewrite product canon.
- Maker self-review is supporting evidence, not final proof.

Return routine implementation defects to the coding agent. Return material deltas or contract gaps to the appropriate design workflow and owner gate, with findings, viable options, recommendation, and trade-offs.

When repeated parity evidence establishes cross-task system drift, a collector limitation, or a verified known non-fit, route that bounded metadata to [maintain-design-knowledge](maintain-design-knowledge.md). One implementation defect does not automatically deserve a durable index entry.

In carried or direct-expansion mode, update the packet with:

- the current step;
- the Implementation Parity Record locator and revision;
- observed coverage and limitations;
- requirements and findings to preserve;
- defects, gaps, and material deltas;
- resolved/new gates;
- the active sequence;
- the next engineering/design/knowledge step and stop.

In direct single-skill mode, return the native parity record without a Design Work Packet.
