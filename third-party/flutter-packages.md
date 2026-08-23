# Direct Flutter Package Inventory

Baseline: Flutter 3.41.7 / Dart 3.11.5, mobile `1.0.0+66`. Exact transitive
versions come from `pubspec.lock` in the private product repository.

| Area | Direct packages |
| --- | --- |
| State/network | flutter_riverpod, dio, signalr_core_new, connectivity_plus |
| Persistence/security | shared_preferences, flutter_secure_storage, crypto, local_auth |
| Maps/location | google_maps_flutter, geolocator |
| Firebase/push | firebase_core, firebase_app_check, firebase_messaging, firebase_crashlytics, flutter_local_notifications |
| Identity | google_sign_in, flutter_facebook_auth, sign_in_with_apple, sms_autofill |
| Store/platform | in_app_purchase, in_app_purchase_android, in_app_review, app_links, url_launcher, permission_handler |
| Voice | livekit_client 2.11.0, flutter_callkit_incoming |
| Files/images | image_picker, file_picker, image_cropper, flutter_image_compress, cached_network_image, path_provider, path, share_plus |
| UI | cupertino_icons, flutter_svg, animations, flutter_animate, shimmer, fl_chart, qr_flutter |
| Localization/device | flutter_localizations, intl, timezone, package_info_plus, device_info_plus |
| Test/lint | flutter_test, integration_test, flutter_lints |

## Native dependency controls

- LiveKit/WebRTC, social/local authentication, and Riverpod upgrades are isolated
  into separate batches.
- Android releases include the supported ARM ABIs and are checked for 16 KB
  native-page alignment.
- Manifest gates reject advertising IDs, over-broad photo permissions, and
  undeclared/unnecessary foreground-service permissions.
- iOS archives are scanned for private/deprecated selectors and reviewed
  entitlements.

Package presence does not imply every optional feature or permission is active in
every release.
