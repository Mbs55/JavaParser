# Broken Access Control

## Summary

Broken access control is when a Java application fails to enforce authorization consistently, allowing users to reach endpoints, data, or actions they should not access. This is a common application-layer issue, especially in REST, MVC, and Spring Security applications.

## CWE

CWE-284: Improper Access Control

## Relevant Java APIs

- javax.servlet.http.HttpServletRequest
- jakarta.servlet.http.HttpServletRequest
- org.springframework.security.access.prepost.PreAuthorize
- org.springframework.security.core.Authentication
- org.springframework.security.web.access.expression.WebSecurityExpressionRoot

## Vulnerable Java example

```java
@GetMapping("/admin/users/{id}")
public User getUser(@PathVariable Long id) {
    return userService.findById(id);
}
```

If the controller does not validate the current user’s role or ownership, any caller may enumerate or modify restricted records.

## Secure Java example

```java
@GetMapping("/admin/users/{id}")
@PreAuthorize("hasRole('ADMIN')")
public User getUser(@PathVariable Long id) {
    return userService.findById(id);
}
```

## Detection indicators

- missing method-level or URL-level authorization
- direct ID lookup without ownership checks
- role checks only on some endpoints or actions
- trust of client-supplied IDs or permission flags

## Mitigation

- enforce authorization at every boundary
- validate access using both role and resource ownership checks
- deny by default and allow only explicit authorized cases
- centralize access rules in service methods and security config
- ensure authorization is enforced on both API and UI layers

## Common false positives

- a route protected by a generic security rule is not automatically broken access control
- a service-layer check may be safe even when a controller is not directly protected, if the service denies unauthorized calls
