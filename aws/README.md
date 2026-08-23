# AWS Integration Overview

KiloDrive integrates with AWS through narrow provider adapters and the standard
credential chain/workload identity where possible. This chapter describes
capabilities, not account-specific deployment.

| AWS capability | KiloDrive use |
| --- | --- |
| S3 | Private documents, approved media, report artifacts, and consented voice recordings |
| KMS / encryption controls | Customer-managed encryption where required by data class |
| Secrets Manager | Optional protected source for signing/provider material |
| End User Messaging SMS/Voice | OTP, transactional SMS, and voice OTP where approved |
| Social Messaging | WhatsApp primary-provider integration where enabled |
| SES | Transactional email and report attachments |
| EventBridge | High-throughput dispatch event publication |
| SQS | Buffered, at-least-once dispatch consumption and dead-letter handling |
| CloudWatch | Logs, metrics, dashboards, alarms, and operational visibility |
| SNS | Alarm notification fan-out |
| ADOT / OpenTelemetry | Collection and export of sanitized traces and metrics |
| STS / IAM roles | Short-lived least-privilege access for workloads and recording retention |

The API must not depend on long-lived access keys when an instance/task role or
assumable role can provide the same capability. Provider access, data retention,
origination identities, country availability, and production messaging access
remain deployment-specific approvals.
