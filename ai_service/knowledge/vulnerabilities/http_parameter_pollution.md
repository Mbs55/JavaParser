# HTTP Parameter Pollution

## Overview

HTTP Parameter Pollution occurs when an application accepts multiple values for the same request parameter and uses them in ways that change control flow, business logic, or forwarded requests. This can lead to bypasses in validation and unsafe downstream behavior.

## CWE

CWE-235: Improper Handling of Extra Parameters

## Relevant Java APIs

- javax.servlet.http.HttpServletRequest.getParameter
- javax.servlet.http.HttpServletRequest.getParameterValues
- javax.servlet.http.HttpServletRequest.getParameterMap
- jakarta.servlet.http.HttpServletRequest.getParameter
- org.springframework.web.bind.annotation.RequestParam

## Attack conditions

The risk appears when the app reads repeated query or form parameters and treats them as a single value without normalization or validation.

## Vulnerable Java example

```java
String username = request.getParameter("username");
String role = request.getParameter("role");

if ("admin".equals(role)) {
    // sensitive path
}
```

Multiple parameter entries like `role=admin&role=user` may be evaluated inconsistently depending on the server framework.

## Secure Java example

```java
String[] values = request.getParameterValues("role");
if (values == null || values.length != 1) {
    response.sendError(HttpServletResponse.SC_BAD_REQUEST);
    return;
}

String role = values[0];
if (!Set.of("user", "admin").contains(role)) {
    response.sendError(HttpServletResponse.SC_BAD_REQUEST);
    return;
}
```

## Detection indicators

- reading multiple parameter values without checking duplicates
- using request parameter maps directly in redirects, filters, or database queries
- acceptance of duplicate parameters in security-sensitive contexts

## Mitigation

- reject duplicate or ambiguous parameters for trusted actions
- normalize parameter maps before validation
- use single-value extraction for sensitive fields
- perform explicit allowlist checks for all policy values

## Spring notes

Spring `@RequestParam` is safe only when the controller is configured to expect a single value and rejects ambiguous inputs.
