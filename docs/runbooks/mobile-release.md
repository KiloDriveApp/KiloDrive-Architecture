# Mobile release runbook

- **Owner:** Mobile release engineering with Android, iOS, security, and product reviewers
- **Status:** Operational store-release procedure
- **Last exercised:** Not yet recorded in this public repository
- **Related architecture:** [Mobile architecture](../architecture/mobile.md), [API architecture](../architecture/api.md), and [application security](../security/application-security.md)
- **Verification policy:** [Testing and verification](../quality/testing-and-verification.md)

## Purpose and scope

Use this runbook to produce, inspect, test, and hand off KiloDrive Android and iOS
store artifacts from one reviewed source commit. It covers versioning, Flutter
quality gates, native dependency/permission inspection, signed-binary checks,
device behavior, store metadata, rollout, and rollback.

A release build is not store-ready merely because `flutter build` exits with
zero. The artifact submitted to a store must be the same artifact whose native
contents, signing identity, privacy behavior, subscription UI, background modes,
and critical workflows were verified.

The test labels and evidence expectations in this runbook use the taxonomy in
[Testing and verification](../quality/testing-and-verification.md). Emulator or
widget evidence cannot replace physical-device lifecycle coverage, and source
manifest review cannot replace inspection of the final merged and signed
artifact.

## Owners and decision rights

| Role | Responsibility |
| --- | --- |
| Mobile release lead | Owns version/build, checklist, artifact identity, and submission decision |
| Flutter engineer | Resolves code/test/localization issues and reviews dependency graph |
| Android release owner | Signing, AAB/APK, manifest, ABI, 16 KB, Play declarations, device tests |
| iOS release owner | Signing, IPA, entitlements, selectors, privacy manifests, App Review evidence |
| API/product owner | Confirms contract compatibility, feature flags, store products, and fixtures |
| Privacy/security reviewer | Confirms permissions, tracking declarations, data use, and artifact redaction |

Submission requires a second-person artifact/hash review. CI credentials may
build or upload; they must not silently change the version or submit every Git
push.

## Preconditions

- The source commit is reviewed and the working tree is clean.
- Flutter/Dart, Android SDK/NDK/Java, Xcode/CocoaPods, and dependency locks are
  pinned to the approved release baseline.
- `pubspec.yaml` contains one semantic version and positive build number; Android
  and iOS will use exactly that value.
- The build number is greater than every build already uploaded to either store.
- The production API contract and minimum-client policy support the release.
- Store product IDs/base plans/offers, localized prices, legal links, privacy
  labels, permissions, support URL, screenshots, and review credentials are
  current.
- Signing and provisioning material is injected from protected CI storage.
- A prior production build and a server-side disable/rollback plan exist.

## Safety and stop conditions

Stop the release when:

- CI or a store script changes the build number independently of `pubspec.yaml`;
- the source commit, generated artifact, or signature cannot be tied together;
- analyzer, test, localization, native selector, entitlement, permission, ABI, or
  16 KB alignment gates fail;
- the merged manifest contains an undeclared or unjustified foreground service,
  broad media permission, advertising identifier, or background mode;
- an app-store privacy declaration says the app tracks users when the release
  does not request ATT—or the app does track without the required consent;
- subscriptions omit title, duration, localized store price, renewal disclosure,
  restore/manage actions, Privacy link, or Terms/EULA link;
- a release artifact contains secrets, fixture credentials, private documents,
  screenshots with credentials, or diagnostic proxy capability; or
- the exact APK/AAB/IPA under test is not the one to be submitted.

Do not bypass an Apple private-selector scan by scanning only Dart source. Do not
remove an Android permission only from the main manifest without checking the
merged release manifest contributed by plugins.

## One version and one artifact lineage

1. Increment the build number once in `pubspec.yaml` before the release build.
2. Record version/build, commit hash, toolchain versions, and lockfile hash.
3. Configure CI to read that value for both platforms. Disable automatic version
   derivation from CI build count.
4. Build from a clean checkout. Cache SDK/package downloads separately from
   disposable `build/` output.
5. Hash every APK, AAB, IPA, mapping/symbol file, and evidence bundle.
6. Never rebuild between certification and upload. If anything changes, rerun the
   gate and issue a higher build if a store has already seen the number.

## Common Flutter quality gate

Run in this order:

1. `flutter pub get --enforce-lockfile`.
2. `flutter gen-l10n` and exact ARB/ICU parity checks for EN, ES, FR, JA,
   zh-Hans, and zh-Hant. The `zh` fallback mirrors Simplified Chinese and is not a
   seventh selectable language.
3. `dart format --output=none --set-exit-if-changed` on application and test code.
4. `flutter analyze`, with repository-defined warnings/errors treated as release
   failures.
5. Fast model, formatter, repository, provider, widget, contract, and security
   tests.
6. Integration tests for tools-only, rider, driver, rental, and system-admin
   workspaces using Flutter semantics, not raw ADB text injection.
7. Render critical routes at 320 px and tablet widths, portrait/landscape,
   1.3x/2.0x platform text, light/dark/high contrast, keyboard open/closed, and
   gesture/three-button navigation.
8. Verify loading shimmer, successful empty state, retryable whole/partial error,
   safe-area bounds, 48 dp targets, focus/semantics order, and no overflow.
9. Produce dependency, license, permission, and generated-file diffs against the
   prior production release.

Test artifacts must redact credentials, access tokens, personal information,
document URLs, and real notification destinations.

## Android release procedure

### Build

Build release APK and AAB with the approved Dart defines and both supported ARM
ABIs: `armeabi-v7a` and `arm64-v8a`. Use the same signing lineage intended for
Play. Keep universal/debug artifacts clearly separated from store output.

### Inspect the exact artifacts

Verify:

- package/application ID, version name/code, signing certificate, and Play app
  signing/upload-key expectations;
- AAB targeting and APK contents include both required ARM ABIs;
- every packaged native `.so` meets Android 16 KB page/alignment requirements;
- merged release manifest permissions, services, receivers, exported components,
  deep links, foreground service types, and backup/data extraction rules;
- target/min SDK and device architecture support match store/device policy;
- no debug flag, cleartext traffic, permissive network security, diagnostic proxy,
  test endpoint, or development Firebase configuration is present;
- R8/shrinker mapping and native symbols are retained securely; and
- Play Integrity, billing, notifications, location, camera/gallery, biometrics,
  and calls match the store declarations and visible app behavior.

For in-app calls, foreground microphone/phone-call service use must be visible,
user-initiated, and limited to an active call. If the release does not provide
that reviewable behavior, remove the service/permission rather than declaring an
invisible “other” use.

### Install and exercise

Install the exact release APK on supported physical/emulated devices. Test both a
fresh install with app data cleared and an upgrade from the previous production
version. Include a supported 32-bit ARM device when `armeabi-v7a` is promised.

Exercise startup, first-run/country/tools-only, login/logout/refresh, rider and
driver onboarding, permissions at point of use, maps/location, ride/bid/chat,
wallet read and fake money flow, membership/store billing, documents, deep links,
push, offline/reconnect, background/killed behavior, biometric lock, and system
navigation insets. Confirm uninstall/reinstall behavior against Android backup
policy rather than assuming uninstall always clears restored preferences.

## iOS release procedure

### Build and export

Archive and export a signed IPA using the same version/build and reviewed export
options. Confirm provisioning came from the intended App Store profile, not a
development or ad-hoc profile.

### Inspect the signed IPA

Extract and inspect the actual `Runner.app` and embedded frameworks:

- signature, designated requirement, application identifier, and embedded
  profile agreement;
- production push and Sign in with Apple entitlements where used;
- minimum iOS version and supported device families;
- camera, photo, location, microphone, and other purpose strings;
- privacy manifests and declared required-reason APIs;
- export-compliance metadata;
- background modes justified by visible behavior; and
- executable Mach-O strings and Objective-C metadata for prohibited private or
  deprecated selectors.

The historical ReplayKit `buttonPressed:` issue is a supply-chain lesson. Scan
every executable image and report the exact offender. Do not scan every NOTICE or
plist resource as executable code, and do not assume upgraded Dart dependencies
prove the signed framework is clean.

### Privacy and App Review behavior

Permission requests should follow a user's feature action. A brief explanatory
screen may explain why access matters, but a dismissible pre-prompt must not
coerce the user and then surprise App Review. If access was already denied,
explain the limitation and offer a Settings link without repeatedly prompting.

Declare only background audio/VoIP behavior the reviewer can actually observe on
a physical device. Provide a screen recording showing an active, visible in-app
call continuing through the supported background scenario if those modes remain.

If KiloDrive does not track users across other companies' apps/sites, ensure App
Store privacy answers say so rather than listing operational contact/location
data as “tracking.” If tracking exists, implement ATT before collecting it.

## Subscription and store-billing certification

For each eligible driver/rental plan and term:

- map the app plan/term to the exact Apple product or Google subscription,
  base-plan, and offer identifiers;
- show product title, benefits/limits, selected term, localized store price,
  automatic-renewal disclosure, renewal/grace/revocation/acknowledgement state;
- provide Restore Purchases and platform subscription-management actions;
- open functional Privacy Policy and Terms of Service/EULA links;
- validate signed StoreKit 2 transactions and Google purchase tokens server-side;
- hide external digital-membership payment methods in store builds; and
- test purchase, acknowledgement pending, restore, resubscribe, upgrade,
  downgrade, grace, retry, refund, revocation, and chargeback with test accounts.

Riders remain free when that is the product policy; do not accidentally display a
rider subscription because a shared screen returned all plans.

## Isolated native dependency batches

Upgrade native-risk packages in separate batches:

1. LiveKit/WebRTC/call stack;
2. social sign-in and local authentication; then
3. Riverpod/state-management stack.

For **each** batch rerun format, analyze, tests, manifest/entitlement/permission
diffs, Android 16 KB and arm64/AAB checks, iOS archive/private-selector scan, and
foreground/background/killed call or auth tests. Do not bundle unrelated major
upgrades; a clean diff is part of the safety mechanism.

## Store evidence and controlled rollout

Retain artifact hashes, commit/toolchain/lockfile, SBOM/notices, analyzer/tests,
render matrix, ABI/alignment results, signed-native inspections, permissions and
privacy diff, store product contract, reviewer videos, screenshots, release notes,
and test cleanup.

Upload only the certified artifact. Keep automatic store submission disabled
unless an explicitly approved release workflow is invoked. Use staged/phased
rollout, watch crash-free sessions, ANRs, startup, authentication, billing,
network errors, and support reports, and define pause thresholds before launch.

## Diagnosis guide

| Symptom | Likely cause | Safe action |
| --- | --- | --- |
| Older Android says “App not installed” | ABI, min SDK, signature lineage, storage, or version downgrade | inspect device/API/ABI and exact APK; do not weaken signing |
| Codemagic archive fails in Swift | plugin/Flutter embedding API or strict Swift capture change | reproduce with pinned toolchain; fix source and rebuild all evidence |
| IPA private-selector gate fails | embedded native framework still references selector | identify exact Mach-O; upgrade/remove isolated dependency |
| App Review rejects background service | declared mode not visible/necessary | remove it or provide accurate in-app behavior and review evidence |
| Membership plans blank | API/product mapping/optional request collapsed core state | keep successful core data, show partial error, verify production contract |
| Map tiles fail only in debug | signing certificate/key restriction differs | fix approved debug restriction; do not ship unrestricted production key |
| Splash never resolves | unbounded plugin/storage bootstrap | fail open for optional services and show retryable required-config error |

## Rollback and recovery

An installed mobile build cannot usually be replaced remotely. Rollback means:

1. stop the staged/phased rollout and store submission;
2. disable the affected server feature with an approved safe flag where possible;
3. preserve API backward compatibility for installed versions;
4. notify support/reviewers with accurate impact;
5. fix forward from the prior reviewed source, increment to a **higher** build,
   and rerun every relevant gate; and
6. resume gradually only after the new artifact is certified.

Never reuse a build number already uploaded. Never make an API breaking change to
force old clients out before the minimum-version and customer migration policy is
ready.

## Completion criteria

- Android and iOS artifacts report the same version/build and reviewed commit.
- Hashes match the files uploaded to each store.
- Flutter, localization, rendering, integration, native, permission, privacy,
  entitlement, billing, and security gates pass.
- Exact release APK/IPA behavior passes fresh install, upgrade, offline,
  background, killed, and critical role workflows.
- Store metadata/legal/privacy/permission declarations match the binary.
- Monitoring and staged-rollout stop conditions are active.
- Test fixtures and screenshots contain no credentials or user data.

## Escalation

Escalate a leaked signing credential, cross-account/country exposure, invalid
store transaction grant, privacy-label mismatch, hidden background recording,
repeat crash/ANR, or inability to prove artifact identity to security, privacy,
financial, and release owners immediately. Halt rollout until resolved.

## Common pitfalls

- Letting CI auto-increment iOS while Android reads `pubspec.yaml`.
- Caching `build/` and submitting stale native frameworks.
- Looking at source manifests instead of the merged/re-signed artifact.
- Testing a debug APK and submitting an untested release AAB.
- Scanning inert resource text as if it were executable—or scanning too narrowly
  and missing the real framework.
- Adding foreground-service declarations “just in case.”
- Capturing screenshots/videos with credentials or personal notifications.
- Treating store upload processing as successful review or product activation.
