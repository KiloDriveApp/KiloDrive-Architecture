# Threat Boundaries

## Primary boundaries

| Boundary | Representative threats | Architectural controls |
| --- | --- | --- |
| Public edge to API | abuse, spoofed proxy headers, injection, replay | trusted proxies, TLS, limits, validation, rate limiting, idempotency |
| Mobile/browser to identity | credential stuffing, token theft, account takeover | short tokens, rotation, step-up, passkeys, audit, revocation |
| Global identity to country cell | cross-cell confusion, partial registration | membership proof, durable saga, reconciler, credential-free projection |
| Tenant to tenant | IDOR and data leakage | tenant resolution, query filters, ownership checks, coarse errors |
| API to provider | secret leakage, timeout, duplicate side effects | workload identity, redaction, timeout, durable outbox, reconciliation |
| Upload to reviewer | malware, polyglot content, public exposure | type/magic checks, quarantine, scan/CDR, private storage |
| Realtime channel | token leakage, stale events, unauthorized subscription | scoped short token, participant checks, entity version, redacted proxy logs |
| Wallet/ledger | double spend, duplicate webhooks, imbalance | locks, idempotent references, double entry, reconciliation, fail-closed cashout |

## Assumptions

- User devices can be rooted, modified, or automated.
- Network calls can be delayed, repeated, reordered, or disconnected.
- Providers can return timeouts after accepting work.
- Database and cache nodes can restart independently.
- Operator accounts are high-value targets and require least privilege and 2FA.

## Exclusions from public detail

Exact alarm thresholds, network rules, internal resource names, privileged
procedures, incident contacts, key locations, and recovery credentials remain in
restricted operational documentation.
