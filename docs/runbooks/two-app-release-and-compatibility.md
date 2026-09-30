# Two-app mobile release and compatibility

- **Owner:** Consumer mobile, System Admin mobile, API, security and release leads
- **Status:** Public-safe decision procedure; not a record of a completed rollout
- **Last exercised:** Not yet recorded for a paired signed release in this public repository
- **Related architecture:** [Two-app architecture](../architecture/two-mobile-apps-and-security-2026-09-30.md)
- **Related:** [Mobile release](mobile-release.md),
  [testing and verification](../quality/testing-and-verification.md)

The consumer and System Admin apps are separate release products that share one
API and global identity authority. A new Admin binary does not mean old
consumer binaries have vanished. A clean source boundary does not by itself
prove store distribution, push routing, application attestation or operational
parity. This runbook keeps those questions separate and avoids production
targets, credential procedures and named private resources.

## Decision owners

| Owner | Decision to record |
| --- | --- |
| API/schema owner | Compatibility of current and previous clients, country-cell state, canonical contract and rollback |
| Consumer release owner | Consumer binary has no operative admin surface and preserves rider/driver journeys |
| Admin release owner | Required workspaces, permission denial, native identity and private distribution |
| Security/privacy reviewer | Session role separation, App Check, device bindings, sensitive displays and artifact redaction |
| Operations owner | Monitoring, alerts, outbox/provider recovery and incident response |
| Product/country owner | Which country and operator cohort may use each capability |

A release decision names one source revision, schema contract, API artifact and
signed app artifact per platform. The owner records where protected evidence is
stored; this public repo records the method and outcome category, not the
private artifact or credential.

## Compatibility matrix to complete before rollout

| Client and server pair | Required result |
| --- | --- |
| Current consumer against current API | Ordinary rider/driver/rental functions work; admin UI and acting context are absent from the source and final binary |
| Previous supported consumer against current API | Existing consumer journeys remain compatible; any legacy admin access follows separately reviewed server policy |
| Current Admin against current API | Authorized workspace/data/action paths work; denied actor/country/tenant paths fail safely |
| Earlier Admin build, if one remains supported, against current API | Additive contract changes do not misrender unknown states or permit stale mutations; otherwise mark this pairing not applicable |
| Consumer and Admin installed together | Separate credentials, native app identity, push routes, storage, logout and deep links |
| Both apps during API or country-cell degradation | Known restrictions stay enforced; partial reads do not invent money, permission or delivery success |

The source repository's route, wire-contract and capability inventories are
inputs to this matrix. They are not substitutes for running the pairings. A
new API field should be additive under `/api/v1`; a breaking change requires a
new major contract. Database evolution uses reviewed MySQL scripts and an
idempotent alignment path, not a runtime EF migration.

## Candidate preparation

1. Freeze a reviewed source revision for the app and API. Record the working
   tree decision. Regenerate owned contracts, localization and metadata before
   the final gate.
2. Run the repository's complete pre-push/build gates for both apps and the
   API/schema/contract checks. A focused green test cannot stand in for a
   failed full gate.
3. Build signed Android and iOS candidates through the approved per-app paths.
   Confirm distinct application identity, native configuration, entitlements,
   permissions, signing/profile, privacy declarations and store destination.
4. Record source revision, build number, artifact hash, toolchain, target store
   track, country/storefront and evidence bundle identity. Do not rebuild after
   testing and upload a different artifact under the same claim.
5. Reconcile the Admin workflow ledger against every release-required
   operation. Mark a missing action unavailable; do not fill a UI gap with raw
   JSON or an unguarded generic mutation.
6. Confirm a compatible API/schema deployment and a verified backup/recovery
   path before enrolling an operator cohort. An object fingerprint proves
   structure, not provider or country readiness.

## Signed-device certification

Use approved non-user fixtures on actual Android and iOS devices for the exact
candidate. Test both apps installed together; admin and consumer accounts,
including a dual-role administrator-rider; scoped/denied country and tenant
selection; login, refresh, logout, session revocation, installation restriction,
reinstall and account switch. Exercise app lock, secure storage, app/OS
backgrounding and process restoration independently on each platform.

For consequential Admin work, verify an allowed action, denied action, stale
revision, duplicate idempotency key, response loss and authoritative read-back.
For consumer billing, verify signed-store product discovery, purchase,
cancellation, interruption, renewal, refund and reconciliation. For
notifications, verify token registration and rotation, generic previews,
foreground/background/terminated tap checks and consumer/admin channel
isolation. Provider acceptance is not device receipt.

Each case records expected versus observed state, sanitized operation
reference, artifact hash, platform/OS, country, provider environment, test
fixture and reviewer. No private document, message body, purchase token,
credential or customer record belongs in a public evidence packet.

## Rollout order and go/no-go

1. Deploy only reviewed, backward-compatible schema/API changes. Verify
   readiness, country routing, permissions, audit and operational metrics.
2. Privately release the Admin app to a small authorized cohort. Observe
   sign-in, dashboard truth, scoped dossier access, alerts, outbox, financial
   recovery and session/device revocation.
3. Release the consumer app through its own stores/tracks after confirming
   ordinary journeys and the absence of privileged UI in the final binary.
4. Expand each cohort only when the support and operations owners can identify
   failures, reconcile unknown outcomes and restore the previous compatible
   state. Record the responsible person and review window in protected systems.
5. Treat any legacy-consumer-admin cutoff as a separate server policy change
   with its own authorization, compatibility, operator communication and
   rollback evidence. Removing source code from a new binary does not perform
   that cutoff for old installed apps.

Stop when a signed artifact cannot be tied to the tested revision; a high-risk
mutation lacks original-key recovery; a denied role can reach another scope; a
known restriction is bypassed; a notification can reveal a prior account's
content; a store/provider event grants the wrong entitlement; or an operator
cannot tell a committed financial outcome from an unknown one. A screen count
or passing analyzer does not override a stop condition.

## Rollback and incident handling

Stop cohort expansion or disable the affected capability first. Roll back the
client only to a build compatible with the deployed API; roll back the API only
after checking existing clients, schema and queued work. Do not reverse an
immutable ledger posting or delete audit/outbox records to make a dashboard
look clean. An interrupted financial or security operation is reconciled by
its original identity and server state before any retry. If app-channel,
session or recipient isolation is in doubt, contain the affected scope,
revoke affected sessions where appropriate and preserve sanitized evidence
for incident response.

## Completion record

| Evidence item | Must be attached to the decision |
| --- | --- |
| Source and contracts | Commit, app versions, API/Schema contract, generated-file and compatibility checks |
| Artifacts | Signed hashes for each platform, native identity and permission review |
| Workflows | Consumer critical journeys and Admin operation-by-operation disposition |
| Security | Allowed/denied roles, tenant/country boundaries, installation/session lifecycle and private-data review |
| Recovery | Duplicate, response-loss, process-death and authoritative read-back results |
| Providers | Store, push, payment and other configured provider observations where relevant |
| Operations | Health, alerts, support owner, rollback rehearsal and country/cohort approval |

The run is complete only when its named owners approve the exact candidate and
remaining exceptions are explicit. Historical screenshots or source tests are
useful context but cannot be relabelled as this candidate's signed-device
evidence. Continue with [API deployment](api-deployment.md) and
[security incident response](security-incident.md) for their distinct scopes.
