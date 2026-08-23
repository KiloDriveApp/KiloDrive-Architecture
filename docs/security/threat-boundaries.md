# Threat boundaries and review model

This is a practical threat model for engineers. It is organized around trust
boundaries because defects usually occur where one component assumes another has
already validated something.

## Assumptions

- Phones can be rooted, instrumented, automated, or running a modified APK.
- Browser JavaScript and hidden fields can be changed.
- Network requests can be replayed, delayed, duplicated, reordered, or dropped
  after the server commits.
- Providers can time out after accepting work.
- MySQL, Valkey, AWS services, and API nodes can restart independently.
- GPS may be inaccurate or deliberately falsified.
- User-supplied files may be malicious even when their extension looks normal.
- Operators and CI accounts are high-value targets.
- A UUID is an identifier, not an authorization secret.

## Boundary catalogue

| Boundary | Representative threats | Required controls | Failure posture |
| --- | --- | --- | --- |
| Internet → edge | scanning, DDoS, spoofed headers | TLS, WAF, trusted proxy list, bounded requests | reject/rate-limit |
| Edge → API | forged client IP, malformed request, header loss | proxy validation, correlation, security headers, validation | sanitized Problem Details |
| Client → identity | credential stuffing, token theft, takeover | short tokens, refresh families, 2FA, passkeys, rate limits | revoke/fail closed |
| Control → country cell | orphan projection, wrong country | durable saga, membership proof, reconciliation | incomplete checkpoint, no fake success |
| Tenant → tenant | IDOR, query-filter bypass | tenant context, ownership, explicit admin scope | coarse denial |
| API → Valkey | ACL denial, stale location, lost ceremony | TLS/ACL, namespace isolation, TTL, durable fallback where safe | degrade or fail closed by use |
| API → provider | secret leak, duplicate side effect, quota | workload identity, timeout, idempotency/reconciliation, outbox | durable retry or explicit unavailable |
| Upload → reviewer | malware, polyglot, public exposure | magic validation, quarantine, scan/CDR, private delivery | remain quarantined |
| SignalR/LiveKit | token logging, group escape, stale event | scoped short tokens, participant auth, redaction, entity version | resync/deny |
| Wallet → ledger | double spend, duplicate webhook, imbalance | row locks, idempotent references, double entry, reconciliation | cashout fail closed |
| Admin → global/country | overreach, wrong workspace, insider misuse | explicit permissions, country selection, step-up, audit | deny and alert |
| Build → stores | signing compromise, extra permissions/SDKs | protected keys, SBOM, binary scans, permission diff | stop release |

## Abuse stories worth testing

### Cross-user UUID attack

User A obtains or guesses User B's payout-method or document UUID and sends a
delete/view request. The query must include both resource ID and authorized owner
or participant. The response should not reveal that the foreign object exists.

### Lost-response replay

A wallet transfer commits, but the phone loses connectivity before receiving the
response. The retry uses the same idempotency key and payload hash and receives
the original result. A changed amount under that key is rejected.

### Stale ride acceptance

A driver bids, then goes offline, begins another assignment, loses compliance,
or changes vehicle before acceptance. The acceptance transaction locks relevant
state and revalidates eligibility. The old bid alone is not authorization.

### OTP account lockout

An attacker repeatedly submits wrong OTPs for a known email. Challenge attempts
expire/lock that challenge but do not increment the victim's password-login
failure counter.

### Social email takeover

A social token contains the same email as an existing account but lacks a
verified-email claim or explicit link ceremony. The API refuses automatic
linking and requires proof through the signed-in account or confirmation channel.

### Outbound token leakage

A social or hub token appears in a URL. Proxy access logs, Serilog request logs,
OTel URL attributes, and exception messages must all redact it. Tests search for
both the parameter name and a known synthetic secret.

### Scanner outage

ClamAV cannot respond. The upload stays private and pending; operations receives
a bounded alert. Nobody changes the row to clean to unblock a reviewer.

### Provider timeout after capture

A payment provider times out after capturing funds. The API records an unknown
outcome and reconciles the provider reference before any retry. It does not debit
the user twice or grant two entitlements.

### Valkey ACL misconfiguration

The connection authenticates but SignalR receives `NOPERM` on pub/sub channels.
Durable state remains queryable, clients use bounded refresh, and operators fix
only the required channel permissions instead of enabling all commands.

## STRIDE prompts for feature review

- **Spoofing:** Which identity, device, provider, or proxy claim could be forged?
- **Tampering:** Which state/version, amount, coordinates, or document metadata
  could the client change?
- **Repudiation:** Is the governed action durably audited with actor and time?
- **Information disclosure:** Can an error, URL, log, object key, or foreign UUID
  reveal private data?
- **Denial of service:** Can one user exhaust a provider quota, lock another
  account, create unbounded metric labels, or force expensive geospatial work?
- **Elevation of privilege:** Can a valid rider token reach an admin/driver route,
  or can an admin act in an unauthorized country?

## Security review evidence

A meaningful review includes:

- data-flow and trust-boundary diagram;
- route/policy/ownership matrix;
- state machine and concurrency/idempotency behavior;
- secret/IAM inventory without secret values;
- log/trace redaction tests;
- positive and negative integration tests;
- dependency/SBOM and native permission diff;
- recovery/rollback runbook; and
- named remaining risks with owners and dates.

## Public versus restricted detail

This public model deliberately omits exact firewall rules, private network
layout, resource identifiers, alarm thresholds, privileged recovery endpoints,
key locations, and incident contacts. Restricted operational documentation may
contain those details under access control. It should never contain plaintext
credentials either.
