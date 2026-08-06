---
source: opaque token
---

**opaque token**

**OAuth 2.0 Resource Server Opaque Token**

## Minimal Dependencies for Introspection
As described in xref:servlet/oauth2/resource-server/jwt.adoc#oauth2resourceserver-jwt-minimaldependencies[Minimal Dependencies for JWT] most of Resource Server support is collected in `spring-security-oauth2-resource-server`.
However unless a custom <<oauth2resourceserver-opaque-introspector,`OpaqueTokenIntrospector`>> is provided, the Resource Server will fallback to `SpringOpaqueTokenIntrospector`.
This means that only `spring-security-oauth2-resource-server` is necessary in order to have a working minimal Resource Server that supports opaque Bearer Tokens.

**Minimal Configuration for Introspection**

Typically, an opaque token can be verified via an https://tools.ietf.org/html/rfc7662[OAuth 2.0 Introspection Endpoint], hosted by the authorization server.
This can be handy when revocation is a requirement.

When using https://spring.io/projects/spring-boot[Spring Boot], configuring an application as a resource server that uses introspection consists of two basic steps.
First, include the needed dependencies and second, indicate the introspection endpoint details.

**Specifying the Authorization Server**

To specify where the introspection endpoint is, simply do:

----
spring:
security:
oauth2:
resourceserver:
opaquetoken:
introspection-uri: https://idp.example.com/introspect
client-id: client
client-secret: secret
----

Where `https://idp.example.com/introspect` is the introspection endpoint hosted by your authorization server and `client-id` and `client-secret` are the credentials needed to hit that endpoint.

Resource Server will use these properties to further self-configure and subsequently validate incoming JWTs.

When using introspection, the authorization server's word is the law.
If the authorization server responses that the token is valid, then it is.

And that's it!

**Startup Expectations**

When this property and these dependencies are used, Resource Server will automatically configure itself to validate Opaque Bearer Tokens.

This startup process is quite a bit simpler than for JWTs since no endpoints need to be discovered and no additional validation rules get added.

**Runtime Expectations**

Once the application is started up, Resource Server will attempt to process any request containing an `Authorization: Bearer` header:

----
GET / HTTP/1.1
Authorization: Bearer some-token-value # Resource Server will process this
----

So long as this scheme is indicated, Resource Server will attempt to process the request according to the Bearer Token specification.

Given an Opaque Token, Resource Server will

1. Query the provided introspection endpoint using the provided credentials and the token
2. Inspect the response for an `{ 'active' : true }` attribute
3. Map each scope to an authority with the prefix `SCOPE_`

The resulting `Authentication#getPrincipal`, by default, is a Spring Security javadoc:org.springframework.security.oauth2.core.OAuth2AuthenticatedPrincipal[] object, and `Authentication#getName` maps to the token's `sub` property, if one is present.

From here, you may want to jump to:

- <<oauth2resourceserver-opaque-architecture>>
- <<oauth2resourceserver-opaque-attributes,Looking Up Attributes Post-Authentication>>
- <<oauth2resourceserver-opaque-authorization-extraction,Extracting Authorities Manually>>
- <<oauth2resourceserver-opaque-jwt-introspector,Using Introspection with JWTs>>

**How Opaque Token Authentication Works**

Next, let's see the architectural components that Spring Security uses to support https://tools.ietf.org/html/rfc7662[opaque token] Authentication in servlet-based applications, like the one we just saw.

javadoc:org.springframework.security.oauth2.server.resource.authentication.OpaqueTokenAuthenticationProvider[] is an xref:servlet/authentication/architecture.adoc#servlet-authentication-authenticationprovider[`AuthenticationProvider`] implementation that leverages a <<oauth2resourceserver-opaque-introspector,`OpaqueTokenIntrospector`>> to authenticate an opaque token.

Let's take a look at how `OpaqueTokenAuthenticationProvider` works within Spring Security.
The figure explains details of how the xref:servlet/authentication/architecture.adoc#servlet-authentication-authenticationmanager[`AuthenticationManager`] in figures from xref:servlet/oauth2/resource-server/index.adoc#oauth2resourceserver-authentication-bearertokenauthenticationfilter[Reading the Bearer Token] works.

.`OpaqueTokenAuthenticationProvider` Usage
image::{figures}/opaquetokenauthenticationprovider.png[]

image:{icondir}/number_1.png[] The authentication `Filter` from xref:servlet/oauth2/resource-server/index.adoc#oauth2resourceserver-authentication-bearertokenauthenticationfilter[Reading the Bearer Token] passes a `BearerTokenAuthenticationToken` to the `AuthenticationManager` which is implemented by xref:servlet/authentication/architecture.adoc#servlet-authentication-providermanager[`ProviderManager`].

image:{icondir}/number_2.png[] The `ProviderManager` is configured to use an xref:servlet/authentication/architecture.adoc#servlet-authentication-authenticationprovider[AuthenticationProvider] of type `OpaqueTokenAuthenticationProvider`.

image:{icondir}/number_3.png[] `OpaqueTokenAuthenticationProvider` introspects the opaque token and adds granted authorities using an <<oauth2resourceserver-opaque-introspector,`OpaqueTokenIntrospector`>>.
When authentication is successful, the xref:servlet/authentication/architecture.adoc#servlet-authentication-authentication[`Authentication`] that is returned is of type `BearerTokenAuthentication` and has a principal that is the `OAuth2AuthenticatedPrincipal` returned by the configured <<oauth2resourceserver-opaque-introspector,`OpaqueTokenIntrospector`>> and a set of authorities that contains at least `FACTOR_BEARER`.
Ultimately, the returned `BearerTokenAuthentication` will be set on the xref:servlet/authentication/architecture.adoc#servlet-authentication-securitycontextholder[`SecurityContextHolder`] by the authentication `Filter`.

**Looking Up Attributes Post-Authentication**

Once a token is authenticated, an instance of `BearerTokenAuthentication` is set in the `SecurityContext`.

This means that it's available in `@Controller` methods when using `@EnableWebMvc` in your configuration:

======
Java::
+
----
@GetMapping("/foo")
public String foo(BearerTokenAuthentication authentication) {
return authentication.getTokenAttributes().get("sub") + " is the subject";
}
----

Kotlin::
+
----
@GetMapping("/foo")
fun foo(authentication: BearerTokenAuthentication): String {
return authentication.tokenAttributes["sub"].toString() + " is the subject"
}
----
======

Since `BearerTokenAuthentication` holds an `OAuth2AuthenticatedPrincipal`, that also means that it's available to controller methods, too:

======
Java::
+
----
@GetMapping("/foo")
public String foo(@AuthenticationPrincipal OAuth2AuthenticatedPrincipal principal) {
return principal.getAttribute("sub") + " is the subject";
}
----

Kotlin::
+
----
@GetMapping("/foo")
fun foo(@AuthenticationPrincipal principal: OAuth2AuthenticatedPrincipal): String {
return principal.getAttribute<Any>("sub").toString() + " is the subject"
}
----
======

**Looking Up Attributes Via SpEL**

Of course, this also means that attributes can be accessed via SpEL.

For example, if using `@EnableGlobalMethodSecurity` so that you can use `@PreAuthorize` annotations, you can do:

======
Java::
+
----
@PreAuthorize("principal?.attributes['sub'] == 'foo'")
public String forFoosEyesOnly() {
return "foo";
}
----

Kotlin::
+
----
@PreAuthorize("principal?.attributes['sub'] == 'foo'")
fun forFoosEyesOnly(): String {
return "foo"
}
----
======

**Overriding or Replacing Boot Auto Configuration**

There are two ``@Bean``s that Spring Boot generates on Resource Server's behalf.

The first is a `SecurityFilterChain` that configures the app as a resource server.
When use Opaque Token, this `SecurityFilterChain` looks like:

.Default Opaque Token Configuration
======
Java::
+
----
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
http
.authorizeHttpRequests((authorize) -> authorize
.anyRequest().authenticated()
)
.oauth2ResourceServer((oauth2) -> oauth2
.opaqueToken(Customizer.withDefaults())
);
return http.build();
}
----

Kotlin::
+
----
@Bean
open fun filterChain(http: HttpSecurity): SecurityFilterChain {
http {
authorizeHttpRequests {
authorize(anyRequest, authenticated)
}
oauth2ResourceServer {
opaqueToken { }
}
}
return http.build()
}
----
======

If the application doesn't expose a `SecurityFilterChain` bean, then Spring Boot will expose the above default one.

Replacing this is as simple as exposing the bean within the application:

.Custom Opaque Token Configuration
======
Java::
+
----
import static org.springframework.security.oauth2.core.authorization.OAuth2AuthorizationManagers.hasScope;

@Configuration
@EnableWebSecurity
public class MyCustomSecurityConfiguration {
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
http
.authorizeHttpRequests((authorize) -> authorize
.requestMatchers("/messages/**").access(hasScope("message:read"))
.anyRequest().authenticated()
)
.oauth2ResourceServer((oauth2) -> oauth2
.opaqueToken((opaqueToken) -> opaqueToken
.introspector(myIntrospector())
)
);
return http.build();
}
}
----

Kotlin::
+
----
import org.springframework.security.oauth2.core.authorization.OAuth2AuthorizationManagers.hasScope;

@Configuration
@EnableWebSecurity
class MyCustomSecurityConfiguration {
@Bean
open fun filterChain(http: HttpSecurity): SecurityFilterChain {
http {
authorizeHttpRequests {
authorize("/messages/**", hasScope("SCOPE_message:read"))
authorize(anyRequest, authenticated)
}
oauth2ResourceServer {
opaqueToken {
introspector = myIntrospector()
}
}
}
return http.build()
}
}
----
======

The above requires the scope of `message:read` for any URL that starts with `/messages/`.

Methods on the `oauth2ResourceServer` DSL will also override or replace auto configuration.

For example, the second `@Bean` Spring Boot creates is an `OpaqueTokenIntrospector`, <<oauth2resourceserver-opaque-architecture-introspector,which decodes `String` tokens into validated instances of `OAuth2AuthenticatedPrincipal`>>:

======
Java::
+
----
@Bean
public OpaqueTokenIntrospector introspector() {
return SpringOpaqueTokenIntrospector.withIntrospectionUri(introspectionUri)
.clientId(clientId).clientSecret(clientSecret).build();
}
----

Kotlin::
+
----
@Bean
fun introspector(): OpaqueTokenIntrospector {
return SpringOpaqueTokenIntrospector.withIntrospectionUri(introspectionUri)
.clientId(clientId).clientSecret(clientSecret).build()
}
----
======

If the application doesn't expose an <<oauth2resourceserver-opaque-architecture-introspector,`OpaqueTokenIntrospector`>> bean, then Spring Boot will expose the above default one.

And its configuration can be overridden using `introspectionUri()` and `introspectionClientCredentials()` or replaced using `introspector()`.

If the application doesn't expose an `OpaqueTokenAuthenticationConverter` bean, then spring-security will build `BearerTokenAuthentication`.

Or, if you're not using Spring Boot at all, then all of these components - the filter chain, an <<oauth2resourceserver-opaque-architecture-introspector,`OpaqueTokenIntrospector`>> and an `OpaqueTokenAuthenticationConverter` can be specified in XML.

The filter chain is specified like so:

.Default Opaque Token Configuration
======
Xml::
+
----
<http>
<intercept-uri pattern="/**" access="authenticated"/>
<oauth2-resource-server>
<opaque-token introspector-ref="opaqueTokenIntrospector"
authentication-converter-ref="opaqueTokenAuthenticationConverter"/>
</oauth2-resource-server>
</http>
----
======

And the <<oauth2resourceserver-opaque-architecture-introspector,`OpaqueTokenIntrospector`>> like so:

.Opaque Token Introspector
======
Xml::
+
----
<bean id="opaqueTokenIntrospector"
class="org.springframework.security.oauth2.server.resource.introspection.SpringOpaqueTokenIntrospector">
<constructor-arg value="${spring.security.oauth2.resourceserver.opaquetoken.introspection_uri}"/>
<constructor-arg value="${spring.security.oauth2.resourceserver.opaquetoken.client_id}"/>
<constructor-arg value="${spring.security.oauth2.resourceserver.opaquetoken.client_secret}"/>
</bean>
----
======

And the `OpaqueTokenAuthenticationConverter` like so:

.Opaque Token Authentication Converter
======
Xml::
+
----
<bean id="opaqueTokenAuthenticationConverter"
class="com.example.CustomOpaqueTokenAuthenticationConverter"/>
----
======

**Using `introspectionUri()`**

An authorization server's Introspection Uri can be configured <<oauth2resourceserver-opaque-introspectionuri,as a configuration property>> or it can be supplied in the DSL:

.Introspection URI Configuration
======
Java::
+
----
@Configuration
@EnableWebSecurity
public class DirectlyConfiguredIntrospectionUri {
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
http
.authorizeHttpRequests((authorize) -> authorize
.anyRequest().authenticated()
)
.oauth2ResourceServer((oauth2) -> oauth2
.opaqueToken((opaqueToken) -> opaqueToken
.introspectionUri("https://idp.example.com/introspect")
.introspectionClientCredentials("client", "secret")
)
);
return http.build();
}
}
----

Kotlin::
+
----
@Configuration
@EnableWebSecurity
class DirectlyConfiguredIntrospectionUri {
@Bean
open fun filterChain(http: HttpSecurity): SecurityFilterChain {
http {
authorizeHttpRequests {
authorize(anyRequest, authenticated)
}
oauth2ResourceServer {
opaqueToken {
introspectionUri = "https://idp.example.com/introspect"
introspectionClientCredentials("client", "secret")
}
}
}
return http.build()
}
}
----

Xml::
+
----
<bean id="opaqueTokenIntrospector"
class="org.springframework.security.oauth2.server.resource.introspection.SpringOpaqueTokenIntrospector">
<constructor-arg value="https://idp.example.com/introspect"/>
<constructor-arg value="client"/>
<constructor-arg value="secret"/>
</bean>
----
======

Using `introspectionUri()` takes precedence over any configuration property.

**Using `introspector()`**

More powerful than `introspectionUri()` is `introspector()`, which will completely replace any Boot auto configuration of <<oauth2resourceserver-opaque-architecture-introspector,`OpaqueTokenIntrospector`>>:

.Introspector Configuration
======
Java::
+
----
@Configuration
@EnableWebSecurity
public class DirectlyConfiguredIntrospector {
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
http
.authorizeHttpRequests((authorize) -> authorize
.anyRequest().authenticated()
)
.oauth2ResourceServer((oauth2) -> oauth2
.opaqueToken((opaqueToken) -> opaqueToken
.introspector(myCustomIntrospector())
)
);
return http.build();
}
}
----

Kotlin::
+
----
@Configuration
@EnableWebSecurity
class DirectlyConfiguredIntrospector {
@Bean
open fun filterChain(http: HttpSecurity): SecurityFilterChain {
http {
authorizeHttpRequests {
authorize(anyRequest, authenticated)
}
oauth2ResourceServer {
opaqueToken {
introspector = myCustomIntrospector()
}
}
}
return http.build()
}
}
----

Xml::
+
----
<http>
<intercept-uri pattern="/**" access="authenticated"/>
<oauth2-resource-server>
<opaque-token introspector-ref="myCustomIntrospector"/>
</oauth2-resource-server>
</http>
----
======

This is handy when deeper configuration, like <<oauth2resourceserver-opaque-authorization-extraction,authority mapping>>, <<oauth2resourceserver-opaque-jwt-introspector,JWT revocation>>, or <<oauth2resourceserver-opaque-timeouts,request timeouts>>, is necessary.

**Exposing a `OpaqueTokenIntrospector` `@Bean`**

Or, exposing a <<oauth2resourceserver-opaque-architecture-introspector,`OpaqueTokenIntrospector`>> `@Bean` has the same effect as `introspector()`:

----
@Bean
public OpaqueTokenIntrospector introspector() {
return SpringOpaqueTokenIntrospector.withIntrospectionUri(introspectionUri)
.clientId(clientId).clientSecret(clientSecret).build();
}
----

**Configuring Authorization**

An OAuth 2.0 Introspection endpoint will typically return a `scope` attribute, indicating the scopes (or authorities) it's been granted, for example:

`{ ..., "scope" : "messages contacts"}`

When this is the case, Resource Server will attempt to coerce these scopes into a list of granted authorities, prefixing each scope with the string "SCOPE_".

This means that to protect an endpoint or method with a scope derived from an Opaque Token, the corresponding expressions should include this prefix:

.Authorization Opaque Token Configuration
======
Java::
+
----
import static org.springframework.security.oauth2.core.authorization.OAuth2AuthorizationManagers.hasScope;

@Configuration
@EnableWebSecurity
public class MappedAuthorities {
@Bean
public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
http
.authorizeHttpRequests((authorizeRequests) -> authorizeRequests
.requestMatchers("/contacts/**").access(hasScope("contacts"))
.requestMatchers("/messages/**").access(hasScope("messages"))
.anyRequest().authenticated()
)
.oauth2ResourceServer((oauth2) -> oauth2
.opaqueToken(Customizer.withDefaults())
);
return http.build();
}
}
----

Kotlin::
+
----
import org.springframework.security.oauth2.core.authorization.OAuth2AuthorizationManagers.hasScope

@Configuration
@EnableWebSecurity
class MappedAuthorities {
@Bean
open fun filterChain(http: HttpSecurity): SecurityFilterChain {
http {
authorizeHttpRequests {
authorize("/contacts/**", hasScope("contacts"))
authorize("/messages/**", hasScope("messages"))
authorize(anyRequest, authenticated)
}
oauth2ResourceServer {
opaqueToken { }
}
}
return http.build()
}
}
----

Xml::
+
----
<http>
<intercept-uri pattern="/contacts/**" access="hasAuthority('SCOPE_contacts')"/>
<intercept-uri pattern="/messages/**" access="hasAuthority('SCOPE_messages')"/>
<oauth2-resource-server>
<opaque-token introspector-ref="opaqueTokenIntrospector"/>
</oauth2-resource-server>
</http>
----
======

Or similarly with method security:

======
Java::
+
----
@PreAuthorize("hasAuthority('SCOPE_messages')")
public List<Message> getMessages(...) {}
----

Kotlin::
+
----
@PreAuthorize("hasAuthority('SCOPE_messages')")
fun getMessages(): List<Message?> {}
----
======

**Using `hasScope` in Method Security**

Because method security expressions can evaluation `AuthorizationManager` instances, you can also use the `hasScope` API by publishing a `DefaultOAuth2AuthorizationManagerFactory` `@Bean`:

include-code::./MethodSecurityHasScopeConfiguration[tag=declare-factory,indent=0]

and then doing:

include-code::./MessageService[tag=protected-method,indent=0]

If you are using xref:servlet/authentication/mfa.adoc[Spring Security's MFA feature], then you can supply its `AuthorizationManagerFactory` instance to ensure that your authentication factors are automatically checked as well by including it in your `DefaultOAuth2AuthorizationManagerFactory` constructor as follows:

include-code::./MethodSecurityHasScopeMfaConfiguration[tag=declare-factory,indent=0]

**Extracting Authorities Manually**

By default, Opaque Token support will extract the scope claim from an introspection response and parse it into individual `GrantedAuthority` instances.

For example, if the introspection response were:

----
{
"active" : true,
"scope" : "message:read message:write"
}
----

Then Resource Server would generate an `Authentication` with two authorities, one for `message:read` and the other for `message:write`.

This can, of course, be customized using a custom <<oauth2resourceserver-opaque-architecture-introspector,`OpaqueTokenIntrospector`>> that takes a look at the attribute set and converts in its own way:

======
Java::
+
----
public class CustomAuthoritiesOpaqueTokenIntrospector implements OpaqueTokenIntrospector {
private OpaqueTokenIntrospector delegate = SpringOpaqueTokenIntrospector
.withIntrospectionUri("https://idp.example.org/introspect")
.clientId("client").clientSecret("secret").build();

public OAuth2AuthenticatedPrincipal introspect(String token) {
OAuth2AuthenticatedPrincipal principal = this.delegate.introspect(token);
return new DefaultOAuth2AuthenticatedPrincipal(
principal.getName(), principal.getAttributes(), extractAuthorities(principal));
}

private Collection<GrantedAuthority> extractAuthorities(OAuth2AuthenticatedPrincipal principal) {
List<String> scopes = principal.getAttribute(OAuth2IntrospectionClaimNames.SCOPE);
return scopes.stream()
.map(SimpleGrantedAuthority::new)
.collect(Collectors.toList());
}
}
----

Kotlin::
+
----
class CustomAuthoritiesOpaqueTokenIntrospector : OpaqueTokenIntrospector {
private val delegate: OpaqueTokenIntrospector = SpringOpaqueTokenIntrospector
.withIntrospectionUri("https://idp.example.org/introspect")
.clientId("client").clientSecret("secret").build()
override fun introspect(token: String): OAuth2AuthenticatedPrincipal {
val principal: OAuth2AuthenticatedPrincipal = delegate.introspect(token)
return DefaultOAuth2AuthenticatedPrincipal(
principal.name, principal.attributes, extractAuthorities(principal))
}

private fun extractAuthorities(principal: OAuth2AuthenticatedPrincipal): Collection<GrantedAuthority> {
val scopes: List<String> = principal.getAttribute(OAuth2IntrospectionClaimNames.SCOPE)
return scopes
.map { SimpleGrantedAuthority(it) }
}
}
----
======

Thereafter, this custom introspector can be configured simply by exposing it as a `@Bean`:

======
Java::
+
----
@Bean
public OpaqueTokenIntrospector introspector() {
return new CustomAuthoritiesOpaqueTokenIntrospector();
}
----

Kotlin::
+
----
@Bean
fun introspector(): OpaqueTokenIntrospector {
return CustomAuthoritiesOpaqueTokenIntrospector()
}
----
======

**Configuring Timeouts**

By default, Resource Server uses connection and socket timeouts of 30 seconds each for coordinating with the authorization server.

This may be too short in some scenarios.
Further, it doesn't take into account more sophisticated patterns like back-off and discovery.

**Using `RestClientOpaqueTokenIntrospector`**

You can use `RestClientOpaqueTokenIntrospector`, which uses `RestClient` to communicate with the introspection endpoint.

====
When using Spring Boot, you can inject `OAuth2ResourceServerProperties` to obtain the introspection URI and client credentials.
====

.Minimal configuration using the builder
include-code::./RestClientOpaqueTokenIntrospectorConfiguration[tag=restclient-simple,indent=0]

To customize timeouts, build a `RestClient` with a custom `RequestFactory` and pass it to the introspector:

.Custom timeouts
include-code::./RestClientOpaqueTokenIntrospectorConfiguration[tag=restclient-timeouts,indent=0]

====
If you prefer to use `RestTemplate`, you can use `SpringOpaqueTokenIntrospector` instead, which accepts an instance of `RestOperations`.
====

**Using Introspection with JWTs**

A common question is whether or not introspection is compatible with JWTs.
Spring Security's Opaque Token support has been designed to not care about the format of the token -- it will gladly pass any token to the introspection endpoint provided.

So, let's say that you've got a requirement that requires you to check with the authorization server on each request, in case the JWT has been revoked.

Even though you are using the JWT format for the token, your validation method is introspection, meaning you'd want to do:

----
spring:
security:
oauth2:
resourceserver:
opaquetoken:
introspection-uri: https://idp.example.org/introspection
client-id: client
client-secret: secret
----

In this case, the resulting `Authentication` would be `BearerTokenAuthentication`.
Any attributes in the corresponding `OAuth2AuthenticatedPrincipal` would be whatever was returned by the introspection endpoint.

But, let's say that, oddly enough, the introspection endpoint only returns whether or not the token is active.
Now what?

In this case, you can create a custom <<oauth2resourceserver-opaque-architecture-introspector,`OpaqueTokenIntrospector`>> that still hits the endpoint, but then updates the returned principal to have the JWTs claims as the attributes:

======
Java::
+
----
public class JwtOpaqueTokenIntrospector implements OpaqueTokenIntrospector {
private OpaqueTokenIntrospector delegate = SpringOpaqueTokenIntrospector
.withIntrospectionUri("https://idp.example.org/introspect")
.clientId("client").clientSecret("secret").build();
private JwtDecoder jwtDecoder = new NimbusJwtDecoder(new ParseOnlyJWTProcessor());

public OAuth2AuthenticatedPrincipal introspect(String token) {
OAuth2AuthenticatedPrincipal principal = this.delegate.introspect(token);
try {
Jwt jwt = this.jwtDecoder.decode(token);
return new DefaultOAuth2AuthenticatedPrincipal(jwt.getClaims(), NO_AUTHORITIES);
} catch (JwtException ex) {
throw new OAuth2IntrospectionException(ex);
}
}

private static class ParseOnlyJWTProcessor extends DefaultJWTProcessor<SecurityContext> {
JWTClaimsSet process(SignedJWT jwt, SecurityContext context)
throws JOSEException {
return jwt.getJWTClaimsSet();
}
}
}
----

Kotlin::
+
----
class JwtOpaqueTokenIntrospector : OpaqueTokenIntrospector {
private val delegate: OpaqueTokenIntrospector = SpringOpaqueTokenIntrospector
.withIntrospectionUri("https://idp.example.org/introspect")
.clientId("client").clientSecret("secret").build()
private val jwtDecoder: JwtDecoder = NimbusJwtDecoder(ParseOnlyJWTProcessor())
override fun introspect(token: String): OAuth2AuthenticatedPrincipal {
val principal = delegate.introspect(token)
return try {
val jwt: Jwt = jwtDecoder.decode(token)
DefaultOAuth2AuthenticatedPrincipal(jwt.claims, NO_AUTHORITIES)
} catch (ex: JwtException) {
throw OAuth2IntrospectionException(ex.message)
}
}

private class ParseOnlyJWTProcessor : DefaultJWTProcessor<SecurityContext>() {
override fun process(jwt: SignedJWT, context: SecurityContext): JWTClaimsSet {
return jwt.jwtClaimsSet
}
}
}
----
======

Thereafter, this custom introspector can be configured simply by exposing it as a `@Bean`:

======
Java::
+
----
@Bean
public OpaqueTokenIntrospector introspector() {
return new JwtOpaqueTokenIntrospector();
}
----

Kotlin::
+
----
@Bean
fun introspector(): OpaqueTokenIntrospector {
return JwtOpaqueTokenIntrospector()
}
----
======

**Calling a `/userinfo` Endpoint**

Generally speaking, a Resource Server doesn't care about the underlying user, but instead about the authorities that have been granted.

That said, at times it can be valuable to tie the authorization statement back to a user.

If an application is also using `spring-security-oauth2-client`, having set up the appropriate `ClientRegistrationRepository`, then this is quite simple with a custom <<oauth2resourceserver-opaque-architecture-introspector,`OpaqueTokenIntrospector`>>.
This implementation below does three things:

- Delegates to the introspection endpoint, to affirm the token's validity
- Looks up the appropriate client registration associated with the `/userinfo` endpoint
- Invokes and returns the response from the `/userinfo` endpoint

======
Java::
+
----
public class UserInfoOpaqueTokenIntrospector implements OpaqueTokenIntrospector {
private final OpaqueTokenIntrospector delegate = SpringOpaqueTokenIntrospector
.withIntrospectionUri("https://idp.example.org/introspect")
.clientId("client").clientSecret("secret").build();
private final OAuth2UserService oauth2UserService = new DefaultOAuth2UserService();

private final ClientRegistrationRepository repository;


@Override
public OAuth2AuthenticatedPrincipal introspect(String token) {
OAuth2AuthenticatedPrincipal authorized = this.delegate.introspect(token);
Instant issuedAt = authorized.getAttribute(ISSUED_AT);
Instant expiresAt = authorized.getAttribute(EXPIRES_AT);
ClientRegistration clientRegistration = this.repository.findByRegistrationId("registration-id");
OAuth2AccessToken token = new OAuth2AccessToken(BEARER, token, issuedAt, expiresAt);
OAuth2UserRequest oauth2UserRequest = new OAuth2UserRequest(clientRegistration, token);
return this.oauth2UserService.loadUser(oauth2UserRequest);
}
}
----

Kotlin::
+
----
class UserInfoOpaqueTokenIntrospector : OpaqueTokenIntrospector {
private val delegate: OpaqueTokenIntrospector = SpringOpaqueTokenIntrospector
.withIntrospectionUri("https://idp.example.org/introspect")
.clientId("client").clientSecret("secret").build()
private val oauth2UserService = DefaultOAuth2UserService()
private val repository: ClientRegistrationRepository? = null


override fun introspect(token: String): OAuth2AuthenticatedPrincipal {
val authorized = delegate.introspect(token)
val issuedAt: Instant? = authorized.getAttribute(ISSUED_AT)
val expiresAt: Instant? = authorized.getAttribute(EXPIRES_AT)
val clientRegistration: ClientRegistration = repository!!.findByRegistrationId("registration-id")
val accessToken = OAuth2AccessToken(BEARER, token, issuedAt, expiresAt)
val oauth2UserRequest = OAuth2UserRequest(clientRegistration, accessToken)
return oauth2UserService.loadUser(oauth2UserRequest)
}
}
----
======

If you aren't using `spring-security-oauth2-client`, it's still quite simple.
You will simply need to invoke the `/userinfo` with your own instance of `WebClient`:

======
Java::
+
----
public class UserInfoOpaqueTokenIntrospector implements OpaqueTokenIntrospector {
private final OpaqueTokenIntrospector delegate = SpringOpaqueTokenIntrospector
.withIntrospectionUri("https://idp.example.org/introspect")
.clientId("client").clientSecret("secret").build();
private final WebClient rest = WebClient.create();

@Override
public OAuth2AuthenticatedPrincipal introspect(String token) {
OAuth2AuthenticatedPrincipal authorized = this.delegate.introspect(token);
return makeUserInfoRequest(authorized);
}
}
----

Kotlin::
+
----
class UserInfoOpaqueTokenIntrospector : OpaqueTokenIntrospector {
private val delegate: OpaqueTokenIntrospector = SpringOpaqueTokenIntrospector
.withIntrospectionUri("https://idp.example.org/introspect")
.clientId("client").clientSecret("secret").build()
private val rest: WebClient = WebClient.create()

override fun introspect(token: String): OAuth2AuthenticatedPrincipal {
val authorized = delegate.introspect(token)
return makeUserInfoRequest(authorized)
}
}
----
======

Either way, having created your <<oauth2resourceserver-opaque-architecture-introspector,`OpaqueTokenIntrospector`>>, you should publish it as a `@Bean` to override the defaults:

======
Java::
+
----
@Bean
OpaqueTokenIntrospector introspector() {
return new UserInfoOpaqueTokenIntrospector(...);
}
----

Kotlin::
+
----
@Bean
fun introspector(): OpaqueTokenIntrospector {
return UserInfoOpaqueTokenIntrospector(...)
}
----
======
