---
source: introduction
---

# introduction

# Introduction

Spring Security Kerberos {spring-security-version} is built and tested with JDK 17,
Spring Security {spring-security-version} and Spring Framework {spring-core-version}.

The dependency coordinates changed with Spring Security 7:

======
Maven::
+
.pom.xml
----
<dependencies>
<!-- ... other dependency elements ... -->
<dependency>
<groupId>org.springframework.security</groupId>
<artifactId>spring-security-kerberos-core</artifactId>
</dependency>
<dependency>
<groupId>org.springframework.security</groupId>
<artifactId>spring-security-kerberos-web</artifactId>
</dependency>
</dependencies>
----

Gradle::
+
.build.gradle
----
dependencies {
implementation "org.springframework.security:spring-security-kerberos-core"
implementation "org.springframework.security:spring-security-kerberos-web"
}
----
======
