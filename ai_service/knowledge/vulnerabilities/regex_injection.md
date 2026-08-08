# Regular Expression Injection

## Overview

Regular expression injection occurs when attacker-controlled data is used to build or modify a regex pattern or to trigger dangerous behavior in a regex engine. In Java, common examples are `Pattern.compile`, `Matcher.matches`, and `String.matches`.

## CWE

CWE-730: Denial of Service by Resource Consumption or Improper Restriction of Operations within the Bounds of a Memory Buffer

## Relevant Java APIs

- java.util.regex.Pattern.compile
- java.util.regex.Pattern.matches
- java.util.regex.Pattern.split
- java.util.regex.Matcher.matches
- java.util.regex.Matcher.find
- java.util.regex.Matcher.replaceAll
- java.lang.String.matches
- java.lang.String.replaceAll
- java.lang.String.split

## Attack conditions

The vulnerability occurs when user input is used directly in a regex pattern or repeated regex execution against untrusted input can cause resource exhaustion or logic bypass.

## Vulnerable Java example

```java
String pattern = request.getParameter("pattern");
Pattern p = Pattern.compile(pattern);
Matcher m = p.matcher(userInput);
boolean ok = m.matches();
```

Patterns such as `(a+)+$` or nested repetitions can trigger catastrophic backtracking.

## Secure Java example

```java
String pattern = request.getParameter("pattern");
if (!pattern.matches("^[A-Za-z0-9_]{1,32}$")) {
    throw new IllegalArgumentException("Invalid pattern");
}
Pattern p = Pattern.compile(pattern);
Matcher m = p.matcher(userInput);
boolean ok = m.matches();
```

## Detection indicators

- regex patterns assembled from request input
- user-controlled pattern strings or replacements
- repeated or complex validation using untrusted regex expressions

## Mitigation

- restrict regex patterns to an allowlist of supported patterns
- validate regex input to reject excessive repetition or nested groups
- use simpler, bounded patterns for validation
- avoid regexes that can cause catastrophic backtracking on user-controlled input

## Common false positives

- fixed regex patterns used internally are safe
- bounded validation regexes are not inherently dangerous
