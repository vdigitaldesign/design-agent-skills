# Support

DAS 0.1.2 supports the documented Codex app and CLI workflows through the plugin and project-local copied-skill routes. Claude support is under development and is not included in this release.

Volodymyr Onishchenko (`vdigitaldesign`) maintains the project. Use the repository's [issue forms](https://github.com/vdigitaldesign/design-agent-skills/issues/new/choose) for ordinary problems and feature requests. There is no guaranteed response time.

## Before opening an issue

Check [installation](INSTALL.md), the [Codex guide](docs/codex.md), and [troubleshooting](docs/advanced-installation.md#troubleshooting). For a design result, identify the requirement the result missed. For an installation problem, include the command and its error.

Provide the release or archive name, client version, installation route, invoked skill, and model/settings when known. Describe what you expected, what happened, and the smallest steps or source excerpt needed to reproduce it. Do not guess missing details.

Remove credentials, customer information, and private project material before posting. Suspected vulnerabilities belong in the [private reporting route](SECURITY.md), not public issues.

## Scope of support

The [tested configurations](docs/advanced-installation.md#support-and-evidence) identify the observations behind this release. Model behavior can vary with task context, available tools, and configuration. The checks do not establish a guarantee for every model, skill, operating system, or product.

DAS does not supply Codex authentication, model access, or external tool integrations. Report those failures to the corresponding provider. The repository's `CLAUDE.md` guides contributors working on this checkout; it does not advertise Claude consumer support.

For a proposed capability, explain the user task and what DAS should help accomplish. [Contributing](CONTRIBUTING.md) covers changes to the package.
