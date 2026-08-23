# AWS Storage and Encryption

## S3 object classes

KiloDrive uses private S3 storage for document evidence, ticket attachments,
approved thumbnails/media, generated reports, and consented voice recordings.
Object prefixes and roles are separated by content class and purpose.

## Controls

- block public access and avoid public object ACLs;
- require TLS and encryption at rest;
- use an approved KMS key when policy requires customer-managed encryption;
- prohibit credentials, PII, and tokens in object names;
- authorize every read through the API or a short-lived signed delivery;
- version or retain only where policy requires it;
- apply lifecycle transitions/deletion by content class;
- record safe object/provider identifiers, not contents, in audit evidence; and
- verify backup/restore and deletion/hold paths with non-production fixtures.

## Upload flow

Objects remain quarantined until magic-byte/type validation and malware/CDR
policy succeed. Clean objects become available to authorized reviewers. Rejected
objects retain only the minimum evidence needed for security investigation and
are removed according to quarantine policy.

## Recording flow

LiveKit egress writes only after consent and an authorized recording state. The
API records egress status and retention metadata. A dedicated role performs
expiration/deletion and treats repeated deletion as idempotent.
