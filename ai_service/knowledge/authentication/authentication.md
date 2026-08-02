---
source: authentication
---

# authentication

# Running a Test as a User in Spring MVC Test

It is often desirable to run tests as a specific user.
There are two simple ways to populate the user:

- <<test-mockmvc-securitycontextholder-rpp,Running as a User in Spring MVC Test with RequestPostProcessor>>
- <<test-mockmvc-withmockuser,Running as a User in Spring MVC Test with Annotations>>

## Running as a User in Spring MVC Test with RequestPostProcessor

You have a number of options to associate a user to the current `HttpServletRequest`.
The following example runs as a user (which does not need to exist) whose username is `user`, whose password is `password`, and whose role is `ROLE_USER`:

======
Java::
+
----
mvc
.perform(get("/").with(user("user")))
----

Kotlin::
+
----
mvc.get("/") {
with(user("user"))
}
----
======

====
The support works by associating the user to the `HttpServletRequest`.
To associate the request to the `SecurityContextHolder`, you need to ensure that the `SecurityContextPersistenceFilter` is associated with the `MockMvc` instance.
You can do so in a number of ways:

- Invoking xref:servlet/test/mockmvc/setup.adoc#test-mockmvc-setup[`apply(springSecurity())`]
- Adding Spring Security's `FilterChainProxy` to `MockMvc`
- Manually adding `SecurityContextPersistenceFilter` to the `MockMvc` instance may make sense when using `MockMvcBuilders.standaloneSetup`
====



You can easily make customizations.
For example, the following will run as a user (which does not need to exist) with the username "admin", the password "pass", and the roles "ROLE_USER" and "ROLE_ADMIN".

======
Java::
+
----
mvc
.perform(get("/admin").with(user("admin").password("pass").roles("USER","ADMIN")))
----

Kotlin::
+
----
mvc.get("/admin") {
with(user("admin").password("pass").roles("USER","ADMIN"))
}
----
======

If you have a custom `UserDetails` that you would like to use, you can easily specify that as well.
For example, the following will use the specified `UserDetails` (which does not need to exist) to run with a `UsernamePasswordAuthenticationToken` that has a principal of the specified `UserDetails`:

======
Java::
+
----
mvc
.perform(get("/").with(user(userDetails)))
----

Kotlin::
+
----
mvc.get("/") {
with(user(userDetails))
}
----
======

You can run as anonymous user using the following:

======
Java::
+
----
mvc
.perform(get("/").with(anonymous()))
----

Kotlin::
+
----
mvc.get("/") {
with(anonymous())
}
----
======

This is especially useful if you are running with a default user and wish to process a few requests as an anonymous user.

If you want a custom `Authentication` (which does not need to exist) you can do so using the following:

======
Java::
+
----
mvc
.perform(get("/").with(authentication(authentication)))
----

Kotlin::
+
----
mvc.get("/") {
with(authentication(authentication))
}
----
======

You can even customize the `SecurityContext` using the following:

======
Java::
+
----
mvc
.perform(get("/").with(securityContext(securityContext)))
----

Kotlin::
+
----
mvc.get("/") {
with(securityContext(securityContext))
}
----
======

We can also ensure to run as a specific user for every request by using ``MockMvcBuilders``'s default request.
For example, the following will run as a user (which does not need to exist) with the username "admin", the password "password", and the role "ROLE_ADMIN":

======
Java::
+
----
mvc = MockMvcBuilders
.webAppContextSetup(context)
.defaultRequest(get("/").with(user("user").roles("ADMIN")))
.apply(springSecurity())
.build();
----

Kotlin::
+
----
mvc = MockMvcBuilders
.webAppContextSetup(context)
.defaultRequest<DefaultMockMvcBuilder>(get("/").with(user("user").roles("ADMIN")))
.apply<DefaultMockMvcBuilder>(springSecurity())
.build()
----
======

If you find you are using the same user in many of your tests, it is recommended to move the user to a method.
For example, you can specify the following in your own class named `CustomSecurityMockMvcRequestPostProcessors`:

======
Java::
+
----
public static RequestPostProcessor rob() {
return user("rob").roles("ADMIN");
}
----

Kotlin::
+
----
fun rob(): RequestPostProcessor {
return user("rob").roles("ADMIN")
}
----
======

Now you can perform a static import on `CustomSecurityMockMvcRequestPostProcessors` and use that within your tests:

======
Java::
+
----
import static sample.CustomSecurityMockMvcRequestPostProcessors.*;

...

mvc
.perform(get("/").with(rob()))
----

Kotlin::
+
----
import sample.CustomSecurityMockMvcRequestPostProcessors.*


mvc.get("/") {
with(rob())
}
----
======

## Running as a User in Spring MVC Test with Annotations

As an alternative to using a `RequestPostProcessor` to create your user, you can use annotations described in xref:servlet/test/method.adoc[Testing Method Security].
For example, the following will run the test with the user with username "user", password "password", and role "ROLE_USER":

======
Java::
+
----
@Test
@WithMockUser
public void requestProtectedUrlWithUser() throws Exception {
mvc
.perform(get("/"))
...
}
----

Kotlin::
+
----
@Test
@WithMockUser
fun requestProtectedUrlWithUser() {
mvc
.get("/")
}
----
======

Alternatively, the following will run the test with the user with username "user", password "password", and role "ROLE_ADMIN":

======
Java::
+
----
@Test
@WithMockUser(roles="ADMIN")
public void requestProtectedUrlWithUser() throws Exception {
mvc
.perform(get("/"))
...
}
----

Kotlin::
+
----
@Test
@WithMockUser(roles = ["ADMIN"])
fun requestProtectedUrlWithUser() {
mvc
.get("/")
}
----
======
