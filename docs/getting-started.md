# Give DAS a useful task

A brief should tell the agent what people need to do, what the product offers, and what you want to receive. Supply the relevant rules, screens, and existing decisions with the request. Replace the bracketed paths and details below with your own.

The examples use the plugin prefix. For project-local copied skills, use `$design-router` or the corresponding unprefixed specialist name.

For a filled-in brief and the work that follows it, read the [ticket-reassignment example](worked-example.md). It shows the options, an illustrative human choice, and a developer handoff.

## Brief template

```text
Use $design-agent-skills:design-router.

Task: [what needs to be designed or improved]
People: [who will use it and what they are trying to do]
Product facts: [offer, options, rules, or authoritative source files]
Current problem: [what is unclear, difficult, or missing]
Keep: [working behavior, brand rules, and constraints]
Existing decisions: [choices already approved and their scope]
Available material: [screens, design system, copy, images, references]
Deliver: [audit, design options, prototype, or implementation handoff]
Work here: [permitted project and artifact paths]
```

Include decisions you have already made so the agent can carry them forward. If a source is missing, say so. Where rules conflict, identify who can resolve the conflict.

## Improve an existing flow

> Use $design-agent-skills:design-router to improve rescheduling in [project]. Read [current flow], [booking rules], and [design system]. People need to change a date without losing their selected service or misunderstanding a price change. Preserve the cancellation policy and existing payment behavior. Show me the material design choices, prototype the selected direction, and prepare it for implementation in [destination].

Give the agent access to adjacent screens, relevant components, and current behavior. A screenshot can show a confusing state while leaving its product rule unknown.

## Audit a screen

> Use $design-agent-skills:audit-design-surface on [preview or screen]. Check whether a visitor can understand the offer, compare the options, and complete [main action]. Inspect the important states and narrow layout, including keyboard use where the environment supports it. Read [product rules] and [design-system source]. Return the issues that matter, their affected states, and practical recommendations in [destination].

This asks for an audit. Include redesign or implementation in the request if you also want those outputs.

## Design a new product page

> Use $design-agent-skills:design-router to design a page for our modular desk accessories. Read [product facts], [brand guide], and [available assets]. The visitor needs to understand the range, compare sizes and prices, and choose an accessory that fits their desk. Use the supplied product claims. Develop the page through meaningful alternatives, my choice, a responsive prototype, and an implementation handoff. Save the work in [destination].

Useful inputs include exact dimensions, materials, options, prices, delivery terms, and the intended action. Identify whether images show real products or illustrations. Provide the actual rules for any calculator or configurator.

## Refine a visual direction

> Use $design-agent-skills:develop-visual-direction for [selected direction or prototype]. Preserve [approved content, behavior, and brand decisions]. Improve the hierarchy, typography, spacing, imagery, and responsive composition for [user task]. Use [design-system source] where it applies. Show the proposed changes in [artifact format] and explain the choices that need my decision.

## Check an implementation

> Use $design-agent-skills:verify-design-implementation. Compare [running interface] with [approved design and requirements]. Check the main action, applicable loading/error/empty/success states, keyboard access, and required viewport sizes. Record what matches, what differs, and what could not be checked. Prepare a focused correction handoff for observed differences.

Provide the approved target and its requirements. A similar product screenshot is a reference, not the specification for your implementation.
