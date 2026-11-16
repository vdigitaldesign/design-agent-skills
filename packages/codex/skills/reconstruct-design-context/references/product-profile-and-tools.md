# Product Design Profile and tool-neutral evidence contract

Use this reference when you adapt the universal workflows to a consumer or when evidence depends on tools. The profile owns consumer mappings, destinations, permissions, and observation metadata. It references product or system canon without duplicating it.

## Product Design Profile template

### Identity and scope

- Profile ID, consumer/product, revision, owner, status, and review date:
- Supported product areas, platforms, devices, themes, locales, and environments:
- Explicit exclusions:

### Source discovery

- Product canon locators and precedence policy:
- Design-system and brand canon locators:
- Current Design Contract and decision-record locators:
- Research, content, support, analytics, implementation, and observed-surface sources:
- Allowed external-reference sources and source classes:
- External-reference intent allowed by source: inspiration / benchmark / explicit reproduction:
- Reproduction and brand-rights policy, including who may authorize each:
- Source freshness rules and conflict destination:

### Authority and permissions

- Consumer policy and decision-authority mapping:
- What the commissioning user may select or approve:
- Design-system, brand, content, product, accessibility, privacy, regulatory, or other owners defined by the consumer:
- Permitted inspection, artifact creation, canon publication, implementation handoff, and verification actions:
- Escalation and conflict policy:

### Language and protected boundaries

- Approved glossary and terminology sources:
- Routes, data, fields, permissions, identity, sensitive content, analytics semantics, legal/privacy constraints, or other protected boundaries:
- Allowed proposal scope and changes that require special authority:

### Design-system state

- Effective system sources and revisions:
- Known maturity by scope, debt, exceptions, adoption state, and drift:
- Approved operating postures and publication destination:

### Evidence and privacy

- Permitted evidence methods and collectors:
- Permitted schemes, hosts, environments, and network boundaries:
- Authentication and production-data policy:
- Capture isolation, size, and time budgets:
- Data minimization, redaction, retention, and sharing limits:
- Prohibited production data or environments:
- Required capture metadata and evidence destination:

### Artifact and handoff destinations

- Design Read, audit, Design Lab, decision, contract, and canon destinations:
- Coding-agent destination and expected packet format:
- Consumer-owned knowledge-index location:
- Naming/revision conventions when supplied by the consumer:

### Verification environments

- Supported builds, platforms, viewports, inputs, themes, locales, RTL, assistive technologies, and fixture accounts/data:
- Environment owner and access limitations:
- Required parity evidence and responsible next lanes:

An absent profile does not block work whose authority and sources are otherwise explicit. Build the smallest task-local profile from permitted evidence. Mark unknown mappings. Avoid claiming consumer facts that the profile has not established.

## Bounded retrieval discipline

When retrieving from repositories, connected workspaces, or document systems:

1. Resolve exact known decision, page, artifact, or record IDs first.
2. Prefer path-, collection-, table-, or product-scope searches over workspace-wide discovery.
3. For an ambiguous noun, inspect the bounded match count and identifiers before opening results or broadening the query.
4. Limit returned fields, records, excerpts, and date range to what the design question requires.
5. Broaden only when the bounded result is insufficient. Record the prior scope, match count, insufficiency, and the next expansion.

A heuristic result or context budget guides retrieval cost. It does not establish correctness and cannot justify dropping material evidence. Consumer-owned search, privacy, routing, and output limits override this default.

## Reference Capture Receipt

Create one receipt for each materially used external reference or coherent capture session. The receipt owns observation metadata and limitations. It does not own product meaning.

- Receipt ID, revision, status, and observer:
- Intent: inspiration / benchmark / explicit reproduction:
- Task Frame and source-intent reference:
- URL or artifact locator and capture time:
- State, viewport, theme, locale, and input condition:
- Permitted collector and privacy boundary:
- Attempted acquisition methods, with result/status for each:
- Selected lowest-sufficient-evidence ladder rung:
- Why that rung is sufficient for the bounded design question:
- Captured screenshots, structure, observed tokens, motion, and assets:
- Facts, inferences, and unknowns:
- Inaccessible, blocked, cross-origin, or otherwise unobserved evidence:
- Provenance, redactions, retention, and limitations:
- Permitted influence on this task:
- What this evidence cannot authorize:

`Explicit reproduction` changes the comparison target only. It does not grant intellectual-property rights, override effective product or design-system canon, or authorize brand, behavior, content, or implementation changes. A receipt may be `partial`, `unavailable`, or `inconclusive`. Never present those states as a complete capture.

## Design Evidence Capability Contract

Tools expose capabilities. They do not grant authority. A workflow asks for the capability it needs and records the actual method, result, and limitation. Concrete design-tool, browser, platform, framework, or media collectors remain downstream.

### Common request envelope

- task and artifact/evidence scope;
- source or target locator and expected revision;
- environment and state to inspect or produce;
- permitted data and privacy constraints;
- required output format and destination;
- authority for any mutation or export.

### `inspect source`

Retrieve authoritative or observed material with its locator, revision or capture time, scope, and access limitations. Explicitly report when the material is unavailable or stale. Do not substitute a convenient secondary source without disclosure.

### `capture surface`

Capture a view, structure, content, state, viewport, theme, locale, input condition, or recording. Return environment, fixture, capture time, method, media locator, redactions, and unobserved conditions. A capture is evidence, not canon.

### `create/edit/export artifact`

Create or revise an authorized prototype, wireframe, mock, diagram, or design document. Export media useful for the decision. Return the editable-source locator, export locator, revision, tool/method, simulated behavior, asset provenance, and fidelity limitations. Keep disposable prototype code isolated. Do not reuse it in production.

### `exercise state`

Set or traverse a named interface condition using documented fixtures or permitted interaction. Return starting state, action sequence, observed transition/result, reset method, failures, and coverage limitations. Do not claim states that could not be reached.

### `collect accessibility evidence`

Collect available semantic structure, name/role/value, keyboard/focus trace, announcements, contrast/readability observations, zoom/reflow, reduced-motion, or assistive-technology evidence. Return tool/method, environment, applicable standard or controlling contract, result, and what still requires human or platform testing.

### `compare implementation`

Map controlling requirements to implementation observations across relevant states/environments. Return requirement reference, evidence locator, parity, method, time, limitations, user consequence, and controlled classification. Comparison cannot make an unapproved delta effective.

## Normalized limitations and fallbacks

For every capability response distinguish:

- `available` — requested evidence/artifact produced;
- `partial` — useful result with named missing coverage;
- `unavailable` — capability or access absent;
- `unauthorized` — action outside the current permission scope;
- `inconclusive` — evidence exists but cannot support the claim.

Before live or static collection, verify all of the following:

- collection permission;
- target, scheme, and host;
- private-network protection;
- authentication and production-data policy;
- isolation;
- size and time budgets;
- redaction and retention rules.

Stop or narrow collection when any check is unresolved. Do not crawl adjacent pages or hosts merely because they are reachable.

Use the first allowed option in this lowest-sufficient-evidence ladder that answers the design question:

1. a supplied authoritative artifact;
2. permitted live browser capture;
3. permitted static document or style inspection;
4. a supplied screenshot, recording, or annotation set;
5. a bounded human evidence request naming the irreducible gap.

Record the chosen fallback in the Reference Capture Receipt. Do not hide a limitation by treating a fallback as equivalent to an unavailable observation. Do not infer unobserved system semantics from visual frequency alone.
