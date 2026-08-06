---
source: top25owasp
---

**Top 25 Java Security Weaknesses**

This document summarizes the most critical software weaknesses for Java code. Each section describes the issue, why it matters, Java examples, mitigation strategies, and mappings to CWE and OWASP.

## Injection Weaknesses

**Description**
Injection weaknesses occur when untrusted input is interpreted as part of a query, command, or expression.

**Why It Matters**
Injection flaws are among the most frequent and damaging vulnerabilities in Java applications.

**Java Examples**
- SQL Injection using `Statement` or Hibernate HQL
- LDAP Injection in JNDI search filters
- OS Command Injection via `Runtime.exec()` or `ProcessBuilder`

**Mitigation**
Use parameterized SQL, escape LDAP filters, avoid shell command concatenation, and validate or allowlist input.

**Mapping**
CWE-89, CWE-78, CWE-91, OWASP A03:2025 Injection.

**Broken Access Control and IDOR**

**Description**
Broken access control happens when authorization checks are missing or enforced incorrectly.

**Why It Matters**
Attackers can access or modify other users’ data, perform administrative actions, or bypass restrictions.

**Java Example**
Returning data based solely on `request.getParameter("id")` without verifying the current user.

**Mitigation**
Apply access control checks at every layer and use framework authorization annotations or policies.

**Mapping**
CWE-284, CWE-862, OWASP A01:2025 Broken Access Control.

**Cross-Site Scripting (XSS)**

**Description**
XSS occurs when untrusted data is rendered into HTML without proper encoding.

**Why It Matters**
An attacker can execute scripts in another user’s browser and steal session tokens or manipulate page content.

**Java Example**
Concatenating `request.getParameter("message")` into HTML output.

**Mitigation**
Encode output for HTML contexts, use safe template engines, and avoid inline script generation.

**Mapping**
CWE-79, OWASP A03:2025 Injection.

**Sensitive Data Exposure**

**Description**
Sensitive data exposure happens when confidential information is stored or transmitted insecurely.

**Why It Matters**
Exposed credentials, personal data, or keys can lead to account takeover and regulatory violations.

**Java Example**
Storing plaintext passwords or using weak hashing algorithms such as MD5.

**Mitigation**
Encrypt sensitive data using strong cryptography, protect secrets with a vault, and avoid hardcoding credentials.

**Mapping**
CWE-200, CWE-311, OWASP A02:2025 Cryptographic Failures.

**Insecure Deserialization**

**Description**
Insecure deserialization happens when untrusted serialized data is accepted and turned into Java objects.

**Why It Matters**
Attackers can execute arbitrary code or instantiate unexpected types during deserialization.

**Java Example**
Calling `ObjectInputStream.readObject()` on request bytes.

**Mitigation**
Avoid Java native serialization, validate serialized input, and use allowlists with `ObjectInputFilter`.

**Mapping**
CWE-502, OWASP A06/A08.

**Server-Side Request Forgery (SSRF)**

**Description**
SSRF occurs when a Java application fetches attacker-controlled URLs and accesses internal resources.

**Why It Matters**
Attackers can reach internal hosts, metadata services, or private APIs behind firewalls.

**Java Example**
Opening `HttpURLConnection` directly to a user-controlled URI.

**Mitigation**
Use host and scheme allowlists, validate URLs, and restrict outbound network access.

**Mapping**
CWE-918, OWASP A08:2025 Server-Side Request Forgery.

**Security Misconfiguration**

**Description**
Security misconfiguration arises when Java environments, servers, or components are deployed insecurely.

**Why It Matters**
Default or incorrect settings can expose management interfaces, debugging endpoints, or sensitive data.

**Java Example**
Running a Spring Boot application with actuator endpoints enabled in production.

**Mitigation**
Harden configuration, disable unused features, and review production settings.

**Mapping**
CWE-16, CWE-933, OWASP A05:2025 Security Misconfiguration.

**Cryptographic Failures and Hardcoded Secrets**

**Description**
Cryptographic failures occur when encryption, hashing, or key management is implemented incorrectly.

**Why It Matters**
Weak cryptography can lead to data disclosure and broken authentication.

**Java Example**
Using SHA-1 for password hashing or storing secrets in code.

**Mitigation**
Use modern algorithms, manage keys securely, and avoid hardcoded credentials.

**Mapping**
CWE-327, CWE-798, OWASP A02:2025 Cryptographic Failures.

**Path Traversal and File Access**

**Description**
Path traversal occurs when user input controls file paths and bypasses directory restrictions.

**Why It Matters**
Attackers can read or write files outside the intended storage area.

**Java Example**
Resolving user filenames against an upload directory without normalization.

**Mitigation**
Normalize paths, verify canonical location, and use file allowlists.

**Mapping**
CWE-22, CWE-73, OWASP A05:2025 Security Misconfiguration.

**Missing Logging and Monitoring**

**Description**
Failures in logging or monitoring mean security events are not captured or acted upon.

**Why It Matters**
Without logs, attacks can persist undetected and incident response is delayed.

**Java Example**
Suppressing exceptions during authentication checks.

**Mitigation**
Log security events with context, preserve audit trails, and monitor for anomalies.

**Mapping**
CWE-778, OWASP A09:2025 Security Logging and Monitoring Failures.
