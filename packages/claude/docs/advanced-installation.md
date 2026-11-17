# Advanced installation

## Install a fixed release

For the native plugin, register the immutable Claude release tag:

```sh
claude plugin marketplace add 'vdigitaldesign/design-agent-skills#v0.1.7' --scope project &&
claude plugin install design-agent-skills@design-agent-skills --scope project
```

For project-local copies:

```sh
npx --yes skills@1.7.4 add https://github.com/vdigitaldesign/design-agent-skills/tree/v0.1.7/packages/claude --agent claude-code --skill '*' --copy --yes
```

The tag fixes the DAS source; `skills@1.7.4` fixes the installer. A fixed tag stays on that release. Choose a newer source explicitly when updating.

## Replace or restore an installation

Before replacement, record the installed version, source, and scope. Keep your current source or package and any local edits. Inspect existing marketplace registrations and skill folders; do not overwrite a different installation or another project's registration.

For a plugin, remove only the intended project installation and then add the selected replacement. If its marketplace source must change, remove and re-add that registration only after confirming no other installation uses it. Restore the previous recorded source to roll back. Start a new session and check the version and skill entries.

For copied skills, preserve your current folders and lock file, remove only the DAS names for the intended agent, then install from the chosen tag. Restore the previous tag or retained copies to roll back. Keep unrelated skills and local edits.

## Download an archive

The [Claude 0.1.7 release](https://github.com/vdigitaldesign/design-agent-skills/releases/tag/v0.1.7) also provides `design-agent-skills-claude-0.1.7.zip` and its checksum. An archive is useful for offline inspection or a retained recovery copy; normal installation is described in [INSTALL](../INSTALL.md).

Keep it outside folders where the agent discovers skills. Verify the supplied checksum before extracting into a fresh directory. In the extracted package, `python3 verify.py` checks its files and source correspondence. A checksum checks consistency; obtain it and the archive from the same trusted release.

## Troubleshooting

If a skill is missing, inspect `claude plugin list` or the project's Claude skills directory. Confirm the intended source and scope, then start a fresh session. Installing the same skills through both routes can create duplicate entries.

If a reference cannot be read, confirm that the complete skill folder was retained, including `references/` and `related/`. Do not copy only `SKILL.md`.

If authentication or model access fails, resolve it with Claude. Reinstalling DAS does not repair the client's account access. For another problem, follow [support](../SUPPORT.md).
