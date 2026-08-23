# Runbook: upload quarantine and scanner failure

- **Owner:** Document security and storage operations
- **Status:** Operational fail-closed recovery procedure
- **Last exercised:** Not yet recorded in this public repository
- **Related architecture:** [Documents, media, and voice](../architecture/documents-media-voice.md) and [AWS storage](../aws/storage.md)

**Use when:** uploads remain pending, document viewing returns a quarantine
conflict, ClamAV is unavailable/outdated, malware is detected, or an object and
metadata state disagree.

**Safety rule:** fail closed. A scanner outage is never a reason to publish an
unscanned file.

## State meanings

| State | Meaning | User/reviewer access |
| --- | --- | --- |
| Quarantined/pending | accepted for scanning; no trusted result yet | metadata/friendly status only |
| Clean/available | type and trusted scanner policy passed | authorized delivery allowed |
| Rejected | malware, invalid type, or policy failure | no content delivery |
| Retry scheduled | transient scanner timeout/unavailable | still quarantined |
| Deleted | retention/approved removal completed | none |

A raw `409` in an admin viewer usually means the quarantine guard worked but the
client surfaced it badly. Preserve the guard and map the stable code to a clear
state and retry action.

## Initial response

1. Determine whether one object, one content type, or all uploads are affected.
2. Record safe document ID, content class, scan state, attempt count, correlation
   ID, and timestamps. Do not record filename if it contains PII, object URL, or
   file content.
3. Confirm the object remains private and cannot be fetched through owner,
   reviewer, thumbnail, report, or direct S3 path.
4. If malicious content is confirmed, follow the security-incident process and
   restrict evidence access.
5. If broad scanner failure, pause/limit new upload intake only if quarantine
   growth threatens capacity; never auto-approve.

## Diagnosis

### Request and type validation

- Was the request within server/IIS size limits?
- Does declared type belong to the content-class allow-list?
- Do magic bytes and structural parser agree?
- Is the format active or risky even if antivirus says clean?

A request-size warning that the server feature is read-only indicates the limit
must be configured earlier at IIS/Kestrel. It is not proof the upload was scanned.

### ClamAV service

- Is `clamd` running and listening only on the intended protected interface?
- Is the application using the correct host/port and bounded timeout?
- Are signature databases present, current, and successfully loaded?
- Does the service account have database/temp access without broad filesystem
  access?
- Are protocol responses complete and authentic according to the adapter's
  configured signing/trust mechanism?
- Is CPU/memory/disk saturation making every scan time out?

`freshclam` updating signatures does not start/configure `clamd`. A misspelled
database directory can also make updates look successful in the wrong location.

### Storage and KMS

- Did the object upload to the quarantine prefix?
- Can the scanner role read only that object/prefix?
- Do bucket policy, IAM, KMS key policy, region, and encryption context agree?
- Did an object lifecycle rule remove it prematurely?

### Worker/retry

- Is a retry intent present and handler registered?
- Is retry bounded with backoff?
- Are repeated attempts classified without storing raw scanner output?
- Did a process restart leave a lease stuck?

## Containment by condition

### Malware detected

Keep bytes isolated. Mark rejected with a safe reason, prevent download and
thumbnail generation, preserve policy-approved evidence, and examine whether the
same actor/content pattern attempted other uploads. Do not send the file through
ordinary email or ticket attachments for review.

### Scanner unavailable

Keep objects pending. Alert on queue age/volume and scanner health. Restore the
scanner or approved managed adapter. If capacity is at risk, temporarily reject
new uploads with a localized “verification uploads are temporarily unavailable”
message; do not claim success.

### False positive suspected

Do not override directly in the database. Use a restricted review process with a
second approved scanner/CDR or security analyst, record reason and evidence, and
make the state transition auditable.

## Recovery

1. Update/repair scanner configuration and signatures.
2. Test clean, EICAR/test-malware, mismatched-magic, oversized, and timeout
   fixtures outside production data.
3. Requeue a small reviewed batch through protected tooling.
4. Verify only trusted clean results become available.
5. Drain gradually while watching scanner and storage saturation.
6. Reconcile metadata/object existence and remove expired quarantine according
   to policy.

## Rollback

If a new scanner/adapter release misclassifies files, stop the scanner worker and
leave objects quarantined while rolling back to the last approved version. Do not
roll back document metadata to `available` or expose previously rejected content.

## Verification

- Pending/rejected files remain inaccessible from every UI/API path.
- Clean files become available exactly once after trusted result.
- Cross-user and cross-tenant reads return coarse denial.
- Thumbnails are re-encoded and metadata stripped.
- Logs/traces contain no object URL, filename content, bytes, document number, or
  scanner raw payload.
- Retention and legal hold behave correctly.
- Readiness/canary reflects scanner state without leaking configuration.

## Never do this

- Register `NullUploadScanner` in production.
- Change pending rows to clean to clear a queue.
- Serve uploads from a public/web-root directory.
- Trust extension or browser MIME alone.
- Log presigned URLs or raw antivirus response/body.
- Give the API broad bucket/KMS administration to resolve one denial.
