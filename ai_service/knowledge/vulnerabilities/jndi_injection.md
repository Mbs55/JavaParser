# JNDI Injection

## Overview

JNDI injection occurs when attacker-controlled data is used in JNDI lookups or directory operations. This can expose internal resources, force lookup of unexpected objects, or access arbitrary naming services.

## CWE

CWE-74: Improper Neutralization of Special Elements in Output Used by a Downstream Component ('Injection')

## Relevant Java APIs

- javax.naming.Context.lookup
- javax.naming.Context.lookupLink
- javax.naming.InitialContext.lookup
- javax.naming.InitialContext.bind
- javax.naming.InitialContext.rebind
- javax.naming.directory.InitialDirContext.lookup
- javax.naming.ldap.InitialLdapContext.lookup
- org.springframework.jndi.JndiTemplate.lookup
- org.springframework.jndi.JndiLocatorDelegate.lookup

## Attack conditions

This is dangerous when the application accepts a user-controlled name, service, or JNDI path and passes it directly to a directory lookup.

## Vulnerable Java example

```java
String name = request.getParameter("jndiName");
InitialContext ctx = new InitialContext();
Object obj = ctx.lookup(name);
```

If an attacker provides a malicious JNDI name, the application may resolve an untrusted object or internal service.

## Secure Java example

```java
String input = request.getParameter("jndiName");
Set<String> allowed = Set.of("jdbc/primary", "jdbc/archive");
if (!allowed.contains(input)) {
    throw new IllegalArgumentException("Invalid JNDI name");
}

InitialContext ctx = new InitialContext();
Object obj = ctx.lookup("java:comp/env/" + input);
```

## Detection indicators

- `lookup`, `bind`, `rebind`, or `InitialContext` usage with request data
- dynamic JNDI names built from user input
- no allowlist for valid service names

## Mitigation

- restrict JNDI lookups to a fixed allowlist
- avoid exposing internal service names to end users
- use safe names and environment configuration instead of dynamic naming
- validate inputs before performing directory access

## Framework notes

Spring JNDI access should also be constrained to trusted names and not built from untrusted input.
