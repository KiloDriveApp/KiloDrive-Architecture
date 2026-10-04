# Lists, pagination, caching and performance

[API Guide](README.md)

## Follow each endpoint's actual pagination contract

The API contains page-number collections and seek-paged histories. Parameter
names and response shapes are endpoint-specific; there is no universal
`offset`/`limit` contract. Read the reference entry and its response model.

| Example | Pagination model | Client rule |
| --- | --- | --- |
| Notification collection | `page`, `pageSize` | Use the returned page model |
| Notification history | `cursor`, `pageSize`, category and unread filters | Preserve opaque `nextCursor`; stop when `hasMore` is false |
| Wallet transactions | Collection parameters include continuation and page compatibility | Do not guess the continuation format |
| Wallet transaction history | Seek cursor plus range/search/timezone context | Reset the cursor when scope or filters change |
| Trip chat | Recorded parameters include time/sequence bounds and page size | Preserve ordering; deduplicate messages by identity/sequence |
| App releases | Page-number listing plus current/version/build reads | Use exact version/build routes when selecting a release |

Cursors are opaque, scope-bound state. They are not transferable bookmarks
between accounts, countries or filters. Do not decode/edit them, concatenate
one with different query parameters or retain them after an account switch.

Server queries must order deterministically before pagination. Client merging
must deduplicate by stable resource ID without reordering authoritative event
sequences. A new row arriving during a paged read should not silently produce
duplicates or skip older records.

## Historical rows versus current balances

Seek-paged wallet history freezes the row-set cutoff in the cursor. Current
wallet balances and aggregates come from their authoritative read endpoints.
A historical page is not a live balance calculation. Likewise, a trip event
page does not prove the current trip assignment or readiness state.

Refreshing a list starts a new read context. Returning from a detail screen
can preserve tab, filter and scroll state, while invalidating any cached data
affected by a successful mutation. Never preserve another account's dossier or
wallet merely to make navigation feel fast.

## Cache scope and freshness

Honor `Cache-Control` and applicable `Vary` headers. Do not invent a public cache
TTL for data marked `no-store`. Session state, private documents, wallet data,
operation recovery and mutable purchase quotes require particular care.

Published content and catalog information can use the configured cache boundary,
but currency/country/language/version must remain part of the key. Anonymous
country-dependent responses must not become one worldwide cached value.
Authenticated responses must never be stored in a shared public cache.

Client caches should be scoped by the data's account, tenant, country and
authorization generation. Logout, account change, device restriction, document
replacement and membership changes can invalidate previously visible data.
Do not use a cached approval or subscription to authorize a new mutation.

The website's root country redirect and page caching are website concerns;
they are not an API entitlement rule. See
[runtime boundary guidance](../architecture/runtime-boundaries-and-certification.md).

## Bounded refresh and realtime recovery

Realtime reduces latency but does not replace durable reads. When a stream
disconnects, use bounded refresh with backoff and refresh on meaningful lifecycle
events. Avoid a timer for every screen or repeated incoming-call checks when
signed out. Stop or pause protected work when the app lacks the required session,
permission or active workflow.

Refresh after notification deep links, returning from provider checkout and
successful administrative changes should read current server state. A push
payload should not overwrite a wallet balance or grant a plan locally.

## Measure the slow boundary

Distinguish DNS/TLS/edge delay, API execution, database query time, provider calls,
serialization, media transfer and client rendering. A slow response is not
automatically fixed by caching its entire payload. First determine whether the
data can be cached safely and whether a query, provider or repeated client
request is the real cause.

Use bounded page sizes, DTO projection, explicit outbound timeouts and scoped
cache invalidation. Do not hide a failed write behind stale data. The
[performance runbooks](../runbooks/README.md) and
[scaling chapter](../architecture/scaling-and-capacity.md) describe operational
measurement without publishing private production access details.
