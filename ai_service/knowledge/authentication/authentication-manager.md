---
source: authentication manager
---

**authentication manager**

**Authentication Services**
Before Spring Security 3.0, an `AuthenticationManager` was automatically registered internally.
Now you must register one explicitly using the `<authentication-manager>` element.
This creates an instance of Spring Security's `ProviderManager` class, which needs to be configured with a list of one or more `AuthenticationProvider` instances.
These can either be created using syntax elements provided by the namespace, or they can be standard bean definitions, marked for addition to the list using the `authentication-provider` element.


## <authentication-manager>
Every Spring Security application which uses the namespace must have include this element somewhere.
It is responsible for registering the `AuthenticationManager` which provides authentication services to the application.
All elements which create `AuthenticationProvider` instances should be children of this element.


**<authentication-manager> Attributes**


- **alias**
This attribute allows you to define an alias name for the internal instance for use in your own configuration.


- **erase-credentials**
If set to true, the AuthenticationManager will attempt to clear any credentials data in the returned Authentication object, once the user has been authenticated.
Literally it maps to the `eraseCredentialsAfterAuthentication` property of the xref:servlet/authentication/architecture.adoc#servlet-authentication-providermanager[`ProviderManager`].

- **observation-registry-ref**
A reference to the `ObservationRegistry` used for the `FilterChain` and related components

- **id**
This attribute allows you to define an id for the internal instance for use in your own configuration.
It is the same as the alias element, but provides a more consistent experience with elements that use the id attribute.


**Child Elements of <authentication-manager>**


- <<nsa-authentication-provider,authentication-provider>>
- xref:servlet/appendix/namespace/ldap.adoc#nsa-ldap-authentication-provider[ldap-authentication-provider]



**<authentication-provider>**
Unless used with a `ref` attribute, this element is shorthand for configuring a `DaoAuthenticationProvider`.
`DaoAuthenticationProvider` loads user information from a `UserDetailsService` and compares the username/password combination with the values supplied at login.
The `UserDetailsService` instance can be defined either by using an available namespace element (`jdbc-user-service` or by using the `user-service-ref` attribute to point to a bean defined elsewhere in the application context).



**Parent Elements of <authentication-provider>**


- <<nsa-authentication-manager,authentication-manager>>



**<authentication-provider> Attributes**


- **ref**
Defines a reference to a Spring bean that implements `AuthenticationProvider`.

If you have written your own `AuthenticationProvider` implementation (or want to configure one of Spring Security's own implementations as a traditional bean for some reason, then you can use the following syntax to add it to the internal list of `ProviderManager`:

----

<security:authentication-manager>
<security:authentication-provider ref="myAuthenticationProvider" />
</security:authentication-manager>
<bean id="myAuthenticationProvider" class="com.something.MyAuthenticationProvider"/>

----




- **user-service-ref**
A reference to a bean that implements UserDetailsService that may be created using the standard bean element or the custom user-service element.


**Child Elements of <authentication-provider>**


- <<nsa-jdbc-user-service,jdbc-user-service>>
- xref:servlet/appendix/namespace/ldap.adoc#nsa-ldap-user-service[ldap-user-service]
- <<nsa-password-encoder,password-encoder>>
- <<nsa-user-service,user-service>>



**<jdbc-user-service>**
Causes creation of a JDBC-based UserDetailsService.


**<jdbc-user-service> Attributes**


- **authorities-by-username-query**
An SQL statement to query for a user's granted authorities given a username.

The default is

----
select username, authority from authorities where username = ?
----




- **cache-ref**
Defines a reference to a cache for use with a UserDetailsService.


- **data-source-ref**
The bean ID of the DataSource which provides the required tables.


- **group-authorities-by-username-query**
An SQL statement to query user's group authorities given a username.
The default is

+

----
select
g.id, g.group_name, ga.authority
from
groups g, group_members gm, group_authorities ga
where
gm.username = ? and g.id = ga.group_id and g.id = gm.group_id
----




- **id**
A bean identifier, used for referring to the bean elsewhere in the context.


- **role-prefix**
A non-empty string prefix that will be added to role strings loaded from persistent storage (default is "ROLE_").
Use the value "none" for no prefix in cases where the default is non-empty.


- **users-by-username-query**
An SQL statement to query a username, password, and enabled status given a username.
The default is

+

----
select username, password, enabled from users where username = ?
----




**<password-encoder>**
Authentication providers can optionally be configured to use a password encoder as described in the xref:features/authentication/password-storage.adoc#authentication-password-storage[Password Storage].
This will result in the bean being injected with the appropriate `PasswordEncoder` instance.


**Parent Elements of <password-encoder>**


- <<nsa-authentication-provider,authentication-provider>>
- xref:servlet/appendix/namespace/authentication-manager.adoc#nsa-password-compare[password-compare]



**<password-encoder> Attributes**


- **hash**
Defines the hashing algorithm used on user passwords.
We recommend strongly against using MD4, as it is a very weak hashing algorithm.


- **ref**
Defines a reference to a Spring bean that implements `PasswordEncoder`.


**<user-service>**
Creates an in-memory UserDetailsService from a properties file or a list of "user" child elements.
Usernames are converted to lower-case internally to allow for case-insensitive lookups, so this should not be used if case-sensitivity is required.


**<user-service> Attributes**


- **id**
A bean identifier, used for referring to the bean elsewhere in the context.


- **properties**
The location of a Properties file where each line is in the format of

+

----
username=password,grantedAuthority[,grantedAuthority][,enabled|disabled]
----




**Child Elements of <user-service>**


- <<nsa-user,user>>



**<user>**
Represents a user in the application.


**Parent Elements of <user>**


- <<nsa-user-service,user-service>>



**<user> Attributes**


- **authorities**
One of more authorities granted to the user.
Separate authorities with a comma (but no space).
For example, "ROLE_USER,ROLE_ADMINISTRATOR"


- **disabled**
Can be set to "true" to mark an account as disabled and unusable.


- **locked**
Can be set to "true" to mark an account as locked and unusable.


- **name**
The username assigned to the user.


- **password**
The password assigned to the user.
This may be hashed if the corresponding authentication provider supports hashing (remember to set the "hash" attribute of the "user-service" element).
This attribute be omitted in the case where the data will not be used for authentication, but only for accessing authorities.
If omitted, the namespace will generate a random value, preventing its accidental use for authentication.
Cannot be empty.
