# Weak Access Control

## Overview

Weak access control occurs when the application allows broad access or uses weak authorization patterns, allowing users to exceed their intended permissions.

## CWE

CWE-284: Improper Access Control

## Relevant Java APIs

- org.springframework.security.access.prepost.PreAuthorize
- java.util.Set.contains
- javax.servlet.http.HttpServletRequest.isUserInRole
- org.springframework.security.core.authority.SimpleGrantedAuthority

## Attack conditions

The app authorizes by incomplete checks, default allow behavior, or checks that are not performed on all sensitive flows.

## Vulnerable Java example

```java
if (request.isUserInRole("USER")) {
    // user can access admin functions
}
```

This may allow roles that are broader than intended or missing a stronger privilege check.

## Secure Java example

```java
@PreAuthorize("hasRole('ADMIN') and hasAuthority('READ_ALL_USERS')")
public List<User> getUsers() {
    return userService.findAll();
}
```

## Detection indicators

- broad allowlists or role checks missing exact permission matches
- permissive default access in security rules
- authorization policies enforced only on some parts of the application

## Mitigation

- enforce least privilege with precise roles and permissions
- validate access in service and domain layers
- deny by default and allow only specific permissions
- test authorization boundaries with security-focused regression checks

## Common false positives

- role names may be intentionally broad for lower-risk functions and still be appropriate