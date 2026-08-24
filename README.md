1-The project Get the cp.txt(dependencies of the project if it is a spring boot app)
*uses this command on the project:
mvn dependency:build-classpath -Dmdep.outputFile=cp.txt
(For A Spring Boot app you should install the dependecies ,demoApp can't be resolved without it)
2-Pass the Root of the project in a post request
3-To run the app:
'cd backend && mvn spring-boot:run'
then cd ../frontend && npm run build && npm run dev

Documentations used:
-OWASP Cheat Sheet Series
-CWE
-CERT Oracle Secure Coding Standard for Java
-Spring Security Documentation
-Oracle Secure Coding Guidelines
-FindSecBugs rules
-SonarSource Java security rules

Prompt:
You are a senior Java Application Security Engineer.

Analyze the following Java method.

============================

Method metadata

{json}

============================

Java Source

...

============================

Relevant Security Documentation

Chunk 1

...

Chunk 2

...

Chunk 3

...

============================

Return ONLY JSON.







authenticate()

===================

Outgoing Method Summary

findUser()

Risk: HIGH

Confirmed Vulnerability:
SQL Injection

Reason:
Uses Statement with concatenated SQL.

Propagation:
Creates SQL query.
Uses user input.

===================

Java Source

...

===================

Relevant Documentation

...

===================

Return JSON















Best approach :
before analyzing a line in this graph we should store the whole line till the leaf and then analyze by querying and add to the prompt.
handling graph using dsa approaches and structures
