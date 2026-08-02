---
source: csrf
---

# csrf

# Testing with CSRF Protection

When testing any non-safe HTTP methods and using Spring Security's CSRF protection, you must include a valid CSRF Token in the request.
To specify a valid CSRF token as a request parameter use the CSRF xref:servlet/test/mockmvc/request-post-processors.adoc[`RequestPostProcessor`] like so:

======
Java::
+
----
mvc
.perform(post("/").with(csrf()))
----

Kotlin::
+
----
mvc.post("/") {
with(csrf())
}
----
======

If you like, you can include CSRF token in the header instead:

======
Java::
+
----
mvc
.perform(post("/").with(csrf().asHeader()))
----

Kotlin::
+
----
mvc.post("/") {
with(csrf().asHeader())
}
----
======

You can also test providing an invalid CSRF token by using the following:

======
Java::
+
----
mvc
.perform(post("/").with(csrf().useInvalidToken()))
----

Kotlin::
+
----
mvc.post("/") {
with(csrf().useInvalidToken())
}
----
======
