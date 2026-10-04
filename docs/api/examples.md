# Synthetic API examples

[API Guide](README.md)

These examples explain contract structure. The host `api.example.invalid` has
no live service, and angle-bracket values are deliberate placeholders. They
are not credentials, valid record IDs or production targets. Use only an
approved environment and authorized synthetic accounts for actual testing.

## Read public membership prices

```http
GET /api/v1/public/membership-prices?countryCode=JM HTTP/1.1
Host: api.example.invalid
Accept: application/json
```

This requests Jamaica's informational price view. The response model contains
`countryCode`, `currency`, `quotedAtUtc` and `plans`. Each plan's fields are
defined in the [field dictionary](schemas/p.md#publicmembershipplanpricedto).
The request does not buy a plan, fix an exchange rate forever or establish
native-store product readiness.

## Sign in through the established ceremony

```http
POST /api/v1/auth/login HTTP/1.1
Host: api.example.invalid
Content-Type: application/json
X-KiloDrive-App: consumer
X-KiloDrive-Device: <admitted-installation-credential>

{
  "identifier": "<authorized-test-identifier>",
  "password": "<private-test-password>"
}
```

Applicable attestation and truthful platform/build metadata are additional
prerequisites, not supplied by this example. Inspect `requiresTwoFactor` and
the returned ceremony state. Only a completed `auth` result supplies the final
session. Never log the password, ticket or returned tokens.

## Read the current wallet

```http
GET /api/v1/wallet HTTP/1.1
Host: api.example.invalid
Authorization: Bearer <access-token>
X-KiloDrive-Device: <admitted-installation-credential>
Accept: application/json
```

An illustrative fragment of the documented wallet model is:

```json
{
  "balanceMinor": 100000,
  "heldBalanceMinor": 0,
  "currency": "USD",
  "updatedAtUtc": "2026-10-03T12:00:00Z",
  "revision": 7
}
```

This is a fragment, not a claim about an actual account. `100000` displays as
`USD 1,000.00` for the illustrated two-decimal currency. Use the full returned
amount breakdown when deciding which funds are available. The timestamp is an
instant; local display depends on the user's configured timezone/format.

## Submit a transfer using the real field names

```http
POST /api/v1/wallet/transfers HTTP/1.1
Host: api.example.invalid
Authorization: Bearer <access-token>
X-KiloDrive-Device: <admitted-installation-credential>
Idempotency-Key: <persisted-original-operation-key>
Content-Type: application/json

{
  "recipientFavoriteId": "<authorized-saved-recipient-uuid>",
  "amountMinor": 10000,
  "note": "Synthetic workflow example"
}
```

The placeholder UUID must be replaced in an approved test with a real
authorized saved recipient reference. A cross-currency operation can also
require the appropriate `fxQuoteToken`. Where the server requires recent
authentication, complete that ceremony and supply the declared proof header.
The example does not omit those rules; it cannot provide private proof values.

Persist this request's original account/country, path, payload and key before
sending. A button label of “retry” must not create another key after an unknown
outcome.

## Discover an interrupted command's outcome

```http
GET /api/v1/operations/status HTTP/1.1
Host: api.example.invalid
Authorization: Bearer <access-token>
X-KiloDrive-Device: <admitted-installation-credential>
Idempotency-Key: <persisted-original-operation-key>
Accept: application/json
```

The original key stays in a header. The response uses `MoneyCommandRecoveryDto`
with numeric `outcome`, optional `responseStatusCode` and `noMutation` proof.
Interpret values using [safe recovery](errors-and-recovery.md). A missing record
is not proof that the original transfer did nothing.

If replay is explicitly permitted, resend the original mutation unchanged.
If the server reports processing, wait and refresh. If it reports succeeded,
refresh the wallet/history and show the result. If the outcome needs review,
keep it visible and use authorized reconciliation rather than starting a second
transfer.

## Use a revision for a new membership edit

The driver membership purchase contract declares `If-Match` and idempotency
requirements. Read the membership state first. For an illustrative strong ETag
`"7"`, the mutation sends:

```http
If-Match: "7"
Idempotency-Key: <persisted-membership-operation-key>
```

Do not substitute a current timestamp or the app's build number. If the response
is interrupted, keep that original ETag for reconciliation/replay. If a known
conflict requires a new deliberate edit, refresh and construct a new operation
after resolving the earlier result.

## Read a notification history page

```http
GET /api/v1/notifications/history?category=all&unreadOnly=false HTTP/1.1
Host: api.example.invalid
Authorization: Bearer <access-token>
X-KiloDrive-Device: <admitted-installation-credential>
```

The model has `items`, `pageSize`, `hasMore`, `nextCursor` and `unreadCount`.
For the next page, send the opaque cursor without changing account or filter
context. Reset it on a filter/account switch. A notification row records its
own delivery/read state; it does not prove a financial command succeeded.

## Interpret an error without exposing evidence

```json
{
  "code": "idempotency_in_progress",
  "supportCode": "<server-support-code>",
  "outcome": "<server-outcome>",
  "safeAction": "<server-safe-action>",
  "correlationId": "<safe-correlation-reference>"
}
```

This demonstrates selected enriched fields, not a complete universal error
envelope. Preserve safe support/correlation context and honor any `Retry-After`
header. Do not attach the bearer token, original private payload, document bytes
or provider receipt to a public issue.
