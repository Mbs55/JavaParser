# Insecure Randomness

## Overview

Insecure randomness occurs when application-level randomness is generated with predictable or weak sources, leading to vulnerable tokens, sessions, or cryptographic values.

## CWE

CWE-330: Use of Insufficiently Random Values

## Relevant Java APIs

- java.util.Random
- java.lang.Math.random
- java.security.SecureRandom

## Attack conditions

The issue is present when a token, nonce, password reset value, session identifier, or cryptographic key is generated using predictable randomness.

## Vulnerable Java example

```java
String token = Long.toString(Math.abs(new Random().nextLong()));
```

This is predictable and unsuitable for security-sensitive tokens.

## Secure Java example

```java
SecureRandom random = new SecureRandom();
byte[] bytes = new byte[32];
random.nextBytes(bytes);
String token = Base64.getUrlEncoder().withoutPadding().encodeToString(bytes);
```

## Detection indicators

- `new Random()` in security-sensitive code
- use of timestamp-based or low-entropy IDs for tokens or salts
- random values reused or not actually cryptographically secure

## Mitigation

- use `SecureRandom` for security-sensitive randomness
- generate long random tokens with sufficient entropy
- avoid custom PRNG logic for secrets or session identifiers
- validate that generated values are not reused or guessable

## Common false positives

- non-sensitive temporary or UI identifiers can use simpler randomness if they are not security-critical