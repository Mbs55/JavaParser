# Trust Boundary Violation

## Overview

A trust boundary violation occurs when an application treats data from a less trusted layer as if it were safe, such as trusting user input or client-side values for security decisions.

## CWE

CWE-501: Trust Boundary Violation

## Relevant Java APIs

- javax.servlet.http.HttpServletRequest.getParameter
- jakarta.servlet.http.HttpServletRequest.getParameter
- org.springframework.web.bind.annotation.RequestHeader
- org.springframework.web.bind.annotation.CookieValue

## Attack conditions

Security-sensitive decisions are made based on values supplied by clients without server-side validation or verification.

## Vulnerable Java example

```java
String isAdmin = request.getParameter("isAdmin");
if ("true".equalsIgnoreCase(isAdmin)) {
    grantAdminAccess();
}
```

This trusts a client-controlled flag.

## Secure Java example

```java
Authentication auth = SecurityContextHolder.getContext().getAuthentication();
if (auth != null && auth.getAuthorities().stream().anyMatch(a -> a.getAuthority().equals("ROLE_ADMIN"))) {
    grantAdminAccess();
}
```

## Detection indicators

- security decisions based on request parameters, cookies, or headers without validation
- authorization or privilege checks controlled by client-supplied values
- trust of browser-provided metadata in server-side policy enforcement

## Mitigation

- enforce all privileged checks on the server using authenticated identity and authorization
- never trust client-side flags for authorization or policy decisions
- validate and re-derive trust from server-side state
- centralize security policy in the application domain, not in the UI or request values
