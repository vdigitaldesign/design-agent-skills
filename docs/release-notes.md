# DAS 0.1.1

DAS helps agents work through product and interface decisions, then give developers a handoff they can act on. This patch makes the installation instructions safer and gives newcomers a concrete example of that work.

## What changed

- Archive verification stops before extraction or execution when the checksum fails.
- Removal instructions distinguish an isolated DAS installation from folders shared with another agent. They explain how to preserve an independent same-named copy.
- The plugin card and README explain the design work, with supported clients described separately.
- A [worked example](worked-example.md) follows a brief through alternatives, a human choice and a developer handoff.
- The [installation evidence](advanced-installation.md#support-and-evidence) includes completed checks of the published 0.1.0 package and keeps them separate from earlier behavior tests.

The design instructions are unchanged. `VERSION` identifies package 0.1.1; `TARGET.json` retains `codex-0.1.0` as the identity of the qualified instruction sources. The source evidence below applies to both packages; installation results belong to each released version.

## Install or upgrade

Use the [installation guide](../INSTALL.md) for the Codex plugin or project-local skills. Both commands select `v0.1.1`. Downloaded release assets are `design-agent-skills-0.1.1.zip` and `design-agent-skills-0.1.1.sha256`.

Existing users should follow [replacement instructions](advanced-installation.md#replace-an-earlier-installation), especially when another agent uses the same project folders. The immutable [0.1.0 release](https://github.com/vdigitaldesign/design-agent-skills/releases/tag/v0.1.0) remains available for recovery. Public installation results for this patch are recorded on the [0.1.1 release](https://github.com/vdigitaldesign/design-agent-skills/releases/tag/v0.1.1).

## What the existing checks establish

The unchanged instructions were tested in synthetic design tasks on macOS with Codex CLI 0.163.0, `gpt-6-astra` and `ultra` reasoning. Each result applies to its stated task:

| Task | Observed result |
| --- | --- |
| BorrowDesk: assemble pickup-request behavior from several sources and owner clarifications | Complete contract, concrete acceptance procedures, validation and a review-ready handoff, including cancellation, eligibility changes and uncertain operation outcomes. |
| Fieldnote: carry supplied requirements into a design contract | Complete source assembly, acceptance procedures, validation and a review-ready handoff. The contract remained non-effective pending its separate approval. |
| Team invitations: carry an exact approved design into the current handoff | A proposal and contract, actual human approval, publication of the approved local design rule, readback, separately authorized contract effectivity and a current handoff in the same session. |

The [route evidence](advanced-installation.md#support-and-evidence) distinguishes RC1 app/CLI observations from installation checks on a public release. These samples do not establish every skill's reliability, cross-platform parity, production implementation or measured time savings. The worked example is illustrative; it is not an additional test result.

Version 0.1.1 supports the documented Codex routes. Claude support is under development and is outside this release's supported configurations. Available tools, authentication and model access come from the user's environment.

Use [GitHub Issues](../SUPPORT.md) for ordinary reports and [private reporting](../SECURITY.md) for suspected vulnerabilities. DAS uses the [MIT license](../LICENSE).
