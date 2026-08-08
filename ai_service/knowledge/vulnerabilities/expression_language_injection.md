# Expression Language Injection

## Overview

Expression language injection occurs when attacker-controlled input is evaluated as a script or expression by a Java expression engine. In Java applications, this commonly affects JSP EL, SpEL, or JEXL execution.

## CWE

CWE-917: Improper Neutralization of Special Elements used in an Expression Language Statement

## Relevant Java APIs

- javax.el.ExpressionFactory.createMethodExpression
- javax.el.ExpressionFactory.createValueExpression
- org.springframework.expression.ExpressionParser.parseExpression
- org.springframework.expression.spel.standard.SpelExpressionParser.parseExpression
- org.apache.commons.jexl3.JexlEngine.createExpression
- org.apache.commons.jexl3.JexlExpression.evaluate

## Attack conditions

The vulnerability exists when untrusted input is passed directly into an expression interpreter without sandboxing, validation, or allowlisting.

## Vulnerable Java example

```java
String expression = request.getParameter("expression");
ExpressionParser parser = new SpelExpressionParser();
Object value = parser.parseExpression(expression).getValue(context);
```

If the input is `T(java.lang.Runtime).getRuntime().exec("calc")`, the application evaluates attacker-controlled code.

## Secure Java example

```java
String userInput = request.getParameter("expression");
if (!userInput.matches("^[A-Za-z0-9_\\s]{1,32}$")) {
    throw new IllegalArgumentException("Invalid expression");
}

ExpressionParser parser = new SpelExpressionParser();
Object value = parser.parseExpression("#root").getValue(context);
```

The safer pattern is to avoid interpreting free-form user input as expressions and instead use explicit business logic.

## Detection indicators

- `parseExpression`, `createValueExpression`, `createMethodExpression`, or `JexlEngine` use with request parameters
- evaluation of user-controlled expressions
- missing allowlist or restricted expression context

## Mitigation

- do not parse user-controlled expressions
- restrict the expression language to a safe subset
- use allowlists for functions and property names
- avoid exposing expression engines to untrusted data
- validate all expression input before evaluation

## Framework guidance

Spring Expression Language is powerful but unsafe if used on request data without restrictions.

## False positives

- using expression engines for fixed internal configuration is not a vulnerability
- parameterized evaluation of trusted values is fine
