# Log Injection / CRLF Injection

## Overview

Log injection occurs when untrusted input is written to log files or log records without neutralization. If an attacker can inject CRLF sequences, they may create fake log entries or manipulate log metadata.

## CWE

CWE-117: Improper Output Neutralization for Logs

## Relevant Java APIs

- java.util.logging.Logger.info
- java.util.logging.Logger.log
- java.util.logging.Logger.warning
- org.slf4j.Logger.info
- org.apache.logging.log4j.Logger.info
- org.apache.log4j.Logger.info

## Attack conditions

The issue occurs when raw request data, headers, or user-controlled message text is directly written to logs without sanitization.

## Vulnerable Java example

```java
String user = request.getParameter("user");
logger.info("Login attempt for user: " + user);
```

If `user` contains `\r\nX-Injected: value`, an attacker may create fake log lines or pollute log analysis.

## Secure Java example

```java
String user = request.getParameter("user");
String safeUser = user == null ? "unknown" : user.replaceAll("[\r\n]+", "_");
logger.info("Login attempt for user: {}", safeUser);
```

## Detection indicators

- logging raw request parameters or headers
- dynamic log messages built with concatenation
- log entries containing untrusted strings without sanitization

## Mitigation

- sanitize CRLF and control characters before logging
- prefer parameterized logging APIs such as `{}` placeholders
- restrict logs to trusted, validated values
- avoid logging secrets, tokens, or untrusted headers directly

## Common false positives

- logging a sanitized username or fixed application value is safe
- parameterized logging is not a vulnerability
