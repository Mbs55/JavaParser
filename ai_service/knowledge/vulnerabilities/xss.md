# Cross-Site Scripting (XSS)

## Overview

XSS occurs when attacker-controlled data is rendered into HTML, JavaScript, or other browser-executable contexts without proper escaping or encoding. This can allow script execution in a victim’s browser.

## CWE

CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')

## Relevant Java APIs

- javax.servlet.http.HttpServletResponse
- org.springframework.web.bind.annotation.ResponseBody
- org.thymeleaf.TemplateEngine
- java.lang.String

## Attack conditions

The app writes untrusted input into HTML templates, JSON responses, or generated web pages without encoding.

## Vulnerable Java example

```java
String name = request.getParameter("name");
response.getWriter().write("<p>Hello, " + name + "</p>");
```

This allows script injection if the name contains `<script>`.

## Secure Java example

```java
String name = request.getParameter("name");
String safeName = HtmlUtils.htmlEscape(name);
response.getWriter().write("<p>Hello, " + safeName + "</p>");
```

## Detection indicators

- writing request values directly into HTML output or templates
- concatenating user strings into JavaScript or URL contexts
- unencoded data rendered in pages without a framework security layer

## Mitigation

- output encode according to context: HTML, JavaScript, URL, CSS, and attribute contexts
- prefer safe templating libraries and escaping functions
- avoid injecting raw user content into JavaScript or event handlers
- validate and constrain input to expected formats

## Common false positives

- data shown in JSON or API responses may still be safe if it is not rendered in a browser without escaping
- some frameworks automatically escape values, which can reduce the risk if used correctly