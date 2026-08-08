# XXE Extended

## Overview

XXE extended covers additional XML parser edge cases where external entities, XInclude, or DTD-based behavior is still enabled or mishandled. This overlaps with XXE but focuses on more specific parser configuration and data-source variants.

## CWE

CWE-611: Improper Restriction of XML External Entity Reference

## Relevant Java APIs

- javax.xml.stream.XMLInputFactory.setProperty
- org.xml.sax.XMLReader.setFeature
- javax.xml.parsers.SAXParserFactory.setFeature

## Attack conditions

The parser accepts untrusted XML with entity expansion, network access, or XInclude while left in an insecure configuration.

## Vulnerable Java example

```java
XMLInputFactory factory = XMLInputFactory.newFactory();
factory.setProperty(XMLInputFactory.IS_SUPPORTING_EXTERNAL_ENTITIES, true);
factory.setProperty(XMLInputFactory.SUPPORT_DTD, true);
```

This allows external entity processing and DTD handling.

## Secure Java example

```java
XMLInputFactory factory = XMLInputFactory.newFactory();
factory.setProperty(XMLInputFactory.IS_SUPPORTING_EXTERNAL_ENTITIES, false);
factory.setProperty(XMLInputFactory.SUPPORT_DTD, false);
```

## Detection indicators

- enabling external entity features in XML parsers
- allowing DTD or XInclude processing for untrusted XML
- configuration of parser factories without security restrictions

## Mitigation

- disable external entities and DTD support uniformly
- reject or sanitize network-reachable references in XML input
- keep parser configuration in a central secure wrapper and reuse it consistently

## Common false positives

- safe XML parsers that are configured securely are not vulnerable