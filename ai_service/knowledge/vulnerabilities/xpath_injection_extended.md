# XPath Injection Extended

## Overview

XPath injection extended covers cases where attackers can influence more complex XML query logic, including selection of multiple nodes, attribute manipulation, or bypass of policy checks in XML-backed applications.

## CWE

CWE-643: Improper Neutralization of Data within XPath Expressions ('XPath Injection')

## Relevant Java APIs

- javax.xml.xpath.XPathFactory
- javax.xml.xpath.XPath.compile
- javax.xml.xpath.XPathExpression.evaluate

## Attack conditions

The app performs XML lookups with query strings that include untrusted data and does not constrain the allowed XPath syntax.

## Vulnerable Java example

```java
String role = request.getParameter("role");
String expr = "/users/user[role='" + role + "']";
NodeList nodes = xpath.evaluate(expr, doc, XPathConstants.NODESET);
```

An attacker can add predicates or wildcard terms to widen the query.

## Secure Java example

```java
String role = request.getParameter("role");
if (!role.matches("^(admin|user|guest)$")) {
    throw new IllegalArgumentException("Invalid role");
}
String expr = "/users/user[role='" + role + "']";
```

## Detection indicators

- user data directly forming XPath predicates or node selectors
- XML-backed authorization checks using unvalidated XPath values
- complex XPath queries built from request data without escaping

## Mitigation

- restrict the query domain to expected values and node names
- escape characters used by XPath expressions
- validate XML access using approved safe data domains
- prefer explicit structured access over dynamic XPath strings when possible
