# Runbook: Upload Quarantine and Scanner Failure

## States

New uploads are quarantined, then become clean/available, rejected, or remain
pending for controlled retry. Production never uses a null scanner.

## Procedure

1. Keep the object private and unavailable to reviewers/users.
2. Confirm file size, declared type, magic bytes, scanner connectivity, signature
   freshness, timeout, and response authenticity.
3. Reject confirmed malware and preserve only policy-approved security evidence.
4. Retry transient scanner failures through a bounded queue; repeated timeout
   requires operator review.
5. Release only after a trusted clean result, then audit the state transition.
6. Verify thumbnails are re-encoded and do not inherit active content.

Never bypass scanning to resolve a queue, expose the quarantined S3 object, or
log file contents.
