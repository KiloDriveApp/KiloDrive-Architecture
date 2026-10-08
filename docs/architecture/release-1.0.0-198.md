# Consumer build 198 and System Admin build 33

- **Owner:** Product architecture and release engineering
- **Last verified:** 2026-10-08
- **Environment:** Committed implementation source
- **Evidence:** Product revision [`b658a8d`](https://github.com/KiloDriveApp/KiloDrive/commit/b658a8d09752254cb74f0ab7a82a5b52c94c8a26), authoritative pubspecs, schema constant and retained host results

Consumer `1.0.0+198` accompanies System Admin `0.1.0+33` and source schema
contract `2026.10.08.2`. [Generated version facts](source-versions.generated.md)
identify the exact source snapshot. This page describes implementation
improvements; distribution and deployment observations have their own
[current evidence record](../current-baseline.md#build-198-source-and-execution-evidence).

## Clearer guidance in six languages

The public KD catalog now covers 2,914 situation-specific warning/error
identities. English, Spanish, French, Japanese, Simplified Chinese and
Traditional Chinese each carry the required title, detail and action copy.
The generated inventory records zero stock meanings, zero incomplete
explanations and zero missing locale keys. Placeholder and artifact checks
keep the catalog, client resolver and public documentation aligned.

Support references connect a user-visible situation to its specific meaning
and recovery action. Semantic machine codes remain separate from the stable
`KD-XXXXX` identity. Financial guidance distinguishes a completed result,
a result that did not complete and an uncertain result requiring reconciliation.

## Account controls and privacy

Security settings distinguish optional verification from mandatory protection.
The server remains authoritative for identity, authorization and sensitive
operations. Account-deletion checks explain outstanding requests and financial
obligations before advancing the lifecycle. Privacy and stability improvements
retain the separation between user-visible guidance and protected operational
evidence.

## Payment and membership continuity

Purchase and payment recovery preserve the original scoped operation instead
of dispatching another charge while an outcome is uncertain. Native SDKs report
observations; verified API processing and the owning country-cell transaction
establish entitlement and ledger results. The wallet presents clearer status
and localized recovery guidance with support references.

The [native platform handbook](native-platform-handbook.md),
[store reconciliation runbook](../runbooks/store-entitlement-reconciliation.md)
and [payment recovery runbook](../runbooks/payment-operation-recovery.md)
describe adapter boundaries, independent status recovery and operator procedures.

## Traceable documentation and release checks

Source-derived version facts tie the documentation baseline to the consumer and
Admin pubspecs, the schema contract and the canonical private v1 contract hash.
The generator and CI drift check keep those facts consistent. Historical
release chapters and the curated public API retain their original provenance.

Retained host execution records 5,046 passing consumer Flutter tests, 1,358
passing Admin Flutter tests and clean analyzers. Android release artifacts
passed signature, permission, ABI, 16 KB alignment and AOT privacy checks.
These observations keep their exact build identity in the evidence record.

Copy review is advisory. Catalog completeness, six-language key and placeholder
parity, generated-artifact checks, analyzers and the complete approved test
lanes remain part of the source-controlled release workflow.

[Official product links](../public-product-links.md) · [Historical release evidence](../quality/historical-release-evidence.md)
