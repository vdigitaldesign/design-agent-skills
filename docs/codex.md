# Use DAS in Codex

Install the [0.1.2 plugin or project-local skills](../INSTALL.md), then open a new Codex session in the project where you want to work. Select a skill from the picker or name it explicitly in your request. If you are replacing an earlier release or a development package, follow [replacement and rollback](advanced-installation.md#replace-an-earlier-installation) first.

| Installation | Router invocation | Specialist example |
| --- | --- | --- |
| Codex plugin | `$design-agent-skills:design-router` | `$design-agent-skills:audit-design-surface` |
| Project-local copied skills | `$design-router` | `$audit-design-surface` |

The plugin entries are namespaced as **Design Agent Skills: …**. Project-local entries may carry the **Project** label. A catalog card can remain after uninstalling a plugin; check the installed state and skill picker to see what the session can use.

## Start with the right scope

Use Design Router when the request spans several design operations or you are unsure which specialist fits. For a clear task, invoke the specialist directly. The [catalog](skills.md) describes all 16 skills.

Attach the relevant source files or identify their locations. Explain the user task, constraints, existing decisions, and the result you need. The [brief template](getting-started.md#brief-template) is a useful starting point.

Codex supplies the model and available tools. DAS has no bundled browser, design service, image generator, or runtime. If a task needs a tool the session cannot access, the result should say what could not be inspected or produced.

## Continue a design task

Keep a connected design task in the same chat when it depends on earlier work. Review proposed alternatives and make material choices explicitly. A direction selection and permission to implement can be different decisions; state which one you are making.

For a new chat, provide the current handoff and its source files. Check that the recipient can open the complete material rather than relying on the earlier chat's memory. [How DAS works](how-das-works.md) explains the authority and handoff boundaries.

## Check a result

Review the proposed behavior against your product rules. Confirm that important states and recovery paths have concrete checks, and that the handoff identifies unresolved questions and protected behavior. After implementation, invoke Verify Design Implementation with the approved target and the running interface.

The recorded design-contract checks used `gpt-6-astra` with `ultra` reasoning. Short installation-route handoffs used `low`. These are observed settings, not a requirement that every task use one effort level or a guarantee for another model. See [support and evidence](advanced-installation.md#support-and-evidence).
