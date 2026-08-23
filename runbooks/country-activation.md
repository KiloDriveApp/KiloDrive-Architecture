# Runbook: Country Activation

## Preconditions

- approved legal, privacy, safety, tax, money-movement, and provider model;
- provisioned and backed-up MySQL country cell;
- canonical schema fingerprint parity;
- country currency, timezone, phone, licence, plate, fare, toll, bank, insurance,
  emergency, membership, and reference rules reviewed;
- tenant routing and System Admin workspace tested;
- non-user provider destinations and canaries configured; and
- rider, driver, rental, wallet, ride, delivery, report, and support fixtures pass.

## Activation

1. Register the shard as provisioned but inactive.
2. Run readiness and country-specific contract tests.
3. Enable the country through the governed activation action.
4. Verify signup selection, account projection, workspace selection, country
   currency/timezone, and a complete non-production lifecycle.
5. Monitor errors, latency, queue lag, and financial exceptions during rollout.

Fingerprint drift or withdrawal of the operating approval blocks/reverses
activation. Disabling signup does not delete the country cell.
