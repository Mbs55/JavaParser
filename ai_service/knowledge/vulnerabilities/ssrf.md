# Server-Side Request Forgery (SSRF)

## Overview

SSRF occurs when a server makes outbound requests to a URL controlled by an attacker. This can allow access to internal services, metadata endpoints, or sensitive network resources.

## CWE

CWE-918: Server-Side Request Forgery (SSRF)

## Relevant Java APIs

- java.net.URL.openConnection
- java.net.http.HttpClient
- org.apache.http.impl.client.CloseableHttpClient
- org.springframework.web.client.RestTemplate

## Attack conditions

The app fetches user-controlled URLs without validating the target host, scheme, or network context.

## Vulnerable Java example

```java
String url = request.getParameter("url");
HttpURLConnection conn = (HttpURLConnection) new URL(url).openConnection();
conn.getInputStream();
```

A user can target internal services like `http://169.254.169.254/` or `http://localhost:8080/admin`.

## Secure Java example

```java
String url = request.getParameter("url");
URI uri = URI.create(url);
if (!"https".equals(uri.getScheme()) || !uri.getHost().endsWith("example.com")) {
    throw new IllegalArgumentException("Invalid destination");
}
HttpURLConnection conn = (HttpURLConnection) uri.toURL().openConnection();
```

## Detection indicators

- outbound HTTP requests with target URLs from user or database input
- no host allowlist or validation for external service calls
- internal network or metadata endpoints reachable from the server

## Mitigation

- allowlist only trusted destinations and schemes
- block internal IP ranges, localhost, metadata endpoints, and link-local addresses
- require explicit URLs in a fixed set of known services
- log outbound request destinations and add network segmentation

## Common false positives

- outbound requests to trusted third-party APIs may be valid if domain validation is strict and controlled