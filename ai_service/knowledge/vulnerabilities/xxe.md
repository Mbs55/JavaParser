# XML External Entity (XXE)

## Overview

XXE occurs when XML parsing accepts external entities or DTDs from untrusted inputs. Attackers can use those features to read local files, perform SSRF, or consume system resources.

## CWE

CWE-611: Improper Restriction of XML External Entity Reference

## Relevant Java APIs

- javax.xml.parsers.DocumentBuilderFactory
- javax.xml.parsers.SAXParserFactory
- javax.xml.stream.XMLInputFactory
- org.xml.sax.XMLReader

## Attack conditions

The parser is configured to allow external entities or DTDs while handling user-controlled XML.

## Vulnerable Java example

```java
DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
DocumentBuilder builder = factory.newDocumentBuilder();
Document doc = builder.parse(new ByteArrayInputStream(xmlBytes));
```

With a default insecure configuration, external entities become active.

## Secure Java example

```java
DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
factory.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
factory.setFeature("http://xml.org/sax/features/external-general-entities", false);
factory.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
factory.setFeature("http://apache.org/xml/features/nonvalidating/load-external-dtd", false);
```

## Detection indicators

- XML parsing of untrusted input without disabling DTDs or external entities
- default parser factory settings in application code
- untrusted XML from uploads, web requests, or message queues

## Mitigation

- disable DTDs and external entity resolution
- reject XML that contains DTD declarations or external references
- use secure XML processing libraries and hardened parser settings
- validate incoming XML against a schema or whitelist

## Common false positives

- trusted internal XML processed with hardened, restricted parser settings is not an XXE issue