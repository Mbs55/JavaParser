---
source: user details service
---

# user details service

# UserDetailsService

javadoc:org.springframework.security.core.userdetails.UserDetailsService[] is used by xref:servlet/authentication/passwords/dao-authentication-provider.adoc#servlet-authentication-daoauthenticationprovider[`DaoAuthenticationProvider`] for retrieving a username, a password, and other attributes for authenticating with a username and password.
Spring Security provides xref:servlet/authentication/passwords/in-memory.adoc#servlet-authentication-inmemory[in-memory], xref:servlet/authentication/passwords/jdbc.adoc#servlet-authentication-jdbc[JDBC], and xref:servlet/authentication/passwords/caching.adoc#servlet-authentication-caching-user-details[caching] implementations of `UserDetailsService`.

You can define custom authentication by exposing a custom `UserDetailsService` as a bean.
For example, the following listing customizes authentication, assuming that `CustomUserDetailsService` implements `UserDetailsService`:

====
This is only used if the `AuthenticationManagerBuilder` has not been populated and no `AuthenticationProviderBean` is defined.
====

.Custom UserDetailsService Bean
======
Java::
+
----
@Bean
CustomUserDetailsService customUserDetailsService() {
return new CustomUserDetailsService();
}
----

XML::
+
----
<b:bean class="example.CustomUserDetailsService"/>
----

Kotlin::
+
----
@Bean
fun customUserDetailsService() = CustomUserDetailsService()
----
======
