# Host Header Injection

## Overview

Host Header Injection is a web vulnerability where untrusted host or Host header values are used to build links, redirects, or application-generated URLs. In Java web apps, this often appears in Spring MVC, servlet code, and mail or password-reset flows.

## CWE

CWE-644: Improper Neutralization of HTTP Headers for Suffixes

## Relevant Java APIs

- javax.servlet.http.HttpServletRequest.getHeader
- javax.servlet.http.HttpServletRequest.getServerName
- javax.servlet.http.HttpServletRequest.getRequestURL
- jakarta.servlet.http.HttpServletRequest.getHeader
- jakarta.servlet.http.HttpServletRequest.getServerName
- org.springframework.http.HttpHeaders.getHost
- org.springframework.web.util.UriComponentsBuilder.fromHttpRequest

## Attack conditions

The issue occurs when the application trusts the `Host` header or request URL to generate redirects, canonical links, or absolute URLs in emails or responses.

## Vulnerable Java example

```java
String host = request.getHeader("Host");
String resetLink = "https://" + host + "/reset?token=" + token;
response.sendRedirect(resetLink);
```

An attacker can send a malicious host value and force the app to generate attacker-controlled URLs.

## Secure Java example

```java
String host = request.getServerName();
if (!isAllowedHost(host)) {
    response.sendError(HttpServletResponse.SC_BAD_REQUEST);
    return;
}

String resetLink = "https://" + host + "/reset?token=" + token;
response.sendRedirect(resetLink);
```

## Detection indicators

- building absolute URLs from `Host` or request headers
- redirecting or composing links using unvalidated host values
- generating email links or password reset URLs from request metadata

## Mitigation

- do not trust the `Host` header for security-sensitive redirects
- validate hosts against an allowlist of known domains
- use server-configured base URLs or fixed canonical domains
- reject unexpected or malformed host headers
- use secure redirect validation for login, password reset, and OAuth callbacks

## False positives

- a fixed application host configured in server settings is not a vulnerability
- server-generated base URLs from trusted configuration are safe
