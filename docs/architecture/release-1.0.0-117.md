# Release 1.0.0 build 117 architecture update

Owner: KiloDrive Identity, Mobile and Release Engineering.
Last source review: 13 September 2026.
Environment: verified production API/schema/release catalogue; locally signed Android artifacts.
Evidence: [source-derived repository facts](https://github.com/KiloDriveApp/KiloDrive/blob/main/docs/generated/repository-facts.md),
[release verification](https://github.com/KiloDriveApp/KiloDrive/blob/main/docs/releases/release-117-production-verification.md),
[emulator evidence boundaries](https://github.com/KiloDriveApp/KiloDrive/blob/main/docs/mobile-emulator-smoke-2026-09-13.md).
Implementation: [release source commit](https://github.com/KiloDriveApp/KiloDrive/commit/6200086393c08d2b837f987f0f539ee1f60464c6).

| Fact | Value | Authority |
| --- | --- | --- |
| Mobile release | 1.0.0+117 | Flutter pubspec.yaml |
| Schema contract | 2026.09.13.1 | SchemaContract.CurrentVersion |
| Public REST | /api/v1 | Reviewed OpenAPI v1 |
| API inventory | 723 paths, 814 operations | Source-generated repository facts |
| OpenAPI SHA-256 | 66b68b440668f4f0f31092cf1cdfff5334c81227ff1195316d64dbfa85129d46 | Reviewed artifact and sidecar |
| Languages | English, Spanish, French, Japanese, Simplified Chinese, Traditional Chinese | ARB configuration |

## Authentication composition and navigation

Email Address authentication remains email plus password. An optional email
code flow must never replace that primary credential flow. Mandatory manual
email verification, two-factor proof, account lock and legal acceptance remain.

Internal authenticated state stays reactive to token rotation, while RootGate
holds the visible workspace behind an explicit session-composition state.
Country/role workspaces are derived from server authorization. Fresh sign-in
selects the primary rider dashboard or driver Bidding Hall; stale stored screen
or optional-workspace choices cannot override that selection. Ordinary cold
restore and background resume still retain the account-scoped last screen.
Asynchronous preference writes cannot republish stale rotated tokens.

Vehicle storage is optional for riders and is not a rider onboarding gate.
Drivers can reach the Bidding Hall before review completion, but the server
readiness checklist still gates going online, offers and bid mutations.
Stopping an obsolete realtime connection is an expected lifecycle event,
not a reason to retry or diagnose failure against a replacement account.

## Durable request-time security email context

Security-code envelopes snapshot the original server request instant,
authoritative account/country timezone, proxy-aware IP and bounded client
device metadata before scheduling delivery. Worker retries do not substitute
their own time, IP or device. Display includes a timezone and numeric offset
to disambiguate daylight-saving transitions. Missing facts remain unavailable.

All required wording/layout comes from the shared notification JSON catalogue.
Tenant template customization retains the mandatory request-details block;
reserved variables are replaced from captured context and HTML-escaped.
Reported device and operating-system fields are informational, not proof of
identity or authorization. Context stays in the existing operational outbox
retention boundary and is not duplicated into presentation history or audit.

Control-only administrator identities may receive exact account-bound code
emails without manufacturing country credential projections. That narrow
worker path excludes suspended/deleted users, unrelated templates, different
recipients and non-email channels. No database schema or v1 wire change is
required; existing metadata-capable mobile releases remain compatible.

## Verification limits

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
