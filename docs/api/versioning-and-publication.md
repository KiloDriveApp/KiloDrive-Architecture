# API versioning and publication governance

[API Guide](README.md)

## One authoritative contract, two audiences

The product repository owns `docs/contracts/openapi/kilodrive-v1.json` and its
SHA-256 sidecar. Controllers, filters, canonical route tests, generated clients
and the reviewed artifact must agree. The public Architecture repository owns
a curated export and human explanations, not a second independently designed
backend contract.

Intentional non-breaking v1 changes update the canonical artifact and checks.
Breaking changes require a new major contract. The unversioned `/api/...`
compatibility alias is deprecated and sunsets on **2027-02-10**. New clients
use native `/api/v1/...` routes; middleware does not rewrite paths to simulate
versioning.

## Explicit publication review

[`publication-policy.json`](publication-policy.json) lists exact approved paths,
methods and documentation groups. The exporter fails if an approved operation
disappears. New paths/methods require deliberate policy changes; no broad rule
automatically republishes all routes outside `/admin`.

The exporter:

1. Checks the private canonical artifact's SHA-256 sidecar.
2. Confirms source commit and source-derived app/schema versions.
3. Selects only approved operations.
4. Rejects privileged route families, callbacks and declared administrative roles.
5. Preserves declared bearer/anonymous security and required wire fields.
6. Removes unreviewed metadata in its OpenAPI context, preserving actual DTO
   properties and response keys even when named `description` or `default`.
7. Includes only transitively referenced components and required security schemes.
8. Checks numeric enum labels against committed source declarations.
9. Independently compares schema/parameter/body shapes with the source and
   generates explanations labelled by their level of semantic review.
10. Records hashes/counts and verifies the reproducible public outputs.

The OpenAPI server is a reserved example host. No production access commands,
live identity fixtures, console screenshots, credentials, private resources,
document bytes or presigned URLs belong in this export.

## Updating a snapshot

An authorized maintainer runs `tools/public_api.py` with `--source-root`,
`--source-commit` and an explicit `--reviewed-date` against the private reviewed
checkout. The tool derives consumer/Admin versions and the schema contract;
maintainers do not copy a historical build number from a deployment log.

Review any publication-policy change before generation. Review field/endpoint
wording in `tools/public_api_semantics.py` and `tools/api_context.py` against the owning controller, DTO,
validator, handler and contract tests. A generic schema-derived explanation
must not invent an unrecorded business rule.

The complete private OpenAPI is never copied into this public repository as a
temporary input. Regeneration accepts it from the separate authorized checkout.
The resulting public subset has a different checksum and scope.

## Verification available to every contributor

Public CI can validate the bundle without private source access:

```bash
python tools/public_api.py --check
python -m unittest discover -s tools -p "test_*.py"
python tools/audit_docs.py
python tools/generate_public_sbom.py --check
npx --yes markdownlint-cli2@0.23.2 "**/*.md"
codespell .
```

The API verification checks publication-policy/hash agreement, route/method
scope, local reference closure, security metadata, path parameters, forbidden
content, complete manifest coverage and exact regenerated catalogs/dictionary.
The maintainer can additionally compare published wire shapes with the
manifest's source artifact:

```text
python tools/public_api.py --check --source-root <authorized-source-checkout>
```

Focused tests exercise
exclusion, shared-schema filtering, anonymous security, dangling references and
unsafe examples/extensions. Repository audits cover links, structure and
high-risk content, heading fragments and cross-platform filename case.

Checksums detect drift. They do not prove a malicious edited artifact is
trustworthy. Source/policy review and private deployment/provider/device evidence
remain necessary. The tests certify the publication tooling's tested boundaries;
they are not application end-to-end tests.

## Reading an API diff

Review path/method additions, permissions, request requiredness, response
nullability, enum values, money units, timestamps, revision/idempotency headers
and new component references. An apparently additive field can still surprise
a strict generated client. A numeric enum addition needs an unknown-state UI
path. A plan/catalog addition needs current pricing and provider mapping, not
just another schema value.

Record the snapshot date and source evidence in public review. Report private
details by controlled runbook title, never by copying its access values into a
public issue or PR description.

## Standards and related governance

The machine-readable export follows
[OpenAPI 3.0.1](https://spec.openapis.org/oas/v3.0.1.html).
Repository contribution/public-safety guidance is in
[CONTRIBUTING.md](../../CONTRIBUTING.md), and
[security reporting](../../SECURITY.md) describes private disclosure.
The [API architecture](../architecture/api.md) explains implementation ownership;
the [native v1 ADR](../adr/012-native-api-v1-and-generated-contract.md) records
the route/contract decision.
