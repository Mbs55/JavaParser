# Command Injection

## Overview

Command injection happens when untrusted input is used to construct an operating-system command. In Java, the high-risk entry points are `Runtime.exec(...)`, `ProcessBuilder`, and shell wrappers.

## CWE

CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')

## Relevant Java APIs

- java.lang.Runtime.exec
- java.lang.ProcessBuilder
- java.lang.ProcessBuilder.command
- scala.sys.process.Process$.apply

## Attack conditions

The pattern is present when untrusted data is concatenated into the command string or argument array without validation and without separating data from command.

## Vulnerable Java example

```java
String userInput = request.getParameter("cmd");
Process p = Runtime.getRuntime().exec("cmd /c " + userInput);
```

If `userInput` is `whoami & del C:\\important.txt`, the shell executes the extra command as well.

## Secure Java example

```java
String userInput = request.getParameter("cmd");
List<String> allowed = List.of("whoami", "hostname");
if (!allowed.contains(userInput)) {
    throw new IllegalArgumentException("Invalid command");
}

ProcessBuilder pb = new ProcessBuilder("cmd", "/c", userInput);
Process p = pb.start();
```

## Detection indicators

- direct use of `Runtime.exec`, `ProcessBuilder`, or shell wrappers with request data
- command strings assembled from user input
- use of shell metacharacters in command arguments without allowlisting

## Mitigation

- avoid OS commands whenever a library API exists
- separate command and arguments using `ProcessBuilder` or explicit argument arrays
- validate against a strict allowlist of commands and arguments
- run processes with minimum privileges
- reject metacharacters and dynamic shell execution in user-controlled inputs

## Common false positives

- fixed internal commands with trusted arguments are not vulnerable
- command execution in a controlled admin task is not a flaw when the command is static and validated
