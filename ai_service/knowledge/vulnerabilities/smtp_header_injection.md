# SMTP Header Injection

## Overview

SMTP header injection occurs when an attacker-controlled value is included in a mail header such as the subject, sender, or recipient fields. This can allow injection of additional headers or message splitting.

## CWE

CWE-93: Improper Neutralization of CRLF Sequences in HTTP Headers

## Relevant Java APIs

- javax.mail.Message.addHeader
- javax.mail.Message.setDescription
- javax.mail.Message.setDisposition
- javax.mail.Message.setSubject

## Attack conditions

This issue appears when Java mail APIs are used with untrusted content in header fields or when CRLF sequences are not filtered.

## Vulnerable Java example

```java
String subject = request.getParameter("subject");
Message msg = new MimeMessage(session);
msg.setSubject(subject);
```

If the subject contains `\r\nBcc: attacker@example.com`, the email may be manipulated to add extra headers or route messages unexpectedly.

## Secure Java example

```java
String subject = request.getParameter("subject");
if (!subject.matches("^[A-Za-z0-9 .,_-]{1,200}$")) {
    throw new IllegalArgumentException("Invalid subject");
}

Message msg = new MimeMessage(session);
msg.setSubject(subject);
```

## Detection indicators

- mail subjects, headers, or description fields built from request data
- lack of CRLF validation before sending mail
- dynamic header values without allowlist validation

## Mitigation

- reject CRLF characters in mail header values
- enforce allowlisted characters for subject and recipient metadata
- validate and constrain all outbound mail fields
- avoid trusting user-supplied values in headers

## Common false positives

- constant mail subjects or safe internal configuration are fine
- validated values with restricted character sets are safe
