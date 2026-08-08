# XPath Injection

## Overview

XPath injection occurs when untrusted input is used to construct an XPath expression. Attackers can bypass authentication checks or retrieve unexpected data by manipulating the XPath semantics.

## CWE

CWE-643: Improper Neutralization of Data within XPath Expressions ('XPath Injection')

## Relevant Java APIs

- javax.xml.xpath.XPath.evaluate
- javax.xml.xpath.XPathExpression
- org.springframework.ldap.core.LdapTemplate

## Attack conditions

The app creates XPath query strings from user-supplied values without escaping special characters or validating allowed patterns.

## Vulnerable Java example

```java
String user = request.getParameter("user");
String expr = "/users/user[@name='" + user + "']";
NodeList nodes = xpath.evaluate(expr, doc, XPathConstants.NODESET);
```

An attacker can craft a value that changes the expression structure and selects more records than expected.

## Secure Java example

```java
String user = request.getParameter("user");
if (!user.matches("^[A-Za-z0-9._-]{1,64}$")) {
    throw new IllegalArgumentException("Invalid user");
}
String expr = "/users/user[@name='" + user.replace("'", "&apos;") + "']";
```

## Detection indicators

- XPath strings assembled from request parameters or user data
- direct evaluation of untrusted XPath expressions
- use of XML query inputs without schema or validation rules

## Mitigation

- validate user input against a strict allowlist or safe pattern
- escape special XML/XPath characters when composing queries
- use parameterized or library-based query construction when possible
- review access checks that rely on XPath-driven XML data retrieval
