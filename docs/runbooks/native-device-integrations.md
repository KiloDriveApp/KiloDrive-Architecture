# Runbook: Native device integration failures

- **Owner:** Mobile platform on-call with Identity/API security, Trips, Maps and Upload owners
- **Status:** Operational policy for implemented adapters; signed-device certification is separate
- **Last source review:** 2026-10-05 against product committed [`8bfe0888`](https://github.com/KiloDriveApp/KiloDrive/tree/8bfe08881bce51535d1165552f2d5be8e05fc872); working tree is dirty
- **Last exercised:** The 2026-10-05 inspection did not exercise its consumer `1.0.0+192` or Admin `0.1.0+32` artifacts end-to-end; that observation is historical
- **Related architecture:** [native OS integrations](../architecture/native-os-integrations.md), [sessions](../architecture/mobile-session-and-device-lifecycle.md), [private media](../architecture/documents-media-voice.md)

## Purpose and safety boundary

Use [generated version facts](../architecture/source-versions.generated.md)
for current source versions and the [current baseline](../current-baseline.md)
for separately dated execution and deployment observations.

Restore an interrupted native operation without crossing identity, account,
location, document or payment boundaries. Do not clear a protected financial
journal, bypass App Check, disable an installation restriction, force an
unverified upload into approved state, or replay an unknown-outcome mutation
just to remove a warning. Native callbacks are observations; the API remains
the authority for account binding, money, trip state, upload review and leases.

## Trigger and customer symptoms

Use this flow for first-install App Attest/Play Integrity rejection, secure
storage or journal corruption, cross-account callback, blank map,
picker/cropper route loss, stale/background GPS gap, deep-link/PayPal return
failure, or an interrupted native mutation. Record the user's safe support
code and approximate time, not tokens, coordinates, document paths or payment
payloads. An app crash, denied OS permission and provider outage are different
failure classes even when the screen looks identical.

## Preconditions and read-only diagnosis

Confirm authorization for the affected account/tenant and identify the exact
app (consumer or System Admin), signed build, OS, installation record,
environment and operation correlation. Use a hashed or internal reference in
restricted evidence, not a raw installation credential in this public runbook.

| Symptom | Read-only checks and decision point |
| --- | --- |
| First-install integrity rejection | Compare app identity/signing/profile and Firebase registration for the exact artifact; inspect sanitized App Check category and API verifier health. Distinguish token-invalid from verifier/network-unavailable and from an authoritative device restriction. |
| Secure-storage/journal warning | Check whether native read/write timed out, was cancelled before invocation, or could have completed late. Compare original operation/account scope and server status. A missing local value does not prove no external mutation. |
| Picker/cropper loses route | Check selected document type, route-mounted generation, native cancel versus crash, permission state and whether an upload reached quarantine. Do not use local path as a support identifier. |
| Background GPS gap | Check current trip/queue lease, permission and GPS service, native tracking observation, fix timestamp/accuracy, OS background policy and server sample acceptance. A screen marker is not proof of live upload. |
| Blank map or failed place search | Separate SDK tile rendering and signing restrictions from `/api/v1/maps/*` proxy response, network reachability and `maps_not_configured`. Preserve manually selected route state. |
| PayPal or deep-link return missing | Read the original server-owned payment/operation status and callback scope. Treat return URI as navigation only; no callback is not proof of no capture. |
| Cross-account callback | Compare recipient/account/tenant/role and callback generation to the current session. Quarantine stale observation; never present another account's entity. |

The [consumer attestation adapter](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/client/mobile/lib/core/platform_adapters/attestation_adapter.dart)
and [API verification boundary](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/server/KiloDrive.Api/Security/AppCheck/AppCheckProtection.cs)
are the source anchors for integrity classification. The
[native location bridge](https://github.com/KiloDriveApp/KiloDrive/blob/8bfe08881bce51535d1165552f2d5be8e05fc872/src/client/mobile/lib/core/location/active_trip_location_service.dart)
is the source anchor for exact trip/lease status.

## Contain and recover

1. Keep the affected protected action in a pending, outcome-unknown or manual
   review state until server/provider evidence resolves it. Allow safe reads
   where policy permits; do not imply a charge, upload or trip update was
   cancelled merely because its callback disappeared.
2. For a verifier outage, retry the same proof path with bounded backoff after
   service health recovers. For an invalid signed app/profile, route to release
   engineering for a corrected artifact. For a device restriction, require
   the established security review; never locally suppress it.
3. For native storage ambiguity, serialize a same-scope read after the prior
   native call settles. Reconcile with the original operation ID and API
   status. Corrupt data is preserved for restricted investigation; a new
   operation needs explicit evidence that no protected prior operation remains.
4. For a picker/cropper failure, retain the mounted form and document class;
   reopen only at user request. If an upload reached quarantine, poll its
   existing status and let the scanner/reviewer finish. Do not duplicate bytes
   solely because a UI route disappeared.
5. For a GPS gap, stop or mark stale as required by the current lease and
   server state. A fresh visible start requires permission, GPS service and a
   current lease. Do not backfill invented coordinates or extend a lease
   client-side. Escalate persistent screen-off gaps to the native release owner.
6. For Maps, validate the exact signed artifact's platform-key restrictions
   and the server proxy independently. Provide a manual location choice when
   the workflow supports it; do not loosen provider restrictions globally.
7. For link/return loss, re-read authoritative server status with the original
   operation. Do not mint a new payment operation or replay a mutation because
   an external app returned twice or not at all.

## Verify, abort and rollback

Verify the same account and tenant can re-enter the original route, that the
server record has one expected outcome, and that any native tracking or media
session ends when its owner/lease ends. Test foreground, background,
terminated and reinstall transitions separately on the exact signed build.
Abort automated recovery if the account scope differs, the provider outcome is
unknown, the protected store remains ambiguous, or a security ban is present.
Return to a read-only/manual-review state and escalate to the responsible
owner. Roll back only a release/configuration change through approved release
control; never rewrite an authoritative trip, payment or security record by
hand to match the UI.

## Evidence, privacy and follow-up

Retain sanitized category, support/correlation code, app/build, OS version,
environment, operation age, API status, permission state, native phase and the
tested lifecycle transition in restricted incident evidence. Exclude App Check
tokens, installation secrets, social credentials, precise location, private
documents, local file paths, PayPal payloads and customer identifiers from
public documentation. Notify the affected product/security owner when an
account-crossing or financial unknown outcome is suspected. Add a regression
for the observed transition, link the exact signed-device/provider evidence
in the certification matrix, and update this runbook only after the authority
and recovery decision are reviewed.
