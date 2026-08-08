# Hardcoded Credentials

## Overview

Hardcoded credentials occur when usernames, passwords, tokens, or API keys are embedded directly in source code or configuration files. Attackers who obtain the code or binary can reuse them.

## CWE

CWE-798: Use of Hard-coded Credentials

## Relevant Java APIs

- javax.naming.InitialContext
- java.sql.DriverManager.getConnection
- org.springframework.jdbc.datasource.DriverManagerDataSource
- com.amazonaws.auth.BasicAWSCredentials

## Attack conditions

This is present whenever account credentials are stored in strings or resource files without secure secret management.

## Vulnerable Java example

```java
String dbUser = "admin";
String dbPassword = "P@ssw0rd";
Connection conn = DriverManager.getConnection("jdbc:mysql://db/app", dbUser, dbPassword);
```

## Secure Java example

```java
String dbUser = System.getenv("DB_USER");
String dbPassword = System.getenv("DB_PASSWORD");
Connection conn = DriverManager.getConnection("jdbc:mysql://db/app", dbUser, dbPassword);
```

## Detection indicators

- literal strings such as `password`, `secret`, `token`, or `apiKey` in code
- database credentials embedded in `application.properties` without encryption
- default account names or passwords left in test or production code

## Mitigation

- store secrets in environment variables, vaults, or secure secret managers
- rotate any hardcoded credentials immediately
- avoid default credentials in code or configuration
- scan code for password-like names before release

## Common false positives

- examples in docs or tests are not a production flaw if they are intentionally fake
- environment injection is fine as long as secrets are not committed to source control