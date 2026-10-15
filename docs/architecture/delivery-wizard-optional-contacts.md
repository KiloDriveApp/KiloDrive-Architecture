# Delivery request wizard: optional contacts and clearer steps

Reviewed 15 October 2026 against consumer source **1.0.0+215** and schema contract **2026.10.14.2**. This describes implemented source awaiting app/API deployment; it is not a claim of store availability or physical-device certification.

## Requesting a delivery

1. Choose the delivery service you need. Only provide details relevant to that job.
2. Select collection and delivery locations. Open **Contact details (Optional)** if you want to identify the sender or recipient. Recipient name and phone number are not required to request a quote or create the booking. Additional-stop contacts are optional too.
3. Describe the package or task and complete the required handling information. Optional contacts do not remove location, parcel, consent, pricing or custody requirements.
4. Choose the applicable timing and service options, then review the quote before submitting.

The **Next** button follows each step's fields. Scroll to the bottom to continue; this prevents a fixed Next button from hiding questions below the visible area. **Back** remains available, entered details are retained when navigating between steps, and each new step opens at the top. Correct the inline validation message if a required answer is missing. A phone number entered voluntarily must still be valid.

## Delivery confirmation without a recipient phone

A missing recipient phone does not bypass custody confirmation. The authenticated requester can obtain the handoff code and share it with the intended recipient. SMS delivery is supplemental and depends on an available destination. Never publish a handoff code in public instructions. Separately authorized alternative returns retain their named-receiver and proof requirements.

## Implementation and verification

The consumer quote/create gates, main wizard, additional-stop editor and API validators agree on optional booking contacts. Server storage normalizes missing names safely. The public API contract is regenerated. Unknown outcomes still require reconciliation with the original request identity; do not create another booking merely because a response was interrupted.

Focused verification passed **37 Flutter tests** and **73 API tests**. Flutter analysis reported no issues. Composition checks include small-phone and tablet layouts, enlarged text, blank contact values, saved addresses, document deliveries and interrupted-request recovery. These are automated checks, not a claim that Android/iOS device certification or the full release gate passed.

## Availability

Use the installed app's current labels until the matching app and API are deployed. The downloadable manuals may describe an earlier release; this update is an online source-preview supplement. Broader provider-workflow catalog/release checks remain outstanding and are not certified by these results.

[Online rider manual](https://kilodrive.com/manuals/rider) · [Release history](https://kilodrive.com/changelog)
