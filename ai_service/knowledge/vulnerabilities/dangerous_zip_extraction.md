# Dangerous ZIP Extraction

## Overview

ZIP extraction can become dangerous when archive members are interpreted as filesystem paths without validation. This can cause path traversal, data overwrite, or resource exhaustion.

## CWE

CWE-22 and CWE-409 are common related issues.

## Relevant Java APIs

- java.util.zip.ZipInputStream
- java.util.jar.JarFile
- java.util.zip.ZipFile
- java.nio.file.Files.copy
- java.nio.file.Path.resolve

## Vulnerable Java example

```java
try (ZipInputStream zis = new ZipInputStream(new FileInputStream(file))) {
    ZipEntry entry;
    while ((entry = zis.getNextEntry()) != null) {
        Files.copy(zis, Paths.get("/tmp/extract/" + entry.getName()));
    }
}
```

If the archive contains `../../app.properties`, the file can overwrite protected application data.

## Secure Java example

```java
Path root = Paths.get("/tmp/extract").toAbsolutePath().normalize();
try (ZipInputStream zis = new ZipInputStream(new FileInputStream(file))) {
    ZipEntry entry;
    while ((entry = zis.getNextEntry()) != null) {
        Path target = root.resolve(entry.getName()).normalize();
        if (!target.startsWith(root)) {
            throw new SecurityException("Invalid zip path: " + entry.getName());
        }
        Files.createDirectories(target.getParent());
        Files.copy(zis, target, StandardCopyOption.REPLACE_EXISTING);
    }
}
```

## Detection indicators

- extracting archive members directly from `ZipEntry.getName()`
- writing untrusted archive content into a web root or application directory
- no size or depth limits on archive extraction

## Mitigation

- normalize and validate every archive member path
- keep extraction in a dedicated sandbox directory
- block absolute paths, traversal, symlinks, and duplicate entries
- enforce archive size and nesting limits
- quarantine uploaded archives before extraction
