# Runbook: Mobile Release

## Preconditions

Pinned Flutter SDK, clean dependency cache/build separation, incremented shared
build number, complete localization generation, and reviewed store configuration.

## Certification

1. Format, analyze, and run model/provider/widget/integration tests.
2. Run the responsive/accessibility matrix and semantics-driven authenticated
   workflows without credentials in screenshots.
3. Build signed Android APK/AAB for supported ARM ABIs; verify signing, target
   SDK, 16 KB native alignment, manifest permissions, and no advertising IDs.
4. Build signed iOS archive/IPA; verify bundle/version, minimum OS, entitlements,
   privacy purpose strings, background modes, and private/deprecated selectors.
5. Exercise permissions, background location/bidding, push, biometrics, offline
   queue, SignalR reconnect, and calls on representative real devices.
6. Reconcile App Store/Play privacy, foreground/background, subscription, and
   export-compliance declarations with the exact binary.
7. Hash and archive artifacts; submit only through an intentional manual/release
   workflow.

Store approval is an external decision; technical certification does not
guarantee acceptance.
