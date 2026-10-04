# Flutter and Native Package Inventory

## Verified baseline

The reviewed source baseline is consumer `1.0.0+172` and System Admin `0.1.0+16`.
The generated [package inventory](direct-packages.md) records exact coordinates,
app ownership and source revision. `pubspec.yaml` identifies direct intent;
`pubspec.lock` identifies selected Dart packages, while release evidence must
also inspect SDK, Gradle/CocoaPods and signed native contents. Package presence
does not mean an optional feature or permission is enabled in every release.

## Direct Flutter dependencies

| Area | Package families |
| --- | --- |
| State/network | `flutter_riverpod`, `dio`, `signalr_core_new`, `connectivity_plus` |
| Persistence/security | `shared_preferences`, `flutter_secure_storage`, `crypto`, `local_auth` |
| Maps/location | `google_maps_flutter`, `geolocator` |
| Firebase/push | core, App Check, Messaging, Crashlytics, local notifications |
| Identity | Google, Facebook, Apple sign-in; SMS autofill |
| Store/platform | in-app purchase/review, app links, URL launcher, permissions |
| Voice | LiveKit and CallKit integration |
| Files/images | picker, crop, compression, cache, path, share |
| UI | SVG, animations, shimmer, charts, QR |
| Localization/device | Flutter localizations, intl, timezone, package/device info |
| Test/lint | Flutter test, integration test, lints |

The resolved graph also includes platform-interface packages and Android/iOS
implementations. Those transitive plugins can add native code, manifests,
privacy declarations, and licenses, so the lockfile alone is not the last check.

### Exact versions and source forks

Use the [generated inventory](direct-packages.md) for versions and ownership;
this chapter no longer duplicates a hand-maintained build-144 version table.
The two apps can select different versions of a package. Reviewed source forks
for calling, Android billing and Riverpod retain distinct identities from hosted
upstream packages. A familiar name/version alone does not prove identical code.
Explicit overrides are included; transitive/native graphs still belong to the
release SBOM. The generator checks its inputs against the source commit and
refuses arbitrary local/Git dependency publication.

## Android native release gates

The Android source targets a current SDK, uses NDK r28, and produces supported
32-bit and 64-bit ARM binaries (`armeabi-v7a`, `arm64-v8a`). Release CI:

1. restores from the pinned Flutter SDK and committed lockfile;
2. builds release APK and AAB for both ARM ABIs;
3. inspects every packaged native library for 16 KB page-size alignment;
4. verifies the expected ABI set rather than accepting an arm64-only accident;
5. diffs the merged manifest and rejects unexpected advertising, photo, or
   foreground-service permissions; and
6. archives signed artifact hashes and inspection output.

The 16 KB check matters because a Dart-only test cannot reveal a misaligned
native `.so`. It must inspect the built release artifact after all plugins are
linked.

## Apple native release gates

The signed IPA is verified, not only Dart source. CI checks the version/build from
`pubspec.yaml`, minimum supported iOS, purpose strings, export-compliance flag,
background modes, code signature, provisioning profile, application identifier,
Sign in with Apple and push entitlements.

Executable Mach-O images are scanned for non-public/deprecated selectors. The
WebRTC-specific ReplayKit `buttonPressed:` issue is rejected in Runner,
Flutter/WebRTC, or LiveKit executable scope; an unrelated framework occurrence is
reported for review rather than blindly treating every inert resource string as
an API call. The reviewed consumer Info.plist declares location and remote-notification
background modes; the Admin app declares remote notification. Declarations do
not prove user permission or successful background delivery. Neither inspected
plist declares audio/VoIP background mode.

## Isolated upgrade batches

Native-heavy changes are sequenced as LiveKit/WebRTC, social/local auth, then
Riverpod. For each batch, run format, localization, fatal analysis, tests,
Android alignment/ABI/manifest gates, iOS archive/entitlement/private-selector
scan, background and killed-state call flows, and permission diffs. Roll back the
single batch if evidence regresses.

## Privacy and permission review

Every plugin is checked for data collection, platform privacy manifest/label
impact, foreground/background behavior, and permission timing. A plugin must not
trigger a permission merely because it initializes. Camera/photo/microphone and
location requests follow an explicit user action and explain degraded behavior
without coercive pre-prompts.

## Inventory and removal

Generate a CycloneDX/SPDX SBOM from the exact resolved build, then combine it with
Gradle, CocoaPods, embedded framework, and store SDK evidence. Removing a package
also removes its platform registrations, manifest/plist keys, permissions,
entitlements, resource bundles, ProGuard/R8 rules, privacy declarations, notices,
and tests.

See the [SBOM contract](sbom.md) for clean-build, native-inspection, and
artifact-binding requirements.
