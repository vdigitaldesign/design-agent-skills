# Use DAS in Claude Code

[Install the plugin or project-local skills](../INSTALL.md), then open a new session in your project. Invoke a skill explicitly:

| Installation | Router | Specialist example |
| --- | --- | --- |
| Native plugin | `/design-agent-skills:design-router` | `/design-agent-skills:audit-design-surface` |
| Project-local copied skills | `/design-router` | `/audit-design-surface` |

Start with the router when the task spans several operations or the next useful step is unclear. Invoke a specialist directly for a clear task. The [catalog](skills.md) describes the sixteen skills.

## Supply the product context

Identify the task, relevant source files, current interface or preview, constraints, and existing decisions. Say what may change, who makes material decisions, and where to save the result. Keep unavailable facts and unresolved choices visible.

For example, ask the agent to audit a flow while preserving its pricing and eligibility rules. A new flow may need alternatives, your choice, and a design contract. A routine correction already governed by an approved rule can go directly to a focused handoff.

## Continue the work

Keep connected work in the same chat while it depends on earlier context. For a new chat, provide the current handoff and its source files, and confirm that the recipient can open them. Do not rely on the previous chat's memory.

## Check the result

Compare the proposed behavior with the product rules. Check exact content, permissions, failure and recovery paths, required acceptance checks, and unresolved decisions. Confirm the approved revision and actual implementation authorization.

After implementation, invoke `verify-design-implementation` with the approved target and a running interface. Report unavailable observations explicitly. A successful package check or the agent's own validation does not establish that the design is complete.
