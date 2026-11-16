# Design Lab protocol

Use a Design Lab when material alternatives need tangible, comparable evidence. A lab may use disposable sandbox code, a design tool, annotated frames, or another authorized medium. Treat prototype source and output as evidence only. Do not reuse them as production implementation.

## Lab manifest

### Identity

- Lab ID, title, revision, status, authoring method, and capture date:
- Material question and intended human decision:
- Authority source and selection authority:
- Source Task Frame, Design Read, audits, reuse assessment, and visual references:

### Fixed facts

List the product facts, approved terminology, data relationships, required content, platform constraints, effective system rules, and protected boundaries that must stay the same across every variant. Link each fact to its owner and revision.

### Variable axes

Name only the decision-relevant axes that are allowed to differ. These may include interaction structure, disclosure, composition, hierarchy, density, visual expressiveness, motion/feedback, or recovery model. Describe variation qualitatively. Do not invent universal numeric dials.

### Comparable variants

For every variant record:

- stable variant ID, name, and premise;
- exact axes changed and facts preserved;
- reuse/system posture;
- interaction, state, accessibility, responsive, content, and visual-craft implications;
- strengths, costs, risks, and conditions of fit.

Keep facts, representative content, evaluation tasks, viewport set, and state set stable unless the changed item is itself the axis under test. Differences should result from the direction rather than accidental prototype drift.

### Required frames and states

Include the smallest set that exposes the material differences:

- entry or context frame;
- primary ready state;
- material decision or action state;
- meaningful success/result state;
- relevant empty, validation, permission, progress, failure, partial success, interruption, cancellation, retry, undo, or recovery states;
- at least one narrow and one wide condition when responsive behavior can affect meaning;
- relevant keyboard/focus and assistive-technology annotations;
- long/localized/RTL or theme condition when it can change the choice.

Omit irrelevant states, but state why the omission cannot change the decision.

### Interaction script

Provide a repeatable script for each variant:

1. starting state and fixture data;
2. input or action sequence;
3. expected prototype response;
4. observation target;
5. reset method.

The script demonstrates the proposed design. It demonstrates actual service behavior only if a real implementation was observed.

### Artifact record

- Editable source locator:
- Export, image, video, or prototype locator:
- Artifact revision and source-revision pins:
- Tool or method used:
- What is interactive, simulated, annotated, or omitted:
- Media provenance and privacy constraints:
- Known fidelity and accessibility limitations:

### Comparison and selection lineage

- Cross-variant findings by material axis:
- Recommendation, trade-offs, and evidence that would change it:
- Owner question:
- Selection status and exact response:
- Selected variant or combination, modifications, decision-record reference, and date:
- Superseded lab revision, if any:

## Golden example: bulk reassignment review

This synthetic, **illustrative** example demonstrates a complete Markdown-first Lab record. Its facts and wireframes are fixtures. They do not define universal product canon or claim that external prototype artifacts exist.

### Identity

- **Lab:** `LAB-BULK-REASSIGN`, “Safer bulk reassignment,” revision `r1`, `proposed`.
- **Material question:** how a supervisor reviews and executes an irreversible reassignment across selected support tickets.
- **Decision:** select an interaction structure and the smallest design-system posture.
- **Authority:** the commissioning human may select this scoped flow; no variant is selected in this revision.
- **Inputs:** synthetic Task Frame, Design Read, table/dialog system assessment, and reuse assessment bundled with the fixture.

### Fixed facts

- The approved term is `assignee`.
- Ticket routes and fields do not change.
- The existing table supports multi-select; supervisors may reassign.
- Some selected tickets are restricted.
- Execution returns success or failure for each ticket and has no undo.
- Effective table-selection and dialog patterns may be consumed.
- The existing side-panel pattern lacks effective keyboard, narrow-layout, and recovery requirements.
- Placeholder ticket IDs and names are prototype data, not claims about real users.

### Variable axes

- placement and persistence of the task surface;
- whether selected scope receives a dedicated review step;
- grouping of assignee choice, irreversible warning, and final action;
- persistence of per-ticket results;
- required system posture: bounded extension versus side-panel repair.

Visual brand, terminology, ticket content, result facts, and permission model remain fixed.

### Variants

#### `A` — Single guardrail dialog

One dialog combines the selected-set summary, assignee choice, no-undo warning, and action. It then becomes the ticket-result view. It consumes the dialog and extends only a result state. It is fastest and smallest, but offers limited opportunity to deliberately review an accidental selection.

#### `B` — Review, then confirm

A staged dialog separates complete selected-set review from assignee confirmation. It then retains ticket-level results. It consumes table/dialog canon and extends a scoped staged bulk pattern. It adds a step but provides the clearest safety boundary without unsupported service assumptions.

#### `C` — Persistent side workspace

A side workspace keeps table context visible beside controls and results. It offers the strongest spatial context. It cannot advance without approved repair of keyboard, narrow-layout, and recovery behavior. Show its unsupported narrow state as a limitation. Do not silently design that state as canon.

### Required frames and fixture states

Every variant shows:

- table context with tickets `T-104`, `T-219`, and `T-337` selected;
- ready/review state;
- final confirmation with `assignee` and no-undo meaning;
- mixed result: two success, one failure, with no invented failure reason;
- wide viewport and narrow viewport;
- focus-order annotations and text status not dependent on color.

The example omits executing progress, retry, timeout, offline, and post-close selection because no governing service facts are supplied. These omissions matter to a final contract but do not prevent selection of the interaction structure.

### Illustrative tangible frames

These compact wireframes are the installed artifact evidence for this example. They share the same fixture content and expose the compared ready/review, confirmation, mixed-result, and narrow conditions.

#### Variant A frames

```text
WIDE · READY AND FINAL CONFIRMATION
┌────────────────────────────────────────┐
│ Reassign 3 tickets                     │
│ T-104 · T-219 · T-337                  │
│ Assignee  [ Morgan Lee ▾ ]             │
│ Some tickets may be restricted.        │
│ Reassignment cannot be undone.         │
│                       [Cancel] [Reassign]│
└────────────────────────────────────────┘

WIDE · MIXED RESULT
┌────────────────────────────────────────┐
│ Reassignment results                   │
│ T-104  Success                         │
│ T-219  Failure                         │
│ T-337  Success                  [Close] │
└────────────────────────────────────────┘

NARROW · READY/CONFIRM
┌──────────────────────┐
│ Reassign 3 tickets   │
│ T-104 · T-219 · T-337│
│ Assignee             │
│ [ Morgan Lee ▾ ]     │
│ Cannot be undone.    │
│ [Cancel]             │
│ [Reassign]           │
└──────────────────────┘
```

The one-step surface makes ready and final confirmation the same state. That compression is the material trade-off, not a missing frame.

#### Variant B frames

```text
WIDE · REVIEW
┌────────────────────────────────────────┐
│ Step 1 · Review selected tickets       │
│ T-104                                  │
│ T-219   Some may be restricted.        │
│ T-337                    [Cancel] [Next]│
└────────────────────────────────────────┘

WIDE · FINAL CONFIRMATION
┌────────────────────────────────────────┐
│ Step 2 · Confirm reassignment           │
│ Assignee  [ Morgan Lee ▾ ]             │
│ Each ticket returns success or failure.│
│ Reassignment cannot be undone.         │
│                       [Back] [Reassign] │
└────────────────────────────────────────┘

WIDE · MIXED RESULT
┌────────────────────────────────────────┐
│ Step 3 · Results                       │
│ T-104  Success                         │
│ T-219  Failure                         │
│ T-337  Success                  [Close] │
└────────────────────────────────────────┘

NARROW · REVIEW → CONFIRM
┌──────────────────────┐  ┌──────────────────────┐
│ Review selected      │  │ Confirm reassignment │
│ T-104                │  │ Assignee             │
│ T-219                │→ │ [ Morgan Lee ▾ ]     │
│ T-337                │  │ Cannot be undone.    │
│ [Cancel] [Next]      │  │ [Back] [Reassign]    │
└──────────────────────┘  └──────────────────────┘
```

#### Variant C frames

```text
WIDE · READY AND FINAL CONFIRMATION
┌──────────────────────┬─────────────────────────┐
│ Ticket table         │ Reassign selected       │
│ ☑ T-104              │ T-104 · T-219 · T-337  │
│ ☑ T-219              │ Assignee [Morgan Lee ▾]│
│ ☑ T-337              │ Cannot be undone.      │
│                      │ [Cancel] [Reassign]     │
└──────────────────────┴─────────────────────────┘

WIDE · MIXED RESULT
┌──────────────────────┬─────────────────────────┐
│ Ticket table         │ Results                 │
│ T-104                │ T-104  Success          │
│ T-219                │ T-219  Failure          │
│ T-337                │ T-337  Success  [Close] │
└──────────────────────┴─────────────────────────┘

NARROW
┌────────────────────────────────────────────────┐
│ INCONCLUSIVE ARTIFACT                          │
│ The side-panel canon has no approved narrow,   │
│ keyboard, or recovery behavior. Do not invent  │
│ a drawer/stack fallback in this Lab revision.  │
└────────────────────────────────────────────────┘
```

Text status labels remain present in every result frame. The diagrams do not rely on color. Focus order follows reading order in A/B. C’s focus and narrow behavior remain explicitly unresolved.

### Interaction script

1. Reset to three selected tickets and no assignee choice.
2. Open each variant from the same table action.
3. Inspect whether all selected tickets are reviewable before execution.
4. Choose the same placeholder assignee.
5. Reach the irreversible action using keyboard only.
6. Trigger the simulated mixed result.
7. Verify every ticket retains a text outcome and no retry/undo is invented.
8. Switch to the narrow frame and repeat the decision-critical steps.

### Artifact record

- **Record locator:** [golden example manifest](#golden-example-bulk-reassignment-review).
- **Artifact/media locators:** [Variant A frames](#variant-a-frames), [Variant B frames](#variant-b-frames), and [Variant C frames](#variant-c-frames).
- **Revision:** `LAB-BULK-REASSIGN r1`; the in-document frames share this revision.
- **Method:** inline Markdown wireframes; no external editable source, export, image, video, or executable prototype is claimed.
- **Simulation boundary:** the frames compare structure and named states only; they do not prove service timing, permissions, restriction detection, responsive implementation, or actual accessibility conformance.
- **Production rule:** the diagrams and placeholder content are illustrative evidence and may not be copied into production as implementation.

### Comparison and recommendation

Recommend `B`: it makes selected scope reviewable before an irreversible action, preserves ticket-level results, and requires only a bounded extension over effective primitives. Choose `A` when evidence shows deliberate selected-set review is unnecessary. Choose `C` only with separate authority to repair the partial side-panel contract.

**Owner question:** “Select A, B, or C and approve its stated system posture; or name a combination that should receive another lab revision.”

**Selection lineage:** `unselected` in `r1`. After an explicit response, create an Owner Decision Record that cites this lab revision and the exact variant/modifications. The lab remains evidence. The decision and later effective contract own approved meaning.
