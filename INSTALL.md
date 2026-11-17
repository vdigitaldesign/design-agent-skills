# Install Design Agent Skills 0.1.7

Choose your client and one route per project. Native plugins need a client that exposes its `plugin` commands. Project-local skills need Git, npm, and Node.js 22.20 or later. Python 3.9 or later is needed only for optional integrity checks and maintenance.

## Codex plugin

```sh
codex plugin marketplace add vdigitaldesign/design-agent-skills --ref v0.1.7 &&
codex plugin add design-agent-skills@design-agent-skills &&
codex plugin list
```

Start a new session and select Design Agent Skills: Design Router, or invoke `$design-agent-skills:design-router`.

## Codex project-local skills

```sh
npx --yes skills@1.7.4 add https://github.com/vdigitaldesign/design-agent-skills/tree/v0.1.7/packages/codex --agent codex --skill '*' --copy --yes
```

This installs the Codex package as complete project-local copies in `.agents/skills/`. Invoke `$design-router` in a new session. That shared directory can also be read by other agents; preserve existing same-named skills before replacement.

## Claude plugin

```sh
claude plugin marketplace add 'vdigitaldesign/design-agent-skills#v0.1.7' --scope project &&
claude plugin install design-agent-skills@design-agent-skills --scope project &&
claude plugin list
```

Start a new session and invoke `/design-agent-skills:design-router`. A marketplace maintained by DAS does not imply a listing in Anthropic's directory.

## Claude project-local skills

```sh
npx --yes skills@1.7.4 add https://github.com/vdigitaldesign/design-agent-skills/tree/v0.1.7/packages/claude --agent claude-code --skill '*' --copy --yes
```

This copies the Claude package into `.claude/skills/`. Invoke `/design-router` in a new session. The source path selects the client instructions; `--agent` selects the installation destination.

## Projects used by both clients

Use native plugins when both clients work in the same project. For copied skills, select one client package for that project: the installer shares source-lock records by skill name.

## Verify or maintain a checkout

```sh
python3 scripts/manage.py check
python3 -m unittest discover -s tests -v
```

The first command checks both complete client packages, their source pins, marketplace pointers, local links and manifests. The second runs offline maintenance checks. Neither invokes a model or installs a plugin.

Use [update and removal](docs/update.md) before replacing an installation. Client authentication and model access are supplied by your environment.
