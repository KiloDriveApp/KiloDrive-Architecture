# Data Ownership, Retention, and Consistency

## Ownership comes before schema

Before adding a table, ask: **which boundary can make a complete decision about
this data?** The answer determines database placement, transaction scope,
retention, failover, authorization, and incident ownership.

KiloDrive's rule is simple to say and important to enforce:

- identity and cross-country coordination belong to the control plane;
- one country's operational and financial lifecycle belongs to that country
  cell;
- live acceleration state belongs in Valkey with a TTL; and
- large private bytes belong in object storage, with ownership and scan state in
  a database.

## Detailed ownership matrix

| Data class | Authority | Why it lives there | Consistency expectation |
| --- | --- | --- | --- |
| Passwords, refresh tokens, resets, recovery, MFA, passkeys, social identities | Control database | One global security boundary per identity | Strong within control transaction |
| Country/tenant workspace authorization | Control database | Prevents a cell projection from granting login authority | Strong control state; projection eventual |
| Global security events and System Admin grants | Control database | Cross-country account/security governance | Append-oriented, strongly recorded |
| Supported-country and shard directory | Control database | One routing/activation authority | Strong and deployment-governed |
| Provisional registrations and projection saga | Control database | Durable cross-store coordination before workspace activation | Eventual cell convergence; inactive until complete |
| Country user projection | Country cell | Local foreign keys and display without secrets | Idempotent projection from control |
| Driver/vehicle/licence operations | Country cell | Country rules and trip eligibility are local | Strong local transaction; global compliance projection eventual where needed |
| Rides, bids, trips, chat, ratings, safety | Country cell | One local lifecycle and participant boundary | Strong state transitions; realtime eventual delivery |
| Deliveries and escrow | Country cell | Hold/release/refund must share wallet transaction | Strong local financial transaction |
| Rental organizations, fleet, bookings, disputes | Country cell | Local team permission, asset, evidence, and settlement graph | Strong transition transaction |
| Wallets, transfers, payments, cashouts, journals | Country cell | No distributed money commit | Strong local transaction and reconciliation |
| Notification and outbox rows | Owning country cell | Side effects must be coupled to local business commit | At-least-once processing, idempotent effects |
| Global support ticket conversation | Control database | One support entry point across workspaces/countries | Strong ticket/message writes; local investigation by references |
| Account deletion orchestration | Control database | Coordinates every country checkpoint | Eventual completion with durable checkpoints |
| Country trip/financial anonymization | Country cell | Local retention and accounting law | Cell-local governed execution |
| Current driver location and GEO candidates | Valkey | High write rate, short-lived presence, multi-node lookup | Eventual/ephemeral with TTL |
| Trip replay samples | Country cell | Durable trip/safety evidence | Batched, deduplicated persistence |
| Trip summary distance and provenance | Country cell | Historical route/telemetry fact belongs to the trip | Strong snapshot; legacy unavailable unless authoritative evidence exists |
| Identity documents and attachments | Private object storage plus control/cell metadata by content class | Bytes do not belong in relational/web roots; metadata carries authorization and scan status | Object and metadata coordinated; quarantined until clean |
| Provider identifiers/status | Owning local operation or global provider-health store | Reconciliation and operational health | Provider-event eventual, idempotent |
| Calculators/reference catalogues | Control or cell according to scope | Universal data once; country rules locally where regulated | Versioned/effective-dated where prices change |

## Three kinds of consistency

### Strong consistency inside one aggregate transaction

Use one local database transaction when correctness requires all-or-nothing:

- accept one bid and create one trip;
- hold delivery fare and record escrow;
- debit one wallet, credit another, and post the journal;
- transition a rental booking and capture its immutable snapshot; or
- change domain state and stage its outbox message.

Keep the transaction short. No network provider belongs between `BEGIN` and
`COMMIT`.

### Eventual consistency across stores

Global identity creation and country projection cannot share a normal atomic
transaction. KiloDrive uses a durable saga with status, lease, attempt count,
next-attempt time, and an inactive membership. The reconciliation worker can
observe exactly which part exists and apply only what is missing.

The user sees a truthful pending state until the projection is complete. That is
better than authenticating into a country where the wallet or role aggregate is
absent.

### Ephemeral consistency for presence

Current location and connection presence change quickly and can disappear. A
Valkey value with a TTL is appropriate. Durable decisions still recheck MySQL
state and freshness, while safety/replay evidence is persisted separately.

## The dual-write trap

This sequence is unsafe:

```text
save global user
save country user
return success
```

If the process dies between saves, the account is half-created. Wrapping two EF
contexts in `TransactionScope` does not create the reliable, observable,
cloud-friendly contract the system needs.

A durable orchestration row fixes the reasoning:

```text
control transaction:
  identity + inactive membership + saga checkpoint

cell operation:
  idempotently ensure projection aggregates

control completion:
  activate membership + complete saga
```

Every step can be retried or inspected. Compensation happens only after proving
the cell side is absent.

## Financial ownership and escrow

Money does not live in `kilodrive_control`. Even when a global product catalogue
defines a product, purchase, balance, entitlement application, settlement, and
accounting for a country transaction remain in that country cell.

For wallet movement, KiloDrive keeps two complementary views:

- `WalletTransactions` are the user's operational subledger.
- `AccountingJournalEntries` and their lines are the immutable platform
  double-entry record.

Both use deterministic references. Reconciliation compares them and can fail
closed for cashout when money is unexplained.

Held balances are explicit. A delivery acceptance does not merely “remember”
that some money should be unavailable; it moves the amount from available to
held and records the escrow reference. Completion releases it to settlement;
cancellation refunds it. A failed notification cannot change that outcome.

## Outbox ownership

An outbox message belongs in the same database transaction as the state that
caused it. A Jamaica ride change creates its durable event in the Jamaica cell,
not in the control plane or a process-memory queue.

Processing is at least once. The worker may crash after the provider accepts a
request but before the row is marked complete. Each handler therefore needs a
stable local/provider idempotency reference or an unknown-result reconciliation
step.

External EventBridge/SQS dispatch can increase throughput and isolation, but the
SQL outbox remains the recovery path and source of durable intent. A bus publish
failure should be visible and recoverable, not silently discard the ride event.

## Object storage ownership

The bytes and the authority to read them are separate concerns.

- Object storage keeps the private bytes encrypted and non-public.
- A database record identifies owner, tenant/country, content class, media type,
  safe original name, hash, scan status, and review relationship.
- The upload remains quarantined until a trusted signed scanner result says
  clean.
- Raster images are re-encoded to strip metadata before final storage.
- Download endpoints re-check role/ownership and emit no-store/attachment
  headers appropriate to the content class.

Never make a bucket public to fix an image-loading problem. Fix the authorized
delivery path or thumbnail workflow.

## Deletion and anonymization

“Delete my account” is not one SQL `DELETE` statement. It is a global case with
country-specific execution checkpoints.

1. The control plane receives and audits the request.
2. It identifies the active country memberships/cells.
3. Each cell performs permitted local anonymization and records completion.
4. Financial, tax, dispute, or safety evidence is retained only where policy or
   legal hold requires it, with direct identifiers minimized.
5. Private objects are deleted, anonymized, or held according to content class.
6. The global identity is disabled/anonymized after required checkpoints reach a
   terminal state.

The control plane coordinates; it does not pull country financial rows into a
global deletion transaction.

## Retention by content class

Retention needs a reason, not a single platform-wide number.

| Content | Typical driver of retention | Correct removal shape |
| --- | --- | --- |
| Authentication/session state | Security and account lifecycle | Revoke/expire, then purge under security policy |
| Security audit | Incident response and compliance | Append-oriented with governed archival/anonymization |
| Trip/business record | Contract, support, dispute, local law | Retain core fact; minimize personal detail when permitted |
| Accounting journal | Financial/legal integrity | Immutable; reverse errors, never edit/delete casually |
| Raw/current location | Operational purpose and privacy | Short TTL for live state |
| Trip replay sample | Safety, dispute, training policy | Time-bounded deletion unless held |
| Identity document | Verification and legal policy | Private, purpose-limited, delete after approved period/hold |
| Support attachment | Case and legal-hold policy | Delete with case policy; never public cache |
| Completed outbox row | Recovery evidence | Archive after configured retention, then purge safely |
| Provider canary result | Operations trend | Retain sanitized status/latency only |

Do not encode public retention promises from implementation defaults alone. A
configuration clamp is not a legal policy approval.

## Data movement between boundaries

### Control to cell

Allowed examples:

- credential-free identity/profile projection;
- active country membership details;
- idempotent compliance version/hash changes; and
- authorized global product/reference definitions needed locally.

Never copy:

- password hashes;
- TOTP secrets or recovery codes;
- refresh tokens or passkey ceremony state;
- raw global security evidence unrelated to local operations; or
- a wallet balance from another cell.

### Cell to control

Allowed examples:

- coarse checkpoint/result for a deletion or verification orchestration;
- global admin notification metadata;
- sanitized status needed for directory/workspace readiness; and
- an idempotent compliance projection.

Avoid turning the control plane into a second copy of every trip or payment. It
increases breach scope and makes authority ambiguous.

### API to telemetry

Export operation, duration, status, bounded counts, and correlation. Do not
export message bodies, document contents, phone numbers, emails, access tokens,
precise coordinates, or arbitrary JSON payloads.

## Failure scenarios

### Control is available, country cell is unavailable

Authentication may still be evaluated, but entering or mutating the affected
workspace must fail honestly. Do not route the user to a different country's
cell or create a shadow wallet in control.

### Country cell is available, control is unavailable

Existing short-lived access tokens may validate cryptographically, but security
state that requires control-plane lookup cannot be invented. Sensitive account
operations fail closed; bounded local operations follow the approved outage
policy.

### Cell write succeeds, realtime delivery fails

The outbox retries. Clients poll/refresh the versioned entity. The business
operation remains committed.

### Object upload succeeds, metadata save fails

The workflow deletes the just-uploaded object or records it for orphan cleanup.
Never leave an unowned private object indefinitely.

### Valkey is lost

Live candidate and backplane behavior degrades. MySQL remains authoritative;
online presence expires, and the service avoids claiming a stale driver is
nearby. Rebuild ephemeral indexes from fresh heartbeats, not old trip history.

## Anti-patterns we have learned to avoid

- Cross-cell SQL joins in request handlers.
- Saving two contexts sequentially without a durable checkpoint.
- Putting wallet balance or trip history in the control database for
  convenience.
- Treating `IgnoreQueryFilters()` as an admin authorization mechanism.
- Copying credentials into the country `Users` projection.
- Using a queue without an outbox and calling it “eventual consistency.”
- Deleting financial rows to make reconciliation green.
- Logging provider payloads to debug a timeout.
- Retaining live location forever because storage is cheap.
- Making private documents public so the portal can render them.

## Feature-design worksheet

For each new entity or workflow, record:

1. **Authority:** control, one country cell, Valkey, object storage, or provider?
2. **Tenant:** global, tenant-scoped, organization-scoped, or user-owned?
3. **Transaction:** which rows must commit together?
4. **Cross-boundary projection:** what is the minimum derived data, and what
   durable checkpoint makes it retryable?
5. **Idempotency and concurrency:** which key prevents replay and which version
   prevents stale state?
6. **Retention:** why is it kept, for how long, and what can a legal hold change?
7. **Audit:** actor, action, subject, outcome, time, and correlation—without
   payload/PII leakage?
8. **Outage behavior:** fail closed, retry durably, or degrade honestly?
9. **Recovery owner:** which team/runbook verifies convergence?
10. **Tests:** partial write, process crash, duplicate event, two tenants, two
    cells, deletion, and restore?

## Related reading

- [Database architecture](README.md)
- [Schema lifecycle](schema-lifecycle.md)
- [Tenancy and country cells](../architecture/tenancy-and-country-cells.md)
- [Country-cell sharding ADR](../adr/001-country-cell-sharding.md)
- [Valkey geospatial-state ADR](../adr/003-valkey-geospatial-state.md)
