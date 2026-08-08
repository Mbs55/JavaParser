# Weak Password Hashing

## Overview

Weak password hashing is when user passwords are stored using algorithms that are fast and easy to brute-force, such as unsalted hashes or legacy algorithms. This allows attackers to recover many passwords from database leaks.

## CWE

CWE-327 and CWE-916 are commonly related, with `Password Hashing` considered a misuse of cryptography.

## Relevant Java APIs

- java.security.MessageDigest
- org.springframework.security.crypto.password.StandardPasswordEncoder
- org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder
- org.springframework.security.crypto.password.Pbkdf2PasswordEncoder

## Attack conditions

The app stores passwords using a weak or unsalted hash such as MD5 or SHA-1, or uses a non-iterative scheme without per-password salts.

## Vulnerable Java example

```java
MessageDigest md = MessageDigest.getInstance("SHA-1");
byte[] hash = md.digest(password.getBytes(StandardCharsets.UTF_8));
```

## Secure Java example

```java
BCryptPasswordEncoder encoder = new BCryptPasswordEncoder();
String hash = encoder.encode(password);
```

## Detection indicators

- direct use of `MessageDigest` on password values without a strong password derivation function
- custom password hashing routines without salts or work factors
- outdated Spring password encoders or insecure defaults

## Mitigation

- use bcrypt, PBKDF2, Argon2, or scrypt
- include unique salts and strong work factors
- never store passwords using unsalted fast hashes
- review auth libraries for modern password storage defaults

## Common false positives

- non-password secret values may use ordinary hashing safely, but password authentication must use a password-hashing function
