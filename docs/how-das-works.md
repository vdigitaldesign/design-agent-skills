# How DAS works

DAS helps agents work from a product request to a design decision and engineering handoff, then compare the built result with the approved design. Its skills share guidance for context, decisions, and verification.

See the [worked example](worked-example.md) for a concrete brief, design options, and a handoff built around one illustrative choice.

## Start from the task

Design Router chooses the work needed for your requested result. An audit can end with findings. A routine correction determined by an existing approved rule can use a short handoff. A material design choice may need alternatives, a prototype, and your decision before a contract is prepared.

You can invoke a specialist directly when the task is clear. The [catalog](skills.md) explains the available operations.

## Establish the product context

Product facts can live in a brief, design files, component code, previous decisions, and the running interface. The agent should distinguish authoritative requirements from observed behavior, inferences, and unresolved questions.

The current implementation shows what exists. An existing component or behavior may still conflict with an approved rule. DAS asks the agent to check applicable product and design-system sources before treating an implementation detail as a requirement.

The same check applies to reuse. Existing components and approved patterns may meet the task; custom work needs a reason tied to the product and its users.

## Make choices inspectable

When a material choice remains, the agent develops alternatives that solve the problem differently and explains their costs. A prototype or layout can make a choice easier to assess than a written description alone.

Exploration, visual direction, and prototyping are separate skills. The task determines which ones help. Their work considers the content, interaction states, accessibility, responsive behavior, and design language that apply.

The agent recommends a direction. The person authorized by the project makes the material decision, with its scope recorded for later work.

## Preserve authority

An observation, a proposal, an approved decision, and a verified implementation mean different things. A recommendation cannot approve itself, and an implementation check cannot authorize new product behavior found in the code.

Existing requirements stay at their authoritative sources. Approved new choices are recorded at the project's designated owner. A Design Contract gathers the applicable requirements and concrete acceptance procedures needed to check the chosen work. Validation can establish that a contract is ready for review; the authorized person makes the exact revision effective for implementation.

When approved requirements already determine a routine correction, a new contract or approval round is unnecessary. A missing detail blocks the work that depends on it; the agent can still complete useful independent work.

## Hand work to engineering

The handoff identifies the applicable requirements, complete source material, protected behavior, checks, unresolved questions, and conditions for returning to design. The recipient should be able to find the material without reconstructing the earlier chat.

For example, approving a recovery screen that explains an expired link and lets a user request another does not also approve account creation or a change to security rules. Those boundaries need to survive the handoff.

After implementation, Verify Design Implementation compares the actual interface and interactions with the approved target. It distinguishes a discrepancy, a missing requirement, a proposed change, and something the environment could not inspect.

## Work with a design system

DAS can assess whether a task can use the current design system, needs an extension or repair, or warrants a larger change. The scope may be one component state or a planned migration.

A proposal or prototype is evidence for a change. The responsible person approves the exact revision for publication in the designated source. Publishing it and confirming its adoption are separate operations. Design knowledge can then retain the decision, source, and current status for later work.

## Use the result with judgment

DAS does not replace product research, testing with users, or accountable human decisions. It has no universal visual style or guarantee of commercial success. Production implementation and engineering architecture remain with the coding workflow.

The instructions use the tools and permissions in your environment. Review source fidelity, coverage, authority, and the usability of the handoff for the task at hand. [Getting started](getting-started.md) helps you supply that context.
