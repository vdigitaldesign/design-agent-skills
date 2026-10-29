# Changelog

## 0.1.2

### Fixed

- A conforming implementation-check result no longer asks for an issue classification. The existing categories still apply to discrepancies and inconclusive observations.

### Changed

- The quick start uses the shorter interactive Skills CLI command, with a fixed-release command available in the installation guide.
- The package identifies the revised instructions as `codex-0.1.2`. Earlier behavior-test results remain attributed to their original sources.

See the [release notes](docs/release-notes.md) for verification scope and [upgrade guidance](docs/advanced-installation.md#replace-an-earlier-installation).

## 0.1.1

### Fixed

- Stop archive extraction and verifier execution when the checksum fails.
- Clarify removal scope so users can preserve another agent's same-named skills.
- Deliver consistent product descriptions in the README and installed plugin.

### Added

- A worked example from a design brief to a selected direction and developer handoff.
- A public summary of completed release-installation checks, with their scope and limits.

The qualified design instructions are unchanged. See the [0.1.1 release notes](https://github.com/vdigitaldesign/design-agent-skills/releases/tag/v0.1.1) and [upgrade guidance](docs/advanced-installation.md#replace-an-earlier-installation).

## 0.1.0

First supported Codex edition of Design Agent Skills.

- Includes 16 design skills and 12 shared references, from context reconstruction and interface audits through design decisions, contracts, and implementation verification.
- Provides a Codex plugin and project-local Skills CLI installation.
- Preserves the instruction sources from the completed RC1 design-contract and approval-chain checks.
- Includes a task brief, skill catalog, engineering integration guidance, installation and replacement instructions, and support and contribution routes.
- Ships a source-pinned package, integrity verifier, reproducible archive builder, and checksums.

Claude is outside this release's supported configurations. Test scope and known limits are in the [0.1.0 release notes](https://github.com/vdigitaldesign/design-agent-skills/releases/tag/v0.1.0).
