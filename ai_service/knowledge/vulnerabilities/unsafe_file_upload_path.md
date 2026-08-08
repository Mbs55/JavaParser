# Unsafe File Upload Path

## Overview

Unsafe file upload path handling occurs when uploaded files are stored in a location derived from user-controlled input without validation, normalization, or access restrictions. This can lead to path traversal, overwrite of critical files, or exposure of application resources.

## CWE

CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')

## Relevant Java APIs

- org.springframework.web.multipart.MultipartFile.getOriginalFilename
- org.springframework.web.multipart.MultipartFile.transferTo
- java.io.File
- java.io.FileOutputStream
- java.io.FileWriter
- java.nio.file.Path.resolve
- java.nio.file.Paths.get
- java.nio.file.Files.copy
- java.nio.file.Files.write

## Attack conditions

This issue appears when uploaded file names or paths are directly used to build a destination path on disk or in the file system.

## Vulnerable Java example

```java
String filename = request.getParameter("filename");
Path path = Paths.get("/uploads/" + filename);
Files.write(path, file.getBytes());
```

An attacker can provide a value such as `../../app.properties` to overwrite application files.

## Secure Java example

```java
String original = uploadedFile.getOriginalFilename();
String safeName = Paths.get(original).getFileName().toString();
Path uploadDir = Paths.get("/var/uploads");
Path target = uploadDir.resolve(UUID.randomUUID() + "-" + safeName).normalize();

if (!target.startsWith(uploadDir)) {
    throw new IllegalArgumentException("Invalid upload path");
}

uploadedFile.transferTo(target);
```

## Detection indicators

- user-controlled file names or raw paths used in `File`, `Path.resolve`, or `Files.write`
- path concatenation without normalization or allowlist checks
- uploads stored under user-controlled relative directories

## Mitigation

- use a fixed upload directory
- sanitize file names and normalize paths
- reject traversal sequences such as `..`, absolute paths, or control characters
- store unique names instead of user-supplied names
- enforce a strict allowlist of allowed extensions and mime types

## Common false positives

- safe upload handling to a fixed directory with a generated filename is not vulnerable
- validation of `Path.normalize()` plus `startsWith` checks is a standard safe pattern
