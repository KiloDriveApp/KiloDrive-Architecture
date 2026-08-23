# Third-Party Dependency Policy

KiloDrive uses centrally pinned .NET packages and a committed Flutter lockfile.
The source manifests and release-generated Software Bill of Materials (SBOM) are
authoritative; this public inventory is a human-readable baseline.

## Policy

1. Pin and review direct dependencies and lock transitive resolution.
2. Scan vulnerabilities and license metadata in CI.
3. Upgrade native/mobile dependencies in isolated functional batches.
4. Compare Android/iOS permissions and entitlements before and after upgrades.
5. Scan signed executables for non-public APIs and native alignment.
6. Generate third-party notices from the exact release dependency graph.
7. Record commercial/dual-license eligibility separately from open-source
   notices.
8. Remove unused packages and permissions.

## Release gates

The mobile gate includes formatting, analysis, unit/widget/integration tests,
Android ARM ABI and 16 KB checks, signed AAB/APK inspection, iOS archive,
entitlement/private-selector scans, background/killed behavior, and permission
diffs. Server gates include restore/build/test, package audit, OpenAPI contract,
schema parity, and secret scanning.

See [.NET packages](dotnet-packages.md), [Flutter packages](flutter-packages.md),
and [license guidance](licenses.md).
