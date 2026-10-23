# Consumer 1.0.0+248 — workflows, manuals and country operating policies

Reviewed 23 October 2026. Consumer source is `1.0.0+248`, System Admin remains
`0.1.0+49`, and the schema contract remains `2026.10.21.3`. Version authorities
match product commit `3630d1c33b03577c7770664f3f7c3f49422cea17`.
The country-policy API change is a separately deployed working-tree package;
that source commit is not claimed to contain it. Store approval and device
certification are independent of source, publication and runtime readiness.

## Customer and provider workflows

The current guides cover customer, driver, courier and rental-provider tasks:
registration and recovery, workspace-specific navigation, identity and licence
readiness, Service Provider membership, native-store recovery, ride offers,
journey safety, courier custody and shopping, and rental qualification,
reservations, payment, collection, return, refund and disputes. Payment
confirmation remains separate from vehicle handover. Rental agencies can
record external payment/refund evidence or use the wallet settlement path.
An unexplained disabled booking control is not acceptable recovery guidance:
dates, quote expiry, handoff choice, identity and driving eligibility are
separate conditions.

Two manuals replace the separate rider, driver and rental-entity books:

| Manual, edition 5.7 | Pages | Full-page framed screenshots |
| --- | ---: | ---: |
| End User Manual | 128 | 56 |
| Transportation Provider Operations Manual | 177 | 75 |

Each illustrated page has one screenshot. Captions retain the actual capture
build and date; illustrations are not relabelled as fresh build-248 tests.
The provider manual includes driver, courier and rental-entity instructions.
Both include feature directories, workflow instructions, error guidance,
recovery paths and links to the current public code directory. The publication
checks validate source anchors, assets, PDF links, page counts, text overflow,
canonical hashes and old download aliases.

Use the [online manual library](https://kilodrive.com/manuals),
[End User PDF](https://kilodrive-public.s3.us-east-1.amazonaws.com/Manuals/KiloDrive-End-User-Manual.pdf)
and [Transportation Provider PDF](https://kilodrive-public.s3.us-east-1.amazonaws.com/Manuals/KiloDrive-Transportation-Provider-Operations-Manual.pdf).

## Country policy release 2026.10.23.1

The main tenants in Jamaica, Cayman Islands, Barbados, Trinidad and Tobago,
Bermuda, United States and Canada received the owner-approved policy release.
This is database/configuration publication using the existing schema; no
account reset or fabricated legal acceptance is involved.

| Capability | Implemented operating behaviour |
| --- | --- |
| Loyalty points | Five points per qualifying completed customer ride or courier request; 25 for a qualified referral. Ten points have a reference value of one US cent. Default conversion minimum is 100 points in increments of ten; published provider minima still apply. |
| Reward safeguards | Source settlement and funding evidence, 24-hour trip/delivery hold, seven-day referral hold, duplicate/self-referral controls, reversible source accounting and lifetime issuance ceilings. Cash completion alone does not prove collected money. |
| Small-value conversion | Integer points retain sub-cent value; quotes require whole minor-unit value and an approved current FX rate for the wallet currency. The original quote and account revision govern confirmation and replay. |
| Courier agreements | Versioned English agreements published for all seven countries. Material changes require the acceptance specified by the existing legal workflow; historical acceptance evidence remains intact. |
| Goods cash collection | Enabled at country level but optional for each assigned job. The requester proposes itemised goods cash before pickup and the courier separately accepts. Goods cash, service fare and shopping reimbursement are different obligations. |
| Automatic assignment | Bidding remains the default. Customer opt-in accepts an eligible driver's exact-fare acceptance through the normal acceptance command. Counteroffers remain manual. Ranking does not itself assign a driver. |
| Automatic completion | Wallet-funded journeys can complete after fresh, accurate, continuous stationary destination evidence and the normal locked settlement checks. Cash/external-payment journeys remain manual because GPS cannot prove payment collection. |

Automatic completion requires an in-progress, unpaused trip started at least
one minute ago, no unfinished stops, at least three samples spanning 30 seconds,
no sample gap over 15 seconds, latest evidence no older than 15 seconds,
accuracy within 25 metres, speed no higher than 1 m/s, and destination distance
within 50 metres. The settlement handler rechecks the evidence and current
revision under its lock. An interrupted response is reconciled from durable
trip state before another command; the existing ledger/outbox transaction
remains authoritative. A GPS exception cannot be invented by automation.

The goods-cash limits are operator risk limits, not exchange-rate quotations:
JMD 10,000, KYD 80, BBD 200, TTD 700, BMD 100, USD 100 and CAD 140 per job;
outstanding courier exposure is five times the corresponding job limit.
Ordinary service-fare cash settings are preserved independently.

## Evidence and remaining dependencies

Deployment confirmed the published policy rows in all seven country cells and
healthy API readiness. The API assembly SHA-256 is
`c25384c52f05381a6b240dfb77909faaa47fa6690317e0cdf12ace82adf2d7f0`.
Focused source tests passed; 17 additional reward tests ran successfully in
isolated real MySQL schemas. Those relational tests use explicit capability
and FX test doubles, not actual seven-country purchases. Later completion
tests cover stale/moving/inaccurate telemetry, cash exclusion and recovery
after a committed result whose response was lost. Overlapping test counts
must not be added into a fabricated unique-test total.

Today's owner approval is separate from country launch certification. Existing
checklist evidence retains its original dates; new review metadata records
the current partial review. No new all-country physical-device, licensing,
insurance, translation or store approval is implied. BM/US/CA rental branch
jurisdiction reviews, Rental Risk Exchange approval, scheduled-ride guarantees,
automated payouts and optional call recording remain separate controls.

The curated public OpenAPI export remains its separately dated historical
snapshot. Updating this architecture baseline does not regenerate or certify
every field in that older export. See [current baseline](../current-baseline.md).

## Public release consolidation

Builds 247 and 224 are consolidated into the published
[build-248 changelog](https://kilodrive.com/changelog/1.0.0/build/248?surface=mobile&platform=all).
It contains 310 detail records, including the 308 previously consolidated
build-247 entries. Original records remain unpublished historical evidence;
their public URLs redirect to 248. Old per-entry dates and internal provenance
labels are not rendered as customer release copy.
