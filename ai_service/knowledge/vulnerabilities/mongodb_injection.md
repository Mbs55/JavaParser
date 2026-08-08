# MongoDB Injection

## Overview

MongoDB injection occurs when attacker-controlled input is used to construct Mongo queries or update operations. This can lead to unauthorized reads, writes, or application logic bypass.

## CWE

CWE-943: Improper Neutralization of Special Elements in Data Query Logic

## Relevant Java APIs

- com.mongodb.client.MongoCollection.find
- com.mongodb.client.MongoCollection.updateOne
- com.mongodb.client.MongoCollection.deleteOne
- org.springframework.data.mongodb.core.MongoTemplate.find
- org.springframework.data.mongodb.core.MongoTemplate.updateFirst
- org.springframework.data.mongodb.core.MongoTemplate.remove

## Attack conditions

The issue appears when user data is concatenated into a Mongo query object, filter, or update document without validation or safe query construction.

## Vulnerable Java example

```java
String user = request.getParameter("user");
Document filter = new Document("username", user);
MongoCollection<Document> collection = mongoDatabase.getCollection("users");
collection.find(filter);
```

If the application accepts and stores complex query structures or unsafely merges user input into BSON objectives, query semantics can be changed.

## Secure Java example

```java
String user = request.getParameter("user");
if (!user.matches("^[A-Za-z0-9_@.-]{1,64}$")) {
    throw new IllegalArgumentException("Invalid username");
}

Document filter = new Document("username", user);
MongoCollection<Document> collection = mongoDatabase.getCollection("users");
collection.find(filter).first();
```

## Detection indicators

- building Mongo filters from untrusted input
- dynamic update operations with request-supplied field names or values
- missing validation on query objects or projection data

## Mitigation

- validate user input before building query filters
- use typed query APIs and parameter binding where available
- do not allow user-controlled field names or complex operators in queries
- keep mongo query construction strict and allowlisted

## Spring notes

The Spring `MongoTemplate` API is safe only when the filters and update criteria are built from validated values instead of raw request strings.
