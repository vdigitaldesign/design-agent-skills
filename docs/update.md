# Update or remove DAS

Record the installed source, version and scope before changing it. Preserve local edits, unrelated plugins, and same-named copies shared with another agent.

## Native plugins

For Codex, inspect `codex plugin list` and `codex plugin marketplace list`. Remove the identified DAS plugin and its marketplace, then register the release tag from the [installation guide](../INSTALL.md):

```sh
codex plugin remove design-agent-skills@design-agent-skills &&
codex plugin marketplace remove design-agent-skills
```

For a project-scoped Claude installation:

```sh
claude plugin uninstall design-agent-skills@design-agent-skills --scope project --keep-data
```

Remove its marketplace declaration only when no other installation needs it:

```sh
claude plugin marketplace remove design-agent-skills --scope project
```

Then use the installation command for the desired version. Inspect other scopes before replacing a marketplace shared with another project. Start a new session and confirm the reported source, version, and enabled state.

## Project-local skills

Identify the exact DAS folders in `.agents/skills/` or `.claude/skills/`, any symlinks, and `skills-lock.json`. Back up edited files outside skill discovery. Remove only the intended DAS copies and matching lock entries; keep a canonical folder still used by another agent. Install the desired client package using its explicit source URL.

The installer’s update command can affect other skills; review its proposed changes before using it. In a project with only disposable DAS copies, the Skills CLI can remove the selected DAS names. Use path-specific removal when same-named copies belong to another client.

## Restore a previous release

Retain the original release or backup until replacement succeeds. Earlier version tags and release assets remain available. Restore the selected client’s documented version and source rather than treating a same-version refresh as an upgrade. Installing files does not establish a model’s design behavior.
