---
source: getting started
---

**getting started**

**Getting Started**

If you are just getting started with Spring Security Authorization Server, the following sections walk you through creating your first application.

## System Requirements

Spring Security Authorization Server requires a Java 17 or higher Runtime Environment.

**Installing Spring Security Authorization Server**

The easiest way to begin using Spring Security Authorization Server is by creating a https://spring.io/projects/spring-boot[Spring Boot]-based application.
You can use https://start.spring.io[start.spring.io] to generate a basic project or use the https://github.com/spring-projects/spring-authorization-server/tree/main/samples/default-authorizationserver[default authorization server sample] as a guide.
Then add Spring Boot's starter for Spring Security Authorization Server as a dependency:

======
Maven::
+
----
<dependency>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-starter-oauth2-authorization-server</artifactId>
</dependency>
----

Gradle::
+
----
implementation "org.springframework.boot:spring-boot-starter-oauth2-authorization-server"
----
======

TIP: See {spring-boot-reference-url}installing.html[Installing Spring Boot] for more information on using Spring Boot with Maven or Gradle.

Alternatively, you can add Spring Security Authorization Server without Spring Boot using the following example:

======
Maven::
+
----
<dependency>
<groupId>org.springframework.security</groupId>
<artifactId>spring-security-oauth2-authorization-server</artifactId>
<version>{spring-security-version}</version>
</dependency>
----

Gradle::
+
----
implementation "org.springframework.security:spring-security-oauth2-authorization-server:{spring-security-version}"
----
======

**Developing Your First Application**

To get started, you need the minimum required components defined as a `@Bean`. When using the `spring-boot-starter-oauth2-authorization-server` dependency, define the following properties and Spring Boot will provide the necessary `@Bean` definitions for you:

.application.yml
----
server:
port: 9000

logging:
level:
org.springframework.security: trace

spring:
security:
user:
name: user
password: password
oauth2:
authorizationserver:
client:
oidc-client:
registration:
client-id: "oidc-client"
client-secret: "{noop}secret"
client-authentication-methods:
- "client_secret_basic"
authorization-grant-types:
- "authorization_code"
- "refresh_token"
redirect-uris:
- "http://127.0.0.1:8080/login/oauth2/code/oidc-client"
post-logout-redirect-uris:
- "http://127.0.0.1:8080/"
scopes:
- "openid"
- "profile"
require-authorization-consent: true
----

If you want to customize the default `HttpSecurity` configuration, you may override Spring Boot's auto-configuration with the following example:

.SecurityConfig.java
----
@Configuration
@EnableWebSecurity
public class SecurityConfig {

@Bean
public SecurityFilterChain securityFilterChain(HttpSecurity http) {
http
.authorizeHttpRequests((authorize) ->
authorize
.anyRequest().authenticated()
)
.formLogin(Customizer.withDefaults())
.oauth2AuthorizationServer((authorizationServer) ->
authorizationServer
.oidc(Customizer.withDefaults())	// Enable OpenID Connect 1.0
);
return http.build();
}

}
----

TIP: Beyond the Getting Started experience, most users will want to customize the default configuration. The xref:servlet/oauth2/authorization-server/getting-started.adoc#oauth2AuthorizationServer-defining-required-components[next section] demonstrates providing all of the necessary beans yourself.

**Defining Required Components**

If you want to customize the default configuration (regardless of whether you're using Spring Boot), you can define the minimum required components as a `@Bean` in a Spring `@Configuration`.

These components can be defined as follows:

.SecurityConfig.java
----
@Configuration
@EnableWebSecurity
public class SecurityConfig {

@Bean // <1>
@Order(1)
public SecurityFilterChain authorizationServerSecurityFilterChain(HttpSecurity http)
throws Exception {

http
.oauth2AuthorizationServer((authorizationServer) -> {
http.securityMatcher(authorizationServer.getEndpointsMatcher());
authorizationServer
.oidc(Customizer.withDefaults());	// Enable OpenID Connect 1.0
})
.authorizeHttpRequests((authorize) ->
authorize
.anyRequest().authenticated()
)
.exceptionHandling((exceptions) -> exceptions
.defaultAuthenticationEntryPointFor(
new LoginUrlAuthenticationEntryPoint("/login"),
new MediaTypeRequestMatcher(MediaType.TEXT_HTML)
)
);

return http.build();
}

@Bean // <2>
@Order(2)
public SecurityFilterChain defaultSecurityFilterChain(HttpSecurity http)
throws Exception {
http
.authorizeHttpRequests((authorize) -> authorize
.anyRequest().authenticated()
)
.formLogin(Customizer.withDefaults());

return http.build();
}

@Bean // <3>
public UserDetailsService userDetailsService() {
UserDetails userDetails = User.withDefaultPasswordEncoder()
.username("user")
.password("password")
.roles("USER")
.build();

return new InMemoryUserDetailsManager(userDetails);
}

@Bean // <4>
public RegisteredClientRepository registeredClientRepository() {
RegisteredClient oidcClient = RegisteredClient.withId(UUID.randomUUID().toString())
.clientId("oidc-client")
.clientSecret("{noop}secret")
.clientAuthenticationMethod(ClientAuthenticationMethod.CLIENT_SECRET_BASIC)
.authorizationGrantType(AuthorizationGrantType.AUTHORIZATION_CODE)
.authorizationGrantType(AuthorizationGrantType.REFRESH_TOKEN)
.redirectUri("http://127.0.0.1:8080/login/oauth2/code/oidc-client")
.postLogoutRedirectUri("http://127.0.0.1:8080/")
.scope(OidcScopes.OPENID)
.scope(OidcScopes.PROFILE)
.clientSettings(ClientSettings.builder().requireAuthorizationConsent(true).build())
.build();

return new InMemoryRegisteredClientRepository(oidcClient);
}

@Bean // <5>
public JWKSource<SecurityContext> jwkSource() {
KeyPair keyPair = generateRsaKey();
RSAPublicKey publicKey = (RSAPublicKey) keyPair.getPublic();
RSAPrivateKey privateKey = (RSAPrivateKey) keyPair.getPrivate();
RSAKey rsaKey = new RSAKey.Builder(publicKey)
.privateKey(privateKey)
.keyID(UUID.randomUUID().toString())
.build();
JWKSet jwkSet = new JWKSet(rsaKey);
return new ImmutableJWKSet<>(jwkSet);
}

private static KeyPair generateRsaKey() { // <6>
KeyPair keyPair;
try {
KeyPairGenerator keyPairGenerator = KeyPairGenerator.getInstance("RSA");
keyPairGenerator.initialize(2048);
keyPair = keyPairGenerator.generateKeyPair();
}
catch (Exception ex) {
throw new IllegalStateException(ex);
}
return keyPair;
}

@Bean // <7>
public JwtDecoder jwtDecoder(JWKSource<SecurityContext> jwkSource) {
return OAuth2AuthorizationServerConfiguration.jwtDecoder(jwkSource);
}

@Bean // <8>
public AuthorizationServerSettings authorizationServerSettings() {
return AuthorizationServerSettings.builder().build();
}

}
----

This is a minimal configuration for getting started quickly. To understand what each component is used for, see the following descriptions:

<1> A Spring Security filter chain for the xref:servlet/oauth2/authorization-server/protocol-endpoints.adoc[Protocol Endpoints].
<2> A Spring Security filter chain for xref:servlet/authentication/index.adoc#servlet-authentication[authentication].
<3> An instance of {security-api-url}/org/springframework/security/core/userdetails/UserDetailsService.html[`UserDetailsService`] for retrieving users to authenticate.
<4> An instance of xref:servlet/oauth2/authorization-server/core-model-components.adoc#oauth2AuthorizationServer-registered-client-repository[`RegisteredClientRepository`] for managing clients.
<5> An instance of `com.nimbusds.jose.jwk.source.JWKSource` for signing access tokens.
<6> An instance of `java.security.KeyPair` with keys generated on startup used to create the `JWKSource` above.
<7> An instance of {security-api-url}/org/springframework/security/oauth2/jwt/JwtDecoder.html[`JwtDecoder`] for decoding signed access tokens.
<8> An instance of xref:servlet/oauth2/authorization-server/configuration-model.adoc#oauth2AuthorizationServer-configuring-authorization-server-settings[`AuthorizationServerSettings`] to configure Spring Security Authorization Server.
