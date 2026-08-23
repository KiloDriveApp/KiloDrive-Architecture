# Glossary

| Term | Meaning |
| --- | --- |
| Control plane | Global identity, country routing, support, privacy, and cross-cell coordination data. |
| Country cell | A country-scoped MySQL database containing operational and financial domain data. |
| Tenant | A logical marketplace or organization boundary inside an authorized country cell. |
| Projection | A credential-free country-local representation of a global user used for domain relationships. |
| Outbox | Durable database records describing side effects that workers deliver after a transaction commits. |
| Valkey | Redis-protocol distributed data service used for cache, realtime scale-out, ephemeral state, and telemetry. |
| Correlation ID | A sanitized request identifier propagated through logs, responses, provider work, and audit evidence. |
| Idempotency key | A caller-supplied identifier that makes a protected mutation safe to retry. |
| UUIDv7 | Time-ordered RFC 9562 universally unique identifier used for externally exposed and transactional entities. |
| Cell fingerprint | Deterministic hash of the expected country-cell relational metadata. |
| JWKS | Public JSON Web Key Set used by clients and services to validate asymmetric access-token signatures. |
| Egress | LiveKit service that records or exports an authorized media room. |
| CDR | Content Disarm and Reconstruction, an optional document-sanitization step after malware scanning. |
| PSP | Payment service provider. |
| KYC/AML | Identity and anti-money-laundering controls applied according to an approved operating model. |
| RPO/RTO | Recovery point and recovery time objectives. Exact production targets are private operational data. |
