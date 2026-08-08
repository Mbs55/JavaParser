# LDAP Injection

## Overview

LDAP injection occurs when untrusted input is used to construct an LDAP filter, DN, or search request without proper neutralization. This can let an attacker alter directory queries and bypass access controls or reveal sensitive entries.

## CWE

CWE-90: Improper Neutralization of Special Elements used in an LDAP Query ('LDAP Injection')

## Relevant Java APIs

- javax.naming.directory.SearchControls
- javax.naming.directory.InitialDirContext
- javax.naming.ldap.InitialLdapContext
- com.unboundid.ldap.sdk.Filter.create

## Attack conditions

The app builds a directory query from user-controlled values without escaping or validating special characters.

## Vulnerable Java example

```java
String user = request.getParameter("user");
String filter = "(uid=" + user + ")";
NamingEnumeration<SearchResult> results = ctx.search("ou=people", filter, controls);
```

If `user` contains `*)(|(uid=*` an attacker may broaden or alter the query.

## Secure Java example

```java
String user = request.getParameter("user");
String safeUser = user.replaceAll("[()\\*]", "");
String filter = "(uid=" + safeUser + ")";
NamingEnumeration<SearchResult> results = ctx.search("ou=people", filter, controls);
```

## Detection indicators

- building LDAP filters with string concatenation from request parameters
- directly embedding username/email or role values into DN or search strings
- no sanitization or escaping of LDAP special characters

## Mitigation

- escape LDAP special characters before composing filters or DNs
- validate against allowed patterns (for example, usernames or group names)
- prefer security libraries that build filters programmatically
- use least privilege LDAP service accounts
