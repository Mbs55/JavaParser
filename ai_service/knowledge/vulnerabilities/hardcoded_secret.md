# Hardcoded Secret

## Overview

Hardcoded secrets are embedded credentials or cryptographic keys that are committed to code, config, or binary artifacts. These secrets can be extracted by attackers and reused across environments.

## CWE

CWE-798 and CWE-321 are commonly associated.

## Relevant Java APIs

- javax.crypto.spec.SecretKeySpec
- java.security.KeyStore
- com.auth0.jwt.algorithms.Algorithm.HMAC256
- javax.crypto.KeyGenerator

## Attack conditions

This appears when secret material is stored as constant strings or source-controlled properties rather than being injected or rotated securely.

## Vulnerable Java example

```java
private static final String JWT_SECRET = "my-dev-secret-123";
```

## Secure Java example

```java
private static final String JWT_SECRET = System.getenv("JWT_SECRET");
```

## Detection indicators

- constant strings for tokens, API keys, signing keys, or encryption keys
- secrets present in `application.properties`, YAML, or Java constants
- repeated secret values across different environments

## Mitigation

- use a secrets manager or environment-based secrets injection
- rotate leaked keys immediately
- avoid committing generated keys or signing secrets to the repository
- separate secret storage from application code

## Common false positives

- placeholder examples are harmless when clearly labeled as samples
- ephemeral test secrets are acceptable only in isolated non-production contexts