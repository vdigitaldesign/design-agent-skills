# DAS 0.1.4

This patch makes design-router and write-design-contract easier to read while preserving every requirement, criterion and applicable case.

## What changed

The router refers to the existing packet-field owner and consolidates repeated continuation instructions. The contract writer separates source binding, unchanged source assembly, proposals, acceptance procedures and coverage. Its dense acceptance paragraph becomes six sequential steps.

Exactly two of the 28 instruction sources differ from 0.1.3. The other 26 sources, human decision authority and the earlier implementation-check template clarification remain unchanged. Package version and instruction target are both `0.1.4` (`codex-0.1.4` in `TARGET.json`).

## Install or upgrade

Use the [installation guide](../INSTALL.md) for the Codex plugin or project-local Skills CLI copies. The plugin command and fixed-release alternative select `v0.1.4`; the short interactive command follows the repository’s default branch. Release assets are `design-agent-skills-0.1.4.zip` and `design-agent-skills-0.1.4.sha256`.

Existing users should follow [replacement instructions](advanced-installation.md#replace-an-earlier-installation), especially when another agent uses the same project folders. The immutable [0.1.3 release](https://github.com/vdigitaldesign/design-agent-skills/releases/tag/v0.1.3) remains available for recovery. Actual publication and public-source installation results belong to the [GitHub release record](https://github.com/vdigitaldesign/design-agent-skills/releases/tag/v0.1.4).

## Verification scope

The source review checks correspondence with the preceding requirements. Offline checks cover the exact two-source composition, complete standalone resources, local links, package integrity, new target identity, preserved historical targets and byte-identical archive rebuilds using the public maintenance tools.

No new model task was run for this editorial patch. BorrowDesk, Fieldnote and team-invitation results belong to their earlier RC1 instruction sources; they are not new behavioral PASS results for 0.1.4. The [evidence summary](advanced-installation.md#support-and-evidence) preserves those results and their limits.

Version 0.1.4 supports the documented Codex plugin and standalone routes. Claude support remains under development and outside this release’s supported configurations. Tools, authentication and model access come from the user’s environment.

Use [GitHub Issues](../SUPPORT.md) for ordinary reports and [private reporting](../SECURITY.md) for suspected vulnerabilities. DAS uses the [MIT license](../LICENSE).
