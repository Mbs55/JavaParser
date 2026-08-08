# Insecure TLS / Trust Configuration

## Overview

Insecure TLS vulnerabilities arise when Java applications accept weak protocols, weak cipher suites, insecure trust configuration, or unsafe hostname verification. This can enable downgrade attacks or silent trust of untrusted endpoints.

## CWE

CWE-295: Improper Certificate Validation

## Relevant Java APIs

- javax.net.ssl.SSLContext
- javax.net.ssl.TrustManager
- javax.net.ssl.HostnameVerifier

## Attack conditions

This danger appears when code or application configuration allows:

- disabled hostname verification
- insecure trust managers that accept any certificate
- legacy TLS versions such as SSLv3 or TLS 1.0
- weak cipher suites or anonymous ciphers

## Vulnerable Java example

```java
HttpsURLConnection connection = (HttpsURLConnection) new URL(url).openConnection();
connection.setHostnameVerifier((hostname, session) -> true);
connection.setSSLSocketFactory(new TrustAllManagerFactory());
```

This disables certificate and hostname verification and allows man-in-the-middle interception.

## Secure Java example

```java
SSLContext sslContext = SSLContext.getInstance("TLS");
sslContext.init(null, null, null);

HttpsURLConnection connection = (HttpsURLConnection) new URL(url).openConnection();
connection.setSSLSocketFactory(sslContext.getSocketFactory());
connection.setHostnameVerifier((hostname, session) ->
    HttpsURLConnection.getDefaultHostnameVerifier().verify(hostname, session));
```

## Detection indicators

- custom `TrustManager` implementations that do not verify certificates
- `HostnameVerifier` returning `true` without validation
- use of insecure algorithms or disabled certificate checks

## Mitigation

- use standard JDK trust stores
- require valid certificate chains and hostname checks
- disable weak protocols and ciphers
- prefer TLS 1.2 or higher and modern cipher suites
- avoid custom trust-all code except in isolated testing scenarios

## Common false positives

- using a legitimate custom `TrustManager` for private CA trust is not inherently unsafe if it properly validates certificates
- testing code may intentionally disable verification but should never be shipped to production
