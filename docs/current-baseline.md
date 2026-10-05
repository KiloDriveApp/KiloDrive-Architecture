# Current documentation baseline and evidence

[Documentation guide](README.md) · [API Guide](api/README.md) · [Capability status](architecture/capability-status.md)

This is the entry point for interpreting dates and completion claims in this
repository. Historical release chapters remain useful, but their versions,
test counts and device observations do not become evidence for newer builds.

## Reviewed source

| Item | Inspected value | Meaning |
| --- | --- | --- |
| Review date | 2026-10-05 | Date of the native-adapter source observation |
| Product source revision | `8bfe08881bce51535d1165552f2d5be8e05fc872` | Git HEAD in the product checkout; the checkout also contained uncommitted adapter/API changes, so this commit alone does not reproduce every observation |
| Consumer source | `1.0.0+192` | Read from the consumer pubspec; not a signed-artifact or store-availability assertion |
| System Admin source | `0.1.0+32` | Read from its independent pubspec; not private-distribution certification |
| Schema contract | `2026.10.05.1` | Source contract version; not proof that any deployed database is aligned |
| Private v1 OpenAPI hash | `5ce23bf4eaba9dd3a187e65b4575673e6e821badba1aeb4a302b4a5cc1383249` | Current local file hash, not a reviewed/public publication claim |
| Public API coverage | 528 operations, 659 models, 5,012 properties | Historical curated export from product revision `1cd27c58f0fd9df6d974fab3718c3cb0b485f251`; it has **not** been regenerated against the current product checkout |

The historical public API export's own source metadata is consumer
`1.0.0+172`, System Admin `0.1.0+16` and schema contract `2026.10.03.1`.
Those values are retained to describe that export, not the current app or
database. Its 528 operations, 659 models and 5,012 properties must not be
read as current private API counts.

The [native source snapshot](architecture/native-source-snapshot.json) records
the inspected versions and hash; its local checker can compare them to a
product checkout. The [generated public API manifest](api/openapi/manifest.json)
is the machine-readable provenance record **for its older curated export**, not
for the current product source. The [reference coverage report](api/reference/coverage.md)
separates operation-specific explanations from route-derived summaries and
lists unresolved schema and field-description gaps. Counts describe coverage,
not quality scores or certification percentages.

## What changed in the documented architecture

| Area | Current source responsibility | What still needs independent evidence |
| --- | --- | --- |
| Two mobile clients | Consumer owns rider, driver and rental tasks; the restricted System Admin app owns operational administration | Exact signed-client access boundaries, distribution and device journeys |
| People and readiness | Admin dossiers connect people, documents, membership, security and activity; the API calculates readiness | Current permission denials, document-preview/decision/replacement and final-approval journeys |
| Membership management | Catalog editing and plan creation, benefit/term-price management, member drill-down and individual membership actions have dedicated source surfaces | Store mappings, country pricing, effective entitlement propagation and real purchase/renewal outcomes |
| Approval policy | Independent second approval is configurable per reviewed domain; source defaults allow one authorized reviewer | Deployed effective policy, policy changes and both enabled/disabled workflow tests |
| Account security | Central identity owns credentials, sessions and recovery; clients carry appropriately scoped sessions | Current credentials, attestation, revocation and cold-restart behavior on signed apps |
| Device identity | Installation credentials and verified app identity establish admission; model/IP metadata alone does not | Reinstall, restored storage, device restriction and cross-app binding observations |
| Notifications | Durable side effects and provider adapters separate account preferences, installation bindings, delivery attempts and admin alerts | Provisioned destinations and observed email/SMS/WhatsApp/push delivery |
| Financial recovery | Stable operation identity, retained payload/revision and authoritative outcome reads govern uncertain results | Provider, ledger and client agreement after real interrupted operations |
| Native adapters | Typed platform observations are separated from server decisions; late callbacks are scoped and fenced | Real StoreKit/Play, secure storage, camera, push, RTC and location behavior |
| API documentation | Public export preserves allowed wire contracts without copying the complete private API | Deeper semantic review where the coverage report flags a gap |

These statements describe inspected source, not a declaration that all
implementation debt has disappeared. For example, the private source's older
`MIGRATION_PARITY.md` still lists some capabilities as unavailable while newer
repositories and the exact-operation ledger contain implementations. This
review uses current source for those named capabilities and keeps broader
parity/certification claims open. A stale inventory is not proof of absence;
a newer route or ledger row is not proof of a completed operator journey.

## Evidence ownership

| Question | Evidence to consult | What it cannot establish alone |
| --- | --- | --- |
| What fields and routes exist? | Canonical OpenAPI, DTO/controller source and public manifest | All runtime validation or lifecycle behavior |
| What business behavior is implemented? | Handler, validator, persistence and focused tests | Live provider behavior |
| What can an operator do? | Capability registry, API permission checks, rendered UI and operation ledger | Signed-device certification of every form |
| What is actually deployed? | Restricted deployment record, artifact hash and schema verification | Store availability or business readiness |
| What is active in a country? | Effective country, feature, rate, provider and product state | That every enabled action has been exercised |
| What passed on a device? | Exact signed artifact, OS/device, environment, scenario and observed result | Untested platforms, accounts or lifecycle variants |
| What does this repository verify? | Documentation CI and source-comparison results | Production health or application test results |

The public dependency baseline was regenerated from the historical API-export
source and covers both apps, .NET projects and explicit package overrides at
that checkpoint. Its
[117-coordinate inventory](third-party/direct-packages.md) is still not the
complete release SBOM. See [SBOM scope](third-party/sbom.md).

## Reading historical chapters

- [Build 168 handover](runbooks/build168-operational-handover.md) retains its
  bounded deployment, host-test and device observations for build 168.
- [2026-09-30 two-app checkpoint](architecture/two-mobile-apps-and-security-2026-09-30.md)
  records the earlier app split and its then-outstanding work.
- Build-numbered release chapters and dated ADR decisions retain their original
  evidence. Later amendments are labelled explicitly.
- Topic chapters link here for the current source baseline. Do not combine a
  historical passing test with a newer build number to manufacture certification.

## How a change stays traceable

1. Identify the authoritative code, contract, configuration example or policy.
2. State whether the observation is implemented source, configurable behavior,
   an operational procedure, a future direction or an observed deployment.
3. Update the owning topic and its navigation, rather than appending a competing
   description elsewhere.
4. Regenerate derived API artifacts; independently compare published wire
   shapes with the approved source and run the public checks.
5. Preserve old exercise dates and bind new test/deployment observations to
   their actual artifacts.
6. Record unresolved dependencies with a clear verification step. Never fill
   missing response schemas, provider results or document content with guesses.

See the [documentation correction record](quality/documentation-audit-2026-10-03.md)
for the defects corrected in this revision and the limits still visible.
