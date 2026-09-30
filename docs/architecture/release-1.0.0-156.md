# Release architecture update: KiloDrive 1.0.0 build 156

- **Owner:** Mobile platform and release engineering
- **Last verified:** 2026-09-28
- **Environment:** Source build `1.0.0+156`; schema contract `2026.09.26.2`
- **Evidence:** `src/client/mobile/pubspec.yaml`,
  `src/server/KiloDrive.Api/Data/SchemaContract.cs`, source
  `docs/releases/release-156-source-verification.md`, the consolidated English
  block in `database/seed-app-release-changelog.sql`, and the public release
  API and website checked on 2026-09-28

Build 156 moves more native behavior behind typed platform adapters while keeping KiloDrive's API authoritative for identity, trip transitions, wallet postings, and membership. The most consequential change is store purchase recovery: an explicit Apple purchase-sheet cancellation is not a potentially charged transaction, while a lost response after provider handoff remains a bounded, recoverable unknown outcome. Late callbacks are fenced by account, tenant, country, role, and generation. Sanitized product-discovery diagnostics distinguish missing quarterly products from mapping or provider timing faults. The current membership card derives its exact plan term from the active period rather than a later transaction.

The [native-adapter and billing architecture](native-adapters-and-store-billing.md) describes the detailed Apple, Google, and cross-platform flows; the [entitlement runbook](../runbooks/store-entitlement-reconciliation.md) describes investigation and recovery. The [build 144 release document](release-1.0.0-144.md) remains historical and does not describe the current source baseline.

The public build-156 changelog is a single current-build entry with ten
structured improvements. It combines the pending source notes from builds
145, 148, 149, and 150 with the build-156 adapter and billing changes. Those
intermediate builds are not separate public release pages. The published
English detail covers task resumption, external driver-experience evidence,
governed administrative recovery, account verification, store diagnostics,
membership and adapter recovery, and release checks. Spanish and French
contain only earlier partial drafts, so public requests fall back to the
complete English entry until the consolidated translations are reviewed.
Build 144 remains a historical public release and retains its previously
consolidated history; publication of 156 did not rewrite it.

The source seed is designed for reruns, and the historical build-144/build-1
consolidation explicitly preserves build 156. Publication changes release
communication only: it does not raise the mobile compatibility minimum, prove
an App Store or Play rollout, or certify a native provider. The public API's
current-release response and the website changelog listing and detail were
checked after publication; the current release and detail reported build 156
with ten improvements.

Recorded build-156 source verification: Flutter analyze passed; the Codemagic-equivalent gate passed 4,739 Flutter tests; 71 focused membership widget tests and 87 focused billing-lifecycle tests passed; .NET solution build reported zero warnings/errors; release governance and Android APK/AAB packaging passed. These results do not certify actual App Store/Play transactions, notification delivery, GPS/RTC, or current production provider health. Each requires separately dated provider or physical-device evidence.
