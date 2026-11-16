# Changelog

## 0.1.6

This client package is distributed from the shared repository tree with explicit installation paths and a common release version. Its instruction resources and existing artwork are unchanged.

## 0.1.5

- Clean public guides and metadata, keeping useful support information and known limitations.
- Keep development experiment history out of the public verifier and generated copies.
- Preserve all design instruction resources and artwork from 0.1.4.
- Add public writing and export guidance for contributors.

No new model task was run for this packaging and documentation patch.

## 0.1.4

### Changed

- Remove repeated packet-field and continuation instructions from design-router.
- Split write-design-contract into focused sections and six acceptance-procedure steps, preserving all requirements and applicable cases.
- Identify the revised instruction sources as `codex-0.1.4`; the other 26 sources remain unchanged from 0.1.3.

No new model task was run for this editorial patch. See the [release notes](docs/release-notes.md) and [upgrade guidance](docs/advanced-installation.md#replace-an-earlier-installation).

## 0.1.3

### Changed

- Update the README banner, plugin icon, and repository social-preview image with the new green artwork.
- Match the plugin colors and README tagline to the artwork.

Skill instructions are unchanged from 0.1.2. See the [release notes](docs/release-notes.md) and [upgrade guidance](docs/advanced-installation.md#replace-an-earlier-installation).

## 0.1.2

### Fixed

- A conforming implementation-check result no longer asks for an issue classification. The existing categories still apply to discrepancies and inconclusive observations.

### Changed

- The quick start uses the shorter interactive Skills CLI command, with a fixed-release command available in the installation guide.
- The package identifies the revised instructions as `codex-0.1.2`. Earlier behavior-test results remain attributed to their original sources.

See the [0.1.2 release notes](https://github.com/vdigitaldesign/design-agent-skills/releases/tag/v0.1.2) for verification scope and [upgrade guidance](docs/advanced-installation.md#replace-an-earlier-installation).

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
- Preserves the instruction sources from the initial design-contract and approval-chain checks.
- Includes a task brief, skill catalog, engineering integration guidance, installation and replacement instructions, and support and contribution routes.
- Ships a source-pinned package, integrity verifier, reproducible archive builder, and checksums.

Claude is outside this release's supported configurations. Test scope and known limits are in the [0.1.0 release notes](https://github.com/vdigitaldesign/design-agent-skills/releases/tag/v0.1.0).
