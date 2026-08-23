# Software Bill of Materials (SBOM)

An SBOM is the ingredient list for a software artifact. It tells us which
packages and native components were resolved, which versions were embedded, how
they are identified, and which evidence belongs to the release. It does **not**
prove by itself that a component is safe, correctly licensed, configured, or
even reachable in the running application.

This page explains KiloDrive's SBOM contract. The readable package pages in this
repository describe the reviewed direct baseline. The repository also publishes
a sanitized, machine-readable
[CycloneDX 1.6 direct-dependency baseline](kilodrive-public-direct.cdx.json) and
its [SHA-256 sidecar](kilodrive-public-direct.cdx.json.sha256).

That public artifact is deliberately labelled `direct-only` and
`authoritative-release-sbom=false`. It proves the reviewed direct coordinates at
this documentation baseline; it does not pretend to be the complete SBOM for a
signed release. The private release pipeline produces the authoritative direct,
transitive, native, asset, and toolchain graph from the exact clean build and
binds it to the API, Portal, Website, APK, AAB, and IPA artifacts.

## Public baseline generation and verification

The standard-library generator reads central NuGet metadata, actual project
references, Flutter `pubspec.yaml`, and `pubspec.lock` from an authorized clean
source checkout. It emits no repository path or infrastructure identifier.

```text
python tools/generate_public_sbom.py --generate \
  --source-root <authorized-source-checkout> \
  --timestamp <reviewed-UTC-timestamp>
python tools/generate_public_sbom.py --check
```

CI performs the second command. It verifies CycloneDX format and version, root
and component identity, unique purls, NuGet and Pub coverage,
sensitive-pattern absence, and the SHA-256 sidecar. Regeneration belongs in the
documentation change that updates the package baseline.

The exact generated release notice bundle is retained with restricted release
evidence because a full SBOM can contain private repository, build-host, and
artifact metadata. The public [license guide](licenses.md) explains obligations
and reviewed direct families; it is not represented as a legal conclusion for
every transitive component.

## What belongs in the inventory

The inventory includes more than the names developers remember adding:

- direct and transitive NuGet packages for every published .NET project;
- Dart packages selected by `pubspec.lock`;
- Android Gradle/AAR/JAR dependencies and every packaged native `.so` by ABI;
- CocoaPods, Swift packages, embedded frameworks, and Mach-O executables in the
  signed iOS application;
- build/runtime containers and operating-system packages when a release uses
  them;
- separately distributed fonts, icons, sounds, map/reference datasets, and
  document-rendering assets;
- build tools that execute untrusted input or hold release credentials; and
- commercial SDKs or vendored source that a package manager cannot discover.

External services such as AWS, Google Maps, payment processors, LiveKit, and
Cloudflare are recorded in the provider/service inventory and threat model.
They are not falsely represented as compiled package components, but their SDKs
are.

## Release evidence model

Each release evidence bundle ties these values together:

| Evidence | Why it matters |
| --- | --- |
| Source commit and clean-tree proof | Identifies the reviewed input |
| Pinned SDK/toolchain versions | Makes resolution reproducible |
| Package-manager lock/restore output | Shows what was selected |
| CycloneDX JSON and/or SPDX JSON | Machine-readable component graph |
| License/NOTICE bundle | Preserves attribution and terms |
| Vulnerability and malware scan | Finds known risk at release time |
| Android manifest/ABI/native inspection | Finds merged permissions and native code |
| iOS entitlement/framework/executable inspection | Finds linked capabilities and private selectors |
| Artifact SHA-256 and signature identity | Binds evidence to what was delivered |
| Exceptions and approvals | Records risk owner, scope, expiry, and remediation |

Do not generate an SBOM from a developer's warm cache and attach it to a
different build. Restore and package first, then inspect the artifact produced
by that same job.

## Generation workflow

### 1. Establish a clean, pinned build

Use the repository's pinned .NET and Flutter SDKs, committed package metadata,
and lockfile enforcement. Isolate dependency caches from build outputs. Record
the source commit, SDK versions, target runtime/ABI, and build configuration.

If a resolver wants to change a locked version, the job fails. A release build
does not “helpfully” update dependencies.

### 2. Export the .NET graph

From the solution root, restore and export direct plus transitive packages for
all projects. A typical evidence command is:

```text
dotnet restore --locked-mode
dotnet list <solution> package --include-transitive --format json
```

Central package management describes direct intent, while the exported graph
captures shared runtime dependencies. The publication step also inspects each
project's publish directory so a test-only package is not mistaken for a
production component and a copied native library is not missed.

### 3. Export Flutter, Android, and iOS graphs

Use lockfile-enforced Flutter restore and export the Dart graph. Then resolve
Gradle and CocoaPods/Swift dependencies on the platform builders. Inspect the
release AAB/APK and signed IPA rather than trusting source manifests alone.

The Android pass records each `.so` and ABI, checks 16 KB page alignment, and
diffs merged permissions. The iOS pass records embedded frameworks, executable
hashes, entitlements, privacy manifests, background modes, and private/deprecated
selector scans.

### 4. Normalize component identity

Components use a stable package URL (purl) where the ecosystem supports it, for
example NuGet, Pub, Maven, CocoaPods, or generic native artifacts. Include:

- package/component name and exact resolved version;
- supplier or publisher when verified;
- purl and upstream location;
- cryptographic hash when available;
- direct/transitive relationship and dependency edges;
- application/runtime/test/build scope;
- concluded and declared license expressions; and
- evidence source and confidence.

Unknown data stays `NOASSERTION` until reviewed. Guessing a license from another
package in the same family produces cleaner-looking but unreliable evidence.

### 5. Scan and review

Run vulnerability, malicious-package, provenance, secret, and license-policy
checks against the full graph. Review native SDK privacy behavior and store
declarations separately. A package with no current CVE may still be abandoned,
over-privileged, commercially ineligible, or unnecessary.

New critical/high findings fail release unless a named security owner records
exploitability, compensating controls, expiry, and upgrade/removal work. Unknown
or copyleft/commercial license results go to license review; they are not waived
by a vulnerability decision.

### 6. Bind and archive

Hash the final signed artifacts and the SBOM/notice bundle. The release evidence
index maps each artifact to its SBOM and signature identity. Internal evidence
can contain repository/build metadata needed by auditors; a public derivative
must first remove private repository URLs, build paths, account identifiers,
operator names, and infrastructure details.

## Machine-readable output requirements

KiloDrive accepts CycloneDX JSON or SPDX JSON when the generator and schema
version are recorded. At minimum, the document must include a unique serial or
namespace, creation timestamp, tool identity/version, root application
component, component versions/purls/hashes, and dependency relationships.

A deliberately generic CycloneDX fragment looks like this:

```json
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.6",
  "version": 1,
  "metadata": {
    "component": {
      "type": "application",
      "name": "KiloDrive component",
      "version": "<release-version>"
    }
  },
  "components": [
    {
      "type": "library",
      "name": "<resolved-package>",
      "version": "<exact-version>",
      "purl": "pkg:<ecosystem>/<name>@<version>"
    }
  ]
}
```

Placeholders in this documentation are not valid release evidence. The release
job substitutes values from its actual graph and signs/archives the result.

## Completeness assertions

The pipeline fails when any of these is true:

- a direct dependency is missing from the SBOM;
- an artifact contains a native framework/library not represented in the SBOM;
- a resolved version differs from the committed lock/baseline without review;
- component identity or license remains unresolved without a current waiver;
- the SBOM hashes refer to a different APK, AAB, IPA, or server publish;
- test/build dependencies are labelled as runtime, or runtime dependencies are
  incorrectly excluded as test-only;
- the generated notices omit an applicable license/NOTICE; or
- the public export contains secrets or private deployment identifiers.

## Handling a vulnerable component

1. Confirm the exact affected component/version and whether it ships in the
   relevant artifact.
2. Trace the dependency path back to the direct package that introduced it.
3. Determine whether the vulnerable code path is reachable in KiloDrive.
4. Prefer upgrading or removing the dependency. Pinning a transitive version is
   acceptable only after compatibility tests and with a reason.
5. If immediate removal is unsafe, document compensating controls, an owner,
   expiry, monitoring, and a target release.
6. Rebuild from clean inputs, regenerate the SBOM, rerun native/store gates, and
   verify the old component is absent from the artifact—not only from a manifest.

## Practical pitfalls

- **Direct-only inventory:** misses most of the actual dependency tree.
- **Source-only native scan:** misses frameworks merged by Gradle/CocoaPods.
- **Stale SBOM:** accurately describes last month's binary, not today's upload.
- **License guessing:** turns uncertainty into incorrect legal evidence.
- **Version without hash:** can be ambiguous for republished or vendored files.
- **Removing a package incompletely:** leaves permissions, entitlements,
  platform registration, resources, or notice obligations behind.
- **Publishing the internal SBOM blindly:** can expose private repository and
  infrastructure metadata even when it contains no application secret.

## Ownership and review cadence

Engineering owns graph generation and artifact completeness. Security owns
vulnerability policy and exceptions. Legal/compliance owns license conclusions
and service terms. Release Engineering owns artifact binding and retention.
Feature owners explain why each direct dependency remains necessary.

Regenerate on every release and after any dependency, SDK, native build,
permission, or entitlement change. Re-scan stored SBOMs when new vulnerability
intelligence appears; a release that was clean on build day can become affected
later.

See the [.NET inventory](dotnet-packages.md),
[Flutter/native inventory](flutter-packages.md), and
[license guidance](licenses.md).
