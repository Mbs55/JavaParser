---
source: http
---

# http

# HTTP

All HTTP-based communication should be protected xref:features/exploits/http.adoc#http[using TLS].

This section discusses the details of servlet-specific features that assist with HTTPS usage.

## Redirect to HTTPS

If a client makes a request using HTTP rather than HTTPS, you can configure Spring Security to redirect to HTTPS.

For example, the following Java or Kotlin configuration redirects any HTTP requests to HTTPS:

.Redirect to HTTPS
======
Java::
+
----
@Configuration
@EnableWebSecurity
public class WebSecurityConfig {

@Bean
public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
http
.redirectToHttps(withDefaults());
return http.build();
}
}
----

Kotlin::
+
----
@Configuration
@EnableWebSecurity
class SecurityConfig {

@Bean
open fun filterChain(http: HttpSecurity): SecurityFilterChain {
http {
redirectToHttps { }
}
return http.build()
}
}
----
======

The following XML configuration redirects all HTTP requests to HTTPS

.Redirect to HTTPS with XML Configuration
----
<http>
<intercept-url pattern="/**" access="ROLE_USER" requires-channel="https"/>
...
</http>
----


## Strict Transport Security

Spring Security provides support for xref:servlet/exploits/headers.adoc#servlet-headers-hsts[Strict Transport Security] and enables it by default.

## Proxy Server Configuration

Spring Security xref:features/exploits/http.adoc#http-proxy-server[integrates with proxy servers].
