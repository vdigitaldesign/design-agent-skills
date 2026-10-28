---
name: validate-design-contract
description: Stress-test a draft or review-ready Design Contract for authority, completeness, contradictions, state coverage, accessibility, responsiveness, and testability before implementation. Use for pre-build design validation; do not approve the contract or silently manufacture material fixes.
---

# Validate Design Contract

Find specification defects before code begins. Distinguish wording that can be repaired from missing design authority.

## Packet mode

- **Carried:** use and update the supplied valid Design Work Packet. Do not reconstruct its intake or reread pinned authority merely to confirm it.
- **Direct single-skill:** when validation is the complete requested outcome, return the Validation Record without creating a packet.
- **Direct expansion:** when direct validation opens a material or uncertain multi-skill chain, create exactly one [Design Work Packet](../references/packet-projections.md#design-work-packet) before the first downstream handoff, using the [governed-view assembly](../references/packet-projections.md#governed-view-assembly) from the existing sources and native records.

Refresh a carried packet only when a required field is missing, a source is stale or conflicting, scope or authority changes, or genuinely new evidence appears.

Without a valid packet, read [authority and status](../references/authority-and-status.md). Use the native [Validation Record template](../references/contract-review-templates.md#validation-record) and [practical design checklists](../references/quality-checklists.md) for applicable validation lenses.

## Validation procedure

Perform the semantic checks on the original sources and current native decision/proposal/contract/acceptance content, including their scope and actual authority. Author the validation findings, verdict, limitations and precise safe corrections once. Mechanically assembled packet/brief/handoff views remain part of the delivered unit: check their source revisions, completeness of required materialization and equivalence, then regenerate them after native corrections. Assembly success never supplies a semantic verdict.

1. Identify the exact contract revision, status, scope, controlling canon, approved decisions, and evidence.
2. Check both directions: every applicable source unit is present in the unchanged assembly and covered by relevant checks, and every material output claim resolves to its authoritative source or exact approved decision. Inspect excluded scope, definitions and co-applicable rules. Byte equality or a list of citations is not evidence of complete selection. Flag observations, summaries or proposals used as canon.
3. Check for contradictions within the supplied sources, between consumed rules and proposals, and throughout the contract, checks and handoff. Apply only supplied authority/precedence decisions; leave unresolved conflicts explicit. Inspect setups, notes, freedoms and gates for an independently authored condition, exception or prohibition.
4. Walk the complete relevant experience: entry, eligibility, primary flow, no-selection, empty, progress, success, permissions, conflict, error, partial success, cancellation, retry, undo, recovery, and exit.
5. Apply relevant accessibility, responsive, localization, RTL, information-architecture, content, visual-system, and motion lenses.
6. Check that source requirements are observable and acceptance procedures exercise their full relevant conditions without writing competing expected behavior or forcing unnecessary implementation choices. Separate a detected/stopped defect from a completed conforming handoff.
7. Ask whether a coding agent could proceed without inventing material design meaning.
8. When human, coding, or Visual System Projections exist, check freshness and semantic equivalence against their pinned sources. A projection cannot compensate for a contract gap or close an unknown.
9. Check that each material motion requirement has purpose, affected states, interaction fallbacks, performance/lifecycle constraint, authority, and validation evidence proportional to the scope.
10. Check that implementation inputs include only production-eligible assets and that prototype-only replacements block precisely their dependent shipping scope.

An approved Motion Choice Record must cite the exact Owner Decision Record revision and approving authority/scope. Treat it as governed decision evidence, never implementation authority. A handoff may carry motion requirements only from effective product canon, effective design-system canon, or an effective Design Contract.

## Outcomes

Return `pass`, `fail`, or `inconclusive` with evidence and limitations.

Classify each issue as:

- editorial or non-material clarification;
- unsupported or contradictory requirement;
- missing state or acceptance criterion;
- material contract gap requiring design work or owner decision;
- source or authority conflict;
- untestable requirement.

Suggest precise corrections. Restore an altered source unit from its pinned original; correct navigation or procedures without changing source meaning. Do not repair an authoritative source by paraphrasing it inside the contract. Do not choose or silently repair a material direction. For a material gap, provide findings, viable options, recommendation, trade-offs, and the smallest owner question.

Recommend `review-ready` only when validation passes for the intended scope. Validation cannot make the contract `effective`. Apply non-material corrections and re-check them in the same turn. Do not stop at the Validation Record when safe dependent work remains.

A match to an external reference does not cure an unsupported or contradictory contract requirement. Record reference alignment separately and let the controlling product contract determine normative validity.

In carried or direct-expansion mode, mechanically materialize the following packet values from this exact Validation Record and actual workflow events; do not independently re-author its verdict or gates:


- the current step;
- the Validation Record locator, revision, and outcome;
- the validated contract revision;
- findings to preserve;
- resolved/new gaps;
- the effectivity or return-to-design gate;
- the active sequence;
- the next step and stop.

In direct single-skill mode, return the native validation without a Design Work Packet.
