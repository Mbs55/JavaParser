# Path Traversal Read

## Overview

Path traversal read occurs when an attacker can read arbitrary files by controlling a path used in file access. This can expose configuration files, source code, credentials, or application data.

## CWE

CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')

## Relevant Java APIs

- java.nio.file.Files.readString
- java.nio.file.Files.readAllBytes
- java.io.FileReader
- java.io.FileInputStream
- java.nio.file.Paths.get

## Attack conditions

The app combines a user-controlled path with a base directory without verifying the result stays within the allowed root.

## Vulnerable Java example

```java
String filename = request.getParameter("file");
Path path = Paths.get("/opt/app/data/" + filename);
String content = Files.readString(path);
```

An attacker can request `../../../../etc/passwd` to read outside the intended directory.

## Secure Java example

```java
String filename = request.getParameter("file");
Path base = Paths.get("/opt/app/data").toAbsolutePath().normalize();
Path target = base.resolve(filename).normalize();
if (!target.startsWith(base)) {
    throw new IllegalArgumentException("Invalid file path");
}
String content = Files.readString(target);
```

## Detection indicators

- reading files using user input without verifying the resolved path stays within a base directory
- direct path concatenation and normalization bypasses
- dynamic file access in file download or report endpoints

## Mitigation

- normalize paths and validate against an allowlisted root directory
- reject traversal sequences, absolute paths, and symlinks
- use fixed storage directories and generated file names
- audit file download and report generation endpoints for path handling

## Common false positives

- reading a file only from a known safe internal path is not a traversal issue
- safe access with `startsWith` validation is acceptable when implemented correctly