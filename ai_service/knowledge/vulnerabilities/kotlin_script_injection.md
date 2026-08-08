# Kotlin Script Injection

## Overview

Kotlin script injection occurs when untrusted input is executed through a Kotlin scripting engine or interpreter. This can execute arbitrary code or expose runtime internals.

## CWE

CWE-94: Improper Control of Generation of Code ('Code Injection')

## Relevant Java APIs

- javax.script.ScriptEngineManager
- javax.script.ScriptEngine.eval
- org.jetbrains.kotlin.script.jsr223.KotlinJsr223JvmLocalScriptEngine

## Attack conditions

The issue appears when user-provided script text is compiled or executed dynamically as Kotlin or JavaScript-like code.

## Vulnerable Java example

```java
String expression = request.getParameter("expression");
ScriptEngine engine = new ScriptEngineManager().getEngineByName("kotlin");
Object result = engine.eval(expression);
```

## Secure Java example

```java
String expression = request.getParameter("expression");
if (!expression.matches("^[A-Za-z0-9_]{1,32}$")) {
    throw new IllegalArgumentException("Invalid expression");
}
// Prefer explicit business logic rather than dynamic scripting.
```

## Detection indicators

- runtime scripting engines with untrusted strings
- DSL or rule evaluation from user input without validation
- script execution in a web-facing endpoint

## Mitigation

- disable runtime script execution from untrusted content
- use strict allowlists for script names or expressions
- avoid evaluation of user-supplied code entirely when a fixed parser or logic engine is possible
