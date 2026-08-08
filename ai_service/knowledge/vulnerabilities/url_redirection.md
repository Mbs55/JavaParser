# URL Redirection

## Overview

URL redirection occurs when an application sends a redirect to a location supplied by user input or external data. This is often exploited for phishing or open redirect attacks.

## CWE

CWE-601: Improper Restriction of Operations within the Bounds of a Restricted URL

## Relevant Java APIs

- java.net.URI.create
- java.net.URI
- java.net.URL
- java.net.URL.toURI
- org.springframework.web.util.UriComponentsBuilder.fromUriString
- org.springframework.web.util.UriComponentsBuilder.fromHttpUrl

## Attack conditions

The risk appears when a redirect target is assembled from request parameters or untrusted data without allowlisting or validation.

## Vulnerable Java example

```java
String target = request.getParameter("next");
response.sendRedirect(target);
```

This allows an attacker to redirect users to phishing or malicious destinations.

## Secure Java example

```java
String target = request.getParameter("next");
if (!Set.of("/home", "/profile", "/dashboard").contains(target)) {
    response.sendError(HttpServletResponse.SC_BAD_REQUEST);
    return;
}
response.sendRedirect(target);
```

## Detection indicators

- sending redirects to request-controlled URLs
- building destinations from untrusted strings
- trust of external redirect URLs without validation

## Mitigation

- use an allowlist of internal paths or safe domains
- reject external or malformed redirect targets
- validate user-supplied URLs before use
- prefer fixed internal redirect destinations for auth flows

## Spring notes

Spring URL builders are useful, but they do not make redirect input safe if the final value is untrusted.
