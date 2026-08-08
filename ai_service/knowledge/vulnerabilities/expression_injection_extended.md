# Expression Injection Extended

## Overview

Expression injection refers to sending user-controlled content into expression engines such as SpEL, JEXL, or EL, allowing the engine to evaluate untrusted logic.

## CWE

CWE-917: Improper Neutralization of Special Elements used in an Expression Language Statement

## Relevant Java APIs

- org.springframework.expression.ExpressionParser.parseExpression
- org.springframework.expression.Expression.getValue
- org.apache.commons.jexl3.JexlEngine.createExpression
- org.apache.commons.jexl3.JexlScript.execute

## Attack conditions

The issue appears when user input is interpreted as an expression rather than as a literal string or validated value.

## Vulnerable Java example

```java
String expr = request.getParameter("expr");
JexlEngine engine = new JexlBuilder().create();
JexlExpression expression = engine.createExpression(expr);
Object result = expression.evaluate(context);
```

If the input can include method calls or object access, the app may execute logic beyond its intended behavior.

## Secure Java example

```java
String expr = request.getParameter("expr");
if (!expr.matches("^[A-Za-z0-9_]{1,32}$")) {
    throw new IllegalArgumentException("Invalid expression");
}

// Use direct application logic instead of evaluating arbitrary expressions.
```

## Mitigation

- avoid allowing free-form expressions from users
- use allowlists or fixed business logic
- disable unsafe expression functionality in the engine
- validate against a known subset of safe identifiers
