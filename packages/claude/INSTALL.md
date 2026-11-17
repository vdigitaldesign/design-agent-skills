# Install DAS in Claude Code

Choose the native plugin or project-local skills. Use one route per project to avoid duplicate entries. [Advanced installation](docs/advanced-installation.md) covers existing copies, fixed releases, and rollback.

You need Claude Code with model access. The plugin route needs a client with `claude plugin` commands. The Skills CLI route also needs Git, npm, and Node.js 22.20 or later. Python 3.9 or later is needed only for optional package verification and maintenance.

## Native plugin

From your project, run:

```sh
claude plugin marketplace add 'vdigitaldesign/design-agent-skills#v0.1.7' --scope project &&
claude plugin install design-agent-skills@design-agent-skills --scope project &&
claude plugin list
```

Both native clients use the same repository release. The marketplace manifest selects the Claude package. A marketplace you add this way is maintained by DAS; it does not imply a listing in Anthropic's directory.

Start a new Claude Code session. Confirm that `/design-agent-skills:design-router` is available. Follow the [first-task example](README.md#start-with-a-task).

Project scope records the installation in this project's Claude settings. If DAS is already registered, inspect `claude plugin marketplace list` and `claude plugin list` before replacing it. Keep installations used by other projects intact.

### Update or remove the plugin

To receive the current registered release:

```sh
claude plugin marketplace update design-agent-skills &&
claude plugin update design-agent-skills@design-agent-skills --scope project
```

Start a new session and inspect the reported version. Background auto-update is a separate client setting; these instructions do not enable it.

To remove this project's installation:

```sh
claude plugin uninstall design-agent-skills@design-agent-skills --scope project --keep-data
```

Remove the marketplace registration only when no other installation needs it. See [replacement and rollback](docs/advanced-installation.md#replace-or-restore-an-installation).

## Project-local skills

From your project, run:

```sh
npx --yes skills@1.7.4 add https://github.com/vdigitaldesign/design-agent-skills/tree/v0.1.7/packages/claude --agent claude-code --skill '*' --copy --yes
```

This copies all sixteen skills into the project's Claude skills directory. The explicit URL selects the Claude edition; `--agent claude-code` selects where to install it. Each complete skill folder includes its supporting references and integrity files.

Start a new session and invoke `/design-router`. These names have no plugin prefix. For a fixed release, use the [pinned command](docs/advanced-installation.md#install-a-fixed-release).

Update copied skills from their recorded source with:

```sh
npx --yes skills@1.7.4 update
```

The update command can affect other installed skills. Review the installer's proposed changes and preserve local edits first. To remove only DAS from this project's Claude installation:

```sh
npx --yes skills@1.7.4 remove assess-design-reuse audit-design-surface audit-design-system design-router develop-visual-direction evolve-design-system explore-design-directions frame-design-task maintain-design-knowledge prototype-design-directions publish-design-system-canon reconstruct-design-context record-design-decision validate-design-contract verify-design-implementation write-design-contract --agent claude-code --yes
```

Check the remaining skill folders and `skills-lock.json`; keep unrelated skills. Installer behavior and telemetry are described in the [Skills CLI documentation](https://github.com/vercel-labs/skills).

## Check your setup

Confirm that the intended entries are available in a fresh session. Use a small task with source files you can inspect, and check that the agent can open the references it needs. If an entry is missing or a file cannot be read, follow [troubleshooting](docs/advanced-installation.md#troubleshooting).
