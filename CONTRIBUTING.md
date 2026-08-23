# Contributing to KiloDrive Architecture Documentation

Thank you for improving this guide. Good architecture documentation is a form
of operational safety: it helps the next engineer understand which shortcut is
harmless, which one risks money or privacy, and where to look when the system is
behaving strangely.

## Write for the engineer who was not in the room

Assume the reader understands programming but does not know KiloDrive's history.
Define the first unfamiliar term, explain why a boundary exists, and include a
small example when a concept is easy to misread.

Aim for the voice of a patient senior engineer pairing with a colleague:

- use direct sentences and ordinary words;
- say “we chose” when describing a real tradeoff;
- explain consequences instead of declaring something “best practice”;
- vary sentence length and avoid repetitive template language;
- admit limitations and unfinished migration work; and
- include the failure that taught the lesson when it is public-safe.

Avoid empty phrases such as “robust, seamless, scalable solution.” A reader
learns more from “the unique reference makes a replay a no-op” than from “the
workflow is robust.”

## Verify before you describe

Every implementation claim needs at least one trustworthy source:

1. current application code;
2. the canonical MySQL schema or approved update script;
3. an automated contract/integration test;
4. a released configuration example with no secrets; or
5. an approved operational policy.

Do not infer the deployed binary from a database version. Do not infer provider
availability from the presence of an adapter. Do not infer that a mobile
permission is used correctly because it appears in a manifest.

Use the repository's status terms:

- **Implemented** for verified code/schema behavior;
- **Configurable** when deployment configuration is still required;
- **Operational policy** for a required procedure; and
- **Planned** for a future direction.

## Keep public documentation public-safe

Never include:

- passwords, API keys, private/signing keys, OTPs, access or refresh tokens;
- cloud account IDs, private resource names, full ARNs, internal addresses, or
  production connection strings;
- customer, employee, provider-destination, or fixture personal data;
- document contents, call recordings, raw chat messages, or presigned URLs;
- console screenshots containing identifiers or configuration;
- exact defensive thresholds or rules that would materially weaken protection;
- copied production logs with payloads or stack details; or
- credential-shaped examples that scanners or readers could mistake as real.

Use placeholders that are obviously placeholders. When a private detail is
necessary to execute a procedure, link to the restricted runbook by title
without copying the value.

If sensitive material reaches Git, do not simply delete the latest line. Treat
it as an incident: restrict access if needed, preserve evidence, rotate exposed
material, and coordinate history rewriting.

## Choose the right document

- Change an **architecture chapter** when responsibilities, boundaries, or data
  flow changed.
- Add or amend an **ADR** when the team made a material tradeoff that future
  engineers might otherwise reverse accidentally.
- Change a **runbook** when alerting, diagnosis, containment, recovery,
  rollback, or verification changed.
- Change a **tutorial** when readers need a guided cross-component example.
- Update **third-party** documents whenever direct dependencies, licences,
  native binaries, or SBOM procedure changes.

Most production changes touch more than one category. A new durable event, for
example, usually needs architecture, an ADR reference, outbox recovery guidance,
and a test expectation.

## Structure detailed chapters

Use headings that help someone answer a question quickly:

1. purpose and status;
2. mental model or context;
3. normal flow;
4. data and security boundaries;
5. failure modes and symptoms;
6. pitfalls and lessons;
7. verification and tests; and
8. related ADRs/runbooks.

Tables are useful for comparisons and ownership maps. Use prose for reasoning.
Do not turn every paragraph into bullets.

## Architecture Decision Records

Copy [`docs/adr/000-template.md`](docs/adr/000-template.md). An ADR should
describe alternatives fairly, including the conditions under which a declined
alternative might become preferable.

Do not rewrite an accepted ADR to make history look cleaner. Supersede it with a
new ADR and retain the old context.

## Runbooks

Copy [`docs/runbooks/_template.md`](docs/runbooks/_template.md). A runbook must
include diagnosis before mutation, containment, recovery, verification,
rollback/abort criteria, evidence safety, and follow-up.

Public runbooks describe decision flow. They must not contain copy-paste access
commands or exact production targets.

## Links and diagrams

Use relative Markdown links so forks and offline copies remain usable. Check
filename case because CI runs on a case-sensitive filesystem.

Mermaid diagrams render on GitHub and are preferred for data flow and state
machines. Label whether an arrow is synchronous, transactional, queued,
ephemeral, or human-approved in the surrounding text.

Do not place sensitive values in diagrams; images are harder to search and
redact than text.

## Review workflow

1. Make a focused branch.
2. Run `python tools/audit_docs.py`.
3. Run `npx --yes markdownlint-cli2@0.23.2 "**/*.md"`.
4. Run `codespell .` when the pinned spelling tool is available.
5. Read the rendered Markdown, not only the source.
6. Confirm every moved/added document appears in an index.
7. Ask an owner of the affected implementation to verify technical claims.
8. Ask security/privacy review when trust, identity, money, location, documents,
   communications, or retention changed.

## Pull-request checklist

- [ ] Claims are implementation-aligned or explicitly labelled.
- [ ] The document explains why and names tradeoffs.
- [ ] Failure modes, safe recovery, and tests are included where relevant.
- [ ] Public-safety review found no secrets, identifiers, or personal data.
- [ ] Links and case are valid.
- [ ] ADR/runbook/index updates are complete.
- [ ] The documentation, Markdown, and spelling gates pass from a clean checkout.
- [ ] Another person read the rendered result for clarity and tone.

Small grammar fixes are welcome. For large architectural changes, include the
source evidence and affected-owner review so readers can trust the result.

For examples and editing advice, see the
[writing style guide](docs/governance/writing-style.md).
