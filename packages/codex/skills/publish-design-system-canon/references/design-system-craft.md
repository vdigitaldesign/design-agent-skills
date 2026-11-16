# Design-system craft, publication, and adoption

Use this reference when you assess, change, publish, adopt, or verify design-system canon. A design system is product infrastructure. It includes visual relationships, behavior, content, states, documentation, ownership, adoption, and evaluation. A component inventory alone is not a design system.

## Inspect by layer

### Foundations, tokens, and theming

Inspect how product intent connects to semantic roles and how those roles resolve to values. Record:

- token purpose, scope, owner, status, revision, aliases, and fallback;
- semantic roles for surface, text, border, action, feedback, focus, spacing, shape, typography, motion, elevation, and imagery when applicable;
- theme or mode axes, inheritance, overrides, contrast relationships, platform differences, and unsupported combinations;
- naming that expresses stable purpose rather than one current value;
- drift between documented tokens, delivered assets, and observed consumers.

A token proposal must show the relationship it creates or repairs and the consumers it affects. Do not create a complete token universe for a single need.

### Component specification

Cover the component’s:

- purpose, anatomy, and variants;
- sizing or density logic, content slots, and layout constraints;
- interaction, semantics, keyboard/focus behavior, and all applicable states;
- responsive behavior, localization/RTL, and theming;
- composition rules and implementation freedoms;
- observable acceptance criteria.

Variants should express recurring product meaning. Avoid variants that merely preserve one historical screenshot or move unresolved product choices into a component API.

### Pattern specification

Patterns own relationships across components and moments. These include entry, task sequence, information hierarchy, permission/destructive behavior, feedback, partial outcomes, recovery, responsive transformations, and content rules. State which underlying primitives the pattern consumes and which behavior it adds.

### Content and behavior contracts

Record approved terminology, naming and description rules, error/recovery structure, status language, destructive meaning, data provenance, and sensitive content boundaries. Content guidance cannot silently rewrite product, legal, privacy, analytics, or localization authority.

### Documentation quality

Every effective system item should make the following retrievable:

- use, avoid, and known non-fit;
- owner, status, revision, effective date, and supersession;
- dependencies and related patterns;
- anatomy or relationship map;
- states and accessibility expectations;
- content, responsive, theme, localization, and RTL behavior where applicable;
- examples and counterexamples tied to decisions, not aesthetic preference;
- acceptance and parity evidence expectations;
- exceptions, debt, migration, and review triggers.

## Agent-ready context

An agent-ready system gives an agent enough authority and retrieval context to apply a rule without guessing. For each effective item, provide:

- stable ID, title, aliases, scope, and retrieval terms;
- normative source locator, revision, status, effective date, and owner;
- required, allowed, and forbidden behavior;
- decision rules and known non-fit;
- relationships to product canon and other system items;
- full-state and environment expectations;
- implementation freedoms and return-to-design conditions;
- examples, counterexamples, and evaluation fixtures where they change application;
- freshness trigger and superseding reference.

This is context for retrieving canon, not a copied prompt or database registry.

## Change craft by posture

- **Extend:** add the smallest missing semantic relationship, component, or pattern while inheriting healthy foundations.
- **Repair:** correct an effective rule or asset whose intent remains valid; name affected consumers and adoption evidence.
- **Constrain:** publish the reliable subset, forbidden uses, temporary exceptions, debt owner, and exit condition.
- **Establish:** create only the foundations and specifications required to make the approved scope coherent and governable.
- **Replace-migrate:** define target canon, compatibility boundary, staged adoption, deprecation, exceptions, verification, rollback, and final removal conditions.

For every posture, distinguish the approved posture from the exact proposed canon text. Approval of the posture authorizes drafting. Only explicit approval of the exact canon text makes that text eligible for publication.

## Canon publication record

Publish into a consumer-owned canonical destination only after exact human effectivity approval.

### Identity and authority

- Canon ID and title:
- Scope and owner:
- Revision and lifecycle status:
- Exact approval record, approver authority, date, and approved revision/digest or unambiguous text locator:
- Effective date and review trigger:

### Normative content

- Required, allowed, and forbidden relationships or behavior:
- Tokens, theme relationships, component/pattern contract, states, content, or documentation in scope:
- Accessibility, responsive, localization, RTL, and platform requirements:
- Implementation freedoms:
- Acceptance criteria:

### Lineage

- Source assessment and approved posture:
- Approved change proposal:
- Product canon and protected-boundary references:
- Supersedes, is superseded by, or revokes:
- Related debt, exceptions, Design Contracts, and knowledge-index entry:

### Adoption and evaluation

- Affected consumers and compatibility:
- Required migration sequence and rollback:
- Adoption evidence and drift checks:
- Evaluation fixtures and parity environments:

## Revision and supersession rules

- Never overwrite history so a prior effective revision becomes unrecoverable.
- A new effective revision names the exact revision it supersedes. The prior record points to the new revision and becomes `superseded` for new work. It remains valid historical evidence.
- Revocation requires authority. Name the safe fallback or explicitly state that no authorized replacement exists.
- Scope-specific revisions may coexist when their boundaries do not conflict. Return conflicts to authority. Never resolve them by last write.
- By default, retrieve the most specific current effective revision for the consumer scope. Also expose applicable exceptions and migration state.

## Adoption or migration receipt

- Receipt ID, consumer, surface, and environment:
- Canon revision adopted:
- Previous revision or local rule displaced:
- Adoption status: planned / in progress / adopted / exception / rolled back:
- Evidence locators and capture time:
- Known gaps, exceptions, debt owner, and expiry/review trigger:
- Parity result and next action:

An adoption receipt reports consumer state. It does not change canon. Multiple receipts may refer to one normative revision.

## Drift and evaluation

Check documentation, delivered design assets, implementation, and retrieval examples against the same revision. Distinguish:

- canon defect or `contract gap`;
- consumer `implementation discrepancy` before handoff or `implementation defect` during parity;
- authorized exception;
- stale documentation or retrieval metadata;
- `inconclusive observation` where evidence is unavailable.

Evaluate realistic state and product fixtures, including known non-fit. Retrieval success against a catalog is not proof of usability, accessibility, or product fit.
