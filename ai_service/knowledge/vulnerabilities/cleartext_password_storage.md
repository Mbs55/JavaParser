# Cleartext Password Storage

## Summary

Cleartext password storage occurs when passwords or secrets are written or persisted without hashing or strong encryption. This is a serious issue even when the application is not directly exposed to a web attack.

## CWE

CWE-256: Plaintext Storage of a Password

## Relevant Java APIs

- java.sql.PreparedStatement
- java.sql.Connection
- javax.crypto.Cipher
- java.security.MessageDigest
- org.springframework.security.crypto.password.PasswordEncoder

## Vulnerable Java example

```java
String sql = "INSERT INTO users(username, password) VALUES (?, ?)";
PreparedStatement ps = connection.prepareStatement(sql);
ps.setString(1, username);
ps.setString(2, password);
ps.executeUpdate();
```

This stores the password in plain form in the database.

## Secure Java example

```java
String encoded = passwordEncoder.encode(password);
String sql = "INSERT INTO users(username, password) VALUES (?, ?)";
PreparedStatement ps = connection.prepareStatement(sql);
ps.setString(1, username);
ps.setString(2, encoded);
ps.executeUpdate();
```

## Detection indicators

- storing raw passwords or secret values in a database or file
- direct persistence of credentials without hashing
- use of weak or reversible encryption for passwords
- password fields named `password`, `passwd`, or `secret` written without a strong password hash

## Mitigation

- hash passwords with BCrypt, PBKDF2, Argon2, or scrypt
- never store raw passwords or reversible secrets for authentication
- use secure random salt values when hashing
- keep keys separate from encrypted material
- rotate password storage schemes carefully during upgrades

## False positives

- encrypted credentials used for transport or secrets management are not always a cleartext password issue when they are not used as user authentication passwords
