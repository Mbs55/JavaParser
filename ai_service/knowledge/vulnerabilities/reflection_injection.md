# Reflection Injection

## Overview

Reflection injection occurs when untrusted input is used to select or invoke methods, classes, or fields via Java reflection. This can bypass normal type checks and produce dangerous behavior or access privileged members.

## CWE

CWE-470: Use of Externally-Controlled Input to Select Classes or Code ('Unsafe Reflection')

## Relevant Java APIs

- java.lang.Class.forName
- java.lang.reflect.Method.invoke
- java.lang.reflect.Field.set
- java.lang.Class.newInstance

## Attack conditions

The application accepts a class or method name from a client or external input and then invokes it without validating the target.

## Vulnerable Java example

```java
String className = request.getParameter("className");
Class<?> clazz = Class.forName(className);
Object instance = clazz.getDeclaredConstructor().newInstance();
```

This allows arbitrary class loading and invocation based on attacker input.

## Secure Java example

```java
String className = request.getParameter("className");
if (!Set.of("OrderService", "UserService").contains(className)) {
    throw new IllegalArgumentException("Invalid class");
}
Class<?> clazz = OrderService.class;
```

## Detection indicators

- `Class.forName` with user-controlled strings
- reflection-based method invocation with unvalidated names
- dynamic class loading from user, file, or URL inputs

## Mitigation

- avoid reflection for user-controlled class selection
- use explicit typed code or a narrow allowlist of valid classes/methods
- reject unknown values before invoking reflective code
- restrict reflective access to private members when necessary

## Common false positives

- reflection used only for internal frameworks or controlled plugin registration may be fine if the target list is fixed and validated