# NoSQL Injection

## Overview

NoSQL injection occurs when user-controlled data alters the logic of a NoSQL query. This can affect MongoDB, Redis, and other document or key-value stores.

## CWE

CWE-943: Improper Neutralization of Special Elements in Data Query Logic

## Relevant Java APIs

- com.mongodb.client.MongoCollection.find
- com.mongodb.client.MongoCollection.aggregate
- org.springframework.data.mongodb.core.MongoTemplate.find
- org.springframework.data.mongodb.core.MongoTemplate.aggregate
- org.springframework.data.redis.core.RedisTemplate.execute
- org.springframework.data.redis.core.RedisTemplate.executePipelined

## Attack conditions

The issue appears when query objects, JSON documents, or Redis script execution commands are built from untrusted data.

## Vulnerable Java example

```java
String query = request.getParameter("query");
Document filter = new Document("$where", "this.user == '" + query + "'");
collection.find(filter);
```

This allows attackers to manipulate query semantics.

## Secure Java example

```java
String user = request.getParameter("user");
if (!user.matches("^[A-Za-z0-9_@.-]{1,64}$")) {
    throw new IllegalArgumentException("Invalid user");
}

Document filter = new Document("user", user);
collection.find(filter);
```

## Detection indicators

- user-controlled values combined into query objects or script strings
- `$where`, `$regex`, or dynamic conditions built from request input
- Redis calls using dynamic Lua or script payloads

## Mitigation

- validate and constrain user data before building queries
- use safe query builders and typed values
- avoid dynamic field names and operator injection
- restrict Redis script execution to trusted internal calls

## False positives

- safe fixed query objects are not a vulnerability
- parameterized query object construction is usually safe
