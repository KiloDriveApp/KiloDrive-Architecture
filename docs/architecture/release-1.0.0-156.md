# Release architecture update: KiloDrive 1.0.0 build 156

- **Owner:** Mobile platform and release engineering
- **Last verified:** 2026-09-28
- **Environment:** Source build `1.0.0+156`; schema contract `2026.09.26.2`
- **Evidence:** `src/client/mobile/pubspec.yaml`, `src/server/KiloDrive.Api/Data/SchemaContract.cs`, source `docs/releases/release-156-source-verification.md`, and reviewed three-language changelog block in `database/seed-app-release-changelog.sql`

Build 156 moves more native behavior behind typed platform adapters while keeping KiloDrive's API authoritative for identity, trip transitions, wallet postings, and membership. The most consequential change is store purchase recovery: an explicit Apple purchase-sheet cancellation is not a potentially charged transaction, while a lost response after provider handoff remains a bounded, recoverable unknown outcome. Late callbacks are fenced by account, tenant, country, role, and generation. Sanitized product-discovery diagnostics distinguish missing quarterly products from mapping or provider timing faults. The current membership card derives its exact plan term from the active period rather than a later transaction.

The [native-adapter and billing architecture](native-adapters-and-store-billing.md) describes the detailed Apple, Google, and cross-platform flows; the [entitlement runbook](../runbooks/store-entitlement-reconciliation.md) describes investigation and recovery. The [build 144 release document](release-1.0.0-144.md) remains historical and does not describe the current source baseline.

Recorded build-156 source verification: Flutter analyze passed; the Codemagic-equivalent gate passed 4,739 Flutter tests; 71 focused membership widget tests and 87 focused billing-lifecycle tests passed; .NET solution build reported zero warnings/errors; release governance and Android APK/AAB packaging passed. These results do not certify actual App Store/Play transactions, notification delivery, GPS/RTC, or current production provider health. Each requires separately dated provider or physical-device evidence.
