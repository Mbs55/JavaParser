# Weak SSL Configuration

## Overview

Weak SSL configuration occurs when a Java application uses insecure protocols, weak cipher suites, skipping hostname verification, or disabling certificate validation. This makes TLS connections vulnerable to interception or downgrade attacks.

## CWE

CWE-327: Use of a Broken or Risky Cryptographic Algorithm

## Relevant Java APIs

- javax.net.ssl.HttpsURLConnection
- javax.net.ssl.SSLContext
- org.apache.http.conn.ssl.NoopHostnameVerifier
- javax.net.ssl.TrustManager

## Attack conditions

The app configures TLS with insecure settings, disables verification, or allows obsolete protocol versions.

## Vulnerable Java example

```java
SSLContext context = SSLContext.getInstance("SSL");
context.init(null, trustAllCerts, new SecureRandom());
```

This disables trust checks and accepts all certificates.

## Secure Java example

```java
SSLContext context = SSLContext.getInstance("TLS");
HttpsURLConnection.setDefaultSSLSocketFactory(context.getSocketFactory());
```

and use proper certificate validation rather than a trust-all strategy.

## Detection indicators

- `SSL` protocol instead of `TLS`
- `NoopHostnameVerifier`, trusting all certificates, or custom trust managers that skip validation
- insecure cipher or weak certificate validation settings

## Mitigation

- enforce modern TLS versions and secure cipher suites
- validate hostnames and certificate chains properly
- avoid trust-all or custom disabled verification in production
- review framework defaults and disable insecure protocol support

## Common false positives

- local development with self-signed certs may require temporary overrides, but production must not skip verification