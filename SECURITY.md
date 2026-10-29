# Security reporting

Report a suspected vulnerability through GitHub's [private vulnerability reporting form](https://github.com/vdigitaldesign/design-agent-skills/security/advisories/new). Keep exploit details, credentials, and private product material out of public issues and pull requests. If the private form is unavailable, do not post the report publicly; ask the maintainer through an existing private contact for a confidential route.

## What to report

Use this route for issues that could expose private data, allow unauthorized actions, compromise package integrity, or cross a trust boundary through unintended instructions or code. An incomplete design result without a security impact belongs in [ordinary support](SUPPORT.md).

Include the affected release and artifact hash when available, client and installation route, impact, prerequisites, and the smallest safe reproduction. Redact real secrets and personal or customer data. Retain the original package and relevant logs locally.

## Supported releases

Version 0.1.1 is the current supported release. Earlier local development and preview packages are not supported releases. No response-time commitment is made.

Security fixes use a new version and release notes. Published tags, archives, and checksums are not replaced in place. See [replacement and rollback](docs/advanced-installation.md#replace-an-earlier-installation) for preserving an existing installation.
