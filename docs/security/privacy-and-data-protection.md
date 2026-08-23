# Privacy and data protection

Privacy begins before encryption. The first question is not “which key protects
this column?” but “does this component need the data at all?” KiloDrive separates
identity, country operations, transient telemetry, audit, provider attempts, and
private artifacts so each subsystem can receive the minimum it needs.

## Data map

| Data class | Why it exists | Typical owner | Special concern |
| --- | --- | --- | --- |
| Global identity | login, recovery, role/country membership | control plane | account takeover and global correlation |
| Country profile | local operations and compliance | country cell | tenant/country isolation |
| Precise location | pickup, matching, active trip safety | Valkey + country cell | physical safety and short useful life |
| Trip/delivery/rental | service lifecycle and evidence | country cell | participant privacy and legal retention |
| Wallet/accounting | balances, settlement, reconciliation | country cell | integrity and mandatory retention |
| Documents | licence, vehicle, ticket evidence | private object storage + metadata | identity theft and malware |
| Communications | notification attempts, chat, call state | country cell/provider | content sensitivity and consent |
| Voice recording | consented call evidence | private recording store | jurisdiction and legal hold |
| Audit | governed action accountability | control/country by action | privileged access and immutability |
| Telemetry | diagnose service behavior | observability systems | accidental payload collection |

## Location minimization

Fresh driver positions are high-frequency operational data. Valkey keeps a
short-lived location and GEO index for matching; MySQL receives asynchronous,
bounded breadcrumbs needed for an active trip, replay, safety, and approved
retention. We do not write every GPS callback to a permanent global table.

Samples include accuracy and time. Stale or poor-quality locations are not used
to represent a driver as nearby. Map matching reduces GPS noise, but the product
must be honest when confidence is insufficient.

Trip-sharing handles are opaque, high entropy, expiring, revocable, and rate
limited. Shared location is coarse, refreshed at a bounded interval, and expires
after the privacy TTL. A short numeric lookup code is not a sufficient secret.

## Documents and images

Identity and vehicle evidence is private and authorization-gated. New uploads
remain quarantined until type/magic validation and the fail-closed scanner approve
them. Identity evidence is delivered as an attachment or controlled viewer and is
never cached publicly.

Avatars and vehicle images use re-encoded thumbnails with removed metadata and
bounded dimensions. The original remains private. A revision-aware authenticated
cache is bound to the account and wiped on logout.

Review notes should be factual and necessary. Do not copy document numbers into
notification bodies, ticket subjects, or audit metadata just because the field is
available.

## Communications and recordings

Notification records store provider, safe provider ID, latency, template/status,
and correlation—not rendered bodies or destinations. Chat content is visible only
to authorized trip participants during the defined lifecycle, with a controlled
administrator investigation path where policy permits.

Voice recording is configurable by country. The user sees a recording state and
provides required consent before egress starts. Metadata records consent,
jurisdiction, timestamps, retention, deletion, and hold. Audio never enters
application logs.

Platform-mediated contact limits exposure of reusable phone numbers. Contact and
call channels close after trip completion/cancellation according to policy.

## Privacy orchestration across cells

A deletion request begins in the global privacy/support orchestration service. It
creates country execution checkpoints. Each country cell knows how to anonymize
or retain its local ride, financial, rental, and safety records. The orchestrator
does not perform a giant cross-shard transaction.

This makes failure visible: one cell can complete while another remains pending,
and the request is not declared finished until every required checkpoint has a
durable result. Retrying a checkpoint is idempotent.

Deletion is not synonymous with erasing legally required financial evidence. The
policy may retain an immutable journal while removing direct identifiers or
severing the profile link. Legal holds override ordinary expiry through an
audited, limited mechanism.

## Retention is a product feature

Every content class needs:

- purpose and lawful/contractual basis;
- collection trigger and user disclosure;
- storage owner and authorized roles;
- retention period and start event;
- archive/backup behavior;
- deletion/anonymization method;
- legal-hold behavior; and
- a tested restoration/deletion path.

Do not set a lifecycle rule without considering database metadata. Deleting an
S3 object while its document row says “available” produces a broken and
misleading user experience. State transitions and object operations reconcile.

## Store privacy and tracking declarations

Apple/Google privacy declarations must describe actual code and provider use.
Data used only to provide ride matching, safety, support, or account operation is
not automatically cross-company advertising tracking. If the app does not track
users under the platform definition, do not mark every collected data type as
tracking merely because it is collected.

Conversely, adding an advertising or attribution SDK can change the answer. Run
a dependency and binary permission/privacy diff on every release. Explain camera,
photo, location, microphone, and call use at the moment of the feature, and
respect denial without manipulative pre-permission flows.

## Telemetry privacy

Logs and traces may be copied, searched, exported, and retained differently from
the primary database. Keep them deliberately boring. Safe context includes a
bounded operation name, status, latency, deployment, provider, and correlation
ID. Avoid contact information, raw device IDs, arbitrary URLs, object keys,
precise coordinates, and serialized DTOs.

## Engineer's checklist

Before adding a field or provider:

1. Name the purpose and data class.
2. Decide whether an opaque surrogate is enough.
3. Identify control-plane or country-cell ownership.
4. Define consent/disclosure and access roles.
5. Define retention, deletion, backup, and hold.
6. Keep it out of object names and telemetry.
7. Add cross-user/cross-tenant authorization tests.
8. Update privacy labels, policy, manuals, and support tooling only after behavior
   is implemented and verified.
