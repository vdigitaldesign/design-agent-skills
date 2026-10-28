---
name: develop-visual-direction
description: Create, compare, critique, or refine a product-grounded visual direction for an interface. Use when hierarchy, composition, typography, color relationships, density, imagery, affordance, distinctiveness, or polish is a material design question; do not impose a universal aesthetic or invent brand canon.
---

# Develop Visual Direction

Create tangible, coherent visual design from product intent and trustworthy references. Generic styling adjectives are not enough.

## Packet mode

- **Carried:** use and update the supplied valid Design Work Packet. Do not reconstruct its intake or reread pinned authority merely to confirm it.
- **Direct single-skill:** when visual-direction work is the complete requested outcome, return its native record or artifact. Do not create a packet.
- **Direct expansion:** when direct visual work becomes a material or uncertain multi-skill chain, create exactly one [Design Work Packet](../references/packet-projections.md#design-work-packet) before the first downstream handoff.

Refresh a carried packet only when a required field is missing, a source is stale or conflicting, scope or authority changes, or genuinely new visual evidence appears.

Without a valid packet, read [authority and status](../references/authority-and-status.md). Load [visual-direction craft](../references/visual-craft.md) when you produce its formal records or need its detailed craft lenses. Load the [Design Lab protocol](../references/design-lab-protocol.md) only for a controlled, tangible comparison of multiple variants or prototypes. Do not load it for a single direction or a low-fidelity comparison.

Keep operational workflows declared in the packet inactive when API, data, implementation, or operational material is only observed evidence. Re-route only for an actual mutation, implementation, diagnosis trigger, or a stronger consumer-policy requirement.

When material external references influence the work, create or use the canonical [Reference Capture Receipt](../references/product-profile-and-tools.md#reference-capture-receipt) before using those references. Reuse a valid receipt if its source, intent, scope, freshness, permissions, and limitations still match. Otherwise, perform the canonical [preflight and lowest-sufficient-evidence fallback](../references/product-profile-and-tools.md#normalized-limitations-and-fallbacks) and create a receipt. Direct invocation remains valid and does not require unrelated framing.

## Establish visual authority

Identify the user moment, product purpose, attentional priority, effective brand/design-system sources, reference type and revision, commissioned intent, permitted influence, content realities, platforms, and visual protected boundaries. Separate fixed identity or system facts from visual axes that remain open. An inspiration, benchmark, or reproduction request does not override controlling product or system canon.

When no brand canon exists, derive a proposed visual premise from product intent and evidence. Label it `proposed`. Do not fabricate a brand personality or make the premise effective through repetition.

## Craft the direction

Actively design the relationships relevant to the task:

- hierarchy and attentional sequence;
- rhythm, grouping, and negative space;
- optical balance and alignment;
- composition and responsive transformation;
- typographic roles and content extremes;
- color relationships across state, surface, and theme;
- density appropriate to the task and input mode;
- imagery and iconography that explain the offering;
- affordance and legibility across all interaction states;
- coherence across content, interaction, motion, and system rules;
- product-specific distinctiveness and polish in edge states.

When physical form, materials, space, or use context matters to the user's decision, make those properties inspectable through coherent subject imagery grounded in facts. Reuse suitable authorized assets. When none fit and image generation is available and permitted, create and use generated imagery within the task budget. Preserve the generated imagery locally.

Use diagrams or CSS/SVG when they better explain structure or behavior. Omit imagery that adds no product understanding. Keep required facts, controls, and feedback live and legible, including on narrow screens and in interaction states. Preserve purpose, provenance, crop, and fallback.

Use effective canon where it fits. When a visual need exposes missing or harmful system guidance, route that scope to [audit-design-system](../SKILL.md) and [evolve-design-system](evolve-design-system.md). Do not hide invention inside a mock.

## Make it visible

Produce the smallest artifact that actually reveals the visual decision. Use annotated composition frames for hierarchy/layout, rendered mocks for visual relationships, and a Design Lab when alternatives must be compared. Include realistic content extremes and relevant conditions: ready, focus, selected, disabled, loading, error, success, narrow/wide, theme, localization, or RTL.

When a material visual choice is open, usually show two or three directions. Keep their facts the same and vary named composition or expression axes. Do not create variants that differ only in accent color or decoration.

Disposable sandbox code is allowed when it is authorized and necessary to evaluate spatial or responsive behavior. Record that code as prototype evidence and forbid its reuse in production.

For material motion and external assets, create or update the central Motion Choice Record and External Asset Candidate Record from [visual-direction craft](../references/visual-craft.md). Carry their IDs and revisions into artifacts. Do not redefine their fields.

The Visual Direction Record is proposal evidence, not a Visual System Projection. Create the optional projection only after an exact approved or effective source exists. Apply the [packet projection](../references/packet-projections.md) status rules.

## Critique, refine, and recommend

Use the Visual Direction Record in the shared craft reference. Identify strengths to preserve and weaknesses with consequences for users. Refine optical, typographic, state, responsive, and content details without changing the material premise.

Recommend a direction when evidence supports it. Name trade-offs and evidence that would falsify the recommendation. If selection is still open, ask the smallest explicit owner question. A visual artifact remains evidence until selection is recorded and its requirements enter effective product canon, effective design-system canon, or an effective Design Contract.

Continue to [record-design-decision](record-design-decision.md) when an explicit scoped selection already exists. Do not stop at a visual critique when the safe dependent chain can proceed.

In carried or direct-expansion mode, update the packet with:

- the current step;
- the Visual Direction Record and artifact locators and revisions;
- motion and asset evidence;
- the recommendation;
- findings to preserve;
- the selection gate;
- the next step and stop.

In direct single-skill mode, return the native visual output without a Design Work Packet.

Route a visual technique or reference non-fit to [maintain-design-knowledge](maintain-design-knowledge.md) only when evidence makes it useful across later tasks. Do not promote a selected product aesthetic into universal guidance.
