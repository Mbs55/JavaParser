# Resource Exhaustion

## Overview

Resource exhaustion happens when an application allows attackers to consume excessive memory, files, CPU, threads, or network resources. This can degrade service performance or cause outages.

## CWE

CWE-400: Uncontrolled Resource Consumption

## Relevant Java APIs

- java.io.ByteArrayOutputStream
- java.nio.file.Files.readAllBytes
- new String(byte[], ...)
- java.util.concurrent.Executors.newFixedThreadPool
- java.util.zip.ZipInputStream

## Attack conditions

The app accepts unbounded input, archive content, or loops with no size checks and then processes them without limits.

## Vulnerable Java example

```java
byte[] data = request.getInputStream().readAllBytes();
String text = new String(data, StandardCharsets.UTF_8);
```

A malicious client can send arbitrarily large payloads and exhaust memory or CPU.

## Secure Java example

```java
InputStream in = request.getInputStream();
byte[] buffer = new byte[8192];
int total = 0;
while ((n = in.read(buffer)) != -1 && total < 1_000_000) {
    total += n;
}
if (total >= 1_000_000) {
    throw new IllegalArgumentException("Request too large");
}
```

## Detection indicators

- unbounded reads or writes from user-controlled streams
- large archive or file uploads without maximum size enforcement
- loops or recursive processing based on external data without limits

## Mitigation

- enforce size limits for uploads, requests, and responses
- cap recursion, iteration counts, and thread pools
- reject or rate-limit abusive input patterns
- tune file and memory limits appropriately for deployment environments

## Common false positives

- bounded internal batch jobs with safe resource limits are not vulnerabilities
- normal application memory use should not be equated with uncontrolled consumption