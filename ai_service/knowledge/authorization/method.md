---
source: method
---

# method

# EnableReactiveMethodSecurity

Spring Security supports method security by using https://projectreactor.io/docs/core/release/reference/#context[Reactor's Context], which is set up by `ReactiveSecurityContextHolder`.
The following example shows how to retrieve the currently logged in user's message:

====
For this example to work, the return type of the method must be a `org.reactivestreams.Publisher` (that is, a `Mono` or a `Flux`).
This is necessary to integrate with Reactor's `Context`.
====

## EnableReactiveMethodSecurity with AuthorizationManager

In Spring Security 5.8, we can enable annotation-based security using the `@EnableReactiveMethodSecurity(useAuthorizationManager=true)` annotation on any `@Configuration` instance.

This improves upon `@EnableReactiveMethodSecurity` in a number of ways. `@EnableReactiveMethodSecurity(useAuthorizationManager=true)`:

1. Uses the simplified `AuthorizationManager` API instead of metadata sources, config attributes, decision managers, and voters.
This simplifies reuse and customization.
2. Supports reactive return types including Kotlin coroutines.
3. Is built using native Spring AOP, removing abstractions and allowing you to use Spring AOP building blocks to customize
4. Checks for conflicting annotations to ensure an unambiguous security configuration
5. Complies with JSR-250

====
For earlier versions, please read about similar support with <<jc-enable-reactive-method-security, @EnableReactiveMethodSecurity>>.
====

For example, the following would enable Spring Security's `@PreAuthorize` annotation:

.Method Security Configuration
======
Java::
+
----
@EnableReactiveMethodSecurity(useAuthorizationManager=true)
public class MethodSecurityConfig {
}
----
======

Adding an annotation to a method (on a class or interface) would then limit the access to that method accordingly.
Spring Security's native annotation support defines a set of attributes for the method.
These will be passed to the various method interceptors, like `AuthorizationManagerBeforeReactiveMethodInterceptor`, for it to make the actual decision:

.Method Security Annotation Usage
======
Java::
+
----
public interface BankService {
@PreAuthorize("hasRole('USER')")
Mono<Account> readAccount(Long id);

@PreAuthorize("hasRole('USER')")
Flux<Account> findAccounts();

@PreAuthorize("@func.apply(#account)")
Mono<Account> post(Account account, Double amount);
}
----
======

In this case `hasRole` refers to the method found in `SecurityExpressionRoot` that gets invoked by the SpEL evaluation engine.

`@bean` refers to a custom component you have defined, where `apply` can return `Boolean` or `Mono<Boolean>` to indicate the authorization decision.
A bean like that might look something like this:

.Method Security Reactive Boolean Expression
======
Java::
+
----
@Bean
public Function<Account, Mono<Boolean>> func() {
return (account) -> Mono.defer(() -> Mono.just(account.getId().equals(12)));
}
----
======

Method authorization is a combination of before- and after-method authorization.

====
Before-method authorization is performed before the method is invoked.
If that authorization denies access, the method is not invoked, and an `AccessDeniedException` is thrown.
After-method authorization is performed after the method is invoked, but before the method returns to the caller.
If that authorization denies access, the value is not returned, and an `AccessDeniedException` is thrown
====

To recreate what adding `@EnableReactiveMethodSecurity(useAuthorizationManager=true)` does by default, you would publish the following configuration:

.Full Pre-post Method Security Configuration
======
Java::
+
----
@Configuration
class MethodSecurityConfig {
@Bean
BeanDefinitionRegistryPostProcessor aopConfig() {
return AopConfigUtils::registerAutoProxyCreatorIfNecessary;
}

@Bean
@Role(BeanDefinition.ROLE_INFRASTRUCTURE)
PreFilterAuthorizationReactiveMethodInterceptor preFilterInterceptor() {
return new PreFilterAuthorizationReactiveMethodInterceptor();
}

@Bean
@Role(BeanDefinition.ROLE_INFRASTRUCTURE)
AuthorizationManagerBeforeReactiveMethodInterceptor preAuthorizeInterceptor() {
return AuthorizationManagerBeforeReactiveMethodInterceptor.preAuthorize();
}

@Bean
@Role(BeanDefinition.ROLE_INFRASTRUCTURE)
AuthorizationManagerAfterReactiveMethodInterceptor postAuthorizeInterceptor() {
return AuthorizationManagerAfterReactiveMethodInterceptor.postAuthorize();
}

@Bean
@Role(BeanDefinition.ROLE_INFRASTRUCTURE)
PostFilterAuthorizationReactiveMethodInterceptor postFilterInterceptor() {
return new PostFilterAuthorizationReactiveMethodInterceptor();
}
}
----
======

Notice that Spring Security's method security is built using Spring AOP.

### Customizing Authorization

Spring Security's `@PreAuthorize`, `@PostAuthorize`, `@PreFilter`, and `@PostFilter` ship with rich expression-based support.


Also, for role-based authorization, Spring Security adds a default `ROLE_` prefix, which is uses when evaluating expressions like `hasRole`.
You can configure the authorization rules to use a different prefix by exposing a `GrantedAuthorityDefaults` bean, like so:

.Custom GrantedAuthorityDefaults
======
Java::
+
----
@Bean
@Role(BeanDefinition.ROLE_INFRASTRUCTURE)
static GrantedAuthorityDefaults grantedAuthorityDefaults() {
return new GrantedAuthorityDefaults("MYPREFIX_");
}
----
======

====
We expose `GrantedAuthorityDefaults` using a `static` method to ensure that Spring publishes it before it initializes Spring Security's method security `@Configuration` classes.
Since the `GrantedAuthorityDefaults` bean is part of internal workings of Spring Security, we should also expose it as an infrastructural bean effectively avoiding some warnings related to bean post-processing (see https://github.com/spring-projects/spring-security/issues/14751[gh-14751]).
====

## Authorizing Methods Programmatically

As you've already seen, there are several ways that you can specify non-trivial authorization rules using xref:servlet/authorization/method-security.adoc#authorization-expressions[Method Security SpEL expressions].

There are a number of ways that you can instead allow your logic to be Java-based instead of SpEL-based.
This gives use access the entire Java language for increased testability and flow control.

### Using a Custom Bean in SpEL

The first way to authorize a method programmatically is a two-step process.

First, declare a bean that has a method that takes a `MethodSecurityExpressionOperations` instance like the following:

======
Java::
+
----
@Component("authz")
public class AuthorizationLogic {
public decide(MethodSecurityExpressionOperations operations): Mono<Boolean> {
}
}
----

Kotlin::
+
----
@Component("authz")
open class AuthorizationLogic {
fun decide(val operations: MethodSecurityExpressionOperations): Mono<Boolean> {
}
}
----
======

Then, reference that bean in your annotations in the following way:

======
Java::
+
----
@Controller
public class MyController {
@PreAuthorize("@authz.decide(#root)")
@GetMapping("/endpoint")
public Mono<String> endpoint() {
}
}
----

Kotlin::
+
----
@Controller
open class MyController {
@PreAuthorize("@authz.decide(#root)")
@GetMapping("/endpoint")
fun endpoint(): Mono<String> {
}
}
----
======

Spring Security will invoke the given method on that bean for each method invocation.

What's nice about this is all your authorization logic is in a separate class that can be independently unit tested and verified for correctness.
It also has access to the full Java language.

In addition to returning a `Mono<Boolean>`, you can also return `Mono.empty()` to indicate that the code abstains from making a decision.

If you want to include more information about the nature of the decision, you can instead return a custom `AuthorizationDecision` like this:

======
Java::
+
----
@Component("authz")
public class AuthorizationLogic {
public Mono<AuthorizationDecision> decide(MethodSecurityExpressionOperations operations) {
return Mono.just(new MyAuthorizationDecision(false, details));
}
}
----

Kotlin::
+
----
@Component("authz")
open class AuthorizationLogic {
fun decide(val operations: MethodSecurityExpressionOperations): Mono<AuthorizationDecision> {
return Mono.just(MyAuthorizationDecision(false, details))
}
}
----
======

Or throw a custom `AuthorizationDeniedException` instance.
Note, though, that returning an object is preferred as this doesn't incur the expense of generating a stacktrace.

Then, you can access the custom details when you xref:servlet/authorization/method-security.adoc#fallback-values-authorization-denied[customize how the authorization result is handled].

### Using a Custom Authorization Manager

The second way to authorize a method programmatically is to create a custom xref:servlet/authorization/architecture.adoc#_the_authorizationmanager[`AuthorizationManager`].

First, declare an authorization manager instance, perhaps like this one:

======
Java::
+
----
@Component
public class MyPreAuthorizeAuthorizationManager implements ReactiveAuthorizationManager<MethodInvocation> {
@Override
public Mono<AuthorizationResult> authorize(Supplier<Authentication> authentication, MethodInvocation invocation) {
}

}
----

Kotlin::
+
----
@Component
class MyPreAuthorizeAuthorizationManager : ReactiveAuthorizationManager<MethodInvocation> {
override fun authorize(authentication: Supplier<Authentication>, invocation: MethodInvocation): Mono<AuthorizationResult> {
}

}
----
======

Then, publish the method interceptor with a pointcut that corresponds to when you want that `ReactiveAuthorizationManager` to run.
For example, you could replace how `@PreAuthorize` and `@PostAuthorize` work like so:

.Only @PreAuthorize and @PostAuthorize Configuration
======
Java::
+
----
@Configuration
@EnableMethodSecurity(prePostEnabled = false)
class MethodSecurityConfig {
@Bean
@Role(BeanDefinition.ROLE_INFRASTRUCTURE)
Advisor preAuthorize(MyPreAuthorizeAuthorizationManager manager) {
return AuthorizationManagerBeforeReactiveMethodInterceptor.preAuthorize(manager);
}

@Bean
@Role(BeanDefinition.ROLE_INFRASTRUCTURE)
Advisor postAuthorize(MyPostAuthorizeAuthorizationManager manager) {
return AuthorizationManagerAfterReactiveMethodInterceptor.postAuthorize(manager);
}
}
----

Kotlin::
+
----
@Configuration
@EnableMethodSecurity(prePostEnabled = false)
class MethodSecurityConfig {
@Bean
@Role(BeanDefinition.ROLE_INFRASTRUCTURE)
fun preAuthorize(val manager: MyPreAuthorizeAuthorizationManager) : Advisor {
return AuthorizationManagerBeforeReactiveMethodInterceptor.preAuthorize(manager)
}

@Bean
@Role(BeanDefinition.ROLE_INFRASTRUCTURE)
fun postAuthorize(val manager: MyPostAuthorizeAuthorizationManager) : Advisor {
return AuthorizationManagerAfterReactiveMethodInterceptor.postAuthorize(manager)
}
}
----
======

====
You can place your interceptor in between Spring Security method interceptors using the order constants specified in `AuthorizationInterceptorsOrder`.
====

### Customizing Expression Handling

Or, third, you can customize how each SpEL expression is handled.
To do that, you can expose a custom `MethodSecurityExpressionHandler`, like so:

.Custom MethodSecurityExpressionHandler
======
Java::
+
----
@Bean
static MethodSecurityExpressionHandler methodSecurityExpressionHandler(RoleHierarchy roleHierarchy) {
DefaultMethodSecurityExpressionHandler handler = new DefaultMethodSecurityExpressionHandler();
handler.setRoleHierarchy(roleHierarchy);
return handler;
}
----

Kotlin::
+
----
companion object {
@Bean
fun methodSecurityExpressionHandler(val roleHierarchy: RoleHierarchy) : MethodSecurityExpressionHandler {
val handler = DefaultMethodSecurityExpressionHandler()
handler.setRoleHierarchy(roleHierarchy)
return handler
}
}
----
======

====
We expose `MethodSecurityExpressionHandler` using a `static` method to ensure that Spring publishes it before it initializes Spring Security's method security `@Configuration` classes
====

You can also subclass xref:servlet/authorization/method-security.adoc#subclass-defaultmethodsecurityexpressionhandler[`DefaultMessageSecurityExpressionHandler`] to add your own custom authorization expressions beyond the defaults.

## EnableReactiveMethodSecurity

======
Java::
+
----
Authentication authentication = new TestingAuthenticationToken("user", "password", "ROLE_USER");

Mono<String> messageByUsername = ReactiveSecurityContextHolder.getContext()
.map(SecurityContext::getAuthentication)
.map(Authentication::getName)
.flatMap(this::findMessageByUsername)
.contextWrite(ReactiveSecurityContextHolder.withAuthentication(authentication));

StepVerifier.create(messageByUsername)
.expectNext("Hi user")
.verifyComplete();
----

Kotlin::
+
----
val authentication: Authentication = TestingAuthenticationToken("user", "password", "ROLE_USER")

val messageByUsername: Mono<String> = ReactiveSecurityContextHolder.getContext()
.map(SecurityContext::getAuthentication)
.map(Authentication::getName)
.flatMap(this::findMessageByUsername) // In a WebFlux application the `subscriberContext` is automatically setup using `ReactorContextWebFilter`
.contextWrite(ReactiveSecurityContextHolder.withAuthentication(authentication))

StepVerifier.create(messageByUsername)
.expectNext("Hi user")
.verifyComplete()
----
======

Where `this::findMessageByUsername` is defined as:

======
Java::
+
----
Mono<String> findMessageByUsername(String username) {
return Mono.just("Hi " + username);
}
----

Kotlin::
+
----
fun findMessageByUsername(username: String): Mono<String> {
return Mono.just("Hi $username")
}
----
======

The following minimal method security configures method security in reactive applications:

======
Java::
+
----
@Configuration
@EnableReactiveMethodSecurity
public class SecurityConfig {
@Bean
public MapReactiveUserDetailsService userDetailsService() {
User.UserBuilder userBuilder = User.withDefaultPasswordEncoder();
UserDetails rob = userBuilder.username("rob")
.password("rob")
.roles("USER")
.build();
UserDetails admin = userBuilder.username("admin")
.password("admin")
.roles("USER","ADMIN")
.build();
return new MapReactiveUserDetailsService(rob, admin);
}
}
----

Kotlin::
+
----
@Configuration
@EnableReactiveMethodSecurity
class SecurityConfig {
@Bean
fun userDetailsService(): MapReactiveUserDetailsService {
val userBuilder: User.UserBuilder = User.withDefaultPasswordEncoder()
val rob = userBuilder.username("rob")
.password("rob")
.roles("USER")
.build()
val admin = userBuilder.username("admin")
.password("admin")
.roles("USER", "ADMIN")
.build()
return MapReactiveUserDetailsService(rob, admin)
}
}
----
======

Consider the following class:

======
Java::
+
----
@Component
public class HelloWorldMessageService {
@PreAuthorize("hasRole('ADMIN')")
public Mono<String> findMessage() {
return Mono.just("Hello World!");
}
}
----

Kotlin::
+
----
@Component
class HelloWorldMessageService {
@PreAuthorize("hasRole('ADMIN')")
fun findMessage(): Mono<String> {
return Mono.just("Hello World!")
}
}
----
======

Alternatively, the following class uses Kotlin coroutines:

======
Kotlin::
+
----
@Component
class HelloWorldMessageService {
@PreAuthorize("hasRole('ADMIN')")
suspend fun findMessage(): String {
delay(10)
return "Hello World!"
}
}
----
======


Combined with our configuration above, `@PreAuthorize("hasRole('ADMIN')")` ensures that `findByMessage` is invoked only by a user with the `ADMIN` role.
Note that any of the expressions in standard method security work for `@EnableReactiveMethodSecurity`.
However, at this time, we support only a return type of `Boolean` or `boolean` of the expression.
This means that the expression must not block.

When integrating with xref:reactive/configuration/webflux.adoc#jc-webflux[WebFlux Security], the Reactor Context is automatically established by Spring Security according to the authenticated user:

======
Java::
+
----
@Configuration
@EnableWebFluxSecurity
@EnableReactiveMethodSecurity
public class SecurityConfig {

@Bean
SecurityWebFilterChain springWebFilterChain(ServerHttpSecurity http) throws Exception {
return http
.authorizeExchange((authorize) -> authorize
.anyExchange().permitAll()
)
.httpBasic(withDefaults())
.build();
}

@Bean
MapReactiveUserDetailsService userDetailsService() {
User.UserBuilder userBuilder = User.withDefaultPasswordEncoder();
UserDetails rob = userBuilder.username("rob")
.password("rob")
.roles("USER")
.build();
UserDetails admin = userBuilder.username("admin")
.password("admin")
.roles("USER","ADMIN")
.build();
return new MapReactiveUserDetailsService(rob, admin);
}
}
----

Kotlin::
+
----
@Configuration
@EnableWebFluxSecurity
@EnableReactiveMethodSecurity
class SecurityConfig {
@Bean
open fun springWebFilterChain(http: ServerHttpSecurity): SecurityWebFilterChain {
return http {
authorizeExchange {
authorize(anyExchange, permitAll)
}
httpBasic { }
}
}

@Bean
fun userDetailsService(): MapReactiveUserDetailsService {
val userBuilder: User.UserBuilder = User.withDefaultPasswordEncoder()
val rob = userBuilder.username("rob")
.password("rob")
.roles("USER")
.build()
val admin = userBuilder.username("admin")
.password("admin")
.roles("USER", "ADMIN")
.build()
return MapReactiveUserDetailsService(rob, admin)
}
}
----
======

You can find a complete sample in {gh-samples-url}/reactive/webflux/java/method[hellowebflux-method].
