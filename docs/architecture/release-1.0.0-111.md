# Release 1.0.0 build 111 architecture update

Owner: KiloDrive Engineering and Operations. Last source review: 12 September 2026.
Environment: source baseline and recorded production API/schema deployment.
Evidence: [source commit 11977549](https://github.com/KiloDriveApp/KiloDrive/commit/119775490f7e3c54e6ff174cb9342993dddd80fe).

## Authoritative baseline

| Fact | Value | Authoritative source |
| --- | --- | --- |
| Mobile version | 1.0.0+111 | Flutter pubspec.yaml |
| Schema contract | 2026.09.12.1 | SchemaContract.CurrentVersion |
| Public REST | /api/v1 | Reviewed OpenAPI v1 |
| OpenAPI inventory | 699 paths, 787 operations | Generated repository facts |
| Mobile languages | English, Spanish, French, Japanese, Simplified Chinese, Traditional Chinese | ARB configuration |

The [source facts](https://github.com/KiloDriveApp/KiloDrive/blob/119775490f7e3c54e6ff174cb9342993dddd80fe/docs/generated/repository-facts.md)
bind these values to the reviewed contract hash. This snapshot supersedes older
current-baseline references; historical release documents remain historical.

## Administration is a permissioned mobile control plane

The mobile side menu now groups authorized leaves into expandable domains: People,
Operations, Finance, Support, Communications, System, Insights and Account. Finance
separates wallet/accounting operations from membership management. System separates
security management from outbox/provider recovery. Grouping is presentation only:
each leaf retains its authorized route and shell index; expanding a branch grants no access.

The 21 former desktop registry capabilities now have typed mobile route entries.
This is registry parity, not certification of every HTTP operation. The compiled
admin policy inventory covers 277 operations and records role, permission, step-up,
revision, idempotency, recovery and individual certification disposition. Generating
an inventory never executes its certification cases.

Driver review remains a sequence of separate proofs: identity, profile, documents,
vehicle, membership/trial, payout and safety. The API owns the readiness result.
Reviewing a document does not make the driver online-eligible by itself. The mobile
checklist must reload after review and after country/account changes.

## Top-up value issuance and investigation

Country-cell top-up cards now retain an issuance operation reference and optional
expiry. Redemption enforces expiry. Issuance records an audit witness in the same
feature boundary; history APIs expose metadata rather than bearer codes, hashes,
ciphertext or raw replay keys. Read-only card and batch surfaces use typed models,
paging and country fencing.

The independent issuance-outcome query derives the support reference from the original
issuer, tenant, key and route and searches tenant-filtered issuance evidence. It can
return issued, unresolved or manual review. Missing evidence never proves no issuance
and does not authorize another batch with a fresh key. Duplicate witness and corrupt
evidence behavior require explicit investigation.

## Non-breaking vehicle concurrency

Vehicle revisions are persisted concurrency tokens. Legacy update/assignment routes
still accept older builds without newly required headers; supplied preconditions are
validated. New revisioned routes require the original revision and idempotency key
and publish committed revision headers. Assignment changes advance the parent vehicle
revision. Modern retry must preserve the original key and revision after response loss.

## Runtime and certification boundaries

Identity credentials remain in the control database. Operational projections, trips,
payments, wallets, audit and outbox remain in the selected country cell. A settlement
does not span control and cell transactions. The combined host and configurable
runtime profiles preserve this ownership; endpoint registration does not replace
configuration readiness.

Recorded deployment for this source aligned eight database schemas and reported the
API Healthy with the expected valid schema contract. Application backup and database
backup occurred before deployment. Restricted backup paths and cloud identifiers are
kept in private operational evidence. Portal and website were not deployed in this run.

Local verification recorded 4,414 passing .NET tests and 54 environment-gated skips,
clean Flutter analysis, and signed APK/AAB packaged-manifest checks. These results do
not certify skipped MySQL concurrency/provider cases, universal mobile process-death
recovery, two-device calling, store approval or all countries. Remaining boundaries are
listed in the [source hardening assessment](https://github.com/KiloDriveApp/KiloDrive/blob/119775490f7e3c54e6ff174cb9342993dddd80fe/docs/audits/admin-operation-hardening-2026-09-12.md).

## Operator documentation

The [mobile administrator guide](https://github.com/KiloDriveApp/KiloDrive/blob/main/docs/user-manuals/system-administrator-guide.md)
documents workspace selection, navigation, evidence review, readiness refresh, top-up
issuance/history and safe investigation. Rider, driver and rental manuals are rebuilt
from controlled HTML sources and checked as PDFs before publication. Manual accuracy
and live feature/provider availability are separate claims.
