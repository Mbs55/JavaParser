---
source: ldap
---

# ldap

# LDAP Namespace Options
LDAP is covered in some details in xref:servlet/authentication/passwords/ldap.adoc#servlet-authentication-ldap[its own chapter].
We will expand on that here with some explanation of how the namespace options map to Spring beans.
The LDAP implementation uses Spring LDAP extensively, so some familiarity with that project's API may be useful.


## Defining the LDAP Server using the
`<ldap-server>` Element
This element sets up a Spring LDAP `ContextSource` for use by the other LDAP beans, defining the location of the LDAP server and other information (such as a username and password, if it doesn't allow anonymous access) for connecting to it.
It can also be used to create an embedded server for testing.
Details of the syntax for both options are covered in the xref:servlet/authentication/passwords/ldap.adoc#servlet-authentication-ldap[LDAP chapter].
The actual `ContextSource` implementation is `DefaultSpringSecurityContextSource` which extends Spring LDAP's `LdapContextSource` class.
The `manager-dn` and `manager-password` attributes map to the latter's `userDn` and `password` properties respectively.

If you only have one server defined in your application context, the other LDAP namespace-defined beans will use it automatically.
Otherwise, you can give the element an "id" attribute and refer to it from other namespace beans using the `server-ref` attribute.
This is actually the bean `id` of the `ContextSource` instance, if you want to use it in other traditional Spring beans.


### <ldap-server> Attributes

- **mode**
Explicitly specifies which embedded ldap server should use. The only supported value is `unboundid`. By default, it will depends if the library is available in the classpath.

- **id**
A bean identifier, used for referring to the bean elsewhere in the context.


- **ldif**
Explicitly specifies an ldif file resource to load into an embedded LDAP server.
The ldif should be a Spring resource pattern (i.e. classpath:init.ldif).
The default is classpath*:*.ldif


- **manager-dn**
Username (DN) of the "manager" user identity which will be used to authenticate to a (non-embedded) LDAP server.
If omitted, anonymous access will be used.


- **manager-password**
The password for the manager DN.
This is required if the manager-dn is specified.


- **port**
Specifies an IP port number.
Used to configure an embedded LDAP server, for example.
The default value is 33389.


- **root**
Optional root suffix for the embedded LDAP server.
Default is "dc=springframework,dc=org"


- **url**
Specifies the ldap server URL when not using the embedded LDAP server.


## <ldap-authentication-provider>
This element is shorthand for the creation of an `LdapAuthenticationProvider` instance.
By default this will be configured with a `BindAuthenticator` instance and a `DefaultAuthoritiesPopulator`.
As with all namespace authentication providers, it must be included as a child of the `authentication-provider` element.


### Parent Elements of <ldap-authentication-provider>


- xref:servlet/appendix/namespace/authentication-manager.adoc#nsa-authentication-manager[authentication-manager]



### <ldap-authentication-provider> Attributes


- **group-role-attribute**
The LDAP attribute name which contains the role name which will be used within Spring Security.
Maps to the ``DefaultLdapAuthoritiesPopulator``'s `groupRoleAttribute` property.
Defaults to "cn".


- **group-search-base**
Search base for group membership searches.
Maps to the ``DefaultLdapAuthoritiesPopulator``'s `groupSearchBase` constructor argument.
Defaults to "" (searching from the root).


- **group-search-filter**
Group search filter.
Maps to the ``DefaultLdapAuthoritiesPopulator``'s `groupSearchFilter` property.
Defaults to `+(uniqueMember={0})+`.
The substituted parameter is the DN of the user.


- **role-prefix**
A non-empty string prefix that will be added to role strings loaded from persistent.
Maps to the ``DefaultLdapAuthoritiesPopulator``'s `rolePrefix` property.
Defaults to "ROLE_".
Use the value "none" for no prefix in cases where the default is non-empty.


- **server-ref**
The optional server to use.
If omitted, and a default LDAP server is registered (using <ldap-server> with no Id), that server will be used.


- **user-context-mapper-ref**
Allows explicit customization of the loaded user object by specifying a UserDetailsContextMapper bean which will be called with the context information from the user's directory entry


- **user-details-class**
Allows the objectClass of the user entry to be specified.
If set, the framework will attempt to load standard attributes for the defined class into the returned UserDetails object


- **user-dn-pattern**
If your users are at a fixed location in the directory (i.e. you can work out the DN directly from the username without doing a directory search), you can use this attribute to map directly to the DN.
It maps directly to the `userDnPatterns` property of `AbstractLdapAuthenticator`.
The value is a specific pattern used to build the user's DN, for example `+uid={0},ou=people+`.
The key `+{0}+` must be present and will be substituted with the username.


- **user-search-base**
Search base for user searches.
Defaults to "".
Only used with a 'user-search-filter'.

+

If you need to perform a search to locate the user in the directory, then you can set these attributes to control the search.
The `BindAuthenticator` will be configured with a `FilterBasedLdapUserSearch` and the attribute values map directly to the first two arguments of that bean's constructor.
If these attributes aren't set and no `user-dn-pattern` has been supplied as an alternative, then the default search values of `+user-search-filter="(uid={0})"+` and `user-search-base=""` will be used.


- **user-search-filter**
The LDAP filter used to search for users (optional).
For example `+(uid={0})+`.
The substituted parameter is the user's login name.

+

If you need to perform a search to locate the user in the directory, then you can set these attributes to control the search.
The `BindAuthenticator` will be configured with a `FilterBasedLdapUserSearch` and the attribute values map directly to the first two arguments of that bean's constructor.
If these attributes aren't set and no `user-dn-pattern` has been supplied as an alternative, then the default search values of `+user-search-filter="(uid={0})"+` and `user-search-base=""` will be used.


### Child Elements of <ldap-authentication-provider>


- <<nsa-password-compare,password-compare>>



## <password-compare>
This is used as child element to `<ldap-provider>` and switches the authentication strategy from `BindAuthenticator` to `PasswordComparisonAuthenticator`.


### Parent Elements of <password-compare>


- <<nsa-ldap-authentication-provider,ldap-authentication-provider>>



### <password-compare> Attributes


- **hash**
Defines the hashing algorithm used on user passwords.
We recommend strongly against using MD4, as it is a very weak hashing algorithm.


- **password-attribute**
The attribute in the directory which contains the user password.
Defaults to "userPassword".


### Child Elements of <password-compare>


- xref:servlet/appendix/namespace/authentication-manager.adoc#nsa-password-encoder[password-encoder]



## <ldap-user-service>
This element configures an LDAP `UserDetailsService`.
The class used is `LdapUserDetailsService` which is a combination of a `FilterBasedLdapUserSearch` and a `DefaultLdapAuthoritiesPopulator`.
The attributes it supports have the same usage as in `<ldap-provider>`.


### <ldap-user-service> Attributes


- **cache-ref**
Defines a reference to a cache for use with a UserDetailsService.


- **group-role-attribute**
The LDAP attribute name which contains the role name which will be used within Spring Security.
Defaults to "cn".


- **group-search-base**
Search base for group membership searches.
Defaults to "" (searching from the root).


- **group-search-filter**
Group search filter.
Defaults to `+(uniqueMember={0})+`.
The substituted parameter is the DN of the user.


- **id**
A bean identifier, used for referring to the bean elsewhere in the context.


- **role-prefix**
A non-empty string prefix that will be added to role strings loaded from persistent storage (e.g.
"ROLE_").
Use the value "none" for no prefix in cases where the default is non-empty.


- **server-ref**
The optional server to use.
If omitted, and a default LDAP server is registered (using <ldap-server> with no Id), that server will be used.


- **user-context-mapper-ref**
Allows explicit customization of the loaded user object by specifying a UserDetailsContextMapper bean which will be called with the context information from the user's directory entry


- **user-details-class**
Allows the objectClass of the user entry to be specified.
If set, the framework will attempt to load standard attributes for the defined class into the returned UserDetails object


- **user-search-base**
Search base for user searches.
Defaults to "".
Only used with a 'user-search-filter'.


- **user-search-filter**
The LDAP filter used to search for users (optional).
For example `+(uid={0})+`.
The substituted parameter is the user's login name.
