# File Disclosure

## Overview

File disclosure happens when an application exposes internal file paths, source files, configuration data, or template locations due to unsafe forwarding, inclusion, or view resolution.

## CWE

CWE-538: Insertion of Sensitive Information into Exposed Parameters

## Relevant Java APIs

- javax.servlet.RequestDispatcher.forward
- javax.servlet.RequestDispatcher.include
- org.apache.struts.action.ActionForward
- org.apache.struts.action.ActionForward.setPath
- org.springframework.web.servlet.ModelAndView
- org.springframework.web.servlet.ModelAndView.setViewName

## Attack conditions

The issue appears when user input controls a file path, view name, or request target and is used in a file or internal resource dispatch.

## Vulnerable Java example

```java
String target = request.getParameter("page");
RequestDispatcher rd = request.getRequestDispatcher(target);
rd.forward(request, response);
```

An attacker can request server-side files or internal resources such as `/WEB-INF/web.xml` or configuration files.

## Secure Java example

```java
String target = request.getParameter("page");
Set<String> allowed = Set.of("home", "profile", "admin");
if (!allowed.contains(target)) {
    response.sendError(HttpServletResponse.SC_BAD_REQUEST);
    return;
}

RequestDispatcher rd = request.getRequestDispatcher("/WEB-INF/views/" + target + ".jsp");
rd.forward(request, response);
```

## Detection indicators

- user-controlled view names or forward targets
- direct use of request parameters in `forward`, `include`, or `setViewName`
- exposure of `/WEB-INF`, `/META-INF`, or application configuration files

## Mitigation

- use allowlists for internal view names
- avoid exposing internal paths or templates directly
- validate request-driven navigation targets
- prevent direct access to configuration or resource directories
- use a safe controller or view mapping layer

## Common false positives

- a static view name is safe
- explicit internal routing controlled by constants is not a vulnerability
