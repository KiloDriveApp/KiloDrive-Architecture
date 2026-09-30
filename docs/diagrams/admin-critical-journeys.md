# System Admin critical journeys

These diagrams show trust and recovery boundaries, not private request formats
or a promise that every path is release-certified. The app is a presentation
client. The API validates the current actor, country, tenant, capability,
target and action proof; the owning database records durable state. `Receipt`
below means a scoped, human-readable result and support reference, never a raw
provider payload. See the [workflow map](../architecture/admin-workflow-contracts.md)
for current source status.

## Lock an account

The operator first reads the current account state. The confirmation explains
the consequence. The server owns the lock and session effects; a local badge
or disabled button is not proof that access was revoked.

```mermaid
sequenceDiagram
    actor Operator
    participant App as Admin app
    participant API as Authorized API
    participant Identity as Identity authority
    participant Audit as Audit/outbox
    Operator->>App: Open user security and review state
    App->>API: Scoped account read
    API->>Identity: Read current status and revision
    Identity-->>App: Authorized view via API
    Operator->>App: Confirm lock and provide required proof
    App->>API: Original operation key, target and precondition
    API->>API: Recheck actor, scope, proof and current state
    API->>Identity: Commit conditional lock and session effect
    API->>Audit: Record action and stage side effects
    API-->>App: Human-readable receipt
    App->>API: Fresh scoped status read
    API-->>App: Authoritative locked or review-needed state
```

If the response is lost, the app keeps the original operation identity and
checks status and account state. It must not send an unrelated second lock or
claim success from a local timeout. A conflicting account change calls for a
fresh review.

## Initiate password recovery

An administrator may start the established recovery ceremony for a permitted
account. They do not choose, receive or display a replacement password.

```mermaid
sequenceDiagram
    actor Operator
    participant App as Admin app
    participant API as Identity API
    participant Control as Central identity
    participant Worker as Delivery worker
    Operator->>App: Give reason and confirm recovery initiation
    App->>API: Scoped request with stable operation identity
    API->>API: Check actor, target, reason and current status
    API->>Control: Create or recover one expiring ceremony
    API->>Control: Audit initiation and stage delivery
    API-->>App: Receipt without secret or password
    Worker->>Control: Claim staged delivery
    Worker->>Worker: Attempt approved recipient channel
    App->>API: Read operation status if response was lost
```

Delivery acceptance, recipient possession and completion of the reset are
different facts. An old or expired ceremony cannot be represented as a
completed account recovery.

## Review a person's documents and readiness

The current mobile app can show scoped review metadata and some vehicle/driver
decisions. Private identity-document viewing and some decisions remain
unavailable in the separate app. This diagram makes that boundary visible
instead of implying a generic approve button exists.

```mermaid
sequenceDiagram
    actor Operator
    participant App as Admin app
    participant API as Scoped review API
    participant Cell as Country record
    participant Evidence as Private evidence service
    Operator->>App: Open person readiness
    App->>API: Load checklist and review metadata
    API->>Cell: Check current subject, documents and status
    Cell-->>App: Summary via API
    alt Reviewed mobile viewer and decision exist
        App->>API: Request permitted evidence/decision
        API->>Evidence: Recheck access and evidence state
        API->>Cell: Conditional decision and audit
        API-->>App: Fresh readiness result
    else Restricted path not yet migrated
        App-->>Operator: Action unavailable or approved secure handoff
    end
```

An upload, a scan result, an individual document approval and trip eligibility
are separate states. A withheld mobile decision remains withheld until its
permission, evidence, audit and recovery contract is reviewed.

## Decide a pending financial operation

Bank-transfer review and cashout decisions are distinct workflows. Both follow
the same response-loss rule: the key and original precondition belong to the
first attempt. The ledger or payment record, not the optimistic UI, decides
whether money moved.

```mermaid
sequenceDiagram
    actor Operator
    participant App as Admin app
    participant API as Financial API
    participant Cell as Country financial records
    participant Outbox as Provider/notification outbox
    Operator->>App: Review pending record and evidence
    App->>API: Scoped detail and current revision
    API->>Cell: Read payment, ledger and eligibility
    Operator->>App: Confirm reviewed decision
    App->>API: Frozen decision, original revision and key
    API->>API: Recheck grant, proof, state and duplicate claim
    API->>Cell: Conditional financial transaction and audit
    API->>Outbox: Stage durable external side effects
    API-->>App: Decision receipt or known conflict
    opt HTTP response is interrupted
        App->>API: Original-key status and scoped read-back
        API->>Cell: Reconcile authoritative result
        API-->>App: Applied, rejected, processing or review-needed
    end
```

The safe retry path may replay the *same* command with its original identity
only when the server contract proves that is appropriate. An unknown result
never authorizes a new financial mutation. Provider settlement and customer
notification have independent status after the transaction.

## Send an administrator notification

The reviewed exact-installation flow is conditional. A historical device-user
association or a visible row does not prove a current recipient. The text is
selected from approved templates rather than entered as arbitrary private
content.

```mermaid
sequenceDiagram
    actor Operator
    participant App as Admin app
    participant API as Notification API
    participant Control as Current binding and operation
    participant Worker as Dispatch worker
    participant Provider as Push provider
    Operator->>App: Select person, installation and template
    App->>API: Check current eligibility
    API->>Control: Verify user, session, app and installation binding
    API-->>App: Eligible or unavailable
    Operator->>App: Confirm purpose and send
    App->>API: Stable operation identity and reviewed template
    API->>Control: Recheck binding and stage audited send
    API-->>App: Queued receipt
    Worker->>Control: Recheck current binding before dispatch
    Worker->>Provider: Send allowed hint
    Provider-->>Worker: Accepted or rejected
    Worker->>Control: Record delivery attempt
    App->>API: Read scoped operation status
```

“Queued,” “accepted by provider,” “shown on device” and “read by recipient”
must not collapse into one success label. A platform without a reviewed safe
presenter stays unavailable. Admin alerts and consumer notifications use
separate channels and authorization on tap.

## Recover an outbox item

An outbox retry repeats delivery of a committed side effect. It does not
re-execute the trip, payment or account command that originally created it.

```mermaid
sequenceDiagram
    actor Operator
    participant App as Admin app
    participant API as Outbox API
    participant Store as Durable outbox
    participant Worker as Scoped worker
    Operator->>App: Inspect failure and prior attempts
    App->>API: Read scoped item and history
    API->>Store: Return current status and eligible action
    Operator->>App: Confirm retry or dismissal
    App->>API: Guarded action with stable operation key
    API->>Store: Conditional state change and audit
    API-->>App: Receipt
    Worker->>Store: Claim item under one tenant/country scope
    Worker->>Worker: Idempotent or reconciled side effect
    Worker->>Store: Record success or bounded failure
    App->>API: Refresh item and delivery history
```

If a retry response is lost, the app reads the same item and operation result.
Archive/retention policy may limit older history; an unavailable retained item
must not be misrepresented as a successful delivery.

## Review questions for every journey

For each actor role and selected country, test success, denied scope,
stale/revoked session, stale revision, duplicate key, interrupted response,
process restart, no-data state and a later independent read. Then test the
signed device and configured provider where the workflow depends on them. The
public diagrams omit private payloads, exact defensive rules and production
identifiers by design.
