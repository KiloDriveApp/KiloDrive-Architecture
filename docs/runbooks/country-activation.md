# Country activation runbook

- **Owner:** Country launch, platform, finance, safety, and legal owners
- **Status:** Operational launch gate
- **Last exercised:** Not yet recorded in this public repository
- **Related architecture:** [Tenancy and country cells](../architecture/tenancy-and-country-cells.md), [financial systems](../architecture/financial-systems.md), and [geospatial processing](../architecture/geospatial.md)

## Purpose and scope

Use this runbook when enabling KiloDrive operations in a new country or
reactivating a country after material rule, legal, provider, or schema changes.
It covers control metadata, the country cell, country-driven validation,
providers, money and safety approvals, fixtures, UI behavior, activation, and
rollback.

Showing a country in a sign-up dropdown is **not** country activation. Activation
means the complete operational chain can safely register people, validate local
evidence, quote and dispatch work, represent money and time correctly, deliver
support, and satisfy local obligations.

## Owners and decision rights

| Role | Responsibility |
| --- | --- |
| Country launch lead | Owns readiness matrix, schedule, and go/no-go decision |
| Database operator | Provisions and fingerprints the country cell and reference data |
| Product/domain owner | Confirms ride, delivery, rental, membership, and support behavior |
| Financial/legal owner | Approves money movement, KYC/AML, tax, retention, and disclosures |
| Safety/privacy owner | Approves emergency, evidence, consent, deletion, and escalation rules |
| Provider owner | Confirms availability, quotas, sender identities, fallbacks, and canaries |
| Localization/accessibility reviewer | Certifies local language, formats, and critical screens |
| Security reviewer | Confirms tenant scope, admin workspace, IAM, secrets, and audit controls |

No single technical operator should activate a country without the named
business, financial, safety, and legal approvals.

## Required country dossier

Create a reviewed, versioned dossier containing at least:

- ISO country and currency codes, currency minor-unit exponent, IANA timezone,
  measurement units, and supported languages;
- phone normalization, emergency number, driver-license format, plate format and
  display guidance, vehicle/document eligibility, and expiry rules;
- address/geospatial providers, bounds, map data, toll/reference data, and known
  route fixtures;
- bidding expiry, proximity expansion, background telemetry, duty, trust, fare,
  and cancellation policies;
- membership plans/terms, wallet/top-up/transfer/cashout permissions, KYC/AML
  tiers, limits, refunds, chargebacks, and reconciliation owner;
- tax, receipts, rentals, insurance, deposits, consumer disclosures, privacy,
  retention, deletion, and safety escalation requirements;
- messaging, payment, map, object-storage, voice, and store availability; and
- support hours, operator SLAs, incident contacts, and rollback owner.

Unknown values are blockers, not fields to copy from an existing country.

## Preconditions

- The country remains inactive for self-signup and new operations.
- A change record and launch owner exist.
- The canonical MySQL schema and all reviewed updates pass empty-bootstrap parity.
- A country cell can be provisioned without manual EF migration or ad-hoc DDL.
- Country rules are database-driven where the product requires operational
  control; mobile and portal clients do not contain a hidden conflicting rule.
- Dedicated non-user provider destinations and sandbox/fake payment state exist.
- Required translations, legal text, support procedures, and app/store regional
  settings are reviewed.
- Rollback preserves existing users' support, privacy, settlement, and safety
  access.

## Safety and stop conditions

Stop activation when:

- the control directory and cell registration disagree;
- the country cell fingerprint drifts from the approved contract;
- currency code/exponent or timezone is missing or falls back to another country;
- local validation rules are unreviewed, hardcoded inconsistently, or cannot be
  delivered to clients;
- a required provider is unavailable, still in sandbox, over quota, or lacks an
  approved sender/origination identity;
- money movement has no approved operating model or reconciliation owner;
- emergency, safety, privacy, deletion, or support escalation is undefined;
- fixtures require direct inconsistent row edits to become “ready”; or
- any test would contact a real user or move real money.

Do not solve activation drift by changing the expected fingerprint in
configuration. Do not clone bank, toll, license, insurance, or legal rules from a
nearby country merely because the language or currency seems similar.

## Activation procedure

### 1. Create inactive control metadata

Add the country directory entry, currency, timezone, display names, supported
languages, and feature posture while the activation flag remains off. Register a
stable rule-set version so API and clients can report what they consumed.

Verify an inactive country cannot be selected for self-signup or new operations,
but authorized system administrators can prepare it through an explicitly scoped
workspace.

### 2. Provision and prove the country cell

Provision from the canonical MySQL 8 schema using reviewed UTF-8 scripts. Apply
the alignment script twice on a disposable clone, then on the target cell through
the [schema alignment runbook](schema-alignment.md). Compare table, column, index,
foreign-key, collation, spatial, version, and normalized fingerprint metadata.

Register the shard as provisioned only after the fingerprint passes. Activation
must fail closed when the registered fingerprint and live cell drift.

### 3. Load and verify reference data

Seed only reviewed sources. Typical country-scoped data includes banks and
branches, payout rails, insurers/brokers, plate/license rules, emergency contacts,
holidays, toll periods/matrices, vehicle eligibility, and local limits.

For each data set, capture source, effective period, reviewer, encoding, natural
key, and idempotent update behavior. Rerunning the seed must update the intended
record without duplicating it. Reject Unicode replacement characters and verify
MySQL-to-API-to-client round trips.

### 4. Configure providers and infrastructure

Configure required providers through workload identity or protected secret
references. Verify country/region availability, spending and sending limits,
origination identity, template approvals, fallback order, timeouts, circuit
breakers, and support ownership.

Run scheduled canaries only after dedicated non-user destinations exist. Store
provider ID, latency, sanitized status, and correlation ID—never recipient,
message body, token, or payload.

### 5. Validate country rules through supported interfaces

Read active settings through the same API contracts used by Flutter and Portal.
Test valid, invalid, pasted, lowercase, whitespace, length, expiry, and
country-switch cases for license plates, driver licences, phone numbers, money,
distance, dates, and addresses. Confirm cache invalidation when a rule changes.

The server is authoritative. Client formatting helps the user, but must not be
the only enforcement.

### 6. Run deterministic lifecycle fixtures

Create dedicated non-user fixtures through supported fixture/admin APIs:

- system administrator with authorized country workspace and 2FA;
- verified rider;
- approved driver with verified licence, compliant assigned primary vehicle,
  active membership, fresh telemetry, no assignment, and `canBid=true`;
- rental organization owner and team members with distinct permissions;
- approved identity/vehicle evidence, wallets, payout methods, plans, and provider
  fakes; and
- active ride, delivery, rental, support, privacy, and report lifecycles.

Exercise registration, login, onboarding, quote, bidding, acceptance, chat,
arrival/start/complete/cancel, accounting, notifications, deletion, and admin
workflows. Clean up in `finally`; keep only sanitized correlation evidence.

### 7. Certify clients and operations

Verify Flutter, Portal, and Website use country-derived money, time, distance,
phone, license, plate, emergency, and legal data. Test cold start, offline cache,
country switch, 320 px screens, large text, dark/high contrast, keyboard/system
insets, and localized empty/error states.

Train support and operations using the same country rules. Confirm admins must
authenticate, complete required step-up, choose an authorized workspace, and
cannot expand scope with a forged header.

### 8. Obtain approval and activate gradually

Record technical, financial, legal, privacy, safety, provider, localization, and
support sign-offs. Set a rollback threshold for error rate, latency, provider
failure, outbox lag, reconciliation, and customer safety signals.

Activate during a controlled window. Start with bounded sign-up/operations where
the product supports it. Observe registration, eligibility, quotes, errors,
latency, queue/outbox lag, provider quotas, and reconciliation for at least two
healthy windows before declaring launch.

## Country-admin workspace verification

Test these authorization cases explicitly:

1. a global system administrator with no local user projection can list only
   countries assigned to that administrator;
2. after required 2FA, the administrator selects one country and proceeds;
3. API calls carry a validated acting-country context and are audit logged;
4. switching country changes data and formatting without leaking the previous
   country's cache;
5. a rider, driver, tenant admin, or modified client cannot access the system
   workspace; and
6. an unprovisioned, inactive, or fingerprint-drifted country cannot be entered.

## Diagnosis guide

| Symptom | Likely cause | Safe action |
| --- | --- | --- |
| Country appears but signup fails | activation state, shard registration, or validation contract mismatch | disable selection; compare control metadata and API rule response |
| API starts but country operations return errors | cell fingerprint/schema/reference gap | block country operations; run metadata comparison |
| Prices display in another currency | missing/stale `CurrencyContext` or fallback | stop financial actions; invalidate cache and verify country/profile context |
| Driver passes UI but cannot bid | licence/vehicle/membership/telemetry rule mismatch | inspect readiness assertion; do not bypass eligibility |
| Admin sees another country's data | acting-workspace authorization/cache leak | contain access, preserve audit, escalate security incident |
| Notifications fail only in new country | provider destination/sender/region/template restriction | disable channel or feature; inspect sanitized provider status |
| Toll names are corrupted | client/script/database encoding mismatch | keep estimates unavailable; repair reviewed UTF-8 seed idempotently |

## Recovery after correction

Correct the failed rule, reference data, provider setup, or application behavior
on disposable country fixtures first. Repeat schema/seed idempotency, provider
canaries, lifecycle tests, client country switching, and financial reconciliation.
Use a new reviewed rule-set or reference-data version so caches and audit evidence
can distinguish the correction from the failed launch. Reactivate only through
the complete approval and gradual-observation gate; do not flip the country back
on because one isolated request now succeeds.

## Rollback and deactivation

Rollback means stopping **new** risk while preserving duties to existing users.

1. Disable new signup and new ride/delivery/rental/financial operations for the
   country.
2. Keep support, safety, account access, privacy requests, required trip history,
   refunds, disputes, and settlement available as policy allows.
3. Drain or pause country workers/providers deliberately; do not abandon pending
   outbox or unknown payment outcomes.
4. Force stale online sessions offline and prevent new matching.
5. Reconcile wallets, holds, cashouts, store/provider events, and outbox.
6. Preserve the cell, audit, legal holds, and retention state. Never delete the
   database as rollback.
7. Correct the defect on clones, repeat the complete gate, and require renewed
   approval before reactivation.

## Verification and completion

Activation is complete only when:

- control metadata, shard registration, schema version, and cell fingerprint
  agree;
- country settings are read and enforced by API, Flutter, and Portal;
- no USD, timezone, unit, or validation rule leaks from another country;
- deterministic rider/driver/rental/admin fixtures pass and clean up;
- required provider canaries and failover tests pass;
- financial reconciliation reports no unexplained exception;
- country admin isolation and audit tests pass;
- monitoring, support, privacy, safety, and rollback coverage are active; and
- all named approvers sign the launch record.

## Evidence to retain

Retain dossier/rule-set version, source reviews, schema/seed fingerprints,
provider approvals and sanitized canary results, fixture correlation IDs and
cleanup, UI/localization evidence, money movement matrix, legal/safety/privacy
approvals, activation UTC time, monitoring baseline, rollback thresholds, and
owner names.

Do not retain credentials, fixture passwords, private phone/email destinations,
customer routes, payment tokens, or private documents.

## Escalation

Immediately escalate cross-country data exposure, money/currency misstatement,
wrong emergency guidance, missing retention/deletion handling, unapproved provider
messages, or an inability to disable new operations. Security, financial, legal,
or safety owners—not the launch operator alone—decide when those risks are closed.

## Common pitfalls

- Activating the dropdown before the cell and providers are ready.
- Copying Jamaica's rules into another country and planning to “fix them later.”
- Seeding a journey-level toll price when the calculator expects plaza-level
  traversal, or the reverse.
- Assuming a global admin needs a local country `Users` row.
- Allowing cached currency or country settings to survive workspace switching.
- Testing only happy-path registration and not money, deletion, safety, and admin
  isolation.
- Directly editing a fixture until `canBid=true`, hiding a broken lifecycle.
- Deleting an inactive country cell instead of preserving existing obligations.
