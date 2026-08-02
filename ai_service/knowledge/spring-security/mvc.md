---
source: mvc
---

# mvc

# Spring MVC Integration

Spring Security provides a number of optional integrations with Spring MVC.
This section covers the integration in further detail.

## @EnableWebSecurity

To enable Spring Security integration with Spring MVC, add the `@EnableWebSecurity` annotation to your configuration.

====
Spring Security provides the configuration by using Spring MVC's {spring-framework-reference-url}web/webmvc/mvc-config/customize.html[`WebMvcConfigurer`].
This means that, if you use more advanced options, such as integrating with `WebMvcConfigurationSupport` directly, you need to manually provide the Spring Security configuration.
====

## PathPatternRequestMatcher

Spring Security provides deep integration with how Spring MVC matches on URLs with `PathPatternRequestMatcher`.
This is helpful to ensure that your Security rules match the logic used to handle your requests.

`PathPatternRequestMatcher` must use the same `PathPatternParser` as Spring MVC.
If you are not customizing the `PathPatternParser`, then you can do:

======
Java::
+
----
@Bean
PathPatternRequestMatcherBuilderFactoryBean usePathPattern() {
return new PathPatternRequestMatcherBuilderFactoryBean();
}
----

Kotlin::
+
----
@Bean
fun usePathPattern(): PathPatternRequestMatcherBuilderFactoryBean {
return PathPatternRequestMatcherBuilderFactoryBean()
}
----

Xml::
+
----
<b:bean class="org.springframework.security.config.web.PathPatternRequestMatcherBuilderFactoryBean"/>
----
======

and Spring Security will find the appropriate Spring MVC configuration for you.

If you *are* customizing Spring MVC's `PathPatternParser` instance, you will need to <<security-mvc-same-application-context, configure Spring Security and Spring MVC in the same `ApplicationContext`>>.

====
We always recommend that you provide authorization rules by matching on the `HttpServletRequest` and method security.

Providing authorization rules by matching on `HttpServletRequest` is good, because it happens very early in the code path and helps reduce the https://en.wikipedia.org/wiki/Attack_surface[attack surface].
Method security ensures that, if someone has bypassed the web authorization rules, your application is still secured.
This is known as https://en.wikipedia.org/wiki/Defense_in_depth_(computing)[Defense in Depth]
====

Now that Spring MVC is integrated with Spring Security, you are ready to write some xref:servlet/authorization/authorize-http-requests.adoc[authorization rules] that will use `PathPatternRequestMatcher`.

## @AuthenticationPrincipal

Spring Security provides `AuthenticationPrincipalArgumentResolver`, which can automatically resolve the current `Authentication.getPrincipal()` for Spring MVC arguments.
By using `@EnableWebSecurity`, you automatically have this added to your Spring MVC configuration.
If you use XML-based configuration, you must add this yourself:

----
<mvc:annotation-driven>
<mvc:argument-resolvers>
<bean class="org.springframework.security.web.method.annotation.AuthenticationPrincipalArgumentResolver" />
</mvc:argument-resolvers>
</mvc:annotation-driven>
----

Once you have properly configured `AuthenticationPrincipalArgumentResolver`, you can entirely decouple from Spring Security in your Spring MVC layer.

Consider a situation where a custom `UserDetailsService` returns an `Object` that implements `UserDetails` and your own `CustomUser` `Object`. The `CustomUser` of the currently authenticated user could be accessed by using the following code:

======
Java::
+
----
@RequestMapping("/messages/inbox")
public ModelAndView findMessagesForUser() {
Authentication authentication =
SecurityContextHolder.getContext().getAuthentication();
CustomUser custom = (CustomUser) authentication == null ? null : authentication.getPrincipal();

}
----

Kotlin::
+
----
@RequestMapping("/messages/inbox")
open fun findMessagesForUser(): ModelAndView {
val authentication: Authentication = SecurityContextHolder.getContext().authentication
val custom: CustomUser? = if (authentication as CustomUser == null) null else authentication.principal

}
----
======

As of Spring Security 3.2, we can resolve the argument more directly by adding an annotation:

======
Java::
+
----
import org.springframework.security.core.annotation.AuthenticationPrincipal;


@RequestMapping("/messages/inbox")
public ModelAndView findMessagesForUser(@AuthenticationPrincipal CustomUser customUser) {

}
----

Kotlin::
+
----
@RequestMapping("/messages/inbox")
open fun findMessagesForUser(@AuthenticationPrincipal customUser: CustomUser?): ModelAndView {

}
----
======

Sometimes, you may need to transform the principal in some way.
For example, if `CustomUser` needed to be final, it could not be extended.
In this situation, the `UserDetailsService` might return an `Object` that implements `UserDetails` and provides a method named `getCustomUser` to access `CustomUser`:

======
Java::
+
----
public class CustomUserUserDetails extends User {
public CustomUser getCustomUser() {
return customUser;
}
}
----

Kotlin::
+
----
class CustomUserUserDetails(
username: String?,
password: String?,
authorities: MutableCollection<out GrantedAuthority>?
) : User(username, password, authorities) {
val customUser: CustomUser? = null
}
----
======

We could then access the `CustomUser` by using a {spring-framework-reference-url}core/expressions.html[SpEL expression] that uses `Authentication.getPrincipal()` as the root object:

======
Java::
+
----
import org.springframework.security.core.annotation.AuthenticationPrincipal;


@RequestMapping("/messages/inbox")
public ModelAndView findMessagesForUser(@AuthenticationPrincipal(expression = "customUser") CustomUser customUser) {

}
----

Kotlin::
+
----
import org.springframework.security.core.annotation.AuthenticationPrincipal


@RequestMapping("/messages/inbox")
open fun findMessagesForUser(@AuthenticationPrincipal(expression = "customUser") customUser: CustomUser?): ModelAndView {

}
----
======

We can also refer to beans in our SpEL expressions.
For example, we could use the following if we were using JPA to manage our users and if we wanted to modify and save a property on the current user:

======
Java::
+
----
import org.springframework.security.core.annotation.AuthenticationPrincipal;


@PutMapping("/users/self")
public ModelAndView updateName(@AuthenticationPrincipal(expression = "@jpaEntityManager.merge(#this)") CustomUser attachedCustomUser,
@RequestParam String firstName) {

attachedCustomUser.setFirstName(firstName);

}
----

Kotlin::
+
----
import org.springframework.security.core.annotation.AuthenticationPrincipal


@PutMapping("/users/self")
open fun updateName(
@AuthenticationPrincipal(expression = "@jpaEntityManager.merge(#this)") attachedCustomUser: CustomUser,
@RequestParam firstName: String?
): ModelAndView {

attachedCustomUser.setFirstName(firstName)

}
----
======

We can further remove our dependency on Spring Security by making `@AuthenticationPrincipal` a meta-annotation on our own annotation.
The next example demonstrates how we could do so on an annotation named `@CurrentUser`.

====
To remove the dependency on Spring Security, it is the consuming application that would create `@CurrentUser`.
This step is not strictly required but assists in isolating your dependency to Spring Security to a more central location.
====

======
Java::
+
----
@Target({ElementType.PARAMETER, ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Documented
@AuthenticationPrincipal
public @interface CurrentUser {}
----

Kotlin::
+
----
@Target(AnnotationTarget.VALUE_PARAMETER, AnnotationTarget.TYPE)
@Retention(AnnotationRetention.RUNTIME)
@MustBeDocumented
@AuthenticationPrincipal
annotation class CurrentUser
----
======

We have isolated our dependency on Spring Security to a single file.
Now that `@CurrentUser` has been specified, we can use it to signal to resolve our `CustomUser` of the currently authenticated user:

======
Java::
+
----
@RequestMapping("/messages/inbox")
public ModelAndView findMessagesForUser(@CurrentUser CustomUser customUser) {

}
----

Kotlin::
+
----
@RequestMapping("/messages/inbox")
open fun findMessagesForUser(@CurrentUser customUser: CustomUser?): ModelAndView {

}
----
======

Once it is a meta-annotation, parameterization is also available to you.

For example, consider when you have a JWT as your principal and you want to say which claim to retrieve.
As a meta-annotation, you might do:

======
Java::
+
----
@Target({ElementType.PARAMETER, ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Documented
@AuthenticationPrincipal(expression = "claims['sub']")
public @interface CurrentUser {}
----

Kotlin::
+
----
@Target(AnnotationTarget.VALUE_PARAMETER, AnnotationTarget.TYPE)
@Retention(AnnotationRetention.RUNTIME)
@MustBeDocumented
@AuthenticationPrincipal(expression = "claims['sub']")
annotation class CurrentUser
----
======

which is already quite powerful.
But, it is also limited to retrieving the `sub` claim.

To make this more flexible, first publish the `AnnotationTemplateExpressionDefaults` bean like so:

======
Java::
+
----
@Bean
public AnnotationTemplateExpressionDefaults templateDefaults() {
return new AnnotationTemplateExpressionDefaults();
}
----

Kotlin::
+
----
@Bean
fun templateDefaults(): AnnotationTemplateExpressionDefaults {
return AnnotationTemplateExpressionDefaults()
}
----

Xml::
+
----
<b:bean name="annotationExpressionTemplateDefaults" class="org.springframework.security.core.annotation.AnnotationTemplateExpressionDefaults"/>
----
======

and then you can supply a parameter to `@CurrentUser` like so:

======
Java::
+
----
@Target({ElementType.PARAMETER, ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
@Documented
@AuthenticationPrincipal(expression = "claims['{claim}']")
public @interface CurrentUser {
String claim() default 'sub';
}
----

Kotlin::
+
----
@Target(AnnotationTarget.VALUE_PARAMETER, AnnotationTarget.TYPE)
@Retention(AnnotationRetention.RUNTIME)
@MustBeDocumented
@AuthenticationPrincipal(expression = "claims['{claim}']")
annotation class CurrentUser(val claim: String = "sub")
----
======

This will allow you more flexibility across your set of applications in the following way:

======
Java::
+
----
@RequestMapping("/messages/inbox")
public ModelAndView findMessagesForUser(@CurrentUser("user_id") String userId) {

}
----

Kotlin::
+
----
@RequestMapping("/messages/inbox")
open fun findMessagesForUser(@CurrentUser("user_id") userId: String?): ModelAndView {

}
----
======

## @CurrentSecurityContext

Spring Security provides `CurrentSecurityContextArgumentResolver`, which can automatically resolve the current `SecurityContext` for Spring MVC arguments.
By using `@EnableWebSecurity`, you automatically have this added to your Spring MVC configuration.
If you use XML-based configuration, you must add this yourself:

----
<mvc:annotation-driven>
<mvc:argument-resolvers>
<bean class="org.springframework.security.web.method.annotation.CurrentSecurityContextArgumentResolver" />
</mvc:argument-resolvers>
</mvc:annotation-driven>
----

Once `CurrentSecurityContextArgumentResolver` is configured, you can access the `SecurityContext` directly:

======
Java::
+
----
@GetMapping("/me")
public String me(@CurrentSecurityContext SecurityContext context) {
return context.getAuthentication().getName();
}
----

Kotlin::
+
----
@GetMapping("/me")
fun me(@CurrentSecurityContext context: SecurityContext): String {
return context.authentication.name
}
----
======

You can also use a SpEL expression that is rooted at the `SecurityContext`:

======
Java::
+
----
@GetMapping("/me")
public String me(@CurrentSecurityContext(expression = "authentication") Authentication authentication) {
return authentication.getName();
}
----

Kotlin::
+
----
@GetMapping("/me")
fun me(@CurrentSecurityContext(expression = "authentication") authentication: Authentication): String {
return authentication.name
}
----
======

## Spring MVC Async Integration

Spring Web MVC 3.2+ has excellent support for {spring-framework-reference-url}web/webmvc/mvc-ann-async.html[Asynchronous Request Processing].
With no additional configuration, Spring Security automatically sets up the `SecurityContext` to the `Thread` that invokes a `Callable` returned by your controllers.
For example, the following method automatically has its `Callable` invoked with the `SecurityContext` that was available when the `Callable` was created:

======
Java::
+
----
@RequestMapping(method=RequestMethod.POST)
public Callable<String> processUpload(final MultipartFile file) {

return new Callable<String>() {
public Object call() throws Exception {
return "someView";
}
};
}
----

Kotlin::
+
----
@RequestMapping(method = [RequestMethod.POST])
open fun processUpload(file: MultipartFile?): Callable<String> {
return Callable {
"someView"
}
}
----
======


.Associating SecurityContext to Callable's
====
More technically speaking, Spring Security integrates with `WebAsyncManager`.
The `SecurityContext` that is used to process the `Callable` is the `SecurityContext` that exists on the `SecurityContextHolder` when `startCallableProcessing` is invoked.
====

There is no automatic integration with a `DeferredResult` that is returned by controllers.
This is because `DeferredResult` is processed by the users and, thus, there is no way of automatically integrating with it.
However, you can still use xref:features/integrations/concurrency.adoc#concurrency[Concurrency Support] to provide transparent integration with Spring Security.

## Spring MVC and CSRF Integration

Spring Security integrates with Spring MVC to add CSRF protection.

### Automatic Token Inclusion

Spring Security automatically xref:servlet/exploits/csrf.adoc#csrf-integration-form[include the CSRF Token] within forms that use the {spring-framework-reference-url}web/webmvc-view/mvc-jsp.html#mvc-view-jsp-formtaglib-formtag[Spring MVC form tag].
Consider the following JSP:

----
<jsp:root xmlns:jsp="http://java.sun.com/JSP/Page"
xmlns:c="http://java.sun.com/jsp/jstl/core"
xmlns:form="http://www.springframework.org/tags/form" version="2.0">
<jsp:directive.page language="java" contentType="text/html" />
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<!-- ... -->

<c:url var="logoutUrl" value="/logout"/>
<form:form action="${logoutUrl}"
method="post">
<input type="submit"
value="Log out" />
<input type="hidden"
name="${_csrf.parameterName}"
value="${_csrf.token}"/>
</form:form>

<!-- ... -->
</html>
</jsp:root>
----

The preceding example output HTMLs that is similar to the following:

----
<!-- ... -->

<form action="/context/logout" method="post">
<input type="submit" value="Log out"/>
<input type="hidden" name="_csrf" value="f81d4fae-7dec-11d0-a765-00a0c91e6bf6"/>
</form>

<!-- ... -->
----

### Resolving the CsrfToken

Spring Security provides `CsrfTokenArgumentResolver`, which can automatically resolve the current `CsrfToken` for Spring MVC arguments.
By using xref:servlet/configuration/java.adoc#jc-hello-wsca[@EnableWebSecurity], you automatically have this added to your Spring MVC configuration.
If you use XML-based configuration, you must add this yourself.

Once `CsrfTokenArgumentResolver` is properly configured, you can expose the `CsrfToken` to your static HTML based application:

======
Java::
+
----
@RestController
public class CsrfController {

@RequestMapping("/csrf")
public CsrfToken csrf(CsrfToken token) {
return token;
}
}
----

Kotlin::
+
----
@RestController
class CsrfController {
@RequestMapping("/csrf")
fun csrf(token: CsrfToken): CsrfToken {
return token
}
}
----
======

It is important to keep the `CsrfToken` a secret from other domains.
This means that, if you use https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS[Cross Origin Sharing (CORS)], you should *NOT* expose the `CsrfToken` to any external domains.

## Configuring Spring MVC and Spring Security in the Same Application Context

If you are using Boot, Spring MVC and Spring Security are in the same application context by default.

Otherwise, for Java Config, including both `@EnableWebMvc` and `@EnableWebSecurity` will construct Spring Security and Spring MVC components in the same context.

Of, if you are using ``ServletListener``s you can do:

======
Java::
+
----
public class SecurityInitializer extends
AbstractAnnotationConfigDispatcherServletInitializer {

@Override
protected Class<?>[] getRootConfigClasses() {
return null;
}

@Override
protected Class<?>[] getServletConfigClasses() {
return new Class[] { RootConfiguration.class,
WebMvcConfiguration.class };
}

@Override
protected String[] getServletMappings() {
return new String[] { "/" };
}
}
----

Kotlin::
+
----
class SecurityInitializer : AbstractAnnotationConfigDispatcherServletInitializer() {
override fun getRootConfigClasses(): Array<Class<*>>? {
return null
}

override fun getServletConfigClasses(): Array<Class<*>> {
return arrayOf(
RootConfiguration::class.java,
WebMvcConfiguration::class.java
)
}

override fun getServletMappings(): Array<String> {
return arrayOf("/")
}
}
----
======

And finally for a `web.xml` file, you configure the `DispatcherServlet` like so:

----
<listener>
<listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>
</listener>

<!-- All Spring Configuration (both MVC and Security) are in /WEB-INF/spring/ -->
<context-param>
<param-name>contextConfigLocation</param-name>
<param-value>/WEB-INF/spring/*.xml</param-value>
</context-param>

<servlet>
<servlet-name>spring</servlet-name>
<servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
<!-- Load from the ContextLoaderListener -->
<init-param>
<param-name>contextConfigLocation</param-name>
<param-value></param-value>
</init-param>
</servlet>

<servlet-mapping>
<servlet-name>spring</servlet-name>
<url-pattern>/</url-pattern>
</servlet-mapping>
----

The following `WebSecurityConfiguration` in placed in the  `ApplicationContext` of the `DispatcherServlet`.
