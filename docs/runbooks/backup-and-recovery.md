# Backup and recovery runbook

- **Owner:** Database reliability, storage operations, and service recovery
- **Status:** Operational recovery procedure
- **Last exercised:** Not yet recorded in this public repository
- **Related architecture:** [Country cells](../architecture/tenancy-and-country-cells.md), [financial systems](../architecture/financial-systems.md), and [document storage](../architecture/documents-media-voice.md)

## Purpose and scope

This runbook explains how KiloDrive verifies backups, rehearses restores, and
recovers service after data loss or corruption. It covers the control database,
country cells, private object storage, key dependencies, release artifacts, and
the reconciliation work needed after a point-in-time restore.

A backup is not proven because a dashboard says “completed.” It is proven when
an authorized team can restore it into isolation, start the matching application
release, verify security and financial invariants, and account for the gap between
the recovery point and the incident.

## Owners and roles

| Role | Responsibility |
| --- | --- |
| Recovery lead | Declares recovery mode, owns sequence and go/no-go decisions |
| Database operator | Selects and restores control/cell snapshots and logs |
| Storage operator | Restores or verifies private objects, versions, holds, and lifecycle state |
| Security/key custodian | Authorizes use of encryption and signing-key recovery material |
| Financial owner | Reconciles provider outcomes, journals, wallets, holds, and cashouts |
| Privacy/legal owner | Protects holds, deletion tombstones, retention, and notification duties |
| Application owner | Supplies the matching immutable release and runs smoke tests |

Recovery should be performed by named people working from a timestamped incident
record. Do not let several operators independently “try fixes” against the same
damaged environment.

## Recovery objectives and data classes

The organization must approve a recovery point objective (RPO) and recovery time
objective (RTO) per class. This public runbook intentionally does not invent
numeric promises.

| Data class | Examples | Recovery concern |
| --- | --- | --- |
| Global identity/security | users, credentials, sessions, passkeys, 2FA, cell memberships | account control and global scope |
| Country financial truth | journals, wallet subledger, holds, payments, cashouts | balanced, immutable, provider-reconciled state |
| Operations/safety | trips, bids, chat metadata, location evidence, safety cases | chronology, participants, retention |
| Privacy orchestration | requests, checkpoints, holds, tombstones | deletions must not reappear after restore |
| Private objects | identity/vehicle documents, receipts, consented recordings | encryption, access audit, object/version lifecycle |
| Rebuildable runtime state | caches, presence, ephemeral maps data | recreate or expire; do not promote to truth |
| Release evidence | package hashes, schema/OpenAPI artifacts, IaC, runbooks | reproduce the software/data contract |

Valkey is normally reconstructible runtime state. MySQL and approved object
storage are durable truth. Restoring stale presence or lock state from a cache
snapshot can be more dangerous than starting empty.

## Preconditions

Before a restore or drill:

- identify the incident scope and desired recovery point in UTC;
- identify the immutable API/worker release compatible with that point;
- inventory control plus every dependent country cell;
- confirm backup integrity metadata and encryption-key availability;
- isolate the destination network/account from production providers;
- disable or fake outbound email, SMS, WhatsApp, push, payment, store, and voice
  adapters;
- prepare read-only reconciliation queries and fixture smoke tests; and
- agree how restored resources will be destroyed or promoted.

For production recovery, document which new writes will be blocked, queued, or
lost while restoration occurs. A technically successful restore can still cause
duplicate charges or reopened privacy records if this cutoff is vague.

## Safety and stop conditions

Stop and escalate when:

- the selected backup, encryption key, or integrity hash cannot be verified;
- control and country-cell recovery points are inconsistent beyond the approved
  tolerance;
- the destination could send real provider messages or payment calls;
- schema/package compatibility is unknown;
- a legal hold or completed deletion tombstone would be lost;
- an operator proposes direct balance edits, journal deletion, or replay of an
  unknown provider call;
- the restore target is not isolated or is ambiguously named; or
- production writes continue while the team assumes they are frozen.

Never copy plaintext secrets or customer exports into a convenient incident
folder. Never store key material beside the backups it decrypts. Never test a
restore by overwriting the only production copy.

## Routine backup assurance

Perform these checks on the approved schedule:

1. Confirm successful snapshots and point-in-time logs for `kilodrive_control`
   and every active or provisioned country cell.
2. Confirm the backup catalog records source role, UTC time, schema version,
   normalized fingerprint, encryption-key reference, size, and integrity hash.
3. Compare object counts and backup size against a bounded baseline. An unusually
   small “successful” backup needs investigation.
4. Verify encryption in transit and at rest, retention, immutability, and any
   cross-account or cross-region copy policy.
5. Verify restore roles are least-privilege and cannot alter source backups.
6. Verify private object versioning, lifecycle, quarantine, legal hold, and
   deletion policies match each content class.
7. Verify release packages, OpenAPI/schema artifacts, infrastructure definitions,
   and public-key history are recoverable independently of the live hosts.
8. Alert on missed, partial, late, unencrypted, integrity-failed, or never-tested
   backups.

Record backup health as metadata only; do not include database rows or object
names that expose customers.

## Isolated restore drill

Run drills often enough to meet the approved recovery policy and after material
storage/schema changes.

1. Open a drill record and choose a known UTC recovery point without consulting
   a precomputed “easy” answer.
2. Build an isolated destination with outbound providers denied by policy.
3. Restore control and the required country cells to mutually consistent points.
4. Restore or mount approved private-object recovery copies. Keep them private;
   do not make a bucket public for convenience.
5. Before running repair SQL, capture database versions, schema versions, and
   normalized fingerprints.
6. Start the exact compatible immutable application package with provider fakes.
7. Verify identity-to-cell membership and ensure no country identity is used as
   a credential authority.
8. Run journal balance, duplicate reference, wallet/subledger, held-fund,
   payment/provider, cashout, voucher, and membership reconciliation.
9. Verify outbox uniqueness and inspect work that would be replayed. Keep real
   outbound dispatch disabled.
10. Verify privacy holds, completed deletion tombstones, and country checkpoints.
11. Verify representative ride, delivery, rental, support, report, document, and
    authentication reads with non-user fixtures.
12. Measure actual RPO and RTO, document gaps, and obtain owner sign-off.
13. Retain sanitized evidence and securely destroy the drill environment.

The drill fails if the database restores but the matching API cannot become
ready, money cannot reconcile, private objects cannot be authorized, or restored
deleted identities become active.

## Production recovery procedure

### 1. Contain and choose the point

Declare incident command. Remove affected nodes from traffic, freeze or narrowly
disable writes, and preserve logs/metadata. Choose the recovery point based on
the last known-consistent data—not simply the newest snapshot.

Record the expected loss window and list external events that may have happened
after it: payment captures, refunds, store renewals, cashout provider actions,
notifications, document scans, and privacy deletions.

### 2. Restore durable truth

Restore control first only as required to establish global identity context;
restore country cells in the documented dependency sequence. Keep application
traffic blocked. Recompute fingerprints before applying any reviewed forward
alignment needed by the chosen binary.

Restore private objects according to content policy. Confirm encryption-key
access, object versions, legal holds, quarantine state, and signed-access behavior.

### 3. Reapply post-cutoff truth

Reapply privacy deletion tombstones and revocations before enabling account
access. Reconcile external provider events around the cutoff using stable provider
and business references. Import a known successful event idempotently; never
repeat a capture because its local row is missing.

Outbox items restored to `Pending` may run again. Prove handler and provider
idempotency before releasing workers. Quarantine unknown-result items for manual
reconciliation.

### 4. Validate in isolation

Start one canary node without public traffic. Run schema, identity, security,
financial, outbox, privacy, and representative lifecycle checks. Then enable
workers in a controlled order, observing queue and outbox lag.

### 5. Restore service gradually

Enable read traffic first where practical, then bounded writes and country cells
in an approved order. Keep cashout and other irreversible money movement disabled
until the [wallet reconciliation runbook](wallet-reconciliation.md) passes. Watch
at least two healthy monitoring windows before normal operation.

## Diagnosis guide

| Symptom | Likely issue | Next safe action |
| --- | --- | --- |
| Snapshot restores, API rejects schema | package/schema mismatch | capture fingerprints; use reviewed forward alignment on a clone first |
| Control users exist, country data is missing | inconsistent recovery points or missing cell | keep login/operations blocked; restore the matching cell |
| Journal balances, wallet snapshot differs | lost/duplicated post-cutoff subledger transition | trace earliest reference; prepare compensating domain repair |
| Provider says captured, payment row missing | external success after recovery point | import/finalize idempotently by provider reference; do not recapture |
| Deleted account becomes active | tombstone/checkpoint not reapplied | disable identity, reapply deletion orchestration, notify privacy owner |
| Documents return access errors | key, object version, quarantine, or ACL mismatch | keep private; validate key and signed-delivery path |
| Outbox backlog grows after start | repeated poison item, missing handler, or provider denial | pause affected handler; follow outbox recovery procedure |

## Rollback and aborting a recovery

If the recovery target fails validation, do not promote it. Preserve evidence,
destroy or isolate the failed target, and return to the last known-good serving
environment if that remains safe. Choose an earlier consistent recovery point or
correct the restore procedure in isolation.

Once new production writes have entered a restored environment, “rollback” is no
longer a file switch. It is a second data recovery with a new cutoff and must be
managed as such.

## Recovery verification

Before declaring recovery:

- control and every enabled cell have the intended schema fingerprint;
- API liveness/readiness and security boundaries pass;
- identity memberships, active sessions, and revocations are coherent;
- debit equals credit, wallet/subledger totals agree, and held funds reconcile;
- provider events around the cutoff are classified success/failure/unknown;
- restored outbox work is deduplicated or quarantined;
- privacy holds, deletion tombstones, and retention exceptions are present;
- private object access is signed, audited, and content-policy compliant;
- monitoring, backups, and the next scheduled backup are active; and
- customer/legal communications are approved where required.

## Evidence to retain

Retain incident/drill ID, roles, UTC timeline, selected recovery point, backup and
key references, integrity results, package hash, schema fingerprints, measured
RPO/RTO, reconciliation summaries, sanitized correlation/provider IDs, outbox
classification, privacy verification, smoke results, promotion/abort decision,
and preventive work.

Do not retain credentials, key material, customer rows, private document names,
message bodies, phone numbers, or access tokens in the evidence bundle.

## Escalation

Escalate immediately for key loss, suspected backup tampering, cross-tenant
exposure, unreconciled financial state, unrecoverable privacy tombstones, missing
legal-hold evidence, or a recovery point outside the approved RPO. The recovery
lead cannot unilaterally accept legal, security, or financial data loss.

## Common pitfalls

- Backing up only the default country cell and forgetting newly provisioned cells.
- Restoring the databases but not the key material needed to read protected data.
- Treating Valkey presence as durable truth and reviving stale online drivers.
- Enabling workers before classifying restored pending outbox messages.
- Replaying a payment webhook without first checking the provider outcome.
- Restoring deleted data without reapplying tombstones.
- Measuring recovery time only until MySQL starts, rather than until the service
  passes readiness and reconciliation.
- Keeping the only restore instructions inside the failed environment.
