# JPA / HQL Injection

## Overview

JPA injection occurs when user-controlled input is concatenated into Java Persistence Query Language or SQL queries. This can produce unexpected database access or result sets.

## CWE

CWE-564: SQL Injection: Hibernate

## Relevant Java APIs

- jakarta.persistence.EntityManager.createQuery
- jakarta.persistence.EntityManager.createNativeQuery
- jakarta.persistence.EntityManager.createNamedQuery
- javax.persistence.EntityManager.createQuery
- org.hibernate.Session.createQuery
- org.hibernate.Session.createNativeQuery
- org.hibernate.Session.createSQLQuery

## Attack conditions

This issue appears when untrusted data is directly mixed into query strings, especially in JPA/Hibernate queries or native SQL.

## Vulnerable Java example

```java
String role = request.getParameter("role");
String jpql = "select u from User u where u.role = '" + role + "'";
Query query = entityManager.createQuery(jpql);
List<User> users = query.getResultList();
```

An attacker can inject query logic or alter the WHERE clause.

## Secure Java example

```java
String role = request.getParameter("role");
String jpql = "select u from User u where u.role = :role";
Query query = entityManager.createQuery(jpql);
query.setParameter("role", role);
List<User> users = query.getResultList();
```

## Detection indicators

- `createQuery` or `createNativeQuery` with string concatenation
- values from request parameters, headers, or cookies inserted into query strings
- dynamic `WHERE`, `ORDER BY`, or `SELECT` fragments coming from user input

## Mitigation

- prefer parameter binding and named parameters
- avoid concatenating user data into JPQL or SQL strings
- validate any dynamic query elements, such as sort columns or entity names
- use typed criteria builders when dynamic queries are required

## Common false positives

- criteria queries built from constants are safe
- binding a trusted value as a parameter is not a vulnerability
