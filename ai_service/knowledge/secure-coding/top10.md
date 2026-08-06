---
source: top10
---

**OWASP Top 10 for Java Security**

This document summarizes the OWASP Top 10 RC1 (2025) from a Java coding perspective. Each section includes a description, Java attack pattern, secure practices, mitigation, and relevant APIs.

## A01:2025 Broken Access Control

**Description**
Broken access control occurs when Java code allows users to perform actions or access data without enforcing authorization checks.

**Why It Is Dangerous**
An attacker can access sensitive resources, perform actions on behalf of other users, or elevate privileges.

**Vulnerable Java Example**
```java
String targetUser = request.getParameter("userId");
User user = userDao.findById(targetUser);
response.getWriter().println(user.getEmail());
```

**Secure Java Example**
```java
String targetUser = request.getParameter("userId");
User currentUser = auth.getCurrentUser();
if (!currentUser.canAccessUser(targetUser)) {
    response.sendError(HttpServletResponse.SC_FORBIDDEN);
    return;
}
User user = userDao.findById(targetUser);
response.getWriter().println(user.getEmail());
```

**Mitigation**
Enforce authorization at each entry point, use a centralized policy engine, and avoid assuming that a request parameter is safe.

**Java APIs**
Spring Security `@PreAuthorize`, `SecurityContextHolder`, `Principal`, `HttpServletRequest`.

**A02:2025 Cryptographic Failures**

**Description**
Cryptographic failures cover weak or incorrect use of encryption, hashing, or key management in Java applications.

**Why It Is Dangerous**
Weak crypto can expose sensitive data at rest or in transit, enabling disclosure or tampering.

**Vulnerable Java Example**
```java
MessageDigest md = MessageDigest.getInstance("SHA-1");
byte[] hash = md.digest(password.getBytes(StandardCharsets.UTF_8));
```

**Secure Java Example**
```java
PasswordHasher hasher = new Argon2PasswordHasher();
String hash = hasher.hash(password);
```

**Mitigation**
Use modern algorithms such as AES-GCM, `Argon2id`, and `PBKDF2`, and manage keys with a vault or secure keystore.

**Java APIs**
`javax.crypto.Cipher`, `SecretKey`, `KeyStore`, third-party Argon2 libraries.

**A03:2025 Injection**

**Description**
Injection occurs when untrusted data is interpreted as code, commands, or query language.

**Why It Is Dangerous**
Injection can lead to data access, data modification, remote code execution, or system compromise.

**Vulnerable Java Example**
```java
String sql = "SELECT * FROM users WHERE name = '" + request.getParameter("name") + "'";
Statement stmt = connection.createStatement();
stmt.executeQuery(sql);
```

**Secure Java Example**
```java
String sql = "SELECT * FROM users WHERE name = ?";
PreparedStatement pstmt = connection.prepareStatement(sql);
pstmt.setString(1, request.getParameter("name"));
pstmt.executeQuery();
```

**Mitigation**
Use parameterized queries, escape output for HTML, and avoid dynamic command construction.

**Java APIs**
`PreparedStatement`, `ProcessBuilder`, `JXPath`, `EL`.

**A04:2025 Insecure Design**

**Description**
Insecure design refers to missing or flawed security architecture in Java applications.

**Why It Is Dangerous**
Even with secure code, a weak design can leave authentication, data protection, or business logic vulnerable.

**Java Security Practice**
Design explicit authorization checks, threat model data flow, and use secure defaults for frameworks and libraries.

**Mitigation**
Use security design reviews, enforce least privilege, and treat security as a first-class requirement during feature design.

**A05:2025 Security Misconfiguration**

**Description**
Security misconfiguration arises when Java environments, frameworks, or dependencies are deployed with unsafe defaults.

**Why It Is Dangerous**
Misconfiguration can expose debug endpoints, enable unnecessary services, or leave sensitive data accessible.

**Java Example**
Leaving Spring Boot actuator endpoints open in production or using default credentials for management consoles.

**Mitigation**
Harden configuration, disable unused features, and audit production settings regularly.

**Java APIs**
Spring Boot `application.properties`, `WebSecurityConfigurerAdapter`, servlet filters.

**A06:2025 Software or Data Integrity Failures**

**Description**
Software or data integrity failures occur when Java applications accept untrusted updates, plugins, or serialized data without verification.

**Why It Is Dangerous**
Attackers can supply malicious dependencies, tamper payloads, or exploit insecure deserialization.

**Java Example**
Loading code from an unsigned JAR or deserializing data without validation.

**Mitigation**
Validate digital signatures, enforce strict deserialization allowlists, and use trusted dependency sources.

**A07:2025 Identification and Authentication Failures**

**Description**
Authentication failures occur when Java code does not properly verify user identity or session credentials.

**Why It Is Dangerous**
Attackers can bypass login, reuse tokens, or take over accounts.

**Java Example**
Accepting an unverified JWT without checking its signature or expiration.

**Mitigation**
Validate authentication tokens, use strong password handling, and require multi-factor authentication when appropriate.

**Java APIs**
`javax.security.auth`, Spring Security authentication managers, JWT libraries.

**A08:2025 Server-Side Request Forgery (SSRF)**

**Description**
SSRF occurs when a server-side Java component fetches a URL provided by an attacker.

**Why It Is Dangerous**
Attackers can access internal hosts, cloud metadata APIs, and services behind the firewall.

**Java Example**
Opening `HttpURLConnection` directly on a user-controlled URL.

**Mitigation**
Validate host allowlists, restrict schemes, and avoid fetching arbitrary external URLs.

**A09:2025 Security Logging and Monitoring Failures**

**Description**
Failures in logging and monitoring occur when security events are not recorded or monitored properly.

**Why It Is Dangerous**
Attackers can persist longer without detection, and incidents may not be investigated effectively.

**Java Example**
Catching security exceptions and dropping them silently instead of logging a warning.

**Mitigation**
Log security-relevant events, preserve audit trails, and monitor for suspicious patterns.

**A10:2025 Missing Protection**

**Description**
Missing protection refers to absent or incomplete defenses that should be present in Java applications.

**Why It Is Dangerous**
Even if code is correct, missing controls leave the application exposed to known attack classes.

**Java Example**
Using `HttpServletResponse.sendRedirect()` without validating the destination or using CSRF tokens on state-changing forms.

**Mitigation**
Apply defense-in-depth controls, validate inputs, and use standard protection frameworks consistently.
