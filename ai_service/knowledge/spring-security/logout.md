---
source: logout
---

# logout

# Testing Logout

While fairly trivial using standard Spring MVC Test, you can use Spring Security's testing support to make testing log out easier.
For example, the following `logout` xref:servlet/test/mockmvc/request-post-processors.adoc[`RequestPostProcessor`] will submit a POST to "/logout" with a valid CSRF token:

======
Java::
+
----
mvc
.perform(logout())
----

Kotlin::
+
----
mvc
.perform(logout())
----
======

You can also customize the URL to post to.
For example, the snippet below will submit a POST to "/signout" with a valid CSRF token:

======
Java::
+
----
mvc
.perform(logout("/signout"))
----

Kotlin::
+
----
mvc
.perform(logout("/signout"))
----
======
