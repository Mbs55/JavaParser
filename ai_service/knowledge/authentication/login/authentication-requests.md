---
source: authentication requests
---

**authentication requests**

**Producing ``<saml2:AuthnRequest>``s**

As stated earlier, Spring Security's SAML 2.0 support produces a `<saml2:AuthnRequest>` to commence authentication with the asserting party.

Spring Security achieves this in part by registering the `Saml2WebSsoAuthenticationRequestFilter` in the filter chain.
This filter by default responds to the endpoints `+/saml2/authenticate/{registrationId}+` and `+/saml2/authenticate?registrationId={registrationId}+`.

For example, if you were deployed to `https://rp.example.com` and you gave your registration an ID of `okta`, you could navigate to:

`https://rp.example.org/saml2/authenticate/okta`

and the result would be a redirect that included a `SAMLRequest` parameter containing the signed, deflated, and encoded `<saml2:AuthnRequest>`.

## Configuring the `<saml2:AuthnRequest>` Endpoint

To configure the endpoint differently from the default, you can set the value in `saml2Login`:

======
Java::
+
----
@Bean
SecurityFilterChain filterChain(HttpSecurity http) {
http
.saml2Login((saml2) -> saml2
.authenticationRequestUriQuery("/custom/auth/sso?peerEntityID={registrationId}")
);
return new CustomSaml2AuthenticationRequestRepository();
}
----

Kotlin::
+
----
@Bean
fun filterChain(http: HttpSecurity): SecurityFilterChain {
http {
saml2Login {
authenticationRequestUriQuery = "/custom/auth/sso?peerEntityID={registrationId}"
}
}
return CustomSaml2AuthenticationRequestRepository()
}
----
======

**Changing How the `<saml2:AuthnRequest>` Gets Stored**

`Saml2WebSsoAuthenticationRequestFilter` uses an `Saml2AuthenticationRequestRepository` to persist an `AbstractSaml2AuthenticationRequest` instance before xref:servlet/saml2/login/authentication-requests.adoc#servlet-saml2login-sp-initiated-factory[sending the `<saml2:AuthnRequest>`] to the asserting party.

Additionally, `Saml2WebSsoAuthenticationFilter` and `Saml2AuthenticationTokenConverter` use an `Saml2AuthenticationRequestRepository` to load any `AbstractSaml2AuthenticationRequest` as part of xref:servlet/saml2/login/authentication.adoc#servlet-saml2login-authenticate-responses[authenticating the `<saml2:Response>`].

By default, Spring Security uses an `HttpSessionSaml2AuthenticationRequestRepository`, which stores the `AbstractSaml2AuthenticationRequest` in the `HttpSession`.

If you have a custom implementation of `Saml2AuthenticationRequestRepository`, you may configure it by exposing it as a `@Bean` as shown in the following example:

======
Java::
+
----
@Bean
Saml2AuthenticationRequestRepository<AbstractSaml2AuthenticationRequest> authenticationRequestRepository() {
return new CustomSaml2AuthenticationRequestRepository();
}
----

Kotlin::
+
----
@Bean
open fun authenticationRequestRepository(): Saml2AuthenticationRequestRepository<AbstractSaml2AuthenticationRequest> {
return CustomSaml2AuthenticationRequestRepository()
}
----
======

**Caching the `<saml2:AuthnRequest>` by the Relay State**

If you don't want to use the session to store the `<saml2:AuthnRequest>`, you can also store it in a distributed cache.
This can be helpful if you are trying to use `SameSite=Strict` and are losing the authentication request in the redirect from the Identity Provider.

=====
It's important to remember that there are security benefits to storing it in the session.
One such benefit is the natural login fixation defense it provides.
For example, if an application looks the authentication request up from the session, then even if an attacker provides their own SAML response to a victim, the login will fail.

On the other hand, if we trust the InResponseTo or RelayState to retrieve the authentication request, then there's no way to know if the SAML response was requested by that handshake.
=====

To help with this, Spring Security has `CacheSaml2AuthenticationRequestRepository`, which you can publish as a bean for the filter chain to pick up:

======
Java::
+
----
@Bean
Saml2AuthenticationRequestRepository<?> authenticationRequestRepository() {
return new CacheSaml2AuthenticationRequestRepository();
}
----

Kotlin::
+
----
@Bean
fun authenticationRequestRepository(): Saml2AuthenticationRequestRepository<*> {
return CacheSaml2AuthenticationRequestRepository()
}
----
======


**Changing How the `<saml2:AuthnRequest>` Gets Sent**

By default, Spring Security signs each `<saml2:AuthnRequest>` and send it as a GET to the asserting party.

Many asserting parties don't require a signed `<saml2:AuthnRequest>`.
This can be configured automatically via `RelyingPartyRegistrations`, or you can supply it manually, like so:


.Not Requiring Signed AuthnRequests
======
Boot::
+
----
spring:
security:
saml2:
relyingparty:
registration:
okta:
assertingparty:
entity-id: ...
singlesignon.sign-request: false
----

Java::
+
----
RelyingPartyRegistration relyingPartyRegistration = RelyingPartyRegistration.withRegistrationId("okta")
.assertingPartyMetadata((party) -> party
.wantAuthnRequestsSigned(false)
)
.build();
----

Kotlin::
+
----
var relyingPartyRegistration: RelyingPartyRegistration =
RelyingPartyRegistration.withRegistrationId("okta")
.assertingPartyMetadata { party: AssertingPartyMetadata.Builder -> party
.wantAuthnRequestsSigned(false)
}
.build()
----
======

Otherwise, you will need to specify a private key to `RelyingPartyRegistration#signingX509Credentials` so that Spring Security can sign the `<saml2:AuthnRequest>` before sending.

By default, Spring Security will sign the `<saml2:AuthnRequest>` using `rsa-sha256`, though some asserting parties will require a different algorithm, as indicated in their metadata.

You can configure the algorithm based on the asserting party's xref:servlet/saml2/login/overview.adoc#servlet-saml2login-relyingpartyregistrationrepository[metadata using `RelyingPartyRegistrations`].

Or, you can provide it manually:

======
Java::
+
----
String metadataLocation = "classpath:asserting-party-metadata.xml";
RelyingPartyRegistration relyingPartyRegistration = RelyingPartyRegistrations.fromMetadataLocation(metadataLocation)
.assertingPartyMetadata((party) -> party
.signingAlgorithms((sign) -> sign.add(SignatureConstants.ALGO_ID_SIGNATURE_RSA_SHA512))
)
.build();
----

Kotlin::
+
----
var metadataLocation = "classpath:asserting-party-metadata.xml"
var relyingPartyRegistration: RelyingPartyRegistration =
RelyingPartyRegistrations.fromMetadataLocation(metadataLocation)
.assertingPartyMetadata { party: AssertingPartyMetadata.Builder -> party
.signingAlgorithms { sign: MutableList<String?> ->
sign.add(
SignatureConstants.ALGO_ID_SIGNATURE_RSA_SHA512
)
}
}
.build()
----
======

NOTE: The snippet above uses the OpenSAML `SignatureConstants` class to supply the algorithm name.
But, that's just for convenience.
Since the datatype is `String`, you can supply the name of the algorithm directly.

Some asserting parties require that the `<saml2:AuthnRequest>` be POSTed.
This can be configured automatically via `RelyingPartyRegistrations`, or you can supply it manually, like so:

======
Java::
+
----
RelyingPartyRegistration relyingPartyRegistration = RelyingPartyRegistration.withRegistrationId("okta")
.assertingPartyMetadata((party) -> party
.singleSignOnServiceBinding(Saml2MessageBinding.POST)
)
.build();
----

Kotlin::
+
----
var relyingPartyRegistration: RelyingPartyRegistration? =
RelyingPartyRegistration.withRegistrationId("okta")
.assertingPartyMetadata { party: AssertingPartyMetadata.Builder -> party
.singleSignOnServiceBinding(Saml2MessageBinding.POST)
}
.build()
----
======

**Customizing OpenSAML's `AuthnRequest` Instance**

There are a number of reasons that you may want to adjust an `AuthnRequest`.
For example, you may want `ForceAuthN` to be set to `true`, which Spring Security sets to `false` by default.

You can customize elements of OpenSAML's `AuthnRequest` by publishing an `OpenSaml5AuthenticationRequestResolver` as a `@Bean`, like so:

======
Java::
+
----
@Bean
Saml2AuthenticationRequestResolver authenticationRequestResolver(RelyingPartyRegistrationRepository registrations) {
RelyingPartyRegistrationResolver registrationResolver =
new DefaultRelyingPartyRegistrationResolver(registrations);
OpenSaml5AuthenticationRequestResolver authenticationRequestResolver =
new OpenSaml5AuthenticationRequestResolver(registrationResolver);
authenticationRequestResolver.setAuthnRequestCustomizer((context) -> context
.getAuthnRequest().setForceAuthn(true));
return authenticationRequestResolver;
}
----

Kotlin::
+
----
@Bean
fun authenticationRequestResolver(registrations : RelyingPartyRegistrationRepository) : Saml2AuthenticationRequestResolver {
val registrationResolver : RelyingPartyRegistrationResolver =
new DefaultRelyingPartyRegistrationResolver(registrations)
val authenticationRequestResolver : OpenSaml5AuthenticationRequestResolver =
new OpenSaml5AuthenticationRequestResolver(registrationResolver)
authenticationRequestResolver.setAuthnRequestCustomizer((context) -> context
.getAuthnRequest().setForceAuthn(true))
return authenticationRequestResolver
}
----
======
