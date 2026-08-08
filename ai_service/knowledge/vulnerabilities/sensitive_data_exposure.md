# Sensitive Data Exposure

## Overview

Sensitive data exposure occurs when confidential information is accessible without proper controls, including through logs, improper storage, or cleartext transport.

## CWE

CWE-200: Exposure of Sensitive Information to an Unauthorized Actor

## Relevant Java APIs

- java.util.logging.Logger
- org.slf4j.Logger.info
- java.sql.Connection
- javax.servlet.http.HttpServletResponse

## Attack conditions

The app stores or transmits secret, personal, or business-sensitive data without appropriate protection or access control.

## Vulnerable Java example

```java
logger.info("User details: {}", user.toString());
```

This may leak token values, password hashes, or sensitive profile data to logs.

## Secure Java example

```java
logger.info("User {} loaded successfully", user.getId());
```

and ensure no secrets or PII are stored or logged in plaintext.

## Detection indicators

- logging tokens, personal data, or secret data without masking
- returning full objects or debug information in responses
- cleartext persistence or transmission of confidential information

## Mitigation

- minimize data collection and exposure
- mask or redact sensitive fields in logs and trace output
- enforce encryption and access controls on stored data
- use least privilege for service-to-service data exchange

## Common false positives

- safe log statements that reference only IDs or non-sensitive metadata are not sensitive data exposure