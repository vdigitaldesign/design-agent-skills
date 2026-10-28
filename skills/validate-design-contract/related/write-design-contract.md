---
name: write-design-contract
description: Assemble approved material design decisions and unchanged normative sources into a scoped, testable Design Contract and implementation handoff. Use when a selected material direction needs specification; routine conformance should use effective product canon, effective design-system canon, or an effective Design Contract without creating a new contract.
---

# Write Design Contract

Assemble the approved experience from its exact sources so a coding agent can implement it without inventing material design decisions.

## Packet mode

- **Carried:** use and update the supplied valid Design Work Packet. Do not reconstruct its intake or reread pinned authority merely to confirm it.
- **Direct single-skill:** when the Design Contract or routine handoff is the complete requested outcome, return that native output without creating a packet.
- **Direct expansion:** when direct specification becomes a material or uncertain multi-skill chain, create exactly one [Design Work Packet](../references/packet-projections.md#design-work-packet) before the first downstream handoff, using the [governed-view assembly](../references/packet-projections.md#governed-view-assembly) from the existing sources and native records.

Refresh a carried packet only when a required field is missing, a source is stale or conflicting, scope or authority changes, or genuinely new evidence appears.

Without a valid packet, read [authority and status](../references/authority-and-status.md). Use the native [contract template](../references/contract-review-templates.md#design-contract) for substantive authoring. The handoff fields are assembly targets sourced from that contract, not a separate writing assignment. Load [practical design checklists](../references/quality-checklists.md) for applicable contract lenses and [packet projections](../references/packet-projections.md) when producing a Human Decision Brief or Coding-Agent Execution Packet.

## Preconditions

- For material work, require a scoped approved design decision and its evidence lineage.
- For routine conformance, do not create a new Design Contract or effectivity gate. Produce a concise engineering handoff from the controlling effective product canon, effective design-system canon, or effective Design Contract, including scope, evidence, acceptance check, and parity plan.
- Confirm the current design-system operating posture when system rules are missing, deficient, or disputed.

If a material selection or authority is missing, complete safe specification preparation. Then return findings, viable options, a recommendation, trade-offs, and the smallest owner question. Keep the contract `draft`.

## Write the contract

Author the native contract, proposed choices and concrete acceptance procedures. Keep each source-owned rule at its existing owner and each new proposed design choice at its exact proposal. Record actual implementation authorization, remaining gates/return conditions, parity request and all required handoff meaning in the native contract. Materialize the required packet/brief/handoff through [governed-view assembly](../references/packet-projections.md#governed-view-assembly); do not author their behavioral, scope or authority prose again. Required outcomes remain complete.

1. Identify the supplied sources, exact revisions, authority and applicable scope. Distinguish effective canon, approved choices, proposals and observations. Include every applicable normative source unit, including its conditions, exceptions and co-applicable rules; account for exclusions against the commissioned scope. A coverage index routes the reader to source text; it cannot narrow that text. An unavailable source or unresolved conflict remains visible and blocks only dependent work. Apply an existing precedence or supersession decision when supplied; otherwise do not silently choose a winner.
2. Assemble **Required experience** from unchanged source text. Include complete small sources; for a larger source, include complete applicable sections with their definitions and dependencies. Preserve source IDs, revisions and status, and make their full text available with the contract. Do not translate existing behavior into new requirements, state tables, boundaries, freedoms or gate rules. Headings, indexes and summaries organize sources and carry no independent behavioral meaning.
3. For a genuine material gap, draft a separately identified proposal with its evidence, alternatives, recommendation, trade-offs and exact scope. Never put proposed behavior among consumed norms or change their meaning through a proposal. Unstructured tickets, notes or discussions retain their original wording and evidence status; a proposed normalization is not an approved source. Use the existing decision/effectivity process for new material behavior, without reopening already determined facts or routine choices.
4. Write acceptance procedures with a complete starting history, ordered actions/events, the exact source units supplying expected behavior, and evidence to collect. For each source-defined alternative applicable at a setup, event or outcome, make that step an explicit parameter with its complete source-supported values. Require the entire procedure for every applicable combination, preserving event position, operation identity and the other givens. Do not count a value exercised in a different history as this variant. Where a combination is inapplicable, identify the source condition; retain the required applicable continuation rather than silently dropping it. Then try to complete all mandatory histories while avoiding each claimed obligation, and tighten the closest procedure when such an execution exists. Preserve source-owned acceptance rules unchanged; unsupported choices and unobserved checks remain explicit. No found escape alone proves completeness.
5. Check coverage from the sources into the assembly and checks, as well as every output claim back to its source. Cover relevant entry, eligibility, structure, actions, state/recovery, content, permissions, accessibility, responsive/localization, system use and implementation freedoms. Missing source content is not an implementation freedom. Do not turn a checklist lens or absent observation into a new product rule or approval gate.

This operation applies throughout the contract and its handoff: source locators or exact text supply existing norms; authored prose supplies navigation, evidence, check procedures or visibly separate proposals. Keep genuine design choices in exploration and proposals rather than treating them as approved behavior. Routine conformance still uses the compact packet and existing effective sources, without a new source inventory form or approval ritual.

When applicable, use the canonical [contract template](../references/contract-review-templates.md) to locate:

- the optional Visual System Projection;
- approved material Motion Choice Records;
- production-eligible External Asset Candidate Records;
- prototype-only replacement blockers.

The projection may restate approved visual meaning but cannot replace the contract or add authority. A prototype asset awaiting replacement remains a bounded blocker for dependent shipping scope. It does not become implementation freedom.

Do not prescribe framework APIs, component internals, or code structure unless the consumer has made them approved constraints and they affect the design contract.

## Status and handoff

Use `draft` while material gaps remain. Use `review-ready` only after internal checks support review. Only the authorized human makes the contract `effective`.

Once a material contract is effective, materialize a Coding-Agent Execution Packet from its native handoff content, unchanged sources and real approval/publication records. It contains:

- the exact contract revision, source assembly and actual authority references;
- accessible unchanged normative source units and their coverage index;
- evidence and acceptance procedures with source-supplied expectations;
- source locators for protected boundaries, freedoms and return conditions;
- required parity evidence and any real outstanding gate with its dependent scope.

A routine packet instead cites the controlling effective product canon, effective design-system canon, or effective Design Contract that already governs the result.

When a Design Work Packet exists, pin the execution packet and any Human Decision Brief to its exact revision and the normative revisions it carries. Without one, pin projections directly to the exact native decision, contract, and canon revisions. Run the freshness/equivalence check before handoff.

If any required source is not effective, label the execution packet `NOT AUTHORIZED FOR IMPLEMENTATION` and name the exact gate. Do not hide the gate behind an otherwise complete handoff.

Include only production-eligible assets in a Coding-Agent Execution Packet. Carry motion requirements only from the controlling effective product canon, effective design-system canon, or effective Design Contract. Retain their purpose, state relationship, reduced- or non-motion fallback, performance/lifecycle constraint, and requirement reference. An approved Motion Choice Record may be cited as decision evidence but cannot authorize implementation.

The handoff carries the same source assembly and checks, without another specification of behavior or new gate. Verify that the receiver can open the controlling text and implement the scoped result without resolving a hidden material choice; links and byte equality alone do not establish completeness or compatibility. Send a material draft to [validate-design-contract](../SKILL.md). Continue through safe corrections. Stop only when selection or effectivity authority is genuinely required.

If contract work establishes a reusable cross-task pattern, source boundary, or known non-fit, route only that metadata to [maintain-design-knowledge](maintain-design-knowledge.md). Contract requirements remain owned by their effective source and are never copied into the index.

In carried or direct-expansion mode, mechanically materialize the following updates from the contract, validation/authority records and actual workflow events:


- the current step;
- Design Contract and projection locators, revisions, and statuses;
- controlling sources;
- findings to preserve;
- resolved and remaining gaps;
- the validation/effectivity gate;
- the active sequence;
- the next step and stop.

In direct single-skill mode, return the native contract or routine handoff without a Design Work Packet.
