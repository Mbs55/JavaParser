# Regular Expression Denial of Service (ReDoS)

## Overview

A ReDoS issue occurs when a regular expression is vulnerable to catastrophic backtracking when given attacker-controlled input. This can consume CPU and make the application unresponsive.

## CWE

CWE-1333: Inefficient Regular Expression Complexity

## Relevant Java APIs

- java.util.regex.Pattern.compile
- java.util.regex.Pattern.matcher
- java.util.regex.Matcher.matches

## Attack conditions

The app compiles a complex regex and matches it against untrusted input that can trigger exponential or catastrophic backtracking.

## Vulnerable Java example

```java
Pattern p = Pattern.compile("^(a+)+$");
boolean match = p.matcher(input).matches();
```

Attackers can send specially crafted strings that cause the matcher to spend excessive CPU time.

## Secure Java example

```java
Pattern p = Pattern.compile("^[a-zA-Z0-9_]{1,50}$");
boolean match = p.matcher(input).matches();
```

This avoids catastrophic backtracking patterns and uses a bounded input size.

## Detection indicators

- nested quantifiers or ambiguous regex patterns
- regex matching on user-provided payloads with no input limits
- patterns such as `(a+)+`, `(.*)+`, or complex alternations in request validation

## Mitigation

- avoid nested quantified patterns or catastrophic regexes
- prefer simpler, linear-time patterns
- enforce reasonable input length limits
- test regex behavior with large malicious payloads

## Common false positives

- small, fixed regexes used on constrained internal values are usually not ReDoS issues