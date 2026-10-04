# Authorization, tenancy and countries

[API Guide](README.md)

## Authority stays on the server

Authentication establishes who is calling. Authorization decides whether that
identity can perform this action on this resource in this country and tenant.
A valid JWT, a visible screen or a known UUID is not enough.

The reviewed API combines declared roles, feature/capability checks, resource
ownership and resolved tenant/country context. The OpenAPI records bearer and
selected role metadata; it cannot express every handler-level relationship or
policy. Clients should use the returned capability/readiness state for a useful
UI, while expecting the server to recheck the same action.

An organization member can have different authority from its owner. A rider
can view their own trips without gaining driver or fleet access. A driver can
read their own documents without gaining approval authority. Consumer sessions
do not acquire System Admin authority because the central identity also has
administrative responsibilities.

## Central identity and operational cells

KiloDrive maintains one central identity/security authority and country-local
operational graphs. The control database owns credentials, security ceremonies,
session families and country memberships. Country cells own trips, documents,
vehicles, wallets, payments, notifications, audit and outbox state.

Country `Users` records are credential-free projections for local domain
relationships. Registration/projecting into a cell is recoverable work, not a
distributed transaction that can be assumed to commit atomically. Client UI must
show the actual setup state if projection or onboarding is incomplete.

Authenticated tenant/country context is bound to signed session claims.
Anonymous tenant context comes from reviewed application-host mappings.
`X-Tenant` is not caller authority. `X-Country` can select applicable anonymous
country context where supported, but cannot change an ordinary authenticated
user's signed country. A legacy compatibility path is not permission to invent
a different tenant or cell.

## Country directory

The provisioned country model covers the following ISO currency pairs. Read the
current supported-country and capability endpoints for actual availability.

| Country | Code | Currency |
| --- | --- | --- |
| Jamaica | JM | JMD |
| Cayman Islands | KY | KYD |
| Barbados | BB | BBD |
| Trinidad and Tobago | TT | TTD |
| Bermuda | BM | BMD |
| United States | US | USD |
| Canada | CA | CAD |

A provisioned database, active country, published page, feature flag, reviewed
FX rate and store product are different readiness facts. Country support does
not establish that every payment, messaging, rental or safety dependency is
available there. The website's IP-based country routing chooses a public page;
it must not change an authenticated account's financial country or currency.

## Ownership and identifier rules

Externally exposed IDs are opaque identifiers. UUIDv7 helps ordering and
uniqueness; it does not encode permission. Never enumerate IDs, accept a client
`userId` as proof of ownership or trust an object found in an unscoped query.

Each tenant-scoped query retains the tenant filter. A deliberately broader
administrative path requires explicit authorized context and an audit record.
Those cross-workspace contracts are private. Operations intended for the
current user obtain identity from the authenticated principal instead of
allowing an arbitrary target account in the request.

Private document retrieval, trip chat/calls, receipts, support attachments and
outcome recovery must check the relevant participant/owner relationship.
Customer financial data and credentials must not flow through shared caches.

## Feature discovery versus action permission

`GET /api/v1/features` and public capability discovery help clients understand
which experiences can be offered. They do not override per-user readiness,
membership benefits, organization permissions, device restrictions, current
resource state or provider health.

If a feature becomes unavailable while a screen is open, refresh state and
explain the returned server reason. Preserve an interrupted operation for
reconciliation. Do not turn a disabled button back on locally, switch tenants
or send a different role header to evade the restriction.

Related: [country-cell architecture](../architecture/tenancy-and-country-cells.md),
[runtime boundaries](../architecture/runtime-boundaries-and-certification.md)
and [jurisdictional compliance](../architecture/jurisdictional-compliance.md).
