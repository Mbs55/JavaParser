# Missing Authorization

## Overview

Missing authorization happens when application routes or methods allow access without verifying the current user has the required permission. This differs from broken access control in that authorization is absent or bypassed entirely.

## CWE

CWE-862: Missing Authorization

## Relevant Java APIs

- org.springframework.security.access.prepost.PreAuthorize
- org.springframework.security.config.annotation.web.configuration.EnableWebSecurity
- jakarta.servlet.Filter
- javax.servlet.Filter

## Attack conditions

The app exposes an action or resource without requiring the user to possess an allowed role or permission.

## Vulnerable Java example

```java
@GetMapping("/reports")
public List<Report> listReports() {
    return reportService.getReports();
}
```

This route is accessible to any caller.

## Secure Java example

```java
@GetMapping("/reports")
@PreAuthorize("hasRole('ADMIN')")
public List<Report> listReports() {
    return reportService.getReports();
}
```

## Detection indicators

- endpoints or methods available without Security annotations or checks
- authorization checks missing on state-changing or sensitive actions
- role restrictions only in UI code or not enforced server-side

## Mitigation

- require authorization on every sensitive action
- enforce access checks in the controller and service layers
- centralize permission policies and validate them consistently
- deny by default and explicitly allow only minimal permission sets

## Common false positives

- public static content or health checks are not necessarily incorrect if they are intended to be accessible
- a general security filter may provide authorization without the route itself requiring explicit annotations