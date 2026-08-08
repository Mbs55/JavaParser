# Unencrypted Socket

## Overview

An unencrypted socket vulnerability occurs when the application communicates over a network channel without confidentiality or integrity guarantees, typically through plain TCP or insecure protocols.

## CWE

CWE-319: Cleartext Transmission of Sensitive Information

## Relevant Java APIs

- java.net.Socket
- java.net.ServerSocket
- javax.net.ssl.SSLSocketFactory
- java.nio.channels.SocketChannel

## Attack conditions

The app opens network sockets for sensitive data without using TLS or a secure encrypted channel.

## Vulnerable Java example

```java
Socket socket = new Socket("db.internal", 5432);
OutputStream out = socket.getOutputStream();
out.write(secretData.getBytes(StandardCharsets.UTF_8));
```

## Secure Java example

```java
SSLSocketFactory factory = (SSLSocketFactory) SSLSocketFactory.getDefault();
SSLSocket socket = (SSLSocketFactory) factory.createSocket("db.internal", 5432);
```

or use a TLS-enabled connection library for the relevant service.

## Detection indicators

- direct `Socket` creation for authenticated or sensitive traffic
- plaintext TCP protocols used for credentials or data exchange
- insecure transport without TLS wrappers or mutual authentication

## Mitigation

- use TLS for all network traffic carrying sensitive data
- prefer secure protocols like HTTPS, LDAPS, or TLS-wrapped database connections
- validate certificates and trust settings appropriately
- disable insecure transport paths in production

## Common false positives

- internal-only data with no sensitive value may be acceptable in controlled networks, but secure default practices should still be preferred