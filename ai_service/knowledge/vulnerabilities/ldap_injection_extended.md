# LDAP Injection Extended

## Overview

LDAP injection happens when attacker-controlled input is inserted into an LDAP filter or DN query. The result is that the application may query unintended directories, bypass authorization, or expose directory contents.

## CWE

CWE-90: Improper Neutralization of Special Elements used in an LDAP Query ('LDAP Injection')

## Relevant Java APIs

- org.springframework.ldap.core.LdapTemplate.search
- org.springframework.ldap.core.LdapTemplate.lookup
- org.springframework.ldap.core.LdapTemplate.authenticate
- org.springframework.ldap.filter.EqualsFilter
- org.springframework.ldap.filter.AndFilter
- org.springframework.ldap.filter.OrFilter
- com.unboundid.ldap.sdk.Filter.create
- com.unboundid.ldap.sdk.LDAPConnection.search

## Attack conditions

This occurs when a filter string such as `(uid={user})` is built from untrusted input without escaping or validation.

## Vulnerable Java example

```java
String user = request.getParameter("user");
String filter = "(uid=" + user + ")";
List<SearchResult> results = ldapTemplate.search("ou=users", filter, (ctx, attrs) -> true);
```

A value such as `*)(|(uid=*))` can alter the query semantics.

## Secure Java example

```java
String user = request.getParameter("user");
if (!user.matches("^[A-Za-z0-9._-]{1,32}$")) {
    throw new IllegalArgumentException("Invalid username");
}

String filter = "(uid={0})";
List<SearchResult> results = ldapTemplate.search("ou=users", filter, new Object[] { user }, (ctx, attrs) -> true);
```

This uses parameterized LDAP filter building and validation.

## Detection indicators

- `search`, `lookup`, or `filter` operations with dynamic string concatenation
- untrusted user data inserted into LDAP DN or filter values
- missing validation or escaping around LDAP special characters

## Mitigation

- build LDAP filters with parameterized APIs or safe filter builders
- escape LDAP special characters such as `*`, `(`, `)`, `\`, and `NUL`
- validate usernames and directory values with allowlists
- do not pass untrusted input to DN or filter templates

## False positives

- fixed LDAP query strings are safe
- parameterized safe filters are not vulnerable
