# Consumer workflow and documentation coverage: build 247

Reviewed 22 October 2026 against product source
`01b9e93f09ad02420145f5c0509e8e9248a88193`. The current authorities remain
consumer `1.0.0+247`, System Admin `0.1.0+49` and schema `2026.10.21.3`.
See [generated source facts](source-versions.generated.md) and the
[release chapter](release-1.0.0-247.md). This review does not imply a new app
release, schema migration, store approval or live certification of every path.

## Additional documented workflows

| Area | User procedure and boundaries | Product source reviewed |
| --- | --- | --- |
| Recurring rides | Route, category, fare, weekdays, pickup time, timezone and active schedule; inspect each generated request independently | `recurring_ride_form_screen.dart` |
| Split fares | Saved recipients, amount/percentage invitations, each payer's authorization; requester retains fallback liability | `fare_split_screen.dart` |
| Assisted travel | Optional practical assistance, boarding time and caregiver notifications; minimum trip-specific disclosure | `assisted_rider_profile_screen.dart` |
| Family/business profiles | Invitations, traveler/booker/manager roles, budgets, cost centers, notification permissions and statements | `travel_profiles_screen.dart`, `supervised_travel_conversation_screen.dart` |
| Wallet commerce | Recipient resolution, transfer outcome, top-up card purchase/redemption and safe handling of one-time voucher codes | `wallet_commerce_screen.dart` |
| Courier recurrence | Finite package-bidding schedules, fresh quotes, skip dates, pause and needs-review occurrences; no automatic offer acceptance or payment | `courier_series_screen.dart` |
| Courier amendments | Recipient/stop/time/payment changes, substitution and waiting require explicit agreement | `courier_amendment_screen.dart` |
| Merchant refunds | Actual goods refund, original receipt, evidence, recipient and requester review; distinct from service fare and tips | `courier_merchant_refund_screen.dart` |
| Driver business tools | Expenses, mileage, goals, availability, destination preference, private demand areas, queues and duty guidance | `driver_business_toolkit_screen.dart` |
| Vehicle care and discovery | Maintenance, calculators, personalization, reputation and support; storing a vehicle does not approve it for service | `vehicle_screen.dart`, calculator screens, `leaderboard_screen.dart` |

Source screen names refer to the consumer application's `lib` tree. Public
documentation describes available controls; country flags, authorization,
readiness, entitlement and provider health determine actual availability.
Forecasts and profitability are estimates, not guarantees or dispatch priority.

## Existing feature groups retained

The guides continue to cover registration/social-link recovery, independent
account/readiness/membership states, workspace switching, document and vehicle
onboarding, ride offers/pickup/journey/safety, courier shopping/custody/returns,
rental branches/policy profiles/qualification/reservations/bookings/receipts,
condition records and signatures, extensions/replacements/deposits/disputes,
provider teams, wallet funding/cashout, rewards/referrals, reports, privacy,
deactivation, deletion and uncertain-operation recovery.

Native-store subscription charges remain separate from wallet-funded services.
Rental Risk Exchange access uses the entity wallet and its governed allowance;
it does not reuse native Service Provider subscription products. Evidence
access must retain its domain authorization owner.

## Published manuals and verification

Edition 5.2 comprises a 91-page End User manual and a 130-page Transportation
Provider manual, retaining 22 and 31 full-page framed screenshots respectively.
The illustrated controls were reviewed against the adjacent instructions.
Older captured states remain dated examples; their values and navigation do not
override the currently installed application. No new UI images were fabricated.
Not every supported workflow has a current device screenshot.

The recheck found and replaced a local `file:` link that readers could not open.
The manual validator now rejects local-only reference links. Internal anchors,
PDF link annotations, images and pagination are checked during publication.
The 62 distinct public error-directory URLs used by the guides returned HTTP
200 during the review. They supplement 42 customer and 61 provider printed
error explanations; the guides do not reproduce the complete error catalogue.

Use the [manual library](https://kilodrive.com/manuals) for the current PDFs
and online readers, and the [error directory](https://kilodrive.com/help/codes)
for current code-specific guidance. Documentation correctness is distinct from
end-to-end testing of the underlying financial or safety operation.

## Release history reconciliation

Production read-only verification confirmed each requested source build
`246, 243, 242, 241, 240, 238, 237, 236, 235, 234, 233, 232, 231, 230, 225, 223`
has one successful consolidation event into build 247. The source records are
retained unpublished; build 225 was supplied twice and is merged once.
Build 247 has 308 detail cards. The
[public changelog](https://kilodrive.com/changelog/1.0.0/build/247?surface=mobile&platform=all)
is the customer-facing merged release. No duplicate merge was performed during
this recheck.
