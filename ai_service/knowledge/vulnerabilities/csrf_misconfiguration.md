# CSRF Misconfiguration

## Summary

Cross-Site Request Forgery occurs when a browser is induced to send a state-changing request to a trusted application without the user’s consent. Java web apps commonly need CSRF protection for state-changing operations.

## CWE

CWE-352: Cross-Site Request Forgery

## Relevant Java APIs

- javax.servlet.http.HttpServletRequest
- jakarta.servlet.http.HttpServletRequest
- org.springframework.security.web.csrf.CsrfToken
- org.springframework.security.config.annotation.web.configurers.CsrfConfigurer

## Vulnerable Java example

```java
@PostMapping("/transfer")
public String transfer(@RequestParam String account, @RequestParam BigDecimal amount) {
    bankService.transfer(account, amount);
    return "ok";
}
```

No CSRF token or validation is enforced.

## Secure Java example

```java
@PostMapping("/transfer")
@PreAuthorize("isAuthenticated()")
public String transfer(@RequestParam String account, @RequestParam BigDecimal amount) {
    bankService.transfer(account, amount);
    return "ok";
}
```

with CSRF tokens enabled and verified by Spring Security.

## Detection indicators

- state-changing requests without anti-CSRF tokens
- cookie-based auth with no token validation
- APIs that accept cross-origin state changes without explicit protection

## Mitigation

- enable CSRF protection on non-GET state-changing requests
- use synchronizer tokens or double-submit mechanisms
- ensure same-site cookie protections are enforced
- review custom API clients and stateless JWT flows carefully

## False positives

- safe stateless endpoints that are intentionally public are not vulnerable
- protected endpoints with explicit CSRF validation are not automatically insecure
