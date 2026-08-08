# Bean Property Injection

## Overview

Bean property injection is an unsafe pattern where untrusted input is bound to Java bean properties or object fields. This can lead to mass-assignment, property override, or reflection-based mutation of application state.

## CWE

CWE-915: Improperly Controlled Modification of Dynamically-Determined Object Attributes

## Relevant Java APIs

- org.apache.commons.beanutils.BeanUtils.copyProperties
- org.apache.commons.beanutils.BeanUtils.populate
- org.apache.commons.beanutils.BeanUtilsBean.populate
- org.springframework.beans.BeanUtils.copyProperties

## Attack conditions

This issue appears when user-controlled data is copied into arbitrary bean properties without a whitelist.

## Vulnerable Java example

```java
String name = request.getParameter("name");
String role = request.getParameter("role");

User user = new User();
BeanUtils.populate(user, request.getParameterMap());
```

If an attacker sends unexpected property names, the framework may overwrite internal fields such as `isAdmin` or `enabled`.

## Secure Java example

```java
Map<String, String> params = request.getParameterMap();
User user = new User();
for (String key : List.of("firstName", "lastName", "email")) {
    if (params.containsKey(key)) {
        BeanUtils.setProperty(user, key, params.get(key)[0]);
    }
}
```

## Detection indicators

- `BeanUtils.populate`, `copyProperties`, or request parameter maps applied to domain objects
- dynamic property binding without allowlist validation
- assignment of request parameters to arbitrary object fields
- role, admin, or privilege fields bound directly from user input

## Mitigation

- bind only allowlisted attributes
- reject unknown or unexpected property names
- do not map raw request parameters directly to security-sensitive fields
- use explicit DTOs and validation
- verify the value types and ranges before assignment

## Common false positives

- binding only a fixed DTO with explicit fields is not automatically dangerous
- safe conversion with a small allowlist is acceptable

## Spring notes

Spring `BeanUtils` can help with copy operations, but it is still unsafe when used to copy untrusted data into security-sensitive beans without validation.
