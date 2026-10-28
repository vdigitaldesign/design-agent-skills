# Installation, replacement, and evidence

The [installation guide](../INSTALL.md) covers the release-tagged plugin and project-local copy routes. Keep downloaded packages and backups outside skill-discovery directories.

## Support and evidence

The release contains 16 skills and 12 shared references. `TARGET.json` identifies `codex-0.1.0`, whose 28 instruction sources match the selected RC1 source map `2084692186f80c00ae9d297d3bbd8dfcda627dcdf39a71bcd1ad92edbd020eca`. A release's archive hash and file manifest identify its packaging; they are separate from that source map.

The recorded observations used macOS. They establish the following scopes:

| Check | Observation and limit |
| --- | --- |
| Source-faithful contract and handoff | The selected sources completed the seven-source BorrowDesk and Fieldnote tasks, including concrete acceptance procedures, actual validation, and accessible handoffs. These explicit native CLI tasks used Codex CLI 0.163.0 with `gpt-6-astra` / `ultra`. The handoffs retained the required authority boundaries. |
| Approval and publication chain | The same sources completed a review-ready proposal and contract, followed by the owner's exact approval in the same history. The continuation published the approved local canon, read it back, checked its relationship to the contract, established the separately authorized contract effectivity, and delivered the current handoff. This observed one complete chain, not product implementation or deployment. |
| RC1 plugin lifecycle and routine use | The 571-file RC1 plugin matched its archive. Installation, enabled inventory, resource reading, a short CLI handoff, removal, and restoration were observed. The app also completed a short explicit-reference handoff; the owner observed picker selection and disappearance after removal. These observations do not establish every skill's behavior. |
| RC1 project-local skills | Skills CLI 1.7.2 copied all 16 complete skills, 528 files, into a disposable project. One same-chat continuation in Codex app runtime 0.165.0-alpha.1.2 with `gpt-6-astra` / `low` read the four required Router resources completely and produced the requested short handoff. The owner observed Project entries and their disappearance after removal. An earlier setup attempt stopped before reading the skills; that result remains separate. |

The release preserves those instruction sources. New archive bytes do not turn an RC1 installation receipt into an exact-release receipt. Public release checks must identify the actual released archive and routes. Tests of one case or model do not establish all-skill reliability, minimum supported client versions, cross-platform parity, or measured time savings. Earlier development failures retain their own source and task scope.

Claude is not a supported consumer configuration for this release. Tool integrations, authentication, and model access come from the user's environment.

## Troubleshooting

If a plugin skill is missing, check `codex plugin list`, its enabled state, and the configured marketplace source. Open a new session after installation. Use the namespaced invocation, such as `$design-agent-skills:design-router`.

For copied skills, check `.agents/skills/<skill-name>/SKILL.md` in the project Codex has opened. Each complete skill folder has 33 files: its entrypoint, 15 related skill texts, 12 references, and five package files. Keep its `VERSION`, `LICENSE`, `TARGET.json`, verifier, and manifest. Copying only `SKILL.md` breaks the package's resource links.

If a resource cannot be read, inspect the path and permissions before reinstalling. If Codex reports an authentication or unavailable-model error, resolve that client error first. Installing the same instructions again does not change account or model access.

If both namespaced and Project versions appear, check whether you installed both routes. Remove the copy you do not intend to use after confirming its source. The plugin catalog can still show an available card after uninstalling it.

## Replace an earlier installation

Local development packages, RC1, and the public 0.1.0 package share the `design-agent-skills@design-agent-skills` plugin identity and version. A displayed `0.1.0` alone does not distinguish them. Check the source and `TARGET.json` before replacement.

1. Record the existing DAS plugin or project-local paths, source, and enabled state. Check symlink targets and relevant skill-lock entries, including any shared with another agent.
2. Keep the original package and a copy of affected settings or lock entries outside discovery. Preserve unrelated entries.
3. For a plugin, remove the identified DAS plugin and its old marketplace registration before registering the release source. Use the commands in [removal](#remove-the-plugin). Keep a marketplace that serves another installation.
4. For project-local skills, replace only the identified DAS folders and their lock entries. If another agent shares those folders or aliases, use a fresh project or plan that migration explicitly.
5. Install from the desired release tag or verified archive. Check its identity and complete files, then start a new session and inspect the skill picker.

A same-version refresh is not proof of a version upgrade. Automatic in-place migration across shared installations is outside the verified scope. Future releases provide their own migration notes; retain the current artifact until the replacement is verified.

## Remove the plugin

After confirming the plugin and marketplace you intend to remove:

```sh
codex plugin remove design-agent-skills@design-agent-skills
codex plugin marketplace remove design-agent-skills
codex plugin list
```

Open or refresh the app's skill picker and confirm that the plugin entries have disappeared. An available catalog card can remain.

## Remove project-local skills

Use Skills CLI's removal interface from the project where you installed DAS:

```sh
npx --yes skills@1.7.2 remove
```

Select only the DAS skills and the intended installation scope. Verify that their canonical `.agents/skills/` directories and corresponding lock entries are gone, while unrelated skills remain. Earlier agent-filtered removal reported success while leaving canonical copies. A success message alone is insufficient; do not remove shared directories or a whole skills lock file to compensate.

## Rollback

Restore the saved package source and only the DAS paths and lock entries affected by replacement. For a plugin, register the retained previous package, install its plugin, and restore the recorded enabled state. Compare its files with the saved manifest and inspect the picker in a new session. Keep the failed state or a focused error record when it is needed to reproduce a problem.

## Command references

The native source/ref syntax is exposed by Codex CLI's `codex plugin marketplace add --help`. The tag URL used by the standalone command is supported by the [Skills CLI 1.7.2 source parser](https://github.com/vercel-labs/skills/blob/v1.7.2/src/source-parser.ts) and [Git checkout implementation](https://github.com/vercel-labs/skills/blob/v1.7.2/src/git.ts). Actual installation from the published DAS source is a separate release observation.
