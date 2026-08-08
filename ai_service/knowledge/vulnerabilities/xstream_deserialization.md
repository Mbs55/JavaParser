# XStream Deserialization

## Overview

XStream deserialization occurs when untrusted XML or object data is processed by XStream without strict type restrictions. This can enable gadget chains and unsafe conversion into arbitrary classes.

## CWE

CWE-502: Deserialization of Untrusted Data

## Relevant Java APIs

- com.thoughtworks.xstream.XStream.fromXML
- com.thoughtworks.xstream.XStream.unmarshal
- com.thoughtworks.xstream.security.NoTypePermission

## Attack conditions

The app deserializes incoming XML or object streams from untrusted sources with permissive XStream configuration.

## Vulnerable Java example

```java
XStream xs = new XStream();
Object obj = xs.fromXML(request.getParameter("payload"));
```

This can allow types or converter chains that execute dangerous behavior.

## Secure Java example

```java
XStream xs = new XStream();
xs.addPermission(NoTypePermission.NONE);
xs.allowTypes(new Class[] { MyDto.class });
MyDto dto = (MyDto) xs.fromXML(payload);
```

## Detection indicators

- `XStream.fromXML` or `unmarshal` on untrusted data
- permissive default XStream settings and no type allowlisting
- deserializing XML from network input without validation

## Mitigation

- restrict allowed types and disallow generic type deserialization
- validate and sanitize incoming payloads before parsing
- avoid XStream for untrusted external input
- prefer safe typed DTO parsing when possible

## Common false positives

- trusted internal XML with a strict type allowlist may be acceptable when controlled