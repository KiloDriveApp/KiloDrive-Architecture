# Consumer 1.0.0+247: rental discovery and recovery

Reviewed 22 October 2026 against product commit
`01b9e93f09ad02420145f5c0509e8e9248a88193`.
The schema contract remains `2026.10.21.3`; this release did not require a new
schema revision. [Source facts](source-versions.generated.md) distinguish the
current authorities from the historical curated public API export.

## Rental discovery and booking

Rental browsing no longer waits on the slow sequential country-directory path
before showing results. Published preview configuration is cached with
scope-aware checks. A failed refresh preserves existing vehicle rows and
provides retry feedback instead of replacing useful results.
Search, selected dates, branch maps, provider details and vehicle galleries
remain part of the customer journey. Availability and customer eligibility
are checked independently of whether a vehicle appears in search results.

Reusable rental policy and eligibility profiles define vehicle requirements,
rental duration, cancellation, collection, return and deposit treatment.
Booking confirmation, payment confirmation and vehicle handover are separate
states. Receipts and exception workflows retain their transaction identity;
unknown payment outcomes must be reconciled before another mutation.
See the [previous platform chapter](release-1.0.0-238.md) for the underlying
provider, courier, organization-team and rental architecture.

## Device admission and account recovery

Invalid device credentials use registration recovery without silently replacing
the installation identity. Push-token cleanup must not prevent a replacement
authenticated session. Account access, legal service readiness and membership
permission remain independent checks. Successful sign-in or a paid subscription
does not approve vehicle or identity evidence.

## Membership and financial boundaries

Service Provider Free, Silver and Gold cover configured ride, courier and rental
benefits. Published revision, beneficiary, service, term and reset window govern
allowances. Native-store offers determine the purchase price; wallet balances do
not renew these subscriptions. Restore and unknown-outcome recovery retain the
original transaction rather than creating a second charge. Country availability
and store approval require separate operational verification.

## Verification and limits

The release gate passed 7,106 consumer tests and 2,058 System Admin tests, with
both Flutter analyzers clean. Strict catalogue and locale structure checks
passed; this is not qualified linguistic approval.
Samsung checks exercised rental browsing, dates, search, maps, detail/gallery,
membership navigation, failed-refresh recovery and device credential recovery.
Catalog rows appeared in the first sub-second sampled frame after remediation;
this is a bounded observation, not a latency percentile or capacity guarantee.
The release AAB includes a later shared-error-notice adjustment covered by
automated tests; the installed APK and final AAB are distinct artifacts.

Complete store renewal/refund lifecycles, all rental exception paths, native
iOS behavior and sustained 50,000-user capacity remain separate certification
work. Android submission is not Google approval. An iOS build start is not
App Store Connect processing or TestFlight availability.

## Published documentation

The [website changelog](https://kilodrive.com/changelog/1.0.0/build/247?surface=mobile&platform=all)
consolidates the requested earlier releases while retaining internal history.
The [manual library](https://kilodrive.com/manuals) publishes the End User Manual
and Transportation Provider Operations Manual. The latter includes driver,
courier and rental-provider procedures. Edition 5 uses one framed screenshot
per illustrated page, task navigation and explicit recovery guidance.
Screenshots illustrate captured states, not certification of untested outcomes.
