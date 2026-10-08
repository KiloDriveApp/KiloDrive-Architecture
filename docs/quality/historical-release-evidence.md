# Historical release verification evidence

Owner: Architecture and release engineering.

This record preserves dated verification observations moved out of release
announcements during the 2026-10-08 editorial alignment. It does not describe
current production health or certify newer builds. See the
[current baseline](../current-baseline.md) for current source and execution scope.

## Build 97

[Release improvements](../architecture/release-1.0.0-97.md)

### Evidence boundaries

Source tests, OpenAPI verification, manual certification and the deployment
manifest are maintained in the application repository. This architecture
repository records the design and operating rationale; it does not claim that
an external provider, store review or country launch is certified merely
because the code path exists.

## Build 101

[Release improvements](../architecture/release-1.0.0-101.md)

### Verification and operations

Focused tests cover chat queue isolation, navigation supersession, provider-lane
isolation, lease replacement/reclamation, payment snapshots and calculator dismissal.
The calculator pass recorded 2,721 host tests passing and a clean analyzer. Native
API-35 build/install succeeded, but the runner stalled before assertions; neither
that attempt nor earlier two-device stalls certify the Android journey. Physical
device and iOS/provider/store evidence remain separately required.

For rollout, package the source-derived contract manifests with the API and Portal,
verify actual database objects in every cell, retain application/database backups,
preserve deployment configuration, and check readiness plus anonymous Portal routes.
When objects already match, do not rerun historical pricing/content seeds or stamp
metadata just to make a release appear newer. Monitor chat/provider lane failures,
oldest pending age, reclaimed leases and conflicting finalizations after rollout.

## Build 111

[Release improvements](../architecture/release-1.0.0-111.md)

### Runtime and certification boundaries

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

## Build 116

[Release improvements](../architecture/release-1.0.0-116.md)

### Verification and operating limits

Production readiness returned Healthy with the reviewed schema contract valid.
Admin, driver and rider sign-in and the safety/incoming-call read routes passed
smoke checks. An authenticated investigator request without its fresh proof
returned Forbidden. Release 116 and 109 are published; consolidated source build
detail routes are absent. The corporate build 116 changelog is published.
The final server suite passed 4,730 tests with no failures; 74 integration cases
requiring dedicated environments were skipped, not certified by this release.

Verification includes hash tampering, MySQL timestamp materialization, rotated
keys, immutable role snapshots, retention holds, open disclosures and explicit
terminal-event mappings. Runtime composition keeps the evidence expiry worker
inside the country-cell worker profile. Source verification and signed Android
artifacts do not imply store approval or physical two-device certification.

Production signing material belongs in the secret manager and restricted
deployment configuration. It is never included in source, documentation,
release packages or investigator responses. Operators must preserve retained
keys while any signed evidence or legal hold still depends on them.

## Build 117

[Release improvements](../architecture/release-1.0.0-117.md)

### Verification limits

Actual emulator rider/driver login and re-login passed in the preceding smoke
pass. Reset request, code entry and local invalid-code handling passed. A real
inbox and completed password replacement, physical two-device calling,
provider failover and store approval remain separate evidence requirements.
Audio recording remains disabled. Deployment results are recorded in the
owned release verification report. The final API hash matches the release
package; read-only schema inspection verified eight aligned databases with
zero mismatches. Dedicated administrator, driver and rider login/identity/
workspace reads passed nine checks. The deployed notification asset matches
source, minimum supported builds are unchanged, and the current release
catalogue is published without resetting its history. Android APK/AAB packaged
manifest and signature checks passed. These facts do not certify inbox delivery,
complete physical journeys or store approval.

## Build 130

[Release improvements](../architecture/release-1.0.0-130.md)

### Evidence limits

Source, schema and automated tests do not prove store approval, licensed-store
discovery, provider delivery, physical-device lifecycle, production credentials
or current production health. The six changed ARB files are hash-bound but
pending qualified native review. Build 130 must not be described as production
certified until the named operational gates retain current positive evidence.

## Build 144

[Release improvements](../architecture/release-1.0.0-144.md)

### Verification represented by the corpus

The source corpus includes deterministic unit, contract, architecture, widget,
MySQL, failure-injection and Codemagic-equivalent gates. A bounded two-device
Android run covered installation, role login, driver navigation, membership
routing, financial back navigation, readiness presentation and resume
restoration on the build-143 candidate immediately before build 144.

That evidence did not execute every provider or trip lifecycle. Store
renewal/refund, PayPal capture/refund/dispute, physical GPS journeys, RTC network
handoff, APNs, multi-node SignalR failure and production webhooks require their
own named sandbox or production-safe certification. They remain “not run” when
the evidence does not show otherwise.

## Build 196

[Release improvements](../architecture/release-1.0.0-196.md)

### Verification, deployment and remaining limits

| Observation retained for this checkpoint | Meaning and limit |
| --- | --- |
| Required pre-push gate passed; consumer 4,839 and Admin 1,335 Flutter tests passed; both analyzers had no issues | Host/source evidence for the recorded candidate, not every OS/provider journey |
| API regression lane: 8,563 passed, 155 environment-dependent tests skipped | Passing executed tests; the skipped lane remains unverified in that record |
| API deployed using AWS Systems Manager; liveness HTTP 200; schema remained `2026.10.05.2` | Deployment receipt, not a new schema migration or full production readiness claim |
| Production readiness remained Degraded before and after deployment | Existing provider/operational dependencies remain; liveness does not replace readiness |
| Signed consumer APK/AAB packaged; Play production changes submitted for review | Review submission is not confirmed live store availability |
| Consumer iOS Codemagic workflow started | Completed IPA signing and TestFlight arrival were not established by the retained start record |
| Admin 33 installed and launched on physical Android devices | Installation/launch verification does not certify every form or administrative workflow |
| Copy exception: 1,571 incomplete explanations and 42,048 missing error-catalog locale keys | Release-owner accepted recorded debt; six app language choices do not mean the error catalog or native-copy review is complete |

Physical iOS StoreKit verification and the final simultaneous paired-device
journey remain outstanding in the build-196 release record. This documentation
update does not clear those limitations. Native certification rows remain
untested until exact signed-artifact, OS, provider, account-scope and lifecycle
evidence is attached. Historical provider/test passes keep their original date
and build. See [native certification matrix](../quality/native-platform-certification-matrix.md).

The published [manual library](https://kilodrive.com/manuals),
[product changes](https://kilodrive.com/changelog),
[support](https://kilodrive.com/contact), [privacy](https://kilodrive.com/privacy)
and [terms](https://kilodrive.com/terms) explain user-facing operation. Country
pages and current in-app/native-store disclosures govern availability and
transactions; this architecture checkpoint is not a substitute for them.

The three English consumer manuals were published as edition 3.3 for build
196 and schema `2026.10.05.2`, with public download hashes verified on
2026-10-06. [Manual downloads](../public-product-links.md#published-build-196-manuals)
provide the rider, driver and rental-provider PDFs. This is publication of
reviewed documentation, not a claim of six translated PDF editions or completed
native-store certification.

## Build 156

[Release improvements](../architecture/release-1.0.0-156.md)

At that publication checkpoint, Spanish and French contained only earlier
partial drafts; public requests fell back to the complete English entry until
consolidated translations were reviewed. This is the historical build-156
publication scope, not the current six-locale catalog status.

Recorded build-156 source verification: Flutter analyze passed; the Codemagic-equivalent gate passed 4,739 Flutter tests; 71 focused membership widget tests and 87 focused billing-lifecycle tests passed; .NET solution build reported zero warnings/errors; release governance and Android APK/AAB packaging passed. These results do not certify actual App Store/Play transactions, notification delivery, GPS/RTC, or current production provider health. Each requires separately dated provider or physical-device evidence.
