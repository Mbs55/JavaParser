# Struts2 OGNL Injection

## Overview

Struts2 OGNL injection occurs when untrusted input is executed as an OGNL expression in a Struts2 application. This can allow attacker-controlled expression execution and bypasses of application logic.

## CWE

CWE-94: Improper Control of Generation of Code ('Code Injection')

## Relevant Java APIs

- ognl.Ognl.getValue
- org.apache.struts2.dispatcher.mapper.DefaultActionMapper
- org.apache.struts2.interceptor.debugging.DebuggingInterceptor

## Attack conditions

The app evaluates a request parameter or URL value as an OGNL expression without sanitization or an allowlist.

## Vulnerable Java example

```java
String expr = request.getParameter("expr");
Object value = Ognl.getValue(expr, context);
```

This can trigger property access or execution via OGNL syntax.

## Secure Java example

```java
String expr = request.getParameter("expr");
if (!expr.matches("^[A-Za-z0-9_]{1,32}$")) {
    throw new IllegalArgumentException("Invalid expression");
}
```

## Detection indicators

- use of OGNL expressions with request data
- Struts2 actions exposing expression-driven evaluation or debug access
- unvalidated parameter values passed into OGNL evaluation paths

## Mitigation

- disable expression evaluation for untrusted input
- validate and restrict user-provided expression content
- remove debug or expression-enabled features in production
- keep Struts2 configuration hardened and minimal
