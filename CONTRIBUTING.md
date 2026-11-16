# Contributing

Use a [GitHub issue](https://github.com/vdigitaldesign/design-agent-skills/issues/new) to report a problem or describe a capability you need. A focused pull request is welcome when you have a concrete change. Read [support](SUPPORT.md) for useful report details; suspected vulnerabilities follow [security reporting](SECURITY.md).

## Source ownership

This is the Claude distribution. Keep the contribution tied to the client edition and release it affects. [AGENTS.md](AGENTS.md) guides agents maintaining this checkout; it is separate from the instructions installed into a user's project.

The editable instructions are `skills/<name>/SKILL.md`, root `references/`, and the writer's `references/source-version-reading.md`. Each skill's other `references/` and `related/` files are generated supporting copies. Edit the owning source and regenerate its copies together.

`TARGET.json` identifies the selected instruction edition and its source digest. Changing instructions creates a new source edition and needs a maintainer decision about behavior and compatibility. Editing identifiers or regenerating manifests cannot give changed instructions the old edition's evidence.

## Check a change

Explain the user's task, the expected result, and how your change helps. For instruction changes, describe a task that could reveal the missing behavior. Keep original model outputs unchanged when using them as evidence.

For a documentation or metadata change, run:

```sh
python3 scripts/manage.py sync &&
python3 scripts/manage.py check &&
python3 -m unittest discover -s tests -v
```

The tool rejects changes to pinned instruction sources before writing. Package checks establish integrity and portability; they do not assess design quality.

Keep public copy focused on installation, use, contribution, and known limitations. Preserve exact commands and supported claims when editing. Keep credentials, customer material, local machine paths, and development experiment logs out of the package and public reports.

## Build and release

Build into a new directory outside the checkout:

```sh
python3 scripts/manage.py build --output-dir ../das-release
```

The builder produces a package directory, deterministic archive, and checksum. It refuses an existing destination and does not publish anything. Published tags and asset bytes remain immutable; changes require a new version. Keep the previous release available for [rollback](docs/advanced-installation.md#replace-or-restore-an-installation).
