<img src="assets/design-agent-skills-hero.svg" alt="Design Agent Skills. Design work for agents. Authority for humans." width="100%">

# Design Agent Skills

Design Agent Skills helps you work through product and interface design with Claude Code. Investigate an existing flow, compare alternatives, or prepare an approved design for implementation. The agent works from your product sources and design system; you make the material design decisions.

This Claude edition is version 0.1.0. It includes [16 skills](docs/skills.md), available as a native plugin or project-local copies through Skills CLI.

[Install DAS](INSTALL.md) · [Use it in Claude Code](docs/claude-code.md) · [How the work flows](docs/how-das-works.md) · [Changes](CHANGELOG.md)

## Install the plugin

From your project, run:

```sh
claude plugin marketplace add 'vdigitaldesign/design-agent-skills#claude' --scope project &&
claude plugin install design-agent-skills@design-agent-skills --scope project
```

The [installation guide](INSTALL.md) also covers project-local Skills CLI copies, updates, and removal. Use one installation route per project.

## Start with a task

After installing the plugin, open Claude Code in your project and try:

```text
/design-agent-skills:design-router Review our checkout flow.

Read the existing screens, product rules, and design-system guidance.
Identify the main usability problems and recommend what to change.
Keep pricing, eligibility, and existing payment behavior unchanged.

Show me material design choices before preparing a selected direction
for implementation. Save the findings and handoff in design/checkout/.
Do not edit product code.
```

Replace the flow, constraints, and destination with your task. Give Claude access to the relevant sources. Project-local skills use `/design-router` without the plugin prefix.

## Work from your product

DAS helps the agent recover context, assess reuse, audit an interface, explore directions, and make a choice tangible. It carries your approved decisions into a design contract and can compare the implemented interface with those requirements. Use the operations your task needs; a small review can end with findings and recommendations.

Approval applies to the choice and scope you actually approved. A prototype, recommendation, or review-ready draft does not authorize implementation or publication. See [decision and handoff boundaries](docs/how-das-works.md).

## Review the handoff

Claude outputs have omitted required behavior and confused review readiness with approval. Before implementation, compare the contract with its governing sources, especially exact content, permissions, failure and recovery paths, and acceptance checks. Confirm the approved revision and any remaining decisions.

The complete contract and implementation-handoff workflow has limited behavioral verification on Claude. Having all sixteen skills installed does not establish that every workflow is reliable. This edition covers Claude Code; Desktop and Cowork behavior are outside its support scope. [Support](SUPPORT.md) explains how to report a problem.

DAS supplies Markdown instructions. Claude Code supplies model access and tools; DAS does not bundle a browser, Figma connection, image generator, or application runtime. The [MIT license](LICENSE) applies.
