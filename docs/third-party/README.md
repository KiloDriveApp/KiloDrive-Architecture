# Third-Party Dependency and SBOM Policy

## Why dependency evidence matters

KiloDrive ships source written by the team and code supplied by package, native,
platform, and service providers. The dependency manifest tells us what we asked
for; the resolved graph tells us what is actually compiled; the signed artifact
proves what went to a store or server. All three are needed.

This public inventory is a readable baseline, not the legal or vulnerability
record for a particular release. The release-generated Software Bill of
Materials (SBOM), third-party notices, package hashes, and signed artifact remain
authoritative.

## Direct versus transitive

A **direct dependency** appears in `PackageReference`/central package management
or Flutter `pubspec.yaml`. The team deliberately selected it and owns the reason
for it. A **transitive dependency** is selected because a direct package requires
it. It still runs in the product and still needs vulnerability and license
review.

Examples from the resolved .NET graph include `AWSSDK.Core`, Open XML libraries,
Google API/GAX helpers, IdentityModel, OpenTelemetry core packages, Serilog core
and sinks, and cryptographic/serialization helpers. Flutter's lockfile similarly
resolves platform-interface and native implementation packages below the direct
plugins. Do not copy a short direct-package list into an SBOM scanner and call it
complete.

## Sources of truth

| Evidence | Purpose |
| --- | --- |
| Central .NET package file and project files | Direct server/browser/test intent and pinned versions |
| `dotnet list ... package --include-transitive` | Resolved .NET graph after restore |
| Flutter `pubspec.yaml` | Direct mobile intent and SDK constraints |
| Flutter `pubspec.lock` / dependency graph | Exact selected Dart/plugin graph |
| CocoaPods/Gradle resolution and signed binaries | Native frameworks actually linked |
| Generated CycloneDX or SPDX SBOM | Machine-readable release inventory |
| Third-party notices | Human-readable copyright/license obligations |
| Artifact hashes/signatures | Binding evidence to a specific build |

## Change policy

1. Explain the operational need and why platform APIs or existing packages are
   insufficient.
2. Review maintainer health, release cadence, vulnerability history, native
   permissions, privacy behavior, and license.
3. Pin the direct dependency through the repository's normal mechanism.
4. Restore from a clean cache and diff the full transitive graph.
5. Run source/binary vulnerability, secret, malware, and license scans.
6. Exercise failure, timeout, upgrade, and rollback behavior.
7. Regenerate SBOM/notices from the exact release restore.
8. Remove unused packages, permissions, entitlements, configuration, and notices.

### Package audit record

The change or release evidence records the feature owner, reason for the
dependency, alternatives, direct/transitive graph change, maintainer health,
supported platforms, native code, permissions, privacy/data behavior,
vulnerability result, license conclusion, size/startup effect, failure behavior,
and rollback. “Popular package” is not a risk review.

An SDK that handles identity, payment, location, media, documents, or
cryptography receives focused threat-model and data-flow review. Native plugins
are inspected in the merged/signed artifact because permissions and entitlements
can come from transitive platform implementations.

## Mobile upgrade batches

Native upgrades are deliberately isolated:

1. LiveKit/WebRTC;
2. social sign-in and local authentication; then
3. Riverpod/state management.

Each batch runs format, localization generation, fatal analysis, unit/widget and
focused integration tests, Android permission/ABI/16 KB native alignment checks,
arm32+arm64 APK/AAB builds, iOS archive/identity/entitlement/private-selector
scans, background/killed call tests, and store-permission diffs. Unrelated major
upgrades are not combined because a regression needs a small attributable change
set.

## Release evidence

Archive the restored graph, SBOM, notices, vulnerability/license results,
Android manifest and native library inspection, iOS entitlement and executable
scan, artifact hashes, approvals, and exception waivers. A waiver names an owner,
scope, expiry, compensating control, and removal/upgrade target.

See [.NET packages](dotnet-packages.md), [Flutter packages](flutter-packages.md),
[license obligations](licenses.md), and the full
[SBOM generation and review contract](sbom.md). The sanitized public evidence is
the [CycloneDX direct-dependency baseline](kilodrive-public-direct.cdx.json) and
its [SHA-256 sidecar](kilodrive-public-direct.cdx.json.sha256); it is explicitly
not a substitute for the artifact-bound release SBOM.
