# Elasticsearch Injection

## Overview

Elasticsearch injection occurs when user-controlled data is embedded into ES queries or request payloads, causing unauthorized search execution or unexpected filtering behavior.

## CWE

CWE-943: Improper Neutralization of Special Elements in Data Query Logic

## Relevant Java APIs

- org.elasticsearch.client.RestHighLevelClient.search
- org.elasticsearch.client.RestClient.performRequest
- co.elastic.clients.elasticsearch.ElasticsearchClient.search

## Attack conditions

The issue is present when a query string, JSON body, or DSL document is created from untrusted input without restricting the structure or content.

## Vulnerable Java example

```java
String query = request.getParameter("query");
String body = "{\"query\":{\"match\":{\"message\":\"" + query + "\"}}}";
client.search(s -> s.index("logs").body(body), String.class);
```

This can distort search semantics or inject query operators.

## Secure Java example

```java
String query = request.getParameter("query");
if (!query.matches("^[A-Za-z0-9 _-]{1,128}$")) {
    throw new IllegalArgumentException("Invalid query");
}

SearchRequest searchRequest = new SearchRequest("logs");
SearchSourceBuilder source = new SearchSourceBuilder();
source.query(QueryBuilders.matchQuery("message", query));
searchRequest.source(source);
```

## Detection indicators

- building raw ES DSL from request data
- dynamic query strings or JSON payloads created with string concatenation
- unvalidated search or filter values

## Mitigation

- use typed query builders instead of raw DSL strings
- validate search strings and restrict allowed operators
- avoid allowing direct user DSL or script injection into index queries
