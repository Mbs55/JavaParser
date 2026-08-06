---
source: cwe
---

**Common Weakness Enumeration for Java Security**

This document maps high-priority weaknesses to Java-specific coding patterns and secure development practices.

## How to Use This Document

Each weakness includes a description, attack scenario, vulnerable and secure examples, mitigation, and relevant Java APIs.

**CWE-89: SQL Injection**

**Description**
SQL Injection happens when untrusted input is concatenated into SQL commands and executed by a database engine.

**Why It Is Dangerous**
An attacker can alter query logic, retrieve unauthorized data, delete records, or escalate privileges by injecting SQL metacharacters.

**Typical Attack Scenario**
A servlet reads a request parameter and appends it into a query string before calling `Statement.executeQuery()`.

**Vulnerable Java Example**
```java
String userId = request.getParameter("userId");
String sql = "SELECT * FROM users WHERE id = " + userId;
Statement stmt = connection.createStatement();
ResultSet rs = stmt.executeQuery(sql);
```

**Secure Java Example**
```java
String userId = request.getParameter("userId");
String sql = "SELECT * FROM users WHERE id = ?";
try (PreparedStatement pstmt = connection.prepareStatement(sql)) {
    pstmt.setString(1, userId);
    try (ResultSet rs = pstmt.executeQuery()) {
        // process results
    }
}
```

**Mitigation**
Use parameterized queries with `PreparedStatement`, avoid dynamic SQL string building, validate input, and apply least privilege to database accounts.

**Java APIs**
`PreparedStatement`, `Statement`, `Connection.prepareStatement()`, `ResultSet`, `executeQuery()`.

**CWE**
CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection').

**OWASP**
A03:2025 Injection.

**CWE-79: Cross-Site Scripting (XSS)**

**Description**
Cross-Site Scripting occurs when a web application includes attacker-controlled data in a web page without proper encoding.

**Why It Is Dangerous**
An attacker can execute scripts in a victim’s browser, steal authentication tokens, perform actions on behalf of the user, or hijack sessions.

**Typical Attack Scenario**
A JSP page prints `request.getParameter("name")` directly into HTML output.

**Vulnerable Java Example**
```java
String name = request.getParameter("name");
response.getWriter().println("<div>Welcome " + name + "</div>");
```

**Secure Java Example**
```java
String name = request.getParameter("name");
String safeName = org.owasp.encoder.Encode.forHtmlContent(name);
response.getWriter().println("<div>Welcome " + safeName + "</div>");
```

**Mitigation**
Use output encoding for HTML contexts, avoid direct string concatenation in page markup, and prefer template engines with auto-escaping.

**Java APIs**
`org.owasp.encoder.Encode.forHtmlContent()`, `StringEscapeUtils.escapeHtml4()`, JSP EL.

**CWE**
CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting').

**OWASP**
A03:2025 Injection.

**CWE-22: Path Traversal**

**Description**
Path Traversal occurs when attacker-controlled input is used to construct file system paths without normalization.

**Why It Is Dangerous**
Attackers can access or modify files outside the intended directory, including configuration files, credentials, or application source.

**Typical Attack Scenario**
A file downloader uses `Paths.get(basePath, request.getParameter("file"))` and reads the resulting path.

**Vulnerable Java Example**
```java
String fileName = request.getParameter("file");
Path filePath = Paths.get("/var/app/data", fileName);
String content = Files.readString(filePath);
```

**Secure Java Example**
```java
String fileName = request.getParameter("file");
Path baseDir = Paths.get("/var/app/data").toRealPath();
Path resolved = baseDir.resolve(fileName).normalize();
if (!resolved.startsWith(baseDir)) {
    throw new SecurityException("Path traversal detected");
}
String content = Files.readString(resolved);
```

**Mitigation**
Normalize paths, enforce allowlists for file names, validate file names with strict patterns, and verify canonical or real paths remain within the allowed directory.

**Java APIs**
`Paths.get()`, `Path.normalize()`, `Path.toRealPath()`, `Files.readString()`, `Path.startsWith()`.

**CWE**
CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal').

**OWASP**
A05:2025 Security Misconfiguration.

**CWE-78: OS Command Injection**

**Description**
OS Command Injection occurs when untrusted input is passed to operating system commands without proper separation or validation.

**Why It Is Dangerous**
Attackers can execute arbitrary commands or inject arguments that alter the behavior of shell utilities.

**Typical Attack Scenario**
A Java application builds a command string and calls `Runtime.exec()` with a concatenated user-supplied argument.

**Vulnerable Java Example**
```java
String path = request.getParameter("path");
Runtime.getRuntime().exec("ls " + path);
```

**Secure Java Example**
```java
String path = request.getParameter("path");
if (!path.matches("[a-zA-Z0-9._/-]{1,200}")) {
    throw new IllegalArgumentException("Invalid path");
}
ProcessBuilder pb = new ProcessBuilder("ls", path);
pb.start();
```

**Mitigation**
Avoid invoking shell interpreters, use `ProcessBuilder` or dedicated APIs, validate arguments with allowlists, and do not allow direct user-controlled commands.

**Java APIs**
`Runtime.exec()`, `ProcessBuilder`, `Process`, `String.matches()`.

**CWE**
CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection').

**OWASP**
A03:2025 Injection.

**CWE-502: Insecure Deserialization**

**Description**
Insecure deserialization happens when untrusted data is deserialized into Java objects without restriction.

**Why It Is Dangerous**
An attacker can instantiate arbitrary classes, execute gadget chains, or modify application behavior during deserialization.

**Typical Attack Scenario**
A server reads bytes from a request and passes them to `ObjectInputStream.readObject()`.

**Vulnerable Java Example**
```java
byte[] payload = request.getInputStream().readAllBytes();
try (ObjectInputStream in = new ObjectInputStream(new ByteArrayInputStream(payload))) {
    Object obj = in.readObject();
}
```

**Secure Java Example**
```java
try (ObjectInputStream in = new ObjectInputStream(new ByteArrayInputStream(payload))) {
    ObjectInputFilter filter = ObjectInputFilter.Config.createFilter("java.base/*;com.example.dto.*;!*");
    in.setObjectInputFilter(filter);
    MyDto dto = (MyDto) in.readObject();
}
```

**Mitigation**
Avoid native Java serialization for untrusted data, use explicit DTOs with JSON or XML, and enforce allowlists with `ObjectInputFilter` or guarded `resolveClass()`.

**Java APIs**
`ObjectInputStream`, `ObjectInputFilter`, `ByteArrayInputStream`, `java.beans.XMLDecoder`.

**CWE**
CWE-502: Deserialization of Untrusted Data.

**OWASP**
A06:2025 Software or Data Integrity Failures.

**CWE-918: Server-Side Request Forgery (SSRF)**

**Description**
SSRF occurs when an application fetches a URL provided by an attacker and accesses internal resources or cloud metadata.

**Why It Is Dangerous**
Attackers can reach internal services, cloud provider metadata endpoints, or private resources behind firewalls.

**Typical Attack Scenario**
A Java service accepts a URL parameter and opens it using `HttpURLConnection`.

**Vulnerable Java Example**
```java
String target = request.getParameter("url");
URL url = new URL(target);
HttpURLConnection conn = (HttpURLConnection) url.openConnection();
conn.connect();
```

**Secure Java Example**
```java
URI uri = new URI(request.getParameter("url"));
if (!"https".equalsIgnoreCase(uri.getScheme())) {
    throw new IllegalArgumentException("Unsupported scheme");
}
Set<String> hosts = Set.of("api.example.com", "internal.example.local");
if (!hosts.contains(uri.getHost())) {
    throw new IllegalArgumentException("Untrusted target");
}
HttpURLConnection conn = (HttpURLConnection) uri.toURL().openConnection();
conn.connect();
```

**Mitigation**
Validate URI scheme and host allowlists, avoid fetching arbitrary user-provided URLs, and apply network-level segmentation.

**Java APIs**
`URL`, `URI`, `HttpURLConnection`, `HttpClient`, `RestTemplate`, `WebClient`.

**CWE**
CWE-918: Server-Side Request Forgery.

**OWASP**
A08:2025 Server-Side Request Forgery.

**CWE-798: Hardcoded Credentials**

**Description**
Hardcoded credentials occur when passwords, API keys, or tokens are embedded directly in source code or configuration files.

**Why It Is Dangerous**
If an attacker gains access to the code or binary, they can reuse credentials to access systems or services.

**Typical Attack Scenario**
A Java application stores `String apiKey = "secret-key"` in source code and uses it to call an external API.

**Vulnerable Java Example**
```java
String apiKey = "my-secret-api-key";
HttpRequest request = HttpRequest.newBuilder()
        .header("Authorization", "Bearer " + apiKey)
        .uri(URI.create("https://api.example.com/data"))
        .build();
```

**Secure Java Example**
```java
String apiKey = System.getenv("API_KEY");
HttpRequest request = HttpRequest.newBuilder()
        .header("Authorization", "Bearer " + apiKey)
        .uri(URI.create("https://api.example.com/data"))
        .build();
```

**Mitigation**
Store secrets in environment variables, secrets managers, or vaults; never commit credentials to source control.

**Java APIs**
`System.getenv()`, `Properties`, `SecretKey`, Vault SDKs.

**CWE**
CWE-798: Use of Hard-coded Credentials.

**OWASP**
A07:2025 Identification and Authentication Failures.
