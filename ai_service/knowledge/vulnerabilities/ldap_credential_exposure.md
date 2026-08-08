# LDAP Credential Exposure

## Overview

LDAP credential exposure occurs when directory credentials or connection details are stored or logged in a way that leaks sensitive information. This can enable unauthorized directory access or impersonation.

## CWE

CWE-532: Insertion of Sensitive Information into Log File

## Relevant Java APIs

- javax.naming.ldap.InitialLdapContext
- javax.naming.directory.DirContext
- com.unboundid.ldap.sdk.LDAPConnection

## Attack conditions

The issue appears when directory bind credentials, passwords, or secret values are written to logs, stack traces, or error output.

## Vulnerable Java example

```java
String user = request.getParameter("user");
String pass = request.getParameter("pass");
logger.error("LDAP login failed for user={} pass={}", user, pass);
```

This exposes passwords to logs.

## Secure Java example

```java
logger.info("LDAP login failed for user={}", user);
```

and ensure the password is never logged or stored in plain form.

## Detection indicators

- logging bind credentials, LDAP DN strings with passwords, or connection details
- using raw credentials in diagnostic output
- secrets stored in connection code without secure secret retrieval

## Mitigation

- never log LDAP credentials or passwords
- use secure secret stores for bind passwords
- restrict access to directory services and review logging policies
- monitor for accidental secret leaks in logs and exceptions
