# HTTP Request Smuggling

## Overview

HTTP Request Smuggling is a protocol-level vulnerability that occurs when a front-end proxy or server interprets the boundaries of multiple HTTP requests differently than the backend. This can allow attackers to smuggle malformed requests and confuse request parsing.

## CWE

CWE-444: Inconsistent Interpretation of HTTP Requests ('HTTP Request Smuggling')

## Relevant Java APIs

- org.apache.http.HttpRequest
- org.apache.http.HttpEntity
- org.apache.http.client.methods.HttpGet
- org.apache.http.client.methods.HttpPost
- java.net.http.HttpClient
- java.net.http.HttpRequest
- java.net.HttpURLConnection

## Attack conditions

This is a vulnerability in HTTP infrastructure and proxy handling, not just Java business logic. It appears when the Java app is behind a front-end that does inconsistent request parsing or the app accepts ambiguous request framing.

## Vulnerable Java example

```java
HttpGet request = new HttpGet(url);
try (CloseableHttpClient client = HttpClients.createDefault()) {
    client.execute(request);
}
```

The app may be vulnerable when proxying or forwarding requests without stricter validation, especially in multi-layer deployments.

## Secure Java example

```java
HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://example.internal/api"))
    .header("Content-Type", "application/json")
    .GET()
    .build();

HttpClient client = HttpClient.newHttpClient();
client.send(request, HttpResponse.BodyHandlers.ofString());
```

## Detection indicators

- reverse proxy or load balancer handling of HTTP requests
- multiple HTTP servers or inconsistent request parsing layers
- forwarding of raw request headers or bodies without validation

## Mitigation

- ensure consistent request parsing across servers and proxies
- disable ambiguous or obsolete HTTP features when possible
- validate and normalize forwarded requests
- use stable, well-tested proxy and backend configurations
- limit request size and reject malformed headers

## Notes

Most Java code is not directly vulnerable to request smuggling by itself; the issue is usually in the deployment, reverse proxy, or HTTP-layer handling.
