# YAML Deserialization

## Overview

YAML deserialization can be unsafe when untrusted YAML is processed into Java objects without restrictions. Some YAML libraries can instantiate arbitrary classes and trigger gadget chains or code execution.

## CWE

CWE-502: Deserialization of Untrusted Data

## Relevant Java APIs

- org.yaml.snakeyaml.Yaml.load
- org.yaml.snakeyaml.Yaml.loadAs
- com.fasterxml.jackson.dataformat.yaml.YAMLMapper

## Attack conditions

The app deserializes untrusted YAML into object graphs or polymorphic types without validation or restrictions.

## Vulnerable Java example

```java
String yaml = request.getParameter("yaml");
Yaml yamlParser = new Yaml();
Object obj = yamlParser.load(yaml);
```

A malicious YAML payload may instantiate dangerous objects or trigger built-in constructors.

## Secure Java example

```java
Yaml yaml = new Yaml(new SafeConstructor(new LoaderOptions()));
MyDto dto = yaml.loadAs(yamlText, MyDto.class);
```

or avoid YAML for untrusted input and use an explicit schema.

## Detection indicators

- `Yaml.load` or `SnakeYAML` on untrusted data
- YAML input for user-controlled configuration or request bodies
- object instantiation from YAML without type restrictions

## Mitigation

- use safe constructors or object-mapping APIs for YAML
- restrict allowed types and disallow arbitrary object construction
- prefer typed DTOs over generic YAML deserialization
- reject untrusted YAML where a schema is not required

## Common false positives

- trusted internal configuration files parsed at startup are not a vulnerability if they are not attacker-controlled