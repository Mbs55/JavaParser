# AWS Misconfiguration

## Overview

AWS misconfiguration is a security issue where cloud resources are exposed or configured with unsafe defaults. In Java applications, this often occurs when a service client is configured without least-privilege access, public exposure, or safe region/network controls.

## CWE

CWE-284: Improper Access Control

## Relevant Java APIs

- com.amazonaws.services.simpledb.model.SelectRequest
- com.amazonaws.services.simpledb.model.SelectRequest.withSelectExpression
- AmazonS3 client configuration and IAM role assumptions
- AWS SDK clients used with overly broad permissions

## Attack conditions

A Java application may be vulnerable when:

- environment variables or config files permit unrestricted AWS access
- IAM policies are over-permissive
- S3 buckets or databases are public or not locked down
- service clients are configured to trust broad default permissions
- untrusted input is used to change resource identifiers or query scope

## Vulnerable Java example

```java
String expression = request.getParameter("query");
SelectRequest req = new SelectRequest()
    .withSelectExpression(expression);

SelectResult result = simpleDB.select(req);
```

If the query or resource selection is attacker-controlled and the AWS service account has excessive privileges, the application can expose or alter unintended data.

## Secure Java example

```java
String expression = request.getParameter("query");
if (!expression.matches("^[A-Za-z0-9_\s=,()'-]{1,256}$")) {
    throw new IllegalArgumentException("Invalid query");
}

SelectRequest req = new SelectRequest()
    .withSelectExpression("select * from ProductCatalog where ItemName = 'safe-value'");

SelectResult result = simpleDB.select(req);
```

## Detection indicators

- AWS SDK clients created with default or broad credentials
- user-controlled resource names, bucket names, or Select expressions
- permissive IAM policy documents or wildcards
- public buckets, public DB access, or region exposure beyond the trust boundary

## Mitigation

- enforce least privilege for AWS identities and roles
- do not use wildcard permissions unless absolutely required
- validate and constrain all user-controlled resource names and query expressions
- keep secrets in managed secret stores, not source code or config files
- restrict public access on storage and network resources
- use secure defaults for bucket policies, network ACLs, and IAM roles

## False positives

- default client configuration that is not exposed to user input is not automatically dangerous
- a Java app may use AWS SDK methods safely when all resource names and queries are fixed and validated

## Relevant guidance

- AWS Identity and Access Management documentation
- AWS well-architected security guidance
- OWASP Cloud Security guidelines
