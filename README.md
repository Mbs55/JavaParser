1-Get the cp.txt(dependencies of the project)
*use this command on the project:
*"mvn --% dependency:build-classpath -Dmdep.outputFile=cp.txt" 
(For A Spring Boot app you should install the dependecies ,demoApp can't be resolved without it)
2-Pass the Root of the project in a post request
3-To run the app:
mvn spring-boot:run
