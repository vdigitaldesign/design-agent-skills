# Contributing

Use an [issue form](https://github.com/vdigitaldesign/design-agent-skills/issues/new/choose) to report a problem or describe a capability you need. A focused pull request is welcome when you have a concrete change. [Support](SUPPORT.md) lists the details that make a report reproducible; suspected vulnerabilities follow [SECURITY.md](SECURITY.md).

[AGENTS.md](AGENTS.md) guides agents maintaining this checkout. It is separate from the instructions installed into a user's project. Contributors do not need access to the maintainer's development repository.

## Source ownership

This repository contains published DAS releases. Maintainers integrate accepted contributions into the development source before generating a subsequent release, so a later export retains the change. Keep the issue or pull request linked to the release that delivers it.

The `codex-0.1.0` target contains the 28 instruction sources selected for this release. `TARGET.json` and the verifier bind their source digest. An instruction change creates a new source edition; it cannot inherit this target's evidence by regenerating manifests or editing its identity.

| Change | Source |
| --- | --- |
| A skill's instructions | `skills/<name>/SKILL.md` |
| Shared design guidance | Root `references/<name>.md` |
| User documentation | `README.md`, `INSTALL.md`, or `docs/` |
| Plugin presentation | `.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json`, and `assets/` |
| Package maintenance | `scripts/manage.py` and root `verify.py` |

Each skill's `references/` and `related/` folders are generated supporting copies. Preserve the existing local-link layout; the package tools reconstruct the canonical instruction sources from it.

## Check a change

Explain what the user needs and how the change helps. For an instruction change, describe a task that would distinguish the proposed behavior from the current behavior. A packaging check does not measure design quality.

With Python 3.9 or later, run from the repository root:

```sh
python3 scripts/manage.py check
python3 -m unittest discover -s tests -v
```

For a permitted documentation or metadata change, `python3 scripts/manage.py sync` refreshes generated files and manifests before checking. The tool rejects instruction-source drift under a frozen target before writing. Do not remove the pin or alter the verifier to make a changed source pass under the old identity.

CI runs the check and repository tests on pull requests and pushes to `main`. Keep a pull request focused and include its relevant verification. A source-edition change also needs a maintainer decision about evidence and compatibility.

## Build and release

Build into a new directory outside the checkout:

```sh
python3 scripts/manage.py build --output-dir ../das-release
```

The builder checks the repository, then writes the package directory, deterministic ZIP, and SHA-256 checksum. It excludes local Git and IDE metadata. It refuses an existing output directory and does not publish a release.

Release notes identify the version, source edition, assets, supported routes, limitations, and migration needs. Keep published tags and asset bytes immutable. A compatible correction gets a new patch version; a capability or compatibility change needs an explained version and migration decision. Keep the previous package and checksum available for [rollback](docs/advanced-installation.md#rollback).
