# Practical design checklists

Use only the lenses relevant to the task. Explicitly consider whether each lens could expose a material omission. Cite applicable product canon or standards instead of inventing universal numeric rules.

## Evidence integrity

- Are facts, inferences, unknowns, and conflicts visibly distinct?
- Does every material claim have a source, authority, scope, confidence, and freshness signal?
- Are screenshots, prototypes, and observed implementation treated as evidence rather than canon?
- Are limitations and unobserved states disclosed?
- Is each external reference's intent, Reference Capture Receipt, fallback, and limitation explicit?
- Was acquisition restricted to permitted schemes, hosts, environments, privacy rules, and the lowest sufficient evidence?

## Interaction and full state cycle

- Entry, eligibility, no-selection, empty, loading, ready, progress, success, and exit.
- Validation, permission denial, conflict, interruption, timeout, offline behavior, cancellation, partial success, failure, retry, undo, and recovery when relevant.
- Repeated actions, concurrency, idempotence, and destructive confirmation when relevant.
- Clear feedback, preserved user input, and a safe next action.

## Accessibility

- Semantic structure, names, descriptions, and relationships.
- Complete keyboard path, visible focus, focus order, focus movement, and focus return.
- Instructions and errors not dependent on color, position, sound, or motion alone.
- Readability, contrast, zoom/reflow, target usability, and assistive-technology announcements.
- Reduced-motion or non-motion alternative when motion is not essential.

## Responsive, localization, and RTL

- Narrow and wide layouts preserve priority and meaning.
- Long, short, pluralized, and translated content do not break hierarchy or controls.
- Directional icons, ordering, alignment, gestures, and navigation behave correctly in RTL where applicable.
- Input method and platform conventions remain usable.

## Information architecture and content

- Labels match the user’s model and approved terminology.
- Grouping, hierarchy, navigation, disclosure, and defaults support the task.
- Destructive, irreversible, permission-sensitive, legal, privacy, or analytics-sensitive text is not rewritten without authority.
- Errors explain what happened, what was preserved, and what the user can do next.

## Visual and system coherence

- Hierarchy and attentional sequence match the task rather than decorative emphasis.
- Rhythm, grouping, negative space, optical balance, and composition survive realistic content and viewport changes.
- Typography roles, measure, emphasis, numerals, truncation, localization, and fallback fit the content.
- Color relationships express surface, hierarchy, action, and state across relevant themes without becoming the only cue.
- Density fits task frequency, expertise, volume, error cost, viewport, and input mode.
- Imagery and iconography have a product job, provenance, fallback, crop, and accessible treatment.
- Affordances remain recognizable across focus, selected, disabled, loading, error, and success states.
- Reused patterns retain their expected behavior and state coverage.
- Coherence and product-specific distinctiveness are motivated by intent or references, not novelty or genre stereotype.
- Polish covers alignment, joins, clipping, state edges, content extremes, and reflow without disguising unresolved behavior.
- Motion communicates relationship, causality, progress, or feedback. Decorative motion does not obscure state.
- Material motion records its user/product job, trigger, affected states, timing relationship, keyboard/touch/no-hover behavior, reduced- or non-motion equivalent, performance/lifecycle budget, dependency/provenance, validation, limitations, status, and authority—without a motion quota.
- Every external asset records provenance, eligibility, rights review, fallback, alt-text ownership, and any replacement-before-shipping requirement. A remote reference asset is not production-eligible by default.

## Specification and parity

- Every material decision maps to an approved source and an observable requirement.
- Requirements cover meaningful states without dictating unnecessary code choices.
- Acceptance criteria can be checked in the intended environments.
- Parity evidence distinguishes implementation defects from design-contract gaps.
- Reference alignment is reported separately from normative contract parity. An apparent reference match cannot override effective product or contract requirements.
- Maker self-review is supporting evidence, not final proof.
