# Flutter and Native Package Inventory

## Verified baseline

The reviewed source uses Flutter 3.41.7, a Dart constraint beginning at 3.11.5,
and mobile version `1.0.0+70`. `pubspec.yaml` identifies direct intent;
`pubspec.lock`, Gradle/CocoaPods resolution, and the signed artifact identify what
was actually selected. Package presence does not mean an optional feature or
permission is enabled in every release.

## Direct Flutter dependencies

| Area | Direct packages | Selected examples |
| --- | --- | --- |
| State/network | `flutter_riverpod`, `dio`, `signalr_core_new`, `connectivity_plus` | Riverpod 3.3.2, Dio 5.11.0 |
| Persistence/security | `shared_preferences`, `flutter_secure_storage`, `crypto`, `local_auth` | secure storage 10.3.1, local auth 3.0.2 |
| Maps/location | `google_maps_flutter`, `geolocator` | maps 2.18.0, geolocator 13.0.4 |
| Firebase/push | core, App Check, Messaging, Crashlytics, local notifications | core 4.13.0, messaging 16.5.0 |
| Identity | Google, Facebook, Apple sign-in; SMS autofill | Google 7.2.0, Facebook 7.2.0, Apple 8.1.0 |
| Store/platform | in-app purchase/review, app links, URL launcher, permissions | purchase 3.3.0, permission handler 12.0.3 |
| Voice | LiveKit and CallKit integration | LiveKit 2.11.0, CallKit plugin 3.1.5 |
| Files/images | picker, crop, compression, cache, path, share | image picker 1.2.3, cache 3.4.1 |
| UI | SVG, animations, shimmer, charts, QR | shared themed/accessible UI building blocks |
| Localization/device | Flutter localizations, intl, timezone, package/device info | runtime locale, time, and diagnostic metadata |
| Test/lint | Flutter test, integration test, lints | fast PR and emulator suites |

The resolved graph also includes platform-interface packages and Android/iOS
implementations. Those transitive plugins can add native code, manifests,
privacy declarations, and licenses, so the lockfile alone is not the last check.

### Reviewed direct-resolution snapshot

The current lockfile resolves these feature-bearing direct packages (Flutter SDK
packages are omitted). This snapshot belongs to mobile version `1.0.0+70`; a
later release regenerates it rather than editing versions from memory.

| Package | Resolved | Package | Resolved |
| --- | ---: | --- | ---: |
| `animations` | 2.2.0 | `app_links` | 7.0.0 |
| `cached_network_image` | 3.4.1 | `connectivity_plus` | 7.3.1 |
| `crypto` | 3.0.7 | `device_info_plus` | 12.4.0 |
| `dio` | 5.11.0 | `file_picker` | 11.0.3 |
| `firebase_app_check` | 0.4.6 | `firebase_core` | 4.13.0 |
| `firebase_crashlytics` | 5.2.7 | `firebase_messaging` | 16.5.0 |
| `fl_chart` | 0.69.2 | `flutter_animate` | 4.5.2 |
| `flutter_callkit_incoming` | 3.1.5 | `flutter_facebook_auth` | 7.2.0 |
| `flutter_image_compress` | 2.5.1 | `flutter_local_notifications` | 22.3.0 |
| `flutter_riverpod` | 3.3.2 | `flutter_secure_storage` | 10.3.1 |
| `flutter_svg` | 2.3.0 | `geolocator` | 13.0.4 |
| `google_maps_flutter` | 2.18.0 | `google_sign_in` | 7.2.0 |
| `image_cropper` | 12.2.1 | `image_picker` | 1.2.3 |
| `in_app_purchase` | 3.3.0 | `in_app_purchase_android` | 0.5.0 |
| `in_app_review` | 2.0.12 | `intl` | 0.20.2 |
| `livekit_client` | 2.11.0 | `local_auth` | 3.0.2 |
| `package_info_plus` | 9.0.1 | `path_provider` | 2.1.6 |
| `permission_handler` | 12.0.3 | `qr_flutter` | 4.1.0 |
| `share_plus` | 12.0.2 | `shared_preferences` | 2.5.5 |
| `shimmer` | 3.0.0 | `sign_in_with_apple` | 8.1.0 |
| `signalr_core_new` | 1.0.3 | `sms_autofill` | 2.5.0 |
| `timezone` | 0.11.1 | `url_launcher` | 6.3.2 |

Utility and UI packages such as `cupertino_icons`, `path`, and the lint
toolchain remain part of the machine SBOM even when this concise table does not
discuss every one separately.

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
an API call. Current Info.plist background mode is remote notification only; it
does not claim audio/VoIP keep-alive without a reviewable user feature.

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
