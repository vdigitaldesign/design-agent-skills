# Installation, replacement, and evidence

The [installation guide](../INSTALL.md) covers the release-tagged plugin and project-local copy routes. Keep downloaded packages and backups outside skill-discovery directories.

## Support and evidence

`VERSION` identifies package version `0.1.1`; `TARGET.json` retains the instruction target `codex-0.1.0`. The instructions remain the qualified RC1 sources: 16 skills and 12 shared references, with source map `2084692186f80c00ae9d297d3bbd8dfcda627dcdf39a71bcd1ad92edbd020eca`. A release's archive hash and file manifest identify its packaging; they are separate from that source map.

The recorded observations used macOS. They establish the following scopes:

| Check | Observation and limit |
| --- | --- |
| Source-faithful contract and handoff | The selected sources completed the seven-source BorrowDesk and Fieldnote tasks, including concrete acceptance procedures, actual validation, and accessible handoffs. These explicit native CLI tasks used Codex CLI 0.163.0 with `gpt-6-astra` / `ultra`. The handoffs retained the required authority boundaries. |
| Approval and publication chain | The same sources completed a review-ready proposal and contract, followed by the owner's exact approval in the same history. The continuation published the approved local canon, read it back, checked its relationship to the contract, established the separately authorized contract effectivity, and delivered the current handoff. This observed one complete chain, not product implementation or deployment. |
| RC1 plugin lifecycle and routine use | The 571-file RC1 plugin matched its archive. Installation, enabled inventory, resource reading, a short CLI handoff, removal, and restoration were observed. The app also completed a short explicit-reference handoff; the owner observed picker selection and disappearance after removal. These observations do not establish every skill's behavior. |
| RC1 project-local skills | Skills CLI 1.7.2 copied all 16 complete skills, 528 files, into a disposable project. One same-chat continuation in Codex app runtime 0.165.0-alpha.1.2 with `gpt-6-astra` / `low` read the four required Router resources completely and produced the requested short handoff. The owner observed Project entries and their disappearance after removal. An earlier setup attempt stopped before reading the skills; that result remains separate. |
| Published v0.1.0 archive | An anonymous download matched the release SHA-256 and passed verification of its 572 files. The archive hash was `cb3006194f1985c819e3bbcb82b2cbdbb7cf4058dd2489a4cb2702ce8122cb7d`. |
| Published v0.1.0 plugin | Codex CLI 0.163.0 installed from the public `v0.1.0` source, removed the plugin and marketplace, and restored the enabled plugin with matching release files. Unrelated plugins and marketplaces were unchanged. This did not include a new model call or fresh Desktop-picker observation. |
| Published v0.1.0 project-local skills | Skills CLI 1.7.2 on Node.js 24.16.0 installed the public `v0.1.0` tag into an empty disposable project. All 16 standalone verifiers passed for 528 files. Full removal left no DAS directories and an empty skills lock. This isolated-project result does not establish safe selective removal in a mixed-client project. |

The v0.1.0 observations above were completed on October 29, 2026. For the v0.1.1 artifact and installation results, see its [release record](https://github.com/vdigitaldesign/design-agent-skills/releases/tag/v0.1.1). Each version's installation evidence is separate; the shared instruction sources preserve the applicability of the scoped behavioral observations above.

Tests of one case or model do not establish all-skill reliability, minimum supported client versions, cross-platform parity, or measured time savings. Earlier development failures retain their own source and task scope.

Claude is not a supported consumer configuration for this release. Tool integrations, authentication, and model access come from the user's environment.

## Troubleshooting

If a plugin skill is missing, check `codex plugin list`, its enabled state, and the configured marketplace source. Open a new session after installation. Use the namespaced invocation, such as `$design-agent-skills:design-router`.

For copied skills, check `.agents/skills/<skill-name>/SKILL.md` in the project Codex has opened. Each complete skill folder has 33 files: its entrypoint, 15 related skill texts, 12 references, and five package files. Keep its `VERSION`, `LICENSE`, `TARGET.json`, verifier, and manifest. Copying only `SKILL.md` breaks the package's resource links.

If a resource cannot be read, inspect the path and permissions before reinstalling. If Codex reports an authentication or unavailable-model error, resolve that client error first. Installing the same instructions again does not change account or model access.

If both namespaced and Project versions appear, check whether you installed both routes. Remove the copy you do not intend to use after confirming its source. The plugin catalog can still show an available card after uninstalling it.

## Replace an earlier installation

Local development packages, RC1, and public releases share the `design-agent-skills@design-agent-skills` plugin identity. RC1 and the first public release also display version `0.1.0`; check their source and `TARGET.json` to distinguish them. Version 0.1.1 is a packaging and documentation update with unchanged skill instructions.

1. Record the existing DAS plugin or project-local paths, source, and enabled state. Check symlink targets and relevant skill-lock entries, including any shared with another agent.
2. Keep the original package and a copy of affected settings or lock entries outside discovery. Preserve unrelated entries.
3. For a plugin, remove the identified DAS plugin and its old marketplace registration before registering the release source. Use the commands in [removal](#remove-the-plugin). Keep a marketplace that serves another installation.
4. For project-local skills, replace only the identified DAS folders and their lock entries. If another agent shares those folders or aliases, use a fresh project or plan that migration explicitly.
5. Install from the desired release tag or verified archive. Check its identity and complete files, then start a new session and inspect the skill picker.

A same-version refresh is not proof of a version upgrade. Automatic in-place migration across shared installations is outside the verified scope. Future releases provide their own migration notes; retain the current artifact until the replacement is verified.

## Remove the plugin

After confirming the plugin and marketplace you intend to remove:

```sh
codex plugin remove design-agent-skills@design-agent-skills &&
codex plugin marketplace remove design-agent-skills &&
codex plugin list
```

Open or refresh the app's skill picker and confirm that the plugin entries have disappeared. An available catalog card can remain.

## Remove project-local skills

Skills CLI 1.7.2's unscoped removal targets the selected names across **all agent directories in the current project**. It does not offer an agent-selection prompt. The `--global` flag changes the filesystem scope; omit it for the project-local route documented here.

### Complete removal from an isolated project

Use this route only when every DAS copy or alias in the project is intended for removal. Back up any customized files first, then run from the project's root:

```sh
npx --yes skills@1.7.2 remove
```

Select only the DAS names from the [catalog](skills.md), then confirm removal. Check that their `.agents/skills/` folders, other agent copies or aliases, and corresponding `skills-lock.json` entries are gone. Unrelated names and lock entries should remain.

### Selective removal from a mixed-client project

Use manual, path-specific removal when another agent has a same-named copy you want to keep. Do not use the unscoped command above. Adding `--agent codex` is not a complete remedy: the CLI can retain the canonical folder and report success when another agent still uses it.

1. Identify the exact Codex folders, the other agents' copies, and any symlink targets. For example, inspect `.agents/skills/design-router` and `.claude/skills/design-router`. Check the project's `skills-lock.json` before changing anything.
2. If another agent reads the same `.agents/skills/<name>` folder directly or through a symlink, keep that folder and its lock entry. Filesystem removal cannot remove it for Codex alone. Move the other consumer to an independent copy first, or use a separate project for Codex.
3. If the Codex folder is an independent copy, move that exact folder to a backup outside skill discovery. For example, after confirming ownership of `design-router`:

```sh
(
  test ! -L .agents &&
  test ! -L .agents/skills &&
  test -d .agents/skills/design-router &&
  test ! -L .agents/skills/design-router &&
  das_backup_dir=$(mktemp -d "${TMPDIR:-/tmp}/das-removed.XXXXXX") &&
  mv .agents/skills/design-router "$das_backup_dir/" &&
  printf 'Retained backup: %s\n' "$das_backup_dir/design-router"
)
```

Repeat only for the other DAS folders you have identified. This command does not touch `.claude/skills/`, other agent directories, or lock files. Keep the printed backup until the remaining installations and Codex picker are checked.

The project lock records skills by name, not by agent. Retain a name's lock entry while another copy or alias still uses it. Once no installed copy or alias remains, remove only that name's entry from the `skills` object in `skills-lock.json` using a text editor; preserve other entries and the lock's version. Never delete the entire lock to clear DAS.

Open a new Codex session and confirm that the intended Project entries have disappeared. Check that the other agent's retained files and links still resolve. Restore the moved folder from the printed backup if the wrong copy was selected.

## Rollback

Restore the saved package source and only the DAS paths and lock entries affected by replacement. For a plugin, register the retained previous package, install its plugin, and restore the recorded enabled state. Compare its files with the saved manifest and inspect the picker in a new session. Keep the failed state or a focused error record when it is needed to reproduce a problem.

## Command references

The native source/ref syntax is exposed by Codex CLI's `codex plugin marketplace add --help`. The tag URL used by the standalone command is supported by the [Skills CLI 1.7.2 source parser](https://github.com/vercel-labs/skills/blob/v1.7.2/src/source-parser.ts) and [Git checkout implementation](https://github.com/vercel-labs/skills/blob/v1.7.2/src/git.ts). Its [removal implementation](https://github.com/vercel-labs/skills/blob/v1.7.2/src/remove.ts#L219-L319) owns the all-agent default, canonical-folder retention, and lock cleanup described above. Actual installation from a published DAS source is a separate release observation.
