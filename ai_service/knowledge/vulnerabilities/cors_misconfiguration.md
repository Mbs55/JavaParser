# CORS Misconfiguration

## Summary

CORS misconfiguration allows cross-origin clients to access sensitive resources that should be restricted to trusted origins. In Java web applications, this often appears in Spring MVC, servlet filters, or custom response headers.

## CWE

CWE-346: Origin Validation Error

## Relevant Java APIs

- javax.servlet.http.HttpServletResponse.setHeader
- jakarta.servlet.http.HttpServletResponse.setHeader
- org.springframework.web.servlet.config.annotation.CorsRegistry
- org.springframework.web.cors.CorsConfiguration

## Vulnerable Java example

```java
response.setHeader("Access-Control-Allow-Origin", "*");
response.setHeader("Access-Control-Allow-Credentials", "true");
```

This permits arbitrary browser origins to call authenticated APIs and read responses.

## Secure Java example

```java
response.setHeader("Access-Control-Allow-Origin", "https://app.example.com");
response.setHeader("Access-Control-Allow-Methods", "GET, POST");
response.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization");
```

## Detection indicators

- wildcard `Access-Control-Allow-Origin` values
- permissive CORS config for authenticated or sensitive endpoints
- reflection of arbitrary `Origin` headers into CORS headers

## Mitigation

- restrict allowed origins to a fixed allowlist
- avoid wildcard origin with credentials
- only expose necessary methods and headers
- inspect CORS policy for sensitive endpoints, not only public APIs
- prefer Spring Security CORS configuration over ad hoc response headers

## False positives

- public APIs with a static trusted origin list are not a vulnerability
- same-origin or strict internal services are not exposed by CORS to untrusted origins
