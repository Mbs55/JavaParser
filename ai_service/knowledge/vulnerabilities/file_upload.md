# File Upload

## Overview

File upload vulnerabilities occur when users can upload files without validation, path controls, or content checks. This can enable malware storage, application compromise, path traversal, or resource exhaustion.

## CWE

CWE-434: Unrestricted Upload of File with Dangerous Type

## Relevant Java APIs

- org.springframework.web.multipart.MultipartFile
- jakarta.servlet.http.Part
- javax.servlet.http.Part
- java.io.FileOutputStream
- java.nio.file.Files.write

## Vulnerable Java example

```java
MultipartFile uploaded = request.getFile("file");
Path path = Paths.get("/uploads/" + uploaded.getOriginalFilename());
Files.write(path, uploaded.getBytes());
```

This allows malicious or dangerous files to be saved in the application’s file system.

## Secure Java example

```java
MultipartFile uploaded = request.getFile("file");
String name = uploaded.getOriginalFilename();
String safeName = Paths.get(name).getFileName().toString();
if (!safeName.matches("^[A-Za-z0-9._-]{1,120}$")) {
    throw new IllegalArgumentException("Invalid upload name");
}
if (!Set.of("pdf", "png", "jpg").contains(Files.getFileAttributeView(...))) {
    throw new IllegalArgumentException("Invalid file type");
}
```

## Detection indicators

- uploaded files stored with names from user input
- insecure file types or file sizes accepted without validation
- lack of content checks or malware scanning for uploaded files

## Mitigation

- restrict accepted file types and sizes
- generate safe internal filenames rather than trusting user names
- isolate uploads to a dedicated directory
- scan or validate uploaded content before storage and processing
- reject executable script or archive files unless explicitly needed

## Common false positives

- safe uploads to a fixed directory with generated names and validated extensions are not vulnerable
- uploads handled by trusted server-side libraries may still require validation
