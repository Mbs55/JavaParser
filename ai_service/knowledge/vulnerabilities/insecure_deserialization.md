# Insecure Deserialization

## Overview

Insecure deserialization occurs when untrusted data is deserialized into Java objects without validation. This can allow attackers to trigger code execution, denial of service, or bypass application logic.

## CWE

CWE-502: Deserialization of Untrusted Data

## Relevant Java APIs

- java.io.ObjectInputStream.readObject
- java.io.ObjectInputStream
- org.springframework.http.converter.json.AbstractJackson2HttpMessageConverter
- com.fasterxml.jackson.databind.ObjectMapper.readValue

## Attack conditions

The issue appears whenever untrusted input is deserialized from a byte stream, object stream, XML, or JSON payload that the application trusts too much.

## Vulnerable Java example

```java
ObjectInputStream ois = new ObjectInputStream(request.getInputStream());
Object obj = ois.readObject();
```

This allows attackers to craft object graphs that trigger dangerous behavior when deserialized.

## Secure Java example

```java
ObjectMapper mapper = new ObjectMapper();
MyDto dto = mapper.readValue(request.getInputStream(), MyDto.class);
```

with explicit DTO types and validation rules rather than raw object deserialization.

## Detection indicators

- use of `readObject`, `ObjectInputStream`, or custom deserializers on untrusted inputs
- deserialization of arbitrary classes or binary blobs from network input
- unchecked deserialization of classes with dangerous types

## Mitigation

- deserialize only trusted, typed, minimal DTOs
- reject untrusted binary objects and arbitrary Java object graphs
- use safe serialization formats and validators
- avoid enabling polymorphic typing or custom deserializers for untrusted inputs

## Common false positives

- safe typed JSON deserialization is not the same as arbitrary object deserialization
- internal-only, signed serialization can be acceptable when properly constrained