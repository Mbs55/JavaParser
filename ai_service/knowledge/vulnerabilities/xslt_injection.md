# XSLT Injection

## Overview

XSLT injection occurs when untrusted input is used to influence XSLT processing or transform logic. This can cause information disclosure, logic alteration, or code execution depending on the transformation engine and runtime environment.

## CWE

CWE-91: XML Injection or related XML-processing issue

## Relevant Java APIs

- javax.xml.transform.TransformerFactory.newInstance
- javax.xml.transform.Transformer.transform
- javax.xml.transform.stream.StreamSource

## Attack conditions

The application compiles or applies XSLT templates based on untrusted values or allows user-controlled stylesheet content.

## Vulnerable Java example

```java
String style = request.getParameter("style");
TransformerFactory tf = TransformerFactory.newInstance();
Templates templates = tf.newTemplates(new StreamSource(new StringReader(style)));
Transformer transformer = templates.newTransformer();
transformer.transform(new StreamSource(xml), new StreamResult(out));
```

If the stylesheet is attacker-controlled, the transformation may perform unexpected actions.

## Secure Java example

```java
String style = request.getParameter("style");
if (!style.matches("^[A-Za-z0-9_./-]{1,64}$")) {
    throw new IllegalArgumentException("Invalid stylesheet");
}
```

and prefer trusted, fixed XSLT templates instead of user-provided stylesheets.

## Detection indicators

- issuing XSLT transforms with user-supplied stylesheets
- dynamic stylesheet generation from request or database values
- XML transformations without strict trust boundaries

## Mitigation

- prefer fixed, trusted XSLT templates
- validate and allowlist stylesheet names or content
- avoid exposing transform functionality to untrusted users
- apply strict input controls on XML and stylesheet sources

## Common false positives

- trusted internal XSLT transformations with fixed templates are not inherently vulnerable