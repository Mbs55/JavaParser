# Jackson Unsafe Deserialization

## Overview

Jackson unsafe deserialization occurs when user-controlled JSON or XML is deserialized using a configuration that accepts polymorphic types or arbitrary classes without strict validation. This can allow gadget chains and code execution.

## CWE

CWE-502: Deserialization of Untrusted Data

## Relevant Java APIs

- com.fasterxml.jackson.databind.ObjectMapper.readValue
- com.fasterxml.jackson.databind.ObjectMapper.enableDefaultTyping
- com.fasterxml.jackson.databind.jsontype.impl.LaissezFaireSubTypeValidator

## Attack conditions

The risk appears when default typing or polymorphic typing is enabled on untrusted input, allowing attackers to force the deserialization of dangerous classes.

## Vulnerable Java example

```java
ObjectMapper mapper = new ObjectMapper();
mapper.enableDefaultTyping();
MyObject obj = mapper.readValue(input, MyObject.class);
```

This allows type information from the payload to drive class creation.

## Secure Java example

```java
ObjectMapper mapper = new ObjectMapper();
mapper.activateDefaultTyping(
    LaissezFaireSubTypeValidator.instance,
    ObjectMapper.DefaultTyping.NON_FINAL,
    JsonTypeInfo.As.PROPERTY
);
```

or, better, avoid polymorphic deserialization entirely and use strict DTO types.

## Detection indicators

- `enableDefaultTyping`, custom type resolvers, or generic object deserialization
- arbitrary `Object` or `Map` deserialization from untrusted JSON
- use of dangerous type metadata in incoming payloads

## Mitigation

- use fixed DTO classes and strict validation
- disable default typing unless absolutely required
- prefer explicit object schemas over polymorphic serialization
- avoid processing untrusted serialized objects from the network

## Common false positives

- safe, typed JSON mapping into known classes is not dangerous
- an internal-only schema with strict validation can be acceptable when not exposed to untrusted users