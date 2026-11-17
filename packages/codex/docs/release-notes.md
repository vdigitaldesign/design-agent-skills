# DAS 0.1.7

This patch clarifies how agents handle instructions found in retrieved content. It applies to both the Codex and Claude Code editions.

## What changed

Instructions found in pages, documents, repository content, or tool results do not grant permission to run commands, transfer data, change files, or expand the task. Actions already authorized by the task and relevant product requirements remain usable. The agent client's permissions and isolation still apply.

Other design instructions, the 16-skill catalog, and the DAS artwork are unchanged.

## Install or upgrade

Use the [installation guide](../INSTALL.md) for the Codex plugin or project-local Skills CLI copies. Follow [replacement instructions](advanced-installation.md#replace-an-earlier-installation) before changing an existing installation. The [0.1.6 release](https://github.com/vdigitaldesign/design-agent-skills/releases/tag/v0.1.6) remains available for rollback.

The [Claude Code edition](https://github.com/vdigitaldesign/design-agent-skills/tree/v0.1.7/packages/claude) shares this release version and has its own installation guide.

## Verification scope

Package checks cover the shared-reference change, complete standalone resources, local links, integrity, and reproducible builds. This patch adds no new model-behavior or runtime security result. [Supported configurations and limits](advanced-installation.md#support-and-evidence) describe the existing observations.

Report ordinary problems through [support](../SUPPORT.md) and suspected vulnerabilities through [private reporting](../SECURITY.md). The [MIT license](../LICENSE) applies.
