# Server-Side Template Injection

## Overview

Server-Side Template Injection (SSTI) occurs when user-controlled input is interpreted by a server-side template engine, allowing code execution or data extraction through template features.

## CWE

CWE-1336: Improper Neutralization of Special Elements Used in a Template Engine

## Relevant Java APIs

- org.apache.velocity.app.Velocity.evaluate
- org.apache.velocity.app.Velocity.mergeTemplate
- org.apache.velocity.app.VelocityEngine.evaluate
- freemarker.template.Template.process
- org.thymeleaf.TemplateEngine.process
- org.springframework.ui.freemarker.FreeMarkerTemplateUtils.processTemplateIntoString

## Attack conditions

This arises when user data is passed into a template engine without restrictions, or when template inputs are user-controlled and the template engine permits scripting or expression evaluation.

## Vulnerable Java example

```java
String template = request.getParameter("template");
String result = FreeMarkerTemplateUtils.processTemplateIntoString(
    configuration.getTemplate("template.ftl"), model);
```

If the template itself or its data model is influenced by attacker input, it may allow expression or code execution.

## Secure Java example

```java
String userName = request.getParameter("name");
if (!userName.matches("^[A-Za-z0-9 _-]{1,64}$")) {
    throw new IllegalArgumentException("Invalid user name");
}
model.put("userName", userName);
String output = templateEngine.process("welcome", context);
```

The template engine should receive trusted templates and sanitized values.

## Detection indicators

- untrusted input passed to template rendering APIs
- dynamic template names or template strings from request parameters
- user-controlled model values influencing template expressions

## Mitigation

- do not allow untrusted input to define template content
- keep templates server-side and static
- validate all values before applying them to templates
- disable direct expression or script execution where possible
- use safe output escaping in templates

## Framework examples

Thymeleaf, Freemarker, and Velocity are powerful, but unsafe when they process attacker-controlled templates or expression data.
