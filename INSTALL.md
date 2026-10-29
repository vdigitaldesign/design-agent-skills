# Install DAS 0.1.1

Choose the Codex plugin or project-local copied skills. Use one route in a project to avoid duplicate DAS entries.

You need Codex with access to an available model. The plugin route also needs a Codex CLI that exposes `codex plugin`; check with `codex plugin --help`. The Skills CLI route needs Git, npm, and [Node.js 22.20.0 or later](https://github.com/vercel-labs/skills/blob/v1.7.2/package.json). Python 3.9 or later is needed only for the package verifier and maintenance commands.

If an older DAS installation is present, read [replacement and rollback](docs/advanced-installation.md#replace-an-earlier-installation) before adding this version. The commands below select tag `v0.1.1`.

## Codex plugin

```sh
codex plugin marketplace add vdigitaldesign/design-agent-skills --ref v0.1.1 &&
codex plugin add design-agent-skills@design-agent-skills &&
codex plugin list
```

Confirm that Design Agent Skills is enabled. Start a new Codex app or CLI session in the project you want to work on, then select **Design Agent Skills: Design Router** from the skill picker. Its explicit invocation is `$design-agent-skills:design-router`.

Adding this repository as a marketplace source installs a Codex plugin from GitHub. It does not imply a listing in an external curated plugin directory.

## Project-local skills

Run this from the root of the project that will use DAS:

```sh
npx --yes skills@1.7.2 add https://github.com/vdigitaldesign/design-agent-skills/tree/v0.1.1 --agent codex --skill '*' --copy --yes
```

This copies all 16 skills into `.agents/skills/`. Before running it, check that the DAS names in the [catalog](docs/skills.md) are not already installed there or shared through symlinks. Keep each complete skill folder, including its `references/`, `related/`, and `TARGET.json` files.

Start a new Codex session in that project. Project-local skills use names such as `$design-router` and `$audit-design-surface`, without the plugin prefix. The app may label them **Project** in its picker.

`npx` may download the pinned Skills CLI from npm. Its [documentation](https://github.com/vercel-labs/skills/tree/v1.7.2) describes the installer and its telemetry settings.

## Download and verify an archive

Download `design-agent-skills-0.1.1.zip` and `design-agent-skills-0.1.1.sha256` from the [v0.1.1 release](https://github.com/vdigitaldesign/design-agent-skills/releases/tag/v0.1.1). Keep the package outside directories where Codex discovers skills.

On macOS, from the download directory:

```sh
(
  shasum -a 256 -c design-agent-skills-0.1.1.sha256 &&
  das_extract_dir=$(mktemp -d "./das-0.1.1.XXXXXX") &&
  unzip design-agent-skills-0.1.1.zip -d "$das_extract_dir" &&
  python3 "$das_extract_dir/design-agent-skills-0.1.1/verify.py" --root "$das_extract_dir/design-agent-skills-0.1.1" &&
  printf 'Verified package: %s\n' "$das_extract_dir/design-agent-skills-0.1.1"
)
```

Copy the whole block, including the parentheses. It stops on failure and creates a fresh extraction directory only after the checksum passes. On systems with `sha256sum`, replace the first command inside the block with `sha256sum -c design-agent-skills-0.1.1.sha256`. Continue only when the verifier succeeds and the block prints the verified package path. Download the checksum from the same trusted release as the archive; the checksum alone does not authenticate a publisher.

Use the printed package path to register a local plugin source. Replace the example path below with its absolute path:

```sh
codex plugin marketplace add /absolute/path/to/das-0.1.1.ABC123/design-agent-skills-0.1.1 &&
codex plugin add design-agent-skills@design-agent-skills
```

Keep that source folder in place while the local marketplace is registered. For project-local copies, replace the GitHub URL in the Skills CLI command with the absolute path to this folder.

## Check your setup

Open the skill picker and confirm the expected DAS entries. Select Design Router, then use a small task with sources you can inspect. [Getting started](docs/getting-started.md) includes a brief template and examples.

If a name is missing, a file cannot be read, or you need to update or remove an installation, follow [advanced installation](docs/advanced-installation.md). Client authentication and unavailable-model errors need to be resolved in Codex; reinstalling the same skill files does not fix them.
