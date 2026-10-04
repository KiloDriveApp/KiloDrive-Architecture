# Coverage, known limits and honest interpretation

[API Guide](README.md)

## Snapshot scope

This publication describes a reviewed source snapshot, not a live probe of all
production workflows. The [manifest](openapi/manifest.json) identifies source
commit, versions, contract hashes and export counts. It is possible for a
deployed service or signed app to differ from that snapshot; release/device
evidence is required to establish its behavior.

The public reference includes anonymous information and first-party consumer/
organization workflows. Its 459 paths and 528 operations are a subset of the
complete 996-path, 1,123-operation source contract. Administrative contracts and
unapproved surfaces have not been silently reclassified as partner APIs.

## Excluded surfaces

| Excluded area | Public explanation retained | Reason for separate documentation |
| --- | --- | --- |
| System Admin routes and cross-workspace authority | App separation, capability boundaries, readiness review, investigations and audit | Restricted operator contracts and executable recovery instructions remain private |
| Provider payment/payout/store callbacks | Signature validation, idempotent reconciliation and server-owned records | Callback authenticity/setup belongs to controlled integration runbooks |
| Realtime grants and operational diagnostics | Durable versus ephemeral state and reconnect behavior | Connection/admission/internal operation details need separate review |
| Sharing-token and tracking callback details | Consent and relationship boundaries | No live capability tokens or private URLs are published |
| Store-review/testing controls | Certification remains separate from source behavior | Test-policy configuration is not a consumer/partner capability |
| Source descriptions, examples, defaults and defensive extensions | Required wire fields, types, relevant guards and local explanations | Source prose/examples are not assumed safe to republish automatically |
| Unreferenced component schemas | Every component needed by approved operations | Prevents excluded admin models leaking through a full schema dump |

Not every organization action is public-safe merely because its URL lacks
`/admin`. Review checks declared roles as well as route families. New source
routes require explicit publication-policy review.

## Metadata is useful but not exhaustive

The generated [coverage report](reference/coverage.md) and its JSON review queue
enumerate route-derived summaries, type-only field explanations and untyped
success responses. This makes semantic incompleteness visible even when every
wire field has a table row. The corrected exporter preserves real properties
named `description`, `default` or other OpenAPI keywords; it strips metadata
only in the appropriate OpenAPI context.

The OpenAPI artifact records types, declared authentication/roles, parameters,
request bodies, selected statuses and concurrency metadata. Important limits
remain:

- Handler validators can enforce requirements not expressed as JSON `required`.
- Some controller results have no typed success schema recorded. The reference
  labels them **No typed schema recorded**; it does not invent missing fields.
- Business, admission and provider paths can return statuses beyond those
  recorded for an operation. For example, membership pricing can be unavailable
  even when the generated price-read metadata lacks an explicit 503 entry.
- Bearer metadata alone does not model installation credentials, App Check,
  recent proof, organization relationships or every feature gate.
- Numeric enum labels require the source registry; the export's separate
  [enum-label snapshot](enum-labels.json) supplies verified labels.
- Source fields can be more semantically specific than a generated schema.
  The field dictionary names that limit instead of inventing units, vocabularies
  or hidden state-machine rules.
- Schema nullability/requiredness describes metadata. It must be compared with
  actual endpoint behavior and validation when building a client.

These are documentation/contract-metadata limits. Listing them does not itself
remediate the implementation or prove a release failed. A source contract gap
should be corrected in the private canonical artifact and its tests, then
regenerated here after review. Do not patch the public JSON to pretend the
private source already promises a different response.

## Feature availability has several gates

| Evidence | What can be concluded |
| --- | --- |
| Source implements a route | The reviewed code has a contract surface |
| Schema aligns | Required database objects match the contract |
| Country/feature active | The corresponding configuration is enabled |
| Provider configured | Required settings/accounts exist at that boundary |
| Provider test succeeds | The tested provider action worked in that environment |
| Signed-device workflow passes | The exact artifact and device journey were observed |
| Full release certification | All required release evidence and unresolved dependencies were assessed |

Do not collapse these into “everything works.” Billing, payouts, notifications,
maps, document scanning, rental protection and country compliance have external
dependencies. An enabled flag cannot create a provisioned destination, reviewed
store product, merchant approval or native attestation.

This documentation update does not claim complete end-to-end certification of
every Admin form, consumer journey, native store, notification channel or
country. It publishes the contract and safe interpretation with its provenance.

## Partner access and compatibility promises

No public developer-key issuance, client-credentials flow, third-party quota or
service-level agreement is established here. Protected routes are documented
for architectural transparency and approved first-party use. A partner must
receive a separate agreed access/data boundary.

The compatibility alias sunset is recorded in [versioning](versioning-and-publication.md).
Client generators should tolerate safe additive changes and unknown enum values,
but must not infer support for unpublished routes. Source publication is not a
license to bypass permission checks or send production test traffic.

## Report gaps safely

For product/integration questions use [Contact KiloDrive](https://kilodrive.com/contact).
For a vulnerability use [SECURITY.md](../../SECURITY.md). Describe the observed
behavior, source/version context and sanitized correlation evidence. Do not
publish customer IDs, tokens, provider receipts, private document URLs or raw
production logs.
