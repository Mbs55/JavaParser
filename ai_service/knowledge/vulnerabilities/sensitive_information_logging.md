# Sensitive Information Logging

## Overview

Sensitive information logging occurs when passwords, tokens, PII, or secret values are written to logs or diagnostic output. Attackers who gain log access can exploit these records directly.

## CWE

CWE-532: Insertion of Sensitive Information into Log File

## Relevant Java APIs

- java.util.logging.Logger
- org.slf4j.Logger
- org.apache.logging.log4j.Logger
- System.out.println

## Attack conditions

The code logs untrusted or sensitive data without masking, redaction, or restricted log access.

## Vulnerable Java example

```java
logger.error("Login failed for user={} password={}", username, password);
```

This exposes credentials in log data.

## Secure Java example

```java
logger.error("Login failed for user={}", username);
```

with secure audit events that do not store secrets or raw tokens.

## Detection indicators

- logging passwords, access tokens, API keys, or session data
- logging entire request or object representations without filtering
- exceptions that include secrets in stack traces or messages

## Mitigation

- redact or omit sensitive fields from logs
- use structured audit records without secret values
- control log access and retention carefully
- review exception handling and debug logging for secret leakage

## Common false positives

- ordinary application logs that record only IDs and operation names are not inherently a problem