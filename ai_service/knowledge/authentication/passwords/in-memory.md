---
source: in memory
---

**in memory**

**In-Memory Authentication**

Spring Security's `InMemoryUserDetailsManager` implements xref:servlet/authentication/passwords/user-details-service.adoc#servlet-authentication-userdetailsservice[UserDetailsService] to provide support for username/password based authentication that is stored in memory.
`InMemoryUserDetailsManager` provides management of `UserDetails` by implementing the `UserDetailsManager` interface.
`UserDetails`-based authentication is used by Spring Security when it is configured to xref:servlet/authentication/passwords/index.adoc#servlet-authentication-unpwd-input[accept a username and password] for authentication.

In the following sample, we use xref:features/authentication/password-storage.adoc#authentication-password-storage-boot-cli[Spring Boot CLI] to encode a password value of `password` and get the encoded password of `+{bcrypt}$2a$10$GRLdNijSQMUvl/au9ofL.eDwmoohzzS7.rmNSJZ.0FxO/BTk76klW+`:

.InMemoryUserDetailsManager Java Configuration
======
Java::
+
----
@Bean
public UserDetailsService users() {
UserDetails user = User.builder()
.username("user")
.password("{bcrypt}$2a$10$GRLdNijSQMUvl/au9ofL.eDwmoohzzS7.rmNSJZ.0FxO/BTk76klW")
.roles("USER")
.build();
UserDetails admin = User.builder()
.username("admin")
.password("{bcrypt}$2a$10$GRLdNijSQMUvl/au9ofL.eDwmoohzzS7.rmNSJZ.0FxO/BTk76klW")
.roles("USER", "ADMIN")
.build();
return new InMemoryUserDetailsManager(user, admin);
}
----

XML::
+
----
<user-service>
<user name="user"
password="{bcrypt}$2a$10$GRLdNijSQMUvl/au9ofL.eDwmoohzzS7.rmNSJZ.0FxO/BTk76klW"
authorities="ROLE_USER" />
<user name="admin"
password="{bcrypt}$2a$10$GRLdNijSQMUvl/au9ofL.eDwmoohzzS7.rmNSJZ.0FxO/BTk76klW"
authorities="ROLE_USER,ROLE_ADMIN" />
</user-service>
----

Kotlin::
+
----
@Bean
fun users(): UserDetailsService {
val user = User.builder()
.username("user")
.password("{bcrypt}$2a$10\$GRLdNijSQMUvl/au9ofL.eDwmoohzzS7.rmNSJZ.0FxO/BTk76klW")
.roles("USER")
.build()
val admin = User.builder()
.username("admin")
.password("{bcrypt}$2a$10\$GRLdNijSQMUvl/au9ofL.eDwmoohzzS7.rmNSJZ.0FxO/BTk76klW")
.roles("USER", "ADMIN")
.build()
return InMemoryUserDetailsManager(user, admin)
}
----
======

The preceding samples store the passwords in a secure format but leave a lot to be desired in terms of a getting started experience.

In the following sample, we use xref:features/authentication/password-storage.adoc#authentication-password-storage-dep-getting-started[User.withDefaultPasswordEncoder] to ensure that the password stored in memory is protected.
However, it does not protect against obtaining the password by decompiling the source code.
For this reason, `User.withDefaultPasswordEncoder` should only be used for "`getting started`" and is not intended for production.

.InMemoryUserDetailsManager with User.withDefaultPasswordEncoder
======
Java::
+
----
@Bean
public UserDetailsService users() {
UserBuilder users = User.withDefaultPasswordEncoder();
UserDetails user = users
.username("user")
.password("password")
.roles("USER")
.build();
UserDetails admin = users
.username("admin")
.password("password")
.roles("USER", "ADMIN")
.build();
return new InMemoryUserDetailsManager(user, admin);
}
----

Kotlin::
+
----
@Bean
fun users(): UserDetailsService {
val users = User.withDefaultPasswordEncoder()
val user = users
.username("user")
.password("password")
.roles("USER")
.build()
val admin = users
.username("admin")
.password("password")
.roles("USER", "ADMIN")
.build()
return InMemoryUserDetailsManager(user, admin)
}
----
======

There is no simple way to use `User.withDefaultPasswordEncoder` with XML-based configuration.
For demos or just getting started, you can choose to prefix the password with `+{noop}+` to indicate xref:features/authentication/password-storage.adoc#authentication-password-storage-dpe-format[no encoding should be used]:

.<user-service> `+{noop}+` XML Configuration
----
<user-service>
<user name="user"
password="{noop}password"
authorities="ROLE_USER" />
<user name="admin"
password="{noop}password"
authorities="ROLE_USER,ROLE_ADMIN" />
</user-service>
----
