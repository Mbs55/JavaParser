# Weak Cryptography

## Overview

Weak cryptography occurs when the application uses deprecated or low-strength algorithms, improper key lengths, or insecure randomization. This can lead to decryption, tampering, or credential compromise.

## CWE

CWE-327: Use of a Broken or Risky Cryptographic Algorithm

## Relevant Java APIs

- javax.crypto.Cipher.getInstance
- java.security.MessageDigest.getInstance
- javax.crypto.KeyGenerator.getInstance
- javax.crypto.spec.SecretKeySpec

## Attack conditions

The app uses algorithms such as MD5, SHA-1, DES, RC4, or small RSA keys for data protected with security assumptions.

## Vulnerable Java example

```java
MessageDigest md = MessageDigest.getInstance("MD5");
byte[] digest = md.digest(input.getBytes(StandardCharsets.UTF_8));
```

MD5 is cryptographically weak for security-sensitive operations.

## Secure Java example

```java
MessageDigest md = MessageDigest.getInstance("SHA-256");
byte[] digest = md.digest(input.getBytes(StandardCharsets.UTF_8));
```

## Detection indicators

- `MD5`, `SHA-1`, `DES`, `RC4`, or similar weak algorithms in security-sensitive code
- insufficient key sizes or poor algorithm configuration
- use of custom crypto with no proven strength

## Mitigation

- prefer modern algorithms such as AES-GCM, SHA-256, or PBKDF2
- use stronger key sizes and correctly configured modes
- avoid deprecated crypto primitives in production code
- review all cryptographic calls for security suitability

## Common false positives

- some non-security uses of hashing may be acceptable with weaker algorithms, but any security-sensitive use must be reviewed