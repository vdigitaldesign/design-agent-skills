# Contributing

Report a concrete problem or propose a focused change with its expected outcome. Identify the client, version, installation route and relevant files. Preserve unrelated work and keep customer data and credentials out of shared examples.

The root marketplace files select `packages/codex` and `packages/claude`. Each client package owns its complete source-preserving skills and integrity checks. Keep those packages intact; edit their owning source files and run the package's maintenance commands rather than editing generated copies independently. A pinned source change needs a distinct source identity and appropriate evidence.

Run `python3 scripts/manage.py sync` after authorized metadata/copy changes, then `python3 scripts/manage.py check` and `python3 -m unittest discover -s tests -v`. Build optional client archives outside this checkout with `python3 scripts/manage.py build --output-dir /absolute/new/output`.

Use clear US English and the available UX Writing and Humanizer capabilities for public prose. Preserve facts, commands, conditions and useful limitations. Private development stages, evaluator grades, logs, machine paths and private links do not belong in user documentation or metadata. These writing capabilities are contributor tools, not installed skill dependencies.

Package integrity and offline maintenance tests do not establish model behavior. Keep original output unchanged when reporting a behavioral problem.
