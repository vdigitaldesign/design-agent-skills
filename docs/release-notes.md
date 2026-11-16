# DAS 0.1.5

This patch cleans up public documentation and package metadata. All 28 design instruction resources and the DAS artwork are unchanged from 0.1.4.

## What changed

Public guides focus on installation, use, supported configurations, and known limitations. Target metadata and the verifier identify this edition without carrying development experiment history. Source-integrity checks still reject changes to pinned instructions, including a changed standalone skill with its target label removed.

Public contributor guidance now covers clear writing, exact technical instructions, and keeping private development records out of exports.

## Install or upgrade

Use the [installation guide](../INSTALL.md) for the Codex plugin or project-local Skills CLI copies. Follow [replacement instructions](advanced-installation.md#replace-an-earlier-installation) before changing an existing installation. The [0.1.4 release](https://github.com/vdigitaldesign/design-agent-skills/releases/tag/v0.1.4) remains available for rollback.

The [Claude Code edition](https://github.com/vdigitaldesign/design-agent-skills/tree/claude) has its own version and install guide. Select the edition for your client.

## Verification scope

Package checks cover unchanged instruction sources, complete standalone resources, local links, integrity, and reproducible builds. This cleanup introduces no new model-behavior result. [Supported configurations and limits](advanced-installation.md#support-and-evidence) explain what the observations establish.

Report ordinary problems through [support](../SUPPORT.md) and suspected vulnerabilities through [private reporting](../SECURITY.md). The [MIT license](../LICENSE) applies.
