# SQL Injection

## Overview

SQL injection occurs when user-controlled input is concatenated into SQL queries without proper validation or parameterization, allowing attackers to alter query logic and access or modify unauthorized data.

## CWE

CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')

## Relevant Java APIs

- java.sql.Statement.executeQuery
- java.sql.Statement.executeUpdate
- java.sql.PreparedStatement
- org.springframework.jdbc.core.JdbcTemplate.query

## Attack conditions

The issue is present whenever dynamic SQL is built from untrusted input or when a query string is modified with tainted values.

## Vulnerable Java example

```java
String username = request.getParameter("username");
String query = "SELECT * FROM users WHERE username = '" + username + "'";
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery(query);
```

This allows attackers to inject additional SQL predicates or comments.

## Secure Java example

```java
String username = request.getParameter("username");
String query = "SELECT * FROM users WHERE username = ?";
PreparedStatement ps = conn.prepareStatement(query);
ps.setString(1, username);
ResultSet rs = ps.executeQuery();
```

## Detection indicators

- string concatenation in SQL queries with request or DB values
- use of `Statement` or dynamic query strings with user input
- raw filtering or search input embedded in repository queries without parameterization

## Mitigation

- use `PreparedStatement` for all user-controlled SQL values
- validate inputs against allowed patterns where appropriate
- keep SQL generation logic separate from user-controlled values
- use ORM or query builders that parameterize inputs safely

## Common false positives

- a fixed SQL string with no dynamic input is not an injection issue
- safe parameterized queries and ORMs are not vulnerable