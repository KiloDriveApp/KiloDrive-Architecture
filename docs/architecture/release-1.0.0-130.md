# Release 1.0.0 build 130 architecture update

Owner: KiloDrive Mobile, Membership, Financial Integrity and Release Engineering.
Last source review: 19 September 2026.
Environment: reviewed source and deterministic verification; not a claim of production deployment or store approval.
Evidence: [source-derived repository facts](https://github.com/KiloDriveApp/KiloDrive/blob/main/docs/generated/repository-facts.md), [source verification](https://github.com/KiloDriveApp/KiloDrive/blob/main/docs/releases/release-130-source-verification.md), and [product and operational doctrine](../governance/product-and-operational-doctrine.md).

| Fact | Value | Authority |
| --- | --- | --- |
| Mobile release | `1.0.0+130` | Flutter `pubspec.yaml` |
| Schema contract | `2026.09.19.2` | `SchemaContractOptions.CurrentVersion` |
| Public REST | `/api/v1` | reviewed OpenAPI v1 artifact |
| API inventory | 770 paths, 864 operations | source-generated repository facts |
| OpenAPI SHA-256 | `3040f0cf29a1541784846875ea6dffadb4f24fedf703086e6ad42cfdfdff33af` | reviewed artifact and sidecar |
| Languages | English, Spanish, French, Japanese, Simplified Chinese, Traditional Chinese | Flutter ARB configuration |

## Membership and financial truth

Membership is projected as current access plus an optional pending transition.
The transition records target plan, effective date, provider/source, revision,
cancellation and audit rather than overwriting present entitlement early.
Interrupted native purchase responses preserve the original operation and enter
an explicit checking/manual-review path. Provider event identity and KiloDrive
idempotency fence duplicate and out-of-order delivery.

Financial investigation uses a read-only evidence graph joining payment,
ledger, hold, cashout, provider event, membership period, receipt, notification
and review-case evidence. Reconciliation can report inconsistency; it cannot
edit balances. Corrections remain reviewed compensating postings.

## Operational readiness

The System Administrator readiness workspace separates four questions:

1. did the source and contract tests pass;
2. is required operational configuration present;
3. did the real provider/native boundary pass its certification matrix; and
4. is the current production dependency fresh and healthy.

Every check identifies its source, last success, freshness, owner, evidence and
one remediation. A feature-policy flag cannot turn missing credentials, stale
webhooks or unavailable native products into a certified capability. Secrets,
purchase tokens, keys, documents and personal data are excluded from the view.

## Mobile recovery boundaries

Membership, wallet, rental, chat, navigation and administration state is mapped
through typed models with neutral unknown-enum handling. Unsafe actions are
disabled when a future contract value cannot be understood. Chat replay uses a
monotonic checkpoint and merges realtime delivery with authoritative history so
a concurrent refresh cannot discard newer content.

## Evidence limits

Source, schema and automated tests do not prove store approval, licensed-store
discovery, provider delivery, physical-device lifecycle, production credentials
or current production health. The six changed ARB files are hash-bound but
pending qualified native review. Build 130 must not be described as production
certified until the named operational gates retain current positive evidence.
