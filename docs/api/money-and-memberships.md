# Wallets, FX, payments and memberships

[API Guide](README.md) · [Wallet reference](reference/wallets.md) ·
[Membership reference](reference/memberships.md)

## Different records answer different questions

| Record/read | What it means | What it does not prove |
| --- | --- | --- |
| Wallet | Current available/held breakdown and currency | A historical transaction page's total |
| Quote | Server-owned amount, fees, currency and applicable FX evidence | A committed purchase or transfer |
| Payment | Pending, captured, settled or other payment state | A notification was delivered |
| Ledger/journal | Durable movement and balancing evidence | The customer saw the UI result |
| Membership plan | Catalog benefits/pricing/eligibility definition | This user currently owns an entitlement |
| User membership/store status | Authoritative entitlement and billing/recovery state | The store configuration works in every country |
| Native store product | Product/offer information supplied by Apple or Google | A matching KiloDrive entitlement was granted |

Read current limits, fees and capability state before offering a financial
action. Recheck on the server at execution. Never authorize from a cached
balance, plan name, UI card or client-calculated price.

## Top-ups

Read `/api/v1/wallet/topup/limits` and the applicable quote before starting a
top-up. `POST /api/v1/wallet/topup` accepts `amountMinor`, provider and applicable
quote/context fields. The returned checkout or payment intent is not itself a
wallet credit.

PayPal capture/return and signed provider events reconcile a server-owned
payment. Use the owner's payment or PayPal operation status to discover the
result after returning from checkout. The client cannot mint balance from a
URL parameter or success screen. Sandbox and production evidence are different;
this guide supplies no live merchant or sandbox credentials.

Bank transfers remain pending until their authorized confirmation/rejection
workflow. Cancelling a bank-transfer intent and confirming receipt are different
operations. An uncertain result must be reconciled using the original operation,
payment and key, never by creating another credit.

## Transfers and cashouts

A wallet transfer uses the documented saved recipient reference and server
quote where applicable. Preserve the key, original payload and any recent
authentication proof requirements. Show the source amount, fees, recipient net
amount and currencies clearly. Do not imply that a same-currency and
cross-currency transfer have identical financial effects.

Cashout reads expose current limits and the applicable plan context. Saved
payout methods use protected owner-scoped CRUD; public presentation uses masked
destinations. Do not store raw bank information in an unrelated client cache,
log or notification. Requesting a cashout reserves value; approval, rejection,
provider dispatch and arrival are later facts. Provider arrival estimates are
estimates, not proof of settlement.

## Country-local prices and FX

Public membership-price discovery takes a `countryCode` and returns local
currency, plan amounts and quote time. The seven provisioned currencies are
listed in [country context](authorization-and-tenancy.md). USD base plan prices
are converted using reviewed authoritative FX data for the relevant country.

Do not publish a static converted price table as a permanent API guarantee.
Rate validity, activation, policy, country/cell consistency and catalog revision
can change. A public price response is informational; an executable purchase
uses the applicable validated quote and native/provider offer.

If reviewed pricing is unavailable, explain that dependency and disable the
purchase. Never replace missing FX with 1:1, a client estimate or an expired
cached amount. The native store's local currency/offer must match the reviewed
mapping and server reconciliation rules.

## Membership state and benefits

Plan catalogs describe benefit allotments, fees and allowed terms. User
membership reads describe status, start/expiry, usage and applicable revisions.
The driver's `/api/v1/driver/membership/store-status` is the authoritative
membership workspace snapshot; the client should not invent a competing
entitlement state by joining independent plan and billing reads.

Benefits and current usage are different values. Show the applicable active
plan, expiry and usage against its allotment. Expiry, a scheduled change, store
pending state and an administrative grant need distinct labels. A gold-colored
card is presentation, not authority.

Administrative plan creation/editing, benefits/prices, grants and expiry
management belong in the restricted Membership Center. Newly added paid plans
can remain inactive drafts until reviewed store mappings and country pricing
are configured. Removing a navigation link does not remove the underlying
capability. Public consumers cannot edit catalog benefits or grant themselves
membership.

## Wallet versus store purchase flows

The API includes wallet membership and provider/native-store workflows. They
are governed by platform, audience, policy and configuration. The existence of
a wallet subscription route does not authorize bypassing a platform's purchase
rules or substituting a wallet grant for a native-store entitlement.

Wallet purchase/renewal records the applicable payment and authoritative
membership. Upgrade credit/proration uses server rules and returned amounts.
An expiry extension does not automatically change the store's billing cycle.
Auto-renewal settings and cancel-pending-change actions use their own secure,
revisioned contracts.

## Native store lifecycle

Read the API product mapping and actual native localized offer. The reviewed
flow includes quote creation, durable preparation where applicable, native
purchase, server verification and entitlement/status reconciliation. Preparation
does not grant benefits. A purchase listener event must be validated before
entitlement is treated as active.

Google's documented flow includes server verification and acknowledgement after
delivery of the entitlement. Pending, cancelled, grace-period and expired states
have different meanings. See the
[official Play Billing integration guide](https://developer.android.com/google/play/billing/integrate).

Apple provides verified transaction/entitlement APIs through StoreKit; use the
appropriate transaction evidence and server reconciliation rather than assuming
a restored item is a new sale. See
[Apple's Transaction documentation](https://developer.apple.com/documentation/storekit/transaction).

KiloDrive restore and verify routes are distinct from a new purchase. Preserve
provider transaction ownership and environment. After an interruption, read the
existing store operation and membership state before initiating another charge.
Do not enter an endless restore loop or show a fresh purchase as the only
recovery path.

## Verification that matters

Test duplicate provider events, pending purchase, interrupted verification,
wrong account/environment/product, upgrades, deferred changes, expiry, refunds,
restoration and account switching. Confirm the wallet/journal and entitlement
agree and that notifications describe the resulting state. Native signed-build,
provider and store evidence remain separate from source tests.

Related: [financial systems](../architecture/financial-systems.md),
[authoritative FX](../architecture/authoritative-foreign-exchange.md) and
[store reconciliation](../runbooks/store-entitlement-reconciliation.md).
