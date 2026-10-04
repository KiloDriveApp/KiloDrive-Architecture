# Reference coverage and review debt

[API Guide](../README.md) · [Operation finder](operations.md)

Generated from the same artifact as the reference. These are documentation
coverage counts, not test pass rates, release readiness or runtime success rates.

## Endpoint explanations

- Published operations: **528**.
- Operation-specific explanations: **136**.
- Route-derived summaries requiring deeper behavior review: **392**.

Both kinds preserve the recorded wire contract. A route-derived summary must
not be mistaken for a reviewed state machine or an exhaustive permission rule.

## Field explanations

| Basis | Properties |
| --- | ---: |
| Model-specific | 55 |
| Naming convention | 1333 |
| Shared convention | 1413 |
| Type only; meaning review open | 2211 |

Shared or naming conventions explain representation, not every business rule.
The [machine-readable review queue](coverage.json) lists every type-only field
and route-derived operation so omissions remain actionable. The
[model usage map](../schemas/usage.json) connects each model to all published
operations that use it, including nested models.

## Untyped success responses

An untyped result is a source-contract documentation gap, not proof of an empty
runtime body. Intentional HTTP 204 responses are excluded. Update the canonical
source response annotation and contract tests before regenerating this reference.

| Operation | Status without a typed body |
| --- | --- |
| [DELETE `/api/v1/account`](identity.md#delete-apiv1account) | 200 |
| [POST `/api/v1/account/activity/settings`](identity.md#post-apiv1accountactivitysettings) | 200 |
| [GET `/api/v1/account/avatar`](identity.md#get-apiv1accountavatar) | 200 |
| [PUT `/api/v1/account/complete-profile`](identity.md#put-apiv1accountcomplete-profile) | 200 |
| [POST `/api/v1/account/contact-details/email/confirm`](identity.md#post-apiv1accountcontact-detailsemailconfirm) | 200 |
| [POST `/api/v1/account/contact-details/phone/confirm`](identity.md#post-apiv1accountcontact-detailsphoneconfirm) | 200 |
| [POST `/api/v1/account/deactivate`](identity.md#post-apiv1accountdeactivate) | 200 |
| [POST `/api/v1/account/deactivate/recoverable`](identity.md#post-apiv1accountdeactivaterecoverable) | 200 |
| [GET `/api/v1/account/export`](identity.md#get-apiv1accountexport) | 200 |
| [POST `/api/v1/account/onboarding/profile-photo-decision`](identity.md#post-apiv1accountonboardingprofile-photo-decision) | 200 |
| [DELETE `/api/v1/account/recoverable`](identity.md#delete-apiv1accountrecoverable) | 200 |
| [POST `/api/v1/auth/change-password`](identity.md#post-apiv1authchange-password) | 200 |
| [POST `/api/v1/auth/login/email/request`](identity.md#post-apiv1authloginemailrequest) | 200 |
| [POST `/api/v1/auth/login/phone/request`](identity.md#post-apiv1authloginphonerequest) | 200 |
| [POST `/api/v1/auth/logout`](identity.md#post-apiv1authlogout) | 200 |
| [DELETE `/api/v1/auth/passkeys/{id}`](identity.md#delete-apiv1authpasskeysid) | 200 |
| [POST `/api/v1/auth/password-reset/confirm`](identity.md#post-apiv1authpassword-resetconfirm) | 200 |
| [POST `/api/v1/auth/password-reset/request`](identity.md#post-apiv1authpassword-resetrequest) | 200 |
| [POST `/api/v1/auth/phone-verification/confirm`](identity.md#post-apiv1authphone-verificationconfirm) | 200 |
| [POST `/api/v1/auth/phone-verification/request`](identity.md#post-apiv1authphone-verificationrequest) | 200 |
| [DELETE `/api/v1/auth/sessions/{id}`](identity.md#delete-apiv1authsessionsid) | 200 |
| [POST `/api/v1/auth/set-password`](identity.md#post-apiv1authset-password) | 200 |
| [DELETE `/api/v1/auth/social-connections/{id}`](identity.md#delete-apiv1authsocial-connectionsid) | 200 |
| [POST `/api/v1/auth/social-link-intents/cancel`](identity.md#post-apiv1authsocial-link-intentscancel) | 200 |
| [DELETE `/api/v1/business-shipping/accounts/{accountId}/members/{memberId}`](profiles.md#delete-apiv1business-shippingaccountsaccountidmembersmemberid) | 200 |
| [DELETE `/api/v1/calculations/{id}`](maps-and-tools.md#delete-apiv1calculationsid) | 200 |
| [PUT `/api/v1/corporate/accounts/{accountId}/members`](profiles.md#put-apiv1corporateaccountsaccountidmembers) | 200 |
| [POST `/api/v1/deliveries/{deliveryRequestId}/cancel`](deliveries.md#post-apiv1deliveriesdeliveryrequestidcancel) | 200 |
| [POST `/api/v1/driver/deliveries/{deliveryId}/cancel`](deliveries.md#post-apiv1driverdeliveriesdeliveryidcancel) | 200 |
| [GET `/api/v1/driver/incentives/current`](drivers.md#get-apiv1driverincentivescurrent) | 200 |
| [POST `/api/v1/driver/profile/onboarding/complete`](drivers.md#post-apiv1driverprofileonboardingcomplete) | 200 |
| [POST `/api/v1/driver/profile/onboarding/progress`](drivers.md#post-apiv1driverprofileonboardingprogress) | 200 |
| [POST `/api/v1/driver/profile/onboarding/step`](drivers.md#post-apiv1driverprofileonboardingstep) | 200 |
| [GET `/api/v1/driver/reports/earnings`](drivers.md#get-apiv1driverreportsearnings) | 200 |
| [DELETE `/api/v1/driver/rider-favorites/{favoriteId}`](drivers.md#delete-apiv1driverrider-favoritesfavoriteid) | 200 |
| [POST `/api/v1/driver/rider-favorites/{riderUserId}`](drivers.md#post-apiv1driverrider-favoritesrideruserid) | 200 |
| [DELETE `/api/v1/driver/rides/bids/{bidId}`](drivers.md#delete-apiv1driverridesbidsbidid) | 200 |
| [POST `/api/v1/driver/rides/{rideRequestId}/inquiry/read`](drivers.md#post-apiv1driverridesriderequestidinquiryread) | 200 |
| [POST `/api/v1/driver/rides/{rideRequestId}/view`](drivers.md#post-apiv1driverridesriderequestidview) | 200 |
| [GET `/api/v1/driver/status`](drivers.md#get-apiv1driverstatus) | 200 |
| [POST `/api/v1/driver/status`](drivers.md#post-apiv1driverstatus) | 200 |
| [DELETE `/api/v1/driver/vehicles/{vehicleId}`](vehicles.md#delete-apiv1drivervehiclesvehicleid) | 200 |
| [DELETE `/api/v1/favorites/{favoriteId}`](rides.md#delete-apiv1favoritesfavoriteid) | 200 |
| [PUT `/api/v1/households/{householdId}/members`](safety.md#put-apiv1householdshouseholdidmembers) | 200 |
| [GET `/api/v1/maps/autocomplete`](maps-and-tools.md#get-apiv1mapsautocomplete) | 200 |
| [GET `/api/v1/maps/geocode`](maps-and-tools.md#get-apiv1mapsgeocode) | 200 |
| [GET `/api/v1/maps/place`](maps-and-tools.md#get-apiv1mapsplace) | 200 |
| [GET `/api/v1/maps/reverse-geocode`](maps-and-tools.md#get-apiv1mapsreverse-geocode) | 200 |
| [GET `/api/v1/maps/route`](maps-and-tools.md#get-apiv1mapsroute) | 200 |
| [GET `/api/v1/maps/traffic-routes`](maps-and-tools.md#get-apiv1mapstraffic-routes) | 200 |
| [DELETE `/api/v1/notifications`](notifications.md#delete-apiv1notifications) | 200 |
| [DELETE `/api/v1/notifications/push-token`](notifications.md#delete-apiv1notificationspush-token) | 200 |
| [POST `/api/v1/notifications/push-token`](notifications.md#post-apiv1notificationspush-token) | 200 |
| [GET `/api/v1/notifications/push-token/installation-state`](notifications.md#get-apiv1notificationspush-tokeninstallation-state) | 200 |
| [POST `/api/v1/notifications/read-all`](notifications.md#post-apiv1notificationsread-all) | 200 |
| [DELETE `/api/v1/notifications/{notificationId}`](notifications.md#delete-apiv1notificationsnotificationid) | 200 |
| [POST `/api/v1/notifications/{notificationId}/read`](notifications.md#post-apiv1notificationsnotificationidread) | 200 |
| [GET `/api/v1/public/capabilities`](discovery.md#get-apiv1publiccapabilities) | 200 |
| [DELETE `/api/v1/recurring-rides/{recurringRideId}`](rides.md#delete-apiv1recurring-ridesrecurringrideid) | 200 |
| [DELETE `/api/v1/recurring-rides/{recurringRideId}/revisioned`](rides.md#delete-apiv1recurring-ridesrecurringrideidrevisioned) | 200 |
| [DELETE `/api/v1/rental-partner/organizations/{organizationId}`](rentals.md#delete-apiv1rental-partnerorganizationsorganizationid) | 200 |
| [DELETE `/api/v1/rental-partner/organizations/{organizationId}/availability-blocks/{blockId}`](rentals.md#delete-apiv1rental-partnerorganizationsorganizationidavailability-blocksblockid) | 200 |
| [POST `/api/v1/rental-partner/organizations/{organizationId}/bookings/{bookingId}/deposit/settle`](rentals.md#post-apiv1rental-partnerorganizationsorganizationidbookingsbookingiddepositsettle) | 200 |
| [PUT `/api/v1/rental-partner/organizations/{organizationId}/bookings/{bookingId}/status`](rentals.md#put-apiv1rental-partnerorganizationsorganizationidbookingsbookingidstatus) | 200 |
| [PUT `/api/v1/rental-partner/organizations/{organizationId}/profile-image`](rentals.md#put-apiv1rental-partnerorganizationsorganizationidprofile-image) | 200 |
| [DELETE `/api/v1/rental-partner/organizations/{organizationId}/team/invitations/{invitationId}`](rentals.md#delete-apiv1rental-partnerorganizationsorganizationidteaminvitationsinvitationid) | 200 |
| [PUT `/api/v1/rental-partner/organizations/{organizationId}/team/{userId}`](rentals.md#put-apiv1rental-partnerorganizationsorganizationidteamuserid) | 200 |
| [DELETE `/api/v1/rental-partner/organizations/{organizationId}/vehicles/{vehicleId}`](rentals.md#delete-apiv1rental-partnerorganizationsorganizationidvehiclesvehicleid) | 200 |
| [PUT `/api/v1/rental-partner/organizations/{organizationId}/vehicles/{vehicleId}`](rentals.md#put-apiv1rental-partnerorganizationsorganizationidvehiclesvehicleid) | 200 |
| [DELETE `/api/v1/rental-partner/organizations/{organizationId}/vehicles/{vehicleId}/images/{imageId}`](rentals.md#delete-apiv1rental-partnerorganizationsorganizationidvehiclesvehicleidimagesimageid) | 200 |
| [PUT `/api/v1/rental-partner/organizations/{organizationId}/vehicles/{vehicleId}/images/{imageId}/primary`](rentals.md#put-apiv1rental-partnerorganizationsorganizationidvehiclesvehicleidimagesimageidprimary) | 200 |
| [POST `/api/v1/rental-partner/team/invitations/accept`](rentals.md#post-apiv1rental-partnerteaminvitationsaccept) | 200 |
| [POST `/api/v1/rentals/bookings/{bookingId}/cancel`](rentals.md#post-apiv1rentalsbookingsbookingidcancel) | 200 |
| [GET `/api/v1/rentals/bookings/{bookingId}/damage-evidence/{evidenceId}`](rentals.md#get-apiv1rentalsbookingsbookingiddamage-evidenceevidenceid) | 200 |
| [GET `/api/v1/rentals/bookings/{bookingId}/dispute-evidence/{evidenceId}`](rentals.md#get-apiv1rentalsbookingsbookingiddispute-evidenceevidenceid) | 200 |
| [GET `/api/v1/rentals/bookings/{bookingId}/inspection-evidence/{evidenceId}`](rentals.md#get-apiv1rentalsbookingsbookingidinspection-evidenceevidenceid) | 200 |
| [POST `/api/v1/rentals/bookings/{bookingId}/rating`](rentals.md#post-apiv1rentalsbookingsbookingidrating) | 200 |
| [DELETE `/api/v1/rentals/favorites/{vehicleId}`](rentals.md#delete-apiv1rentalsfavoritesvehicleid) | 200 |
| [PUT `/api/v1/rentals/favorites/{vehicleId}`](rentals.md#put-apiv1rentalsfavoritesvehicleid) | 200 |
| [GET `/api/v1/rentals/organizations/{organizationId}/profile-image`](rentals.md#get-apiv1rentalsorganizationsorganizationidprofile-image) | 200 |
| [GET `/api/v1/rentals/vehicles/{vehicleId}/images/{imageId}`](rentals.md#get-apiv1rentalsvehiclesvehicleidimagesimageid) | 200 |
| [GET `/api/v1/reports/exports/{artifactId}/download`](reports.md#get-apiv1reportsexportsartifactiddownload) | 200 |
| [DELETE `/api/v1/reports/scheduled/{scheduleId}`](reports.md#delete-apiv1reportsscheduledscheduleid) | 200 |
| [GET `/api/v1/reports/{reportType}`](reports.md#get-apiv1reportsreporttype) | 200 |
| [GET `/api/v1/resources/manuals`](discovery.md#get-apiv1resourcesmanuals) | 200 |
| [GET `/api/v1/rides/{rideRequestId}/bids/{bidId}/avatar`](rides.md#get-apiv1ridesriderequestidbidsbididavatar) | 200 |
| [POST `/api/v1/rides/{rideRequestId}/bids/{bidId}/reject`](rides.md#post-apiv1ridesriderequestidbidsbididreject) | 200 |
| [POST `/api/v1/rides/{rideRequestId}/cancel`](rides.md#post-apiv1ridesriderequestidcancel) | 200 |
| [POST `/api/v1/rides/{rideRequestId}/inquiries/{driverProfileId}/read`](rides.md#post-apiv1ridesriderequestidinquiriesdriverprofileidread) | 200 |
| [GET `/api/v1/safety/cases`](safety.md#get-apiv1safetycases) | 200 |
| [POST `/api/v1/safety/cases`](safety.md#post-apiv1safetycases) | 200 |
| [POST `/api/v1/safety/cases/recoverable`](safety.md#post-apiv1safetycasesrecoverable) | 200 |
| [POST `/api/v1/safety/cases/{id}/acknowledge`](safety.md#post-apiv1safetycasesidacknowledge) | 200 |
| [POST `/api/v1/safety/cases/{id}/acknowledge/recoverable`](safety.md#post-apiv1safetycasesidacknowledgerecoverable) | 200 |
| [POST `/api/v1/safety/events`](safety.md#post-apiv1safetyevents) | 200 |
| [POST `/api/v1/safety/events/{id}/acknowledge`](safety.md#post-apiv1safetyeventsidacknowledge) | 200 |
| [GET `/api/v1/safety/trusted-contacts`](safety.md#get-apiv1safetytrusted-contacts) | 200 |
| [POST `/api/v1/safety/trusted-contacts`](safety.md#post-apiv1safetytrusted-contacts) | 200 |
| [DELETE `/api/v1/safety/trusted-contacts/{id}`](safety.md#delete-apiv1safetytrusted-contactsid) | 200 |
| [GET `/api/v1/support/tickets/{ticketId}/messages/{messageId}/attachments/{index}`](support.md#get-apiv1supportticketsticketidmessagesmessageidattachmentsindex) | 200 |
| [PUT `/api/v1/support/tickets/{ticketId}/read`](support.md#put-apiv1supportticketsticketidread) | 200 |
| [POST `/api/v1/tools/calculators/export/pdf`](maps-and-tools.md#post-apiv1toolscalculatorsexportpdf) | 200 |
| [DELETE `/api/v1/travel-profiles/{profileId}`](profiles.md#delete-apiv1travel-profilesprofileid) | 200 |
| [DELETE `/api/v1/travel-profiles/{profileId}/cost-centers/{costCenterId}`](profiles.md#delete-apiv1travel-profilesprofileidcost-centerscostcenterid) | 200 |
| [DELETE `/api/v1/travel-profiles/{profileId}/members/{memberId}`](profiles.md#delete-apiv1travel-profilesprofileidmembersmemberid) | 200 |
| [POST `/api/v1/trips/{tripId}/cancel`](trips.md#post-apiv1tripstripidcancel) | 200 |
| [GET `/api/v1/trips/{tripId}/driver-avatar`](trips.md#get-apiv1tripstripiddriver-avatar) | 200 |
| [GET `/api/v1/trips/{tripId}/passenger-avatar`](trips.md#get-apiv1tripstripidpassenger-avatar) | 200 |
| [DELETE `/api/v1/trips/{tripId}/peer-block`](trips.md#delete-apiv1tripstripidpeer-block) | 200 |
| [PUT `/api/v1/trips/{tripId}/peer-block`](trips.md#put-apiv1tripstripidpeer-block) | 200 |
| [POST `/api/v1/trips/{tripId}/rating`](trips.md#post-apiv1tripstripidrating) | 200 |
| [GET `/api/v1/trips/{tripId}/receipt.pdf`](trips.md#get-apiv1tripstripidreceiptpdf) | 200 |
| [POST `/api/v1/trips/{tripId}/receipt/email`](trips.md#post-apiv1tripstripidreceiptemail) | 200 |
| [POST `/api/v1/trips/{tripId}/reservation/decline`](trips.md#post-apiv1tripstripidreservationdecline) | 200 |
| [POST `/api/v1/trips/{tripId}/route-alterations/{alterationId}/reject`](trips.md#post-apiv1tripstripidroute-alterationsalterationidreject) | 200 |
| [POST `/api/v1/trips/{tripId}/share/revoke`](trips.md#post-apiv1tripstripidsharerevoke) | 200 |
| [POST `/api/v1/uploads`](uploads.md#post-apiv1uploads) | 200 |
| [GET `/api/v1/uploads/operations/{operationId}`](uploads.md#get-apiv1uploadsoperationsoperationid) | 200 |
| [POST `/api/v1/uploads/recoverable`](uploads.md#post-apiv1uploadsrecoverable) | 200 |
| [GET `/api/v1/uploads/{fileRef}`](uploads.md#get-apiv1uploadsfileref) | 200 |
| [DELETE `/api/v1/user-blocks/{blockId}`](safety.md#delete-apiv1user-blocksblockid) | 200 |
| [PUT `/api/v1/user-blocks/{userId}`](safety.md#put-apiv1user-blocksuserid) | 200 |
| [DELETE `/api/v1/vehicles/{vehicleId}`](vehicles.md#delete-apiv1vehiclesvehicleid) | 200 |
| [POST `/api/v1/voice/call/end`](communications.md#post-apiv1voicecallend) | 200 |
| [POST `/api/v1/voice/call/gsm`](communications.md#post-apiv1voicecallgsm) | 200 |
| [GET `/api/v1/wallet/financial-history/export/pdf`](wallets.md#get-apiv1walletfinancial-historyexportpdf) | 200 |
| [GET `/api/v1/wallet/financial-history/{entryId}/export/pdf`](wallets.md#get-apiv1walletfinancial-historyentryidexportpdf) | 200 |
| [DELETE `/api/v1/wallet/payout-methods/{id}`](wallets.md#delete-apiv1walletpayout-methodsid) | 200 |
| [DELETE `/api/v1/wallet/recipients/{id}`](wallets.md#delete-apiv1walletrecipientsid) | 200 |
| [POST `/api/v1/wallet/topup/bank-transfers/{paymentId}/cancel`](wallets.md#post-apiv1wallettopupbank-transferspaymentidcancel) | 200 |
| [GET `/api/v1/wallet/transactions/export`](wallets.md#get-apiv1wallettransactionsexport) | 200 |

## Remediation order

1. Clarify identity, money, eligibility and document-handling contracts first.
2. Review the controller, validator and handler together; add model-specific
   descriptions where a shared name is ambiguous.
3. Correct missing status/body annotations in the private canonical API contract.
4. Add focused publication tests, regenerate and compare wire shapes with source.
5. Record provider/device observations separately; documentation cannot certify them.
