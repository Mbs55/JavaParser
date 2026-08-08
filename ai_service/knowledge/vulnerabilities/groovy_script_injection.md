# Groovy Script Injection

## Overview

Groovy script injection occurs when untrusted input is executed as a Groovy script or expression. This can allow attackers to execute arbitrary code inside the application runtime.

## CWE

CWE-94: Improper Control of Generation of Code ('Code Injection')

## Relevant Java APIs

- groovy.lang.GroovyShell.evaluate
- groovy.util.GroovyScriptEngine.run
- javax.script.ScriptEngineManager
- javax.script.ScriptEngine.eval

## Attack conditions

The risk appears when an application allows user-controlled strings to be compiled or evaluated as code.

## Vulnerable Java example

```java
String script = request.getParameter("script");
GroovyShell shell = new GroovyShell();
Object result = shell.evaluate(script);
```

This effectively executes attacker-controlled code inside the Java process.

## Secure Java example

```java
String script = request.getParameter("script");
if (!script.matches("^[A-Za-z0-9_\s]{1,64}$")) {
    throw new SecurityException("Invalid script input");
}
// Prefer fixed application logic over runtime script evaluation.
```

## Detection indicators

- use of `GroovyShell`, `ScriptEngine`, or similar dynamic interpreters with user input
- runtime code generation from request or database values
- expressions embedded into rules engines or calculators without validation

## Mitigation

- avoid executing scripts from untrusted input
- use a restricted or sandboxed interpreter if script execution is truly required
- allowlist permitted commands and identifiers
- enforce least-privilege execution and no direct access to privileged classes
