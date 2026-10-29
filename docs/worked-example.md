# Worked example: reassign selected tickets

This fictional walkthrough adapts the [bulk-reassignment design example](../references/design-lab-protocol.md#golden-example-bulk-reassignment-review). The brief, wireframes, human reply, and handoff are illustrative. They do not report a model run, a real approval, or a shipped interface.

## The request

> Design a bulk-reassignment flow for a support-ticket table. Supervisors need to review the selected tickets and choose an assignee before an action that cannot be undone. Compare ways to organize that work, recommend one, and prepare the selected design for a developer. Keep the existing ticket fields, routes, terminology, and permissions.

The supplied product facts are:

- The table already supports selecting several tickets. Supervisors can reassign them, and some selected tickets may be restricted.
- The field is called **assignee**. Reassignment returns success or failure for each ticket and has no undo.
- Approved table-selection and dialog patterns are available. The side-panel pattern has unresolved keyboard, narrow-layout, and recovery behavior.
- The comparison uses tickets `T-104`, `T-219`, and `T-337`, with Morgan Lee as a placeholder assignee. The mixed-result fixture has two successes and one failure, with no supplied failure reason.

## The options

The design choice is where the supervisor reviews the selection and confirms the action. The underlying ticket rules stay fixed.

| Option | What the supervisor sees | Trade-off |
| --- | --- | --- |
| A: one dialog | Selected tickets, assignee, warning, and action together; results replace the form | Fewest steps, but less opportunity to notice an accidental selection |
| B: review, then confirm | A selection-review step, an assignee-confirmation step, then ticket-level results | One extra step makes the selected scope explicit before the irreversible action |
| C: side workspace | The table remains visible beside the controls and results | Preserves spatial context, but needs the missing side-panel behavior resolved before it can advance |

The recommendation is **B**. It gives the selected tickets a deliberate review step and builds on the existing table and dialog patterns. Only the staged bulk flow and its result state need design-system work.

## The human choice

An illustrative reply:

> Choose B. Keep the selected-ticket review separate from the assignee confirmation, and retain a result for every ticket. Use the existing table and dialog patterns with the scoped extension described above. Keep the ticket rules and permissions unchanged.

This selects the interaction structure. It leaves the unsupplied service behavior open.

## The developer handoff

The handoff identifies the chosen flow, content, checks, and remaining product questions. Here is the useful part a developer would receive.

### Selected flow

Use the existing dialog pattern for two steps followed by results:

```text
REVIEW SELECTED TICKETS
┌─────────────────────────────┐
│ T-104                       │
│ T-219                       │
│ T-337                       │
│ Some may be restricted.     │
│             [Cancel] [Next] │
└─────────────────────────────┘

CONFIRM REASSIGNMENT
┌─────────────────────────────┐
│ Assignee                    │
│ [ Morgan Lee ▾ ]            │
│ Cannot be undone.           │
│           [Back] [Reassign] │
└─────────────────────────────┘

RESULTS
┌─────────────────────────────┐
│ T-104  Success              │
│ T-219  Failure              │
│ T-337  Success              │
│                     [Close] │
└─────────────────────────────┘
```

The content and reading order carry into the narrow layout. Each ticket keeps a written result; color alone is insufficient. Follow the existing dialog's keyboard and focus behavior. Keep ticket routes, fields, the term *assignee*, and the permission model unchanged.

### Checks for the selected design

- With the three fixture tickets selected, each ID is reviewable before confirmation.
- The confirmation step identifies the assignee and states that the action cannot be undone.
- The mixed-result view retains `T-104: Success`, `T-219: Failure`, and `T-337: Success`. It invents no reason for the failure, retry, or undo.
- At wide and narrow sizes, inspect the review and confirmation steps and every ticket result. Check keyboard access and focus order against the existing dialog pattern.

These are checks to perform when a prototype or implementation exists. The wireframes alone do not establish that they pass.

### What remains open

The brief supplies no rules for executing progress, retry, timeout, offline behavior, or selection after closing. Restriction detection also needs a source. The developer can use this handoff to understand and prototype the selected structure; a complete production contract needs those product and service rules, followed by the project's implementation approval.

The next useful request is specific: provide the rules for those states so the agent can complete the acceptance checks and handoff. It should retain the selected B structure unless the new facts reveal a conflict.

Use the [brief template](getting-started.md#brief-template) for your own task. [How DAS works](how-das-works.md) explains how the selected design carries into implementation and later verification.
