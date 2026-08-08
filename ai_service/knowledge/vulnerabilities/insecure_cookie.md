# Insecure Cookie

## Overview

Insecure cookies are session or authentication cookies that are missing security attributes or are configured in a weak way. This allows attackers to steal or replay sessions.

## CWE

CWE-614: Sensitive Cookie in HTTPS Session Without 'Secure' Attribute

## Relevant Java APIs

- javax.servlet.http.Cookie
- jakarta.servlet.http.Cookie
- org.springframework.http.ResponseCookie
- org.springframework.security.web.authentication.rememberme.PersistentTokenBasedRememberMeServices

## Attack conditions

The issue is present when cookies are created without `Secure`, `HttpOnly`, `SameSite`, or verified domain restrictions, or when they are sent over plaintext HTTP.

## Vulnerable Java example

```java
Cookie cookie = new Cookie("session", token);
cookie.setHttpOnly(false);
response.addCookie(cookie);
```

## Secure Java example

```java
ResponseCookie cookie = ResponseCookie.from("session", token)
    .httpOnly(true)
    .secure(true)
    .sameSite("Strict")
    .path("/")
    .build();
response.addHeader(HttpHeaders.SET_COOKIE, cookie.toString());
```

## Detection indicators

- session cookies missing `Secure` or `HttpOnly`
- cookie configuration with wildcards or an overly broad path/domain
- session cookies sent over HTTP without transport security

## Mitigation

- set `Secure`, `HttpOnly`, and `SameSite` appropriately
- protect all sessions with HTTPS only
- restrict cookie scope to the necessary path and host
- review frameworks default settings and override insecure defaults

## Common false positives

- a cookie containing only non-sensitive public data may be lower risk, but authentication cookies still require strict controls