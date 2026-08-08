# Open Redirect

## Overview

Open redirect vulnerabilities allow attackers to trick users into visiting malicious external destinations by controlling a redirect target. This is especially dangerous in login flows, password resets, or trust-based redirects.

## CWE

CWE-601: URL Redirection to Untrusted Site ('Open Redirect')

## Relevant Java APIs

- javax.servlet.http.HttpServletResponse.sendRedirect
- jakarta.servlet.http.HttpServletResponse.sendRedirect
- org.springframework.web.servlet.mvc.support.RedirectAttributes
- org.springframework.web.servlet.view.RedirectView

## Attack conditions

The app sends a redirect based on user-controlled input without validating that the new URL is trusted or relative.

## Vulnerable Java example

```java
String next = request.getParameter("next");
response.sendRedirect(next);
```

Any external URL can be used for phishing or abuse.

## Secure Java example

```java
String next = request.getParameter("next");
if (!next.startsWith("/")) {
    throw new IllegalArgumentException("Invalid redirect target");
}
response.sendRedirect(next);
```

## Detection indicators

- redirect targets derived from request parameters or URL values
- `sendRedirect` calls with little or no validation
- user-controlled return URLs after login or logout

## Mitigation

- allow only relative internal paths or strict allowlisted destinations
- validate hostnames and schemes before redirecting
- reject absolute URLs and unknown domains
- prefer server-side canonicalization over client-side redirects

## Common false positives

- redirects to a trusted application-owned domain may be safe if validated and allowlisted
- public static redirects to known safe URLs are not a vulnerability