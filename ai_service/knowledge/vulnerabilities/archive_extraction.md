# Archive Extraction

## Summary

Archive extraction vulnerabilities happen when untrusted archive content is extracted without validating path names, file types, or compression depth. This can lead to path traversal, overwrite of application data, denial of service, or remote code execution when extracted files are later processed.

## CWE

CWE-22 and CWE-409 are common related classes, depending on whether the extraction uses attacker-controlled paths or resource exhaustion.

## Relevant Java APIs

- java.util.zip.ZipFile
- java.util.jar.JarFile
- java.nio.file.Files.copy
- java.nio.file.Files.newInputStream
- java.nio.file.Path.resolve

## Vulnerable Java example

```java
Path targetDir = Paths.get("/tmp/extract");
try (ZipInputStream zis = new ZipInputStream(new FileInputStream(uploadFile))) {
    ZipEntry entry;
    while ((entry = zis.getNextEntry()) != null) {
        Path resolved = targetDir.resolve(entry.getName()).normalize();
        Files.copy(zis, resolved, StandardCopyOption.REPLACE_EXISTING);
    }
}
```

If an entry name contains `../`, the file can overwrite application files.

## Secure Java example

```java
Path targetDir = Paths.get("/var/app/uploads");
try (ZipInputStream zis = new ZipInputStream(new FileInputStream(uploadFile))) {
    ZipEntry entry;
    while ((entry = zis.getNextEntry()) != null) {
        Path resolved = targetDir.resolve(entry.getName()).normalize();
        if (!resolved.startsWith(targetDir)) {
            throw new SecurityException("Invalid archive entry: " + entry.getName());
        }
        Files.createDirectories(resolved.getParent());
        Files.copy(zis, resolved, StandardCopyOption.REPLACE_EXISTING);
    }
}
```

## Detection indicators

- extracting uploaded ZIP, JAR, or TAR files without a validated destination
- direct use of archive entry names to create filesystem paths
- extraction of nested archives or large unbounded archives without limits

## Mitigation

- validate all extracted paths against a fixed root directory
- reject absolute paths, traversal sequences, and symlinks
- cap archive size and nested entry depth
- scan or quarantine uploaded archives before extraction
- extract into a dedicated sandbox directory with restricted permissions
