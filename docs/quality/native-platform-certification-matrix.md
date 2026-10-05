# Native platform certification matrix

- **Owner:** Mobile release and provider-certification owners
- **Last verified:** 2026-10-05
- **Environment:** Documentation-only review of a modified product checkout; no app installed or provider event executed for this pass
- **Evidence:** [Source baseline](../current-baseline.md), [adapter inventory](../architecture/native-adapter-inventory.json), [generated scenario rows](native-platform-certification-matrix.csv)

The CSV is a scenario register, **not a pass report**. It expands each
applicable inventory capability across iOS/Android, foreground/background/
terminated/reinstall and, where relevant, sandbox/test versus production
provider context. Every current-source row is `untested` because this
documentation assignment did not execute an exact signed artifact. The
baseline link in each row records that limitation; it is not a test log.

| Evidence tier | What it can establish | What it cannot establish |
| --- | --- | --- |
| Source and configuration review | Interface, platform call, API boundary and intended recovery | Deployed configuration, actual provider response or native lifecycle |
| Host unit/widget/API test | Deterministic parsing, fencing and conditional transitions | App signing, OS callback delivery, StoreKit/Play sheet or audible presentation |
| Emulator/simulator | Selected OS integration and UI states | Physical-device radios, Focus/Doze, store review environment or push guarantee |
| Signed physical device plus provider | One exact build, OS, account and provider scenario observed | Other products, markets, lifecycle states, builds or production traffic |

Do not fill a `passed` row without a signed artifact identifier, provider
environment, UTC date, exact steps and restricted evidence link. A `failed`
row needs a defect/reference; `blocked` needs a concrete dependency and owner.
Do not use `blocked` merely because a scenario was not attempted. Inapplicable
platform combinations are omitted rather than mislabeled as failures.

## Priority exercise packets

1. On a signed iPhone: discover all six reviewed driver subscription terms,
   open each native sheet, distinguish cancellation from an unfinished charge,
   verify server entitlement and account binding, then exercise restart,
   renewal, upgrade/downgrade, refund and notification-history replay. Use the
   [StoreKit chapter](../architecture/native-adapters-and-store-billing.md).
2. On Play-installed signed Android: discover product/base plan/offer, verify
   licensed purchase, pending/acknowledgement, replacement, linked-token
   retirement, RTDN loss/replay and process-death recovery. Use the
   [Play chapter](../architecture/google-play-billing-native-adapter.md).
3. On both apps and OSs: fresh installation attestation/admission, logout and
   account switch, old push tap, token rotation, background/terminated
   notification receipt, actual sound/vibration, two-device call teardown,
   picker/cropper resume, screen-off trip location and PayPal return.

The historical [build-168 handover](../runbooks/build168-operational-handover.md)
and [2026-09-30 two-app checkpoint](../architecture/two-mobile-apps-and-security-2026-09-30.md)
retain their own dates and evidence. Neither is silently promoted to consumer
`1.0.0+192` or Admin `0.1.0+32` certification.

Regenerate the CSV with `python tools/native_handbook.py --write`, then run
`python tools/native_handbook.py` and `python tools/audit_docs.py` from this
repository. With a local product checkout, pass `--source-root` to verify the
captured versions, schema contract, OpenAPI hash and source-path references.
