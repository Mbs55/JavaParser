# Format String Injection

## Overview

Format string injection occurs when untrusted data is passed into a format operation that treats arguments as format specifiers. In Java, this is commonly seen with `String.format`, `Formatter`, or `PrintStream.printf`.

## CWE

CWE-134: Use of Externally-Controlled Format String

## Relevant Java APIs

- java.io.PrintStream.format
- java.io.PrintStream.printf
- java.lang.String.format
- java.util.Formatter.format

## Attack conditions

The vulnerability appears when user-controlled input is directly used as the format string or when arguments are not validated before formatting.

## Vulnerable Java example

```java
String message = request.getParameter("message");
System.out.printf(message);
```

If the request contains `%n%s`, the output may leak or manipulate formatting behavior unexpectedly.

## Secure Java example

```java
String message = request.getParameter("message");
String safeMessage = message == null ? "" : message;
System.out.printf("Message: %s%n", safeMessage);
```

The format string is fixed and user data is passed as an argument, not interpreted as formatting directives.

## Detection indicators

- `printf`, `format`, or `Formatter` with untrusted first argument
- dynamic format strings built from request parameters or database values
- logging that passes raw attacker-controlled strings as format patterns

## Mitigation

- use a fixed format string and pass user data as arguments
- never allow untrusted input to define the format template
- treat log statements as controlled output, not data-driven format strings
- validate suspicious format tokens before use

## Common false positives

- using `String.format("Hello %s", userInput)` is safe
- using a constant pattern is not vulnerable
