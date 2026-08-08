# Unsafe Reflection

## Overview

Unsafe reflection allows code to inspect and invoke arbitrary classes, methods, or fields using reflective APIs without validating the target. This can bypass business rules and expose internal APIs.

## CWE

CWE-470: Use of Externally-Controlled Input to Select Classes or Code ('Unsafe Reflection')

## Relevant Java APIs

- java.lang.Class.forName
- java.lang.reflect.Method.invoke
- java.lang.reflect.Field.get
- java.lang.Class.getDeclaredMethod

## Attack conditions

The application binds reflective calls to data from a client or external system without restricting the resource being accessed.

## Vulnerable Java example

```java
String methodName = request.getParameter("method");
Method m = MyService.class.getMethod(methodName);
m.invoke(service, args);
```

An attacker may trigger unintended methods or access protected internals.

## Secure Java example

```java
String methodName = request.getParameter("method");
if (!Set.of("getUser", "saveUser").contains(methodName)) {
    throw new IllegalArgumentException("Invalid method");
}
Method m = MyService.class.getMethod(methodName);
m.invoke(service, args);
```

## Detection indicators

- reflective invocation of methods or fields from user-controlled strings
- dynamic class discovery without allowlists
- uses of `forName`, `getDeclaredMethod`, or `invoke` on security-sensitive classes

## Mitigation

- restrict reflective targets to a fixed allowlist
- avoid exposing reflective APIs to end users
- prefer ordinary method calls over reflection when possible
- review all reflective access for privilege escalation risks

## Common false positives

- internal framework use of reflection can be safe when the set of classes is fixed and not externally controlled