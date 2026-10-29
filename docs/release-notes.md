# DAS 0.1.2

When an implementation matches the approved design, its verification record should say so without assigning an issue category. This patch makes that exception explicit in the implementation-check template.

## What changed

The classification field now says to omit it for `conforms`. The four existing classifications remain available for discrepancies and inconclusive observations. Missing evidence still cannot establish conformance, and a parity review still cannot approve a material design change.

This is the only instruction-source change. The other 27 source files are unchanged. Package and instruction target are both identified as `0.1.2` (`codex-0.1.2` in `TARGET.json`), so the revised sources cannot be mistaken for the earlier tested edition.

The quick start also includes the shorter interactive installation command already available in the repository. The installation guide retains a fixed-release alternative.

## Install or upgrade

Use the [installation guide](../INSTALL.md) for the Codex plugin or project-local skills. The plugin command and fixed-release alternative select `v0.1.2`; the short interactive command follows the repository's default branch. Release assets are `design-agent-skills-0.1.2.zip` and `design-agent-skills-0.1.2.sha256`.

Existing users should follow [replacement instructions](advanced-installation.md#replace-an-earlier-installation), especially when another agent uses the same project folders. The immutable [0.1.1 release](https://github.com/vdigitaldesign/design-agent-skills/releases/tag/v0.1.1) remains available for recovery. Publication and installation results for this patch belong to its [GitHub release record](https://github.com/vdigitaldesign/design-agent-skills/releases/tag/v0.1.2).

## Verification scope

Offline checks cover the exact source change, complete resource copies, local links, rejection of source or identity drift, and a byte-identical archive rebuild using the public maintenance tools.

No new model task was run for this patch. The recorded BorrowDesk, Fieldnote and team-invitation results belong to the earlier RC1 instruction sources used in 0.1.0 and 0.1.1. The [evidence summary](advanced-installation.md#support-and-evidence) preserves those results and their limits; they are not a new behavioral PASS for this revised source edition.

Version 0.1.2 supports the documented Codex routes. Claude support remains under development and outside this release's supported configurations. Available tools, authentication and model access come from the user's environment.

Use [GitHub Issues](../SUPPORT.md) for ordinary reports and [private reporting](../SECURITY.md) for suspected vulnerabilities. DAS uses the [MIT license](../LICENSE).
