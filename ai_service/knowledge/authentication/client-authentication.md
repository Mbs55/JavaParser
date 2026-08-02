---
source: client authentication
---

# client authentication

# [[oauth2Client-client-auth-support]]Client Authentication Support

## [[oauth2Client-client-credentials-auth]]Client Credentials

### Authenticate using `client_secret_basic`

Client Authentication with HTTP Basic is supported out of the box and no customization is necessary to enable it.
The default implementation is provided by `DefaultOAuth2TokenRequestHeadersConverter`.

Given the following Spring Boot properties for an OAuth 2.0 client registration:

----
spring:
security:
oauth2:
client:
registration:
okta:
client-id: client-id
client-secret: client-secret
client-authentication-method: client_secret_basic
authorization-grant-type: authorization_code
...
----

The following example shows how to configure `RestClientAuthorizationCodeTokenResponseClient` to disable URL encoding of the client credentials:

======
Java::
+
----
DefaultOAuth2TokenRequestHeadersConverter<OAuth2AuthorizationCodeGrantRequest> headersConverter =
new DefaultOAuth2TokenRequestHeadersConverter<>();
headersConverter.setEncodeClientCredentials(false);

RestClientAuthorizationCodeTokenResponseClient tokenResponseClient =
new RestClientAuthorizationCodeTokenResponseClient();
tokenResponseClient.setHeadersConverter(headersConverter);
----

Kotlin::
+
----
val headersConverter = DefaultOAuth2TokenRequestHeadersConverter<OAuth2AuthorizationCodeGrantRequest>()
headersConverter.setEncodeClientCredentials(false)

val tokenResponseClient = RestClientAuthorizationCodeTokenResponseClient()
tokenResponseClient.setHeadersConverter(headersConverter)
----
======

### Authenticate using `client_secret_post`

Client Authentication with client credentials included in the request-body is supported out of the box and no customization is necessary to enable it.

The following Spring Boot properties for an OAuth 2.0 client registration demonstrate the configuration:

----
spring:
security:
oauth2:
client:
registration:
okta:
client-id: client-id
client-secret: client-secret
client-authentication-method: client_secret_post
authorization-grant-type: authorization_code
...
----

## [[oauth2Client-jwt-bearer-auth]]JWT Bearer

====
Please refer to JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants for further details on https://datatracker.ietf.org/doc/html/rfc7523#section-2.2[JWT Bearer] Client Authentication.
====

The default implementation for JWT Bearer Client Authentication is `NimbusJwtClientAuthenticationParametersConverter`,
which is a `Converter` that customizes the Token Request parameters by adding
a signed JSON Web Token (JWS) in the `client_assertion` parameter.

The `java.security.PrivateKey` or `javax.crypto.SecretKey` used for signing the JWS
is supplied by the `com.nimbusds.jose.jwk.JWK` resolver associated with `NimbusJwtClientAuthenticationParametersConverter`.

### Authenticate using `private_key_jwt`

Given the following Spring Boot properties for an OAuth 2.0 Client registration:

----
spring:
security:
oauth2:
client:
registration:
okta:
client-id: okta-client-id
client-authentication-method: private_key_jwt
authorization-grant-type: authorization_code
...
----

The following example shows how to configure `RestClientAuthorizationCodeTokenResponseClient`:

======
Java::
+
----
Function<ClientRegistration, JWK> jwkResolver = (clientRegistration) -> {
if (clientRegistration.getClientAuthenticationMethod().equals(ClientAuthenticationMethod.PRIVATE_KEY_JWT)) {
RSAPublicKey publicKey = ...
RSAPrivateKey privateKey = ...
return new RSAKey.Builder(publicKey)
.privateKey(privateKey)
.keyID(UUID.randomUUID().toString())
.build();
}
return null;
};

RestClientAuthorizationCodeTokenResponseClient tokenResponseClient =
new RestClientAuthorizationCodeTokenResponseClient();
tokenResponseClient.addParametersConverter(
new NimbusJwtClientAuthenticationParametersConverter<>(jwkResolver));
----

Kotlin::
+
----
val jwkResolver: Function<ClientRegistration, JWK> =
Function<ClientRegistration, JWK> { clientRegistration ->
if (clientRegistration.clientAuthenticationMethod.equals(ClientAuthenticationMethod.PRIVATE_KEY_JWT)) {
var publicKey: RSAPublicKey
var privateKey: RSAPrivateKey
RSAKey.Builder(publicKey) = //...
.privateKey(privateKey) = //...
.keyID(UUID.randomUUID().toString())
.build()
}
null
}

val tokenResponseClient = RestClientAuthorizationCodeTokenResponseClient()
tokenResponseClient.addParametersConverter(
NimbusJwtClientAuthenticationParametersConverter(jwkResolver)
)
----
======

### Authenticate using `client_secret_jwt`

Given the following Spring Boot properties for an OAuth 2.0 Client registration:

----
spring:
security:
oauth2:
client:
registration:
okta:
client-id: okta-client-id
client-secret: okta-client-secret
client-authentication-method: client_secret_jwt
authorization-grant-type: client_credentials
...
----

The following example shows how to configure `RestClientClientCredentialsTokenResponseClient`:

======
Java::
+
----
Function<ClientRegistration, JWK> jwkResolver = (clientRegistration) -> {
if (clientRegistration.getClientAuthenticationMethod().equals(ClientAuthenticationMethod.CLIENT_SECRET_JWT)) {
SecretKeySpec secretKey = new SecretKeySpec(
clientRegistration.getClientSecret().getBytes(StandardCharsets.UTF_8),
"HmacSHA256");
return new OctetSequenceKey.Builder(secretKey)
.keyID(UUID.randomUUID().toString())
.build();
}
return null;
};

RestClientClientCredentialsTokenResponseClient tokenResponseClient =
new RestClientClientCredentialsTokenResponseClient();
tokenResponseClient.addParametersConverter(
new NimbusJwtClientAuthenticationParametersConverter<>(jwkResolver));
----

Kotlin::
+
----
val jwkResolver = Function<ClientRegistration, JWK?> { clientRegistration: ClientRegistration ->
if (clientRegistration.clientAuthenticationMethod == ClientAuthenticationMethod.CLIENT_SECRET_JWT) {
val secretKey = SecretKeySpec(
clientRegistration.clientSecret.toByteArray(StandardCharsets.UTF_8),
"HmacSHA256"
)
OctetSequenceKey.Builder(secretKey)
.keyID(UUID.randomUUID().toString())
.build()
}
null
}

val tokenResponseClient = RestClientClientCredentialsTokenResponseClient()
tokenResponseClient.addParametersConverter(
NimbusJwtClientAuthenticationParametersConverter(jwkResolver)
)
----
======

### Customizing the JWT assertion

The JWT produced by `NimbusJwtClientAuthenticationParametersConverter` contains the `iss`, `sub`, `aud`, `jti`, `iat` and `exp` claims by default. You can customize the headers and/or claims by providing a `Consumer<NimbusJwtClientAuthenticationParametersConverter.JwtClientAuthenticationContext<T>>` to `setJwtClientAssertionCustomizer()`. The following example shows how to customize claims of the JWT:

======
Java::
+
----
Function<ClientRegistration, JWK> jwkResolver = ...

NimbusJwtClientAuthenticationParametersConverter<OAuth2ClientCredentialsGrantRequest> converter =
new NimbusJwtClientAuthenticationParametersConverter<>(jwkResolver);
converter.setJwtClientAssertionCustomizer((context) -> {
context.getHeaders().header("custom-header", "header-value");
context.getClaims().claim("custom-claim", "claim-value");
});
----

Kotlin::
+
----
val jwkResolver = ...

val converter: NimbusJwtClientAuthenticationParametersConverter<OAuth2ClientCredentialsGrantRequest> =
NimbusJwtClientAuthenticationParametersConverter(jwkResolver)
converter.setJwtClientAssertionCustomizer { context ->
context.headers.header("custom-header", "header-value")
context.claims.claim("custom-claim", "claim-value")
}
----
======

## [[oauth2Client-public-auth]]Public Authentication

Public Client Authentication is supported out of the box and no customization is necessary to enable it.

The following Spring Boot properties for an OAuth 2.0 client registration demonstrate the configuration:

----
spring:
security:
oauth2:
client:
registration:
okta:
client-id: client-id
client-authentication-method: none
authorization-grant-type: authorization_code
...
----

====
Public Clients are supported using https://tools.ietf.org/html/rfc7636[Proof Key for Code Exchange] (PKCE).
PKCE will automatically be used when `client-authentication-method` is set to "none" (`ClientAuthenticationMethod.NONE`).
====
