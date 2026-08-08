# Insecure Direct Object Reference (IDOR)

## Overview

IDOR occurs when an application exposes a reference to an internal object, such as a database ID or path, without verifying the current user is allowed to access it.

## CWE

CWE-639: Authorization Bypass Through User-Controlled Key

## Relevant Java APIs

- org.springframework.web.bind.annotation.PathVariable
- org.springframework.web.bind.annotation.RequestParam
- javax.persistence.EntityManager.find
- org.springframework.data.repository.CrudRepository.findById

## Attack conditions

The app takes a user-controlled identifier and directly loads or modifies the corresponding resource without checking ownership or role.

## Vulnerable Java example

```java
@GetMapping("/invoice/{id}")
public Invoice getInvoice(@PathVariable Long id) {
    return invoiceRepository.findById(id).orElse(null);
}
```

A user can request another customer’s invoice by guessing the numeric ID.

## Secure Java example

```java
@GetMapping("/invoice/{id}")
@PreAuthorize("@invoiceSecurity.canView(authentication, #id)")
public Invoice getInvoice(@PathVariable Long id) {
    return invoiceRepository.findById(id).orElse(null);
}
```

## Detection indicators

- direct use of object IDs from URL parameters without authorization checks
- repository lookups by raw user-supplied keys
- endpoints exposing private resources by predictable identifiers

## Mitigation

- enforce role and ownership checks on each object access
- use security expressions or service-layer authorization checks
- avoid exposing internal IDs if indirect references are enough
- log and monitor access to sensitive object IDs

## Common false positives

- authorization enforced in the service layer may still be safe even if the controller passes ID values directly
- a route may be intentionally public when the object is not sensitive