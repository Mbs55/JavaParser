# Dangerous XML External Entities

## Overview

XXE occurs when XML parsers process external entities or DTDs from untrusted input. This can expose local files, internal services, or cause external resource retrieval.

## CWE

CWE-611: Improper Restriction of XML External Entity Reference

## Relevant Java APIs

- javax.xml.parsers.DocumentBuilderFactory
- javax.xml.parsers.SAXParserFactory
- javax.xml.stream.XMLInputFactory
- javax.xml.validation.SchemaFactory
- org.xml.sax.XMLReader

## Attack conditions

The risk appears when an XML parser is configured to allow DTDs, external entities, or XInclude and then processes attacker-controlled XML.

## Vulnerable Java example

```java
DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
DocumentBuilder db = dbf.newDocumentBuilder();
Document doc = db.parse(new ByteArrayInputStream(xmlBytes));
```

If the parser accepts external entities, attacker-supplied XML can load `file:///etc/passwd` or remote resources.

## Secure Java example

```java
DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
dbf.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
dbf.setFeature("http://xml.org/sax/features/external-general-entities", false);
dbf.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
dbf.setFeature("http://apache.org/xml/features/nonvalidating/load-external-dtd", false);
dbf.setXIncludeAware(false);
dbf.setExpandEntityReferences(false);
```

## Detection indicators

- XML parsing of untrusted input without disabling DTDs or external entities
- use of default parser configuration without secure features enabled
- processing of XML from internet or user-controlled sources

## Mitigation

- disable DTDs and external entity resolution
- disable external DTD loading, XInclude, and entity expansion
- use safe parser configuration for all XML entry points
- validate XML schema and parser settings

## Common false positives

- parsing trusted internal XML with secure parser settings is not a vulnerability
- safe parser configuration is acceptable and recommended
