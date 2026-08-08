# Path Traversal Write

## Overview

Path traversal write occurs when an attacker manipulates a write path so that the application writes files outside the intended directory. This can overwrite application files, secrets, or configuration.

## CWE

CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')

## Relevant Java APIs

- java.nio.file.Files.write
- java.nio.file.Files.createFile
- java.io.FileOutputStream
- java.nio.file.Path.resolve

## Attack conditions

The app writes a file to a path derived from untrusted input without validating the final path stays within a trusted root.

## Vulnerable Java example

```java
String name = request.getParameter("name");
Path target = Paths.get("/var/app/uploads/" + name);
Files.write(target, data);
```

A crafted value can overwrite a different file or config file.

## Secure Java example

```java
String name = request.getParameter("name");
Path root = Paths.get("/var/app/uploads").toAbsolutePath().normalize();
Path target = root.resolve(name).normalize();
if (!target.startsWith(root)) {
    throw new SecurityException("Invalid write path");
}
Files.write(target, data);
```

## Detection indicators

- writing files to paths based on request or database values
- direct path concatenation with uploads or exports
- no validation of the final resolved path

## Mitigation

- validate paths before writing
- restrict writes to a known safe directory
- generate non-user-controlled filenames where possible
- reject traversal sequences and symlinks
- log suspicious writes and isolate upload directories

## Common false positives

- writing to fixed application directories with generated names is not a traversal issue
- safe normalization checks are valid controls