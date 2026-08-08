# Script Engine Injection

## Overview

Script engine injection happens when a Java application evaluates user-controlled expressions using a scripting engine, enabling code execution or dangerous logic evaluation.

## CWE

CWE-94: Improper Control of Generation of Code ('Code Injection')

## Relevant Java APIs

- javax.script.ScriptEngineManager
- javax.script.ScriptEngine.eval
- javax.script.Invocable.invokeFunction

## Attack conditions

The application directly evaluates untrusted strings as scripts or code fragments.

## Vulnerable Java example

```java
String expression = request.getParameter("expression");
ScriptEngine engine = new ScriptEngineManager().getEngineByName("JavaScript");
Object result = engine.eval(expression);
```

This can run attacker-controlled JavaScript or script logic.

## Secure Java example

```java
String expression = request.getParameter("expression");
if (!expression.matches("^[A-Za-z0-9_]{1,64}$")) {
    throw new IllegalArgumentException("Invalid expression");
}
// Use explicit application logic instead of script evaluation.
```

## Detection indicators

- use of `ScriptEngineManager` and `eval` with request values
- dynamic rule evaluation from user inputs
- execution of code fragments from database or configuration

## Mitigation

- avoid allowing arbitrary scripts from untrusted users
- validate input against a strict allowlist
- restrict script execution environment and permissions
- prefer dedicated application logic over dynamic script evaluation
