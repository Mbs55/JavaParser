# HTTP Response Splitting

## Overview

HTTP Response Splitting occurs when untrusted input is used to set HTTP headers or response content without sanitization. Attackers can inject CRLF sequences and split one response into multiple responses.

## CWE

CWE-93: Improper Neutralization of CRLF Sequences in HTTP Headers ('HTTP Response Splitting')

## Relevant Java APIs

- javax.servlet.http.Cookie
- javax.servlet.http.Cookie.setValue
- javax.servlet.http.HttpServletResponse.addHeader
- javax.servlet.http.HttpServletResponse.setHeader
- javax.servlet.http.HttpServletResponseWrapper.addHeader
- javax.servlet.http.HttpServletResponseWrapper.setHeader

## Attack conditions

The vulnerability exists when response headers accept attacker-controlled data without validation.

## Vulnerable Java example

```java
String location = request.getParameter("redirect");
response.setHeader("Location", location);
```

If `location` contains `\r\nSet-Cookie: ...`, the response may be split or manipulated.

## Secure Java example

```java
String location = request.getParameter("redirect");
if (!location.matches("^[A-Za-z0-9/_-]{1,128}$")) {
    response.sendError(HttpServletResponse.SC_BAD_REQUEST);
    return;
}
response.setHeader("Location", "/safe-path");
```

## Detection indicators

- setting `Location`, `Set-Cookie`, or other response headers from request data
- lack of validation for CRLF characters
- unsafe redirect logic based on user input

## Mitigation

- reject CRLF and control characters in header values
- avoid using user-controlled values in response headers
- use fixed redirect paths or allowlists
- encode and validate header data before sending it

## Common false positives

- static header values are safe
- safe redirect codes with fixed internal paths are not vulnerable
