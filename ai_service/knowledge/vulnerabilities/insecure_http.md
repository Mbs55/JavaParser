# Insecure HTTP

## Overview

Insecure HTTP means an application uses plaintext HTTP for sensitive traffic, allowing interception or tampering by attackers. This is common when web apps or APIs are configured to accept non-TLS transport.

## CWE

CWE-319: Cleartext Transmission of Sensitive Information

## Relevant Java APIs

- java.net.URL.openConnection
- java.net.HttpURLConnection
- org.apache.http.client.HttpClient
- org.springframework.web.client.RestTemplate

## Attack conditions

The risk appears whenever credentials, tokens, secrets, or sensitive data are transmitted over plain HTTP instead of HTTPS.

## Vulnerable Java example

```java
URL url = new URL("http://api.example.com/secure");
HttpURLConnection conn = (HttpURLConnection) url.openConnection();
```

## Secure Java example

```java
URL url = new URL("https://api.example.com/secure");
HttpURLConnection conn = (HttpURLConnection) url.openConnection();
```

## Detection indicators

- URLs beginning with `http://` for authenticated or sensitive flows
- HTTP client configuration that ignores TLS or certificate checks
- redirects or endpoints that allow insecure transport

## Mitigation

- require HTTPS for all sensitive flows
- redirect HTTP to HTTPS
- use secure transport defaults in client libraries
- avoid disabling certificate validation unless explicitly justified and controlled

## Common false positives

- local development or test infrastructure may use HTTP under controlled conditions, but production should not