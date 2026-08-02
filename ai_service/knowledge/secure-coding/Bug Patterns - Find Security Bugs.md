---
source: Bug Patterns   Find Security Bugs
---

# Bug Patterns   Find Security Bugs

Bug Patterns - Find Security Bugs
    
    


    
    

    
    
    
    
    

    








    


        {}Find Security Bugs

        
            
        

        

            

                
Home

                

                    How To 
                    

                        
Use the plugin with..

                        
Maven

                        
Eclipse

                        
NetBeans

                        
IntelliJ

                        
Jenkins

                        
Sonar

                        


                        
Knowledge base

                        
Getting started in security

                    

                

                
Bug Patterns

                
Download

            

            

                
License

            

        

    











    


        
  Bugs Patterns


        
The complete list of descriptions given when FindBugs identify potential weaknesses.


    









    

        



            
Table of Contents


            

                
                    Display / Hide
                
            

            

                


                    

                        
                        

                            Predictable pseudorandom number generator (PREDICTABLE_RANDOM)
                        

                        
                        

                            Predictable pseudorandom number generator (Scala) (PREDICTABLE_RANDOM_SCALA)
                        

                        
                        

                            Untrusted servlet parameter (SERVLET_PARAMETER)
                        

                        
                        

                            Untrusted Content-Type header (SERVLET_CONTENT_TYPE)
                        

                        
                        

                            Untrusted Hostname header (SERVLET_SERVER_NAME)
                        

                        
                        

                            Untrusted session cookie value (SERVLET_SESSION_ID)
                        

                        
                        

                            Untrusted query string (SERVLET_QUERY_STRING)
                        

                        
                        

                            HTTP headers untrusted (SERVLET_HEADER)
                        

                        
                        

                            Untrusted Referer header (SERVLET_HEADER_REFERER)
                        

                        
                        

                            Untrusted User-Agent header (SERVLET_HEADER_USER_AGENT)
                        

                        
                        

                            Potentially sensitive data in a cookie (COOKIE_USAGE)
                        

                        
                        

                            Potential Path Traversal (file read) (PATH_TRAVERSAL_IN)
                        

                        
                        

                            Potential Path Traversal (file write) (PATH_TRAVERSAL_OUT)
                        

                        
                        

                            Potential Path Traversal using Scala API (file read) (SCALA_PATH_TRAVERSAL_IN)
                        

                        
                        

                            Potential Command Injection (COMMAND_INJECTION)
                        

                        
                        

                            Potential Command Injection (Scala) (SCALA_COMMAND_INJECTION)
                        

                        
                        

                            FilenameUtils not filtering null bytes (WEAK_FILENAMEUTILS)
                        

                        
                        

                            TrustManager that accept any certificates (WEAK_TRUST_MANAGER)
                        

                        
                        

                            HostnameVerifier that accept any signed certificates (WEAK_HOSTNAME_VERIFIER)
                        

                        
                        

                            Found JAX-WS SOAP endpoint (JAXWS_ENDPOINT)
                        

                        
                        

                            Found JAX-RS REST endpoint (JAXRS_ENDPOINT)
                        

                        
                        

                            Found Tapestry page (TAPESTRY_ENDPOINT)
                        

                        
                        

                            Found Wicket WebPage (WICKET_ENDPOINT)
                        

                        
                        

                            MD2, MD4 and MD5 are weak hash functions (WEAK_MESSAGE_DIGEST_MD5)
                        

                        
                        

                            SHA-1 is a weak hash function (WEAK_MESSAGE_DIGEST_SHA1)
                        

                        
                        

                            DefaultHttpClient with default constructor is not compatible with TLS 1.2 (DEFAULT_HTTP_CLIENT)
                        

                        
                        

                            Weak SSLContext (SSL_CONTEXT)
                        

                        
                        

                            Message digest is custom (CUSTOM_MESSAGE_DIGEST)
                        

                        
                        

                            Tainted filename read (FILE_UPLOAD_FILENAME)
                        

                        
                        

                            Regex DOS (ReDOS) (REDOS)
                        

                        
                        

                            XML parsing vulnerable to XXE (XMLStreamReader) (XXE_XMLSTREAMREADER)
                        

                        
                        

                            XML parsing vulnerable to XXE (XPathExpression) (XXE_XPATH)
                        

                        
                        

                            XML parsing vulnerable to XXE (SAXParser) (XXE_SAXPARSER)
                        

                        
                        

                            XML parsing vulnerable to XXE (XMLReader) (XXE_XMLREADER)
                        

                        
                        

                            XML parsing vulnerable to XXE (DocumentBuilder) (XXE_DOCUMENT)
                        

                        
                        

                            XML parsing vulnerable to XXE (TransformerFactory) (XXE_DTD_TRANSFORM_FACTORY)
                        

                        
                        

                            XSLT parsing vulnerable to XXE (TransformerFactory) (XXE_XSLT_TRANSFORM_FACTORY)
                        

                        
                        

                            XML schema processing vulnerable to XXE (XXE_SCHEMA_FACTORY)
                        

                        
                        

                            XML validation vulnerable to XXE (XXE_VALIDATOR)
                        

                        
                        

                            Potential XPath Injection (XPATH_INJECTION)
                        

                        
                        

                            Found Struts 1 endpoint (STRUTS1_ENDPOINT)
                        

                        
                        

                            Found Struts 2 endpoint (STRUTS2_ENDPOINT)
                        

                        
                        

                            Found Spring endpoint (SPRING_ENDPOINT)
                        

                        
                        

                            Spring CSRF protection disabled (SPRING_CSRF_PROTECTION_DISABLED)
                        

                        
                        

                            Spring CSRF unrestricted RequestMapping (SPRING_CSRF_UNRESTRICTED_REQUEST_MAPPING)
                        

                        
                        

                            Potential injection (custom) (CUSTOM_INJECTION)
                        

                        
                        

                            Potential SQL Injection (SQL_INJECTION)
                        

                        
                        

                            Potential SQL Injection with Turbine (SQL_INJECTION_TURBINE)
                        

                        
                        

                            Potential SQL/HQL Injection (Hibernate) (SQL_INJECTION_HIBERNATE)
                        

                        
                        

                            Potential SQL/JDOQL Injection (JDO) (SQL_INJECTION_JDO)
                        

                        
                        

                            Potential SQL/JPQL Injection (JPA) (SQL_INJECTION_JPA)
                        

                        
                        

                            Potential JDBC Injection (Spring JDBC) (SQL_INJECTION_SPRING_JDBC)
                        

                        
                        

                            Potential JDBC Injection (SQL_INJECTION_JDBC)
                        

                        
                        

                            Potential Scala Slick Injection (SCALA_SQL_INJECTION_SLICK)
                        

                        
                        

                            Potential Scala Anorm Injection (SCALA_SQL_INJECTION_ANORM)
                        

                        
                        

                            Potential SQL Injection with Vert.x Sql Client (SQL_INJECTION_VERTX)
                        

                        
                        

                            Potential Android SQL Injection (SQL_INJECTION_ANDROID)
                        

                        
                        

                            Potential LDAP Injection (LDAP_INJECTION)
                        

                        
                        

                            Potential code injection when using Script Engine (SCRIPT_ENGINE_INJECTION)
                        

                        
                        

                            Potential code injection when using Spring Expression (SPEL_INJECTION)
                        

                        
                        

                            Potential code injection when using Expression Language (EL) (EL_INJECTION)
                        

                        
                        

                            Potential code injection in Seam logging call (SEAM_LOG_INJECTION)
                        

                        
                        

                            Potential code injection when using OGNL expression (OGNL_INJECTION)
                        

                        
                        

                            Potential code injection when using GroovyShell (GROOVY_SHELL)
                        

                        
                        

                            Potential HTTP Response Splitting (HTTP_RESPONSE_SPLITTING)
                        

                        
                        

                            Potential CRLF Injection for logs (CRLF_INJECTION_LOGS)
                        

                        
                        

                            Potential external control of configuration (EXTERNAL_CONFIG_CONTROL)
                        

                        
                        

                            Bad hexadecimal concatenation (BAD_HEXA_CONVERSION)
                        

                        
                        

                            Hazelcast symmetric encryption (HAZELCAST_SYMMETRIC_ENCRYPTION)
                        

                        
                        

                            NullCipher is insecure (NULL_CIPHER)
                        

                        
                        

                            Unencrypted Socket (UNENCRYPTED_SOCKET)
                        

                        
                        

                            Unencrypted Server Socket (UNENCRYPTED_SERVER_SOCKET)
                        

                        
                        

                            DES is insecure (DES_USAGE)
                        

                        
                        

                            DESede is insecure (TDES_USAGE)
                        

                        
                        

                            RSA with no padding is insecure (RSA_NO_PADDING)
                        

                        
                        

                            Hard coded password (HARD_CODE_PASSWORD)
                        

                        
                        

                            Hard coded key (HARD_CODE_KEY)
                        

                        
                        

                            Unsafe hash equals (UNSAFE_HASH_EQUALS)
                        

                        
                        

                            Struts Form without input validation (STRUTS_FORM_VALIDATION)
                        

                        
                        

                            XSSRequestWrapper is a weak XSS protection (XSS_REQUEST_WRAPPER)
                        

                        
                        

                            Blowfish usage with short key (BLOWFISH_KEY_SIZE)
                        

                        
                        

                            RSA usage with short key (RSA_KEY_SIZE)
                        

                        
                        

                            Unvalidated Redirect (UNVALIDATED_REDIRECT)
                        

                        
                        

                            Unvalidated Redirect (Play Framework) (PLAY_UNVALIDATED_REDIRECT)
                        

                        
                        

                            Spring Unvalidated Redirect (SPRING_UNVALIDATED_REDIRECT)
                        

                        
                        

                            Unexpected property leak (ENTITY_LEAK)
                        

                        
                        

                            Mass assignment (ENTITY_MASS_ASSIGNMENT)
                        

                        
                        

                            Dynamic JSP inclusion (JSP_INCLUDE)
                        

                        
                        

                            Dynamic variable in Spring expression (JSP_SPRING_EVAL)
                        

                        
                        

                            Escaping of special XML characters is disabled (JSP_JSTL_OUT)
                        

                        
                        

                            Potential XSS in JSP (XSS_JSP_PRINT)
                        

                        
                        

                            Potential XSS in Servlet (XSS_SERVLET)
                        

                        
                        

                            XMLDecoder usage (XML_DECODER)
                        

                        
                        

                            Static IV (STATIC_IV)
                        

                        
                        

                            ECB mode is insecure (ECB_MODE)
                        

                        
                        

                            Cipher is susceptible to Padding Oracle (PADDING_ORACLE)
                        

                        
                        

                            Cipher with no integrity (CIPHER_INTEGRITY)
                        

                        
                        

                            Use of ESAPI Encryptor (ESAPI_ENCRYPTOR)
                        

                        
                        

                            External file access (Android) (ANDROID_EXTERNAL_FILE_ACCESS)
                        

                        
                        

                            Broadcast (Android) (ANDROID_BROADCAST)
                        

                        
                        

                            World writable file (Android) (ANDROID_WORLD_WRITABLE)
                        

                        
                        

                            WebView with geolocation activated (Android) (ANDROID_GEOLOCATION)
                        

                        
                        

                            WebView with JavaScript enabled (Android) (ANDROID_WEB_VIEW_JAVASCRIPT)
                        

                        
                        

                            WebView with JavaScript interface (Android) (ANDROID_WEB_VIEW_JAVASCRIPT_INTERFACE)
                        

                        
                        

                            Cookie without the secure flag (INSECURE_COOKIE)
                        

                        
                        

                            Cookie without the HttpOnly flag (HTTPONLY_COOKIE)
                        

                        
                        

                            Object deserialization is used (OBJECT_DESERIALIZATION)
                        

                        
                        

                            Unsafe Jackson deserialization configuration (JACKSON_UNSAFE_DESERIALIZATION)
                        

                        
                        

                            This class could be used as deserialization gadget (DESERIALIZATION_GADGET)
                        

                        
                        

                            Trust Boundary Violation (TRUST_BOUNDARY_VIOLATION)
                        

                        
                        

                            A malicious XSLT could be provided to the JSP tag (JSP_XSLT)
                        

                        
                        

                            A malicious XSLT could be provided (MALICIOUS_XSLT)
                        

                        
                        

                            Potential information leakage in Scala Play (SCALA_SENSITIVE_DATA_EXPOSURE)
                        

                        
                        

                            Scala Play Server-Side Request Forgery (SSRF) (SCALA_PLAY_SSRF)
                        

                        
                        

                            URLConnection Server-Side Request Forgery (SSRF) and File Disclosure (URLCONNECTION_SSRF_FD)
                        

                        
                        

                            Potential XSS in Scala Twirl template engine (SCALA_XSS_TWIRL)
                        

                        
                        

                            Potential XSS in Scala MVC API engine (SCALA_XSS_MVC_API)
                        

                        
                        

                            Potential template injection with Velocity (TEMPLATE_INJECTION_VELOCITY)
                        

                        
                        

                            Potential template injection with Freemarker (TEMPLATE_INJECTION_FREEMARKER)
                        

                        
                        

                            Potential template injection with Pebble (TEMPLATE_INJECTION_PEBBLE)
                        

                        
                        

                            Overly permissive CORS policy (PERMISSIVE_CORS)
                        

                        
                        

                            Anonymous LDAP bind (LDAP_ANONYMOUS)
                        

                        
                        

                            LDAP Entry Poisoning (LDAP_ENTRY_POISONING)
                        

                        
                        

                            Persistent Cookie Usage (COOKIE_PERSISTENT)
                        

                        
                        

                            URL rewriting method (URL_REWRITING)
                        

                        
                        

                            Insecure SMTP SSL connection (INSECURE_SMTP_SSL)
                        

                        
                        

                            AWS Query Injection (AWS_QUERY_INJECTION)
                        

                        
                        

                            JavaBeans Property Injection (BEAN_PROPERTY_INJECTION)
                        

                        
                        

                            Struts File Disclosure (STRUTS_FILE_DISCLOSURE)
                        

                        
                        

                            Spring File Disclosure (SPRING_FILE_DISCLOSURE)
                        

                        
                        

                            RequestDispatcher File Disclosure (REQUESTDISPATCHER_FILE_DISCLOSURE)
                        

                        
                        

                            Format String Manipulation (FORMAT_STRING_MANIPULATION)
                        

                        
                        

                            HTTP Parameter Pollution (HTTP_PARAMETER_POLLUTION)
                        

                        
                        

                            Information Exposure Through An Error Message (INFORMATION_EXPOSURE_THROUGH_AN_ERROR_MESSAGE)
                        

                        
                        

                            SMTP Header Injection (SMTP_HEADER_INJECTION)
                        

                        
                        

                            Enabling extensions in Apache XML RPC server or client. (RPC_ENABLED_EXTENSIONS)
                        

                        
                        

                            Disabling HTML escaping put the application at risk for XSS (WICKET_XSS1)
                        

                        
                        

                            Ignoring XML comments in SAML may lead to authentication bypass (SAML_IGNORE_COMMENTS)
                        

                        
                        

                            Overly permissive file permission (OVERLY_PERMISSIVE_FILE_PERMISSION)
                        

                        
                        

                            Improper handling of Unicode transformations (IMPROPER_UNICODE)
                        

                        
                        

                            String is modified after validation and not before it (MODIFICATION_AFTER_VALIDATION)
                        

                        
                        

                            String is normalized after validation and not before it (NORMALIZATION_AFTER_VALIDATION)
                        

                        
                        

                            Dangerous combination of permissions granted (DANGEROUS_PERMISSION_COMBINATION)
                        

                        
                        

                            An unsafe string is potentially injected into an XML string (POTENTIAL_XML_INJECTION)
                        

                        
                    

                

            


    
    

        
        

            Predictable pseudorandom number generator
            
        

        
Bug Pattern: PREDICTABLE_RANDOM


        
            

The use of a predictable random value can lead to vulnerabilities when used in certain security critical contexts. For example, when the value is used as:




a CSRF token: a predictable token can lead to a CSRF attack as an attacker will know the value of the token


a password reset token (sent by email): a predictable password token can lead to an account takeover, since an attacker will guess the URL of the "change password" form


any other secret value





A quick fix could be to replace the use of java.util.Random with something stronger, such as java.security.SecureRandom.




Vulnerable Code:


String generateSecretToken() {
    Random r = new Random();
    return Long.toHexString(r.nextLong());
}





Solution:

import org.apache.commons.codec.binary.Hex;

String generateSecretToken() {
    SecureRandom secRandom = new SecureRandom();

    byte[] result = new byte[32];
    secRandom.nextBytes(result);
    return Hex.encodeHexString(result);
}







References

Cracking Random Number Generators - Part 1 (https://jazzy.id.au)

CERT: MSC02-J. Generate strong random numbers

CWE-330: Use of Insufficiently Random Values

Predicting Struts CSRF Token (Example of real-life vulnerability and exploitation)



        

        

        

    

    
    

        
        

            Predictable pseudorandom number generator (Scala)
            
        

        
Bug Pattern: PREDICTABLE_RANDOM_SCALA


        
            

The use of a predictable random value can lead to vulnerabilities when used in certain security critical contexts. For example, when the value is used as:




a CSRF token: a predictable token can lead to a CSRF attack as an attacker will know the value of the token


a password reset token (sent by email): a predictable password token can lead to an account takeover, since an attacker will guess the URL of the "change password" form


any other secret value





A quick fix could be to replace the use of java.util.Random with something stronger, such as java.security.SecureRandom.




Vulnerable Code:


import scala.util.Random

def generateSecretToken() {
    val result = Seq.fill(16)(Random.nextInt)
    return result.map("%02x" format _).mkString
}





    Solution:

import java.security.SecureRandom

def generateSecretToken() {
    val rand = new SecureRandom()
    val value = Array.ofDim[Byte](16)
    rand.nextBytes(value)
    return value.map("%02x" format _).mkString
}








References

Cracking Random Number Generators - Part 1 (http://jazzy.id.au)

CERT: MSC02-J. Generate strong random numbers

CWE-330: Use of Insufficiently Random Values

Predicting Struts CSRF Token (Example of real-life vulnerability and exploitation)



        

        

        

    

    
    

        
        

            Untrusted servlet parameter
            
        

        
Bug Pattern: SERVLET_PARAMETER


        
            

The Servlet can read GET and POST parameters from various methods. The value obtained should be considered unsafe.
You may need to validate or sanitize those values before passing them to sensitive APIs such as:




SQL query (May leads to SQL injection)


File opening (May leads to path traversal)


Command execution (Potential Command injection)


HTML construction (Potential XSS)


etc...








Reference

CWE-20: Improper Input Validation



        

        

        

    

    
    

        
        

            Untrusted Content-Type header
            
        

        
Bug Pattern: SERVLET_CONTENT_TYPE


        
            


The HTTP header Content-Type can be controlled by the client. As such, its value should not be used in any security critical decisions.






Reference

CWE-807: Untrusted Inputs in a Security Decision



        

        

        

    

    
    

        
        

            Untrusted Hostname header
            
        

        
Bug Pattern: SERVLET_SERVER_NAME


        
            

The hostname header can be controlled by the client. As such, its value should not be used in any security critical decisions.
Both ServletRequest.getServerName() and HttpServletRequest.getHeader("Host") have the same
behavior which is to extract the Host header.

GET /testpage HTTP/1.1
Host: www.example.com
[...]


The web container serving your application may redirect requests to your application by default. This would allow
a malicious user to place any value in the Host header. It is recommended that you do not trust this value in any security
decisions you make with respect to a request.






Reference

CWE-807: Untrusted Inputs in a Security Decision



        

        

        

    

    
    

        
        

            Untrusted session cookie value
            
        

        
Bug Pattern: SERVLET_SESSION_ID


        
            


The method HttpServletRequest.getRequestedSessionId()
typically returns the value of the cookie JSESSIONID. This value is normally only accessed by the session management logic and not normal developer code.




The value passed to the client is generally an alphanumeric value (e.g., JSESSIONID=jp6q31lq2myn). However, the value can be altered by the client.
The following HTTP request illustrates the potential modification.

GET /somePage HTTP/1.1
Host: yourwebsite.com
User-Agent: Mozilla/5.0
Cookie: JSESSIONID=Any value of the user's choice!!??'''">





As such, the JSESSIONID should only be used to see if its value matches an existing session ID. If it does not, the user should be
considered an unauthenticated user. In addition, the session ID value should never be logged. If it is, then the log file could contain
valid active session IDs, allowing an insider to hijack any sessions whose IDs have been logged and are still active.






References

OWASP: Session Management Cheat Sheet

CWE-20: Improper Input Validation




        

        

        

    

    
    

        
        

            Untrusted query string
            
        

        
Bug Pattern: SERVLET_QUERY_STRING


        
            

The query string is the concatenation of the GET parameter names and values. Parameters other than those intended can
be passed in.


For the URL request /app/servlet.htm?a=1&b=2, the query string extract will be a=1&b=2


Just as is true for individual parameter values retrieved via methods like HttpServletRequest.getParameter(),
the value obtained from HttpServletRequest.getQueryString() should be considered unsafe.
You may need to validate or sanitize anything pulled from the query string before passing it to sensitive APIs.






Reference

CWE-20: Improper Input Validation



        

        

        

    

    
    

        
        

            HTTP headers untrusted
            
        

        
Bug Pattern: SERVLET_HEADER


        
            

Request headers can easily be altered by the requesting user. In general, no assumption should be made that
the request came from a regular browser without modification by an attacker. As such, it is recommended that you
not trust this value in any security decisions you make with respect to a request.





Reference

CWE-807: Untrusted Inputs in a Security Decision



        

        

        

    

    
    

        
        

            Untrusted Referer header
            
        

        
Bug Pattern: SERVLET_HEADER_REFERER


        
            


Behavior:




Any value can be assigned to this header if the request is coming from a malicious user.


The "Referer" will not be present if the request was initiated from another origin that is secure (HTTPS).








Recommendations:




No access control should be based on the value of this header.


No CSRF protection should be based only on this value (because it is optional).










Reference

CWE-807: Untrusted Inputs in a Security Decision



        

        

        

    

    
    

        
        

            Untrusted User-Agent header
            
        

        
Bug Pattern: SERVLET_HEADER_USER_AGENT


        
            

The header "User-Agent" can easily be spoofed by the client. Adopting different behaviors based on the User-Agent (for
crawler UA) is not recommended.





Reference

CWE-807: Untrusted Inputs in a Security Decision



        

        

        

    

    
    

        
        

            Potentially sensitive data in a cookie
            
        

        
Bug Pattern: COOKIE_USAGE


        
            

The information stored in a custom cookie should not be sensitive or related to the session. In most cases, sensitive data should only be stored in session
and referenced by the user's session cookie. See HttpSession (HttpServletRequest.getSession())


Custom cookies can be used for information that needs to live longer than and is independent of a specific session.





Reference

CWE-315: Cleartext Storage of Sensitive Information in a Cookie



        

        

        

    

    
    

        
        

            Potential Path Traversal (file read)
            
        

        
Bug Pattern: PATH_TRAVERSAL_IN


        
            

A file is opened to read its content. The filename comes from an input parameter.
If an unfiltered parameter is passed to this file API, files from an arbitrary filesystem location could be read.


This rule identifies potential path traversal vulnerabilities. In many cases, the constructed file path cannot be controlled
by the user. If that is the case, the reported instance is a false positive.






    Vulnerable Code:


@GET
@Path("/images/{image}")
@Produces("images/*")
public Response getImage(@javax.ws.rs.PathParam("image") String image) {
    File file = new File("resources/images/", image); //Weak point

    if (!file.exists()) {
        return Response.status(Status.NOT_FOUND).build();
    }

    return Response.ok().entity(new FileInputStream(file)).build();
}








    Solution:


import org.apache.commons.io.FilenameUtils;

@GET
@Path("/images/{image}")
@Produces("images/*")
public Response getImage(@javax.ws.rs.PathParam("image") String image) {
    File file = new File("resources/images/", FilenameUtils.getName(image)); //Fix

    if (!file.exists()) {
        return Response.status(Status.NOT_FOUND).build();
    }

    return Response.ok().entity(new FileInputStream(file)).build();
}







References

WASC: Path Traversal

OWASP: Path Traversal

CAPEC-126: Path Traversal

CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')



        

        

        

    

    
    

        
        

            Potential Path Traversal (file write)
            
        

        
Bug Pattern: PATH_TRAVERSAL_OUT


        
            

A file is opened to write to its contents. The filename comes from an input parameter.
If an unfiltered parameter is passed to this file API, files at an arbitrary filesystem location could be modified.


This rule identifies potential path traversal vulnerabilities. In many cases, the constructed file path cannot be controlled
by the user. If that is the case, the reported instance is a false positive.





References

WASC-33: Path Traversal

OWASP: Path Traversal

CAPEC-126: Path Traversal

CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')



        

        

        

    

    
    

        
        

            Potential Path Traversal using Scala API (file read)
            
        

        
Bug Pattern: SCALA_PATH_TRAVERSAL_IN


        
            

A file is opened to read its content. The filename comes from an input parameter.
If an unfiltered parameter is passed to this file API, files from an arbitrary filesystem location could be read.


This rule identifies potential path traversal vulnerabilities. In many cases, the constructed file path cannot be controlled
by the user. If that is the case, the reported instance is a false positive.






    Vulnerable Code:


def getWordList(value:String) = Action {
  if (!Files.exists(Paths.get("public/lists/" + value))) {
    NotFound("File not found")
  } else {
    val result = Source.fromFile("public/lists/" + value).getLines().mkString // Weak point
    Ok(result)
  }
}








    Solution:


import org.apache.commons.io.FilenameUtils;

def getWordList(value:String) = Action {
  val filename = "public/lists/" + FilenameUtils.getName(value)

  if (!Files.exists(Paths.get(filename))) {
    NotFound("File not found")
  } else {
    val result = Source.fromFile(filename).getLines().mkString // Fix
    Ok(result)
  }
}







References

WASC: Path Traversal

OWASP: Path Traversal

CAPEC-126: Path Traversal

CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')



        

        

        

    

    
    

        
        

            Potential Command Injection
            
        

        
Bug Pattern: COMMAND_INJECTION


        
            

The highlighted API is used to execute a system command. If unfiltered input is passed to this API, it can lead to arbitrary command execution.





    Vulnerable Code:


import java.lang.Runtime;

Runtime r = Runtime.getRuntime();
r.exec("/bin/sh -c some_tool" + input);





References

OWASP: Command Injection

OWASP: Top 10 2013-A1-Injection

CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')



        

        

        

    

    
    

        
        

            Potential Command Injection (Scala)
            
        

        
Bug Pattern: SCALA_COMMAND_INJECTION


        
            

The highlighted API is used to execute a system command. If unfiltered input is passed to this API, it can lead to arbitrary command execution.





    Vulnerable Code:


def executeCommand(value:String) = Action {
    val result = value.!
    Ok("Result:\n"+result)
}





References

OWASP: Command Injection

OWASP: Top 10 2013-A1-Injection

CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')



        

        

        

    

    
    

        
        

            FilenameUtils not filtering null bytes
            
        

        
Bug Pattern: WEAK_FILENAMEUTILS


        
            

Some FilenameUtils' methods don't filter NULL bytes (0x00).


If a null byte is injected into a filename, if this filename is passed to the underlying OS, the file retrieved will be the
name of the file that is specified prior to the NULL byte, since at the OS level, all strings are terminated by a null byte even
though Java itself doesn't care about null bytes or treat them special. This OS behavior can be used to bypass filename validation
that looks at the end of the filename (e.g., ends with ".log") to make sure it's a safe file to access.


To fix this, two things are recommended:




Upgrade to Java 7 update 40 or later, or Java 8+ since
NULL byte injection in filenames is fixed in those versions.


Strongly validate any filenames provided by untrusted users to make sure they are valid (i.e., don't contain null, don't include path characters, etc).




If you know you are using a modern version of Java immune to NULL byte injection, you can probably disable this rule.






References

WASC-28: Null Byte Injection

CWE-158: Improper Neutralization of Null Byte or NUL Character



        

        

        

    

    
    

        
        

            TrustManager that accept any certificates
            
        

        
Bug Pattern: WEAK_TRUST_MANAGER


        
            

Empty TrustManager implementations are often used to connect easily to a host that is not signed by a root
certificate authority. As a consequence, this is vulnerable to
Man-in-the-middle attacks
since the client will trust any certificate.




A TrustManager allowing specific certificates (based on a TrustStore for example) should be built.
Detailed information for a proper implementation is available at:
[1]
[2]






    Vulnerable Code:


class TrustAllManager implements X509TrustManager {

    @Override
    public void checkClientTrusted(X509Certificate[] x509Certificates, String s) throws CertificateException {
        //Trust any client connecting (no certificate validation)
    }

    @Override
    public void checkServerTrusted(X509Certificate[] x509Certificates, String s) throws CertificateException {
        //Trust any remote server (no certificate validation)
    }

    @Override
    public X509Certificate[] getAcceptedIssuers() {
        return null;
    }
}







    Solution (TrustMangager based on a keystore):


KeyStore ks = //Load keystore containing the certificates trusted

SSLContext sc = SSLContext.getInstance("TLS");

TrustManagerFactory tmf = TrustManagerFactory.getInstance("SunX509");
tmf.init(ks);

sc.init(kmf.getKeyManagers(), tmf.getTrustManagers(),null);








References

WASC-04: Insufficient Transport Layer Protection

CWE-295: Improper Certificate Validation



        

        

        

    

    
    

        
        

            HostnameVerifier that accept any signed certificates
            
        

        
Bug Pattern: WEAK_HOSTNAME_VERIFIER


        
            

A HostnameVerifier that accept any host are often use because of certificate reuse on many hosts.
As a consequence, this is vulnerable to
Man-in-the-middle attacks
since the client will trust any certificate.




A TrustManager allowing specific certificates (based on a truststore for example) should be built.
Wildcard certificates should be created for reused on multiples subdomains.
Detailed information for a proper implementation is available at:
[1]
[2]






    Vulnerable Code:


public class AllHosts implements HostnameVerifier {
    public boolean verify(final String hostname, final SSLSession session) {
        return true;
    }
}







    Solution (TrustManager based on a keystore):


KeyStore ks = //Load keystore containing the certificates trusted

SSLContext sc = SSLContext.getInstance("TLS");

TrustManagerFactory tmf = TrustManagerFactory.getInstance("SunX509");
tmf.init(ks);

sc.init(kmf.getKeyManagers(), tmf.getTrustManagers(),null);








References

WASC-04: Insufficient Transport Layer Protection

CWE-295: Improper Certificate Validation



        

        

        

    

    
    

        
        

            Found JAX-WS SOAP endpoint
            
        

        
Bug Pattern: JAXWS_ENDPOINT


        
            

This method is part of a SOAP Web Service (JSR224).



The security of this web service should be analyzed. For example:




Authentication, if enforced, should be tested.


Access control, if enforced, should be tested.


The inputs should be tracked for potential vulnerabilities.


The communication should ideally be over SSL.










References

OWASP: Web Service Security Cheat Sheet

CWE-20: Improper Input Validation



        

        

        

    

    
    

        
        

            Found JAX-RS REST endpoint
            
        

        
Bug Pattern: JAXRS_ENDPOINT


        
            

This method is part of a REST Web Service (JSR311).



The security of this web service should be analyzed. For example:




Authentication, if enforced, should be tested.


Access control, if enforced, should be tested.


The inputs should be tracked for potential vulnerabilities.


The communication should ideally be over SSL.


If the service supports writes (e.g., via POST), its vulnerability to CSRF should be investigated.[1]










References

OWASP: REST Assessment Cheat Sheet

OWASP: REST Security Cheat Sheet

OWASP: Web Service Security Cheat Sheet

1. OWASP: Cross-Site Request Forgery

OWASP: CSRF Prevention Cheat Sheet

CWE-20: Improper Input Validation



        

        

        

    

    
    

        
        

            Found Tapestry page
            
        

        
Bug Pattern: TAPESTRY_ENDPOINT


        
            

A Tapestry endpoint was discovered at application startup. Tapestry apps are structured with a backing Java class and a corresponding
Tapestry Markup Language page (a .tml file) for each page. When a request is received, the GET/POST parameters are mapped to specific
inputs in the backing Java class. The mapping is either done with field name:


    [...]
    protected String input;
    [...]


or the definition of an explicit annotation:



    [...]
    @org.apache.tapestry5.annotations.Parameter
    protected String parameter1;

    @org.apache.tapestry5.annotations.Component(id = "password")
    private PasswordField passwordField;
    [...]


The page is mapped to the view /resources/package/PageName.tml.


Each Tapestry page in this application should be researched to make sure all inputs that are automatically
mapped in this way are properly validated before they are used.





References

Apache Tapestry Home Page

CWE-20: Improper Input Validation



        

        

        

    

    
    

        
        

            Found Wicket WebPage
            
        

        
Bug Pattern: WICKET_ENDPOINT


        
            

This class represents a Wicket WebPage. Input is automatically read from a PageParameters instance passed to the constructor.
The current page is mapped to the view /package/WebPageName.html.


Each Wicket page in this application should be researched to make sure all inputs that are automatically
mapped in this way are properly validated before they are used.





References

Apache Wicket Home Page

CWE-20: Improper Input Validation



        

        

        

    

    
    

        
        

            MD2, MD4 and MD5 are weak hash functions
            
        

        
Bug Pattern: WEAK_MESSAGE_DIGEST_MD5


        
            

The algorithms MD2, MD4 and MD5 are not a recommended MessageDigest. PBKDF2 should be used to hash password for example.



    "The security of the MD5 hash function is severely compromised. A collision attack exists that can find collisions
    within seconds on a computer with a 2.6 GHz Pentium 4 processor (complexity of 224.1).[1] Further, there is also a
    chosen-prefix collision attack that can produce a collision for two inputs with specified prefixes within hours, using
    off-the-shelf computing hardware (complexity 239).[2]"

    - Wikipedia: MD5 - Security



    "SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, and SHA-512/256:

    The use of these hash functions is acceptable for all hash function applications."

    - NIST: Transitioning the Use of Cryptographic Algorithms and Key Lengths p.15


    "The main idea of a PBKDF is to slow dictionary or brute force attacks on the passwords by increasing the time
    needed to test each password. An attacker with a list of likely passwords can evaluate the PBKDF using the known
    iteration counter and the salt. Since an attacker has to spend a significant amount of computing time for each try,
    it becomes harder to apply the dictionary or brute force attacks."

- NIST: Recommendation for Password-Based Key Derivation  p.12





    Vulnerable Code:

    
MessageDigest md5Digest = MessageDigest.getInstance("MD5");
    md5Digest.update(password.getBytes());
    byte[] hashValue = md5Digest.digest();
    

    byte[] hashValue = DigestUtils.getMd5Digest().digest(password.getBytes());







    Solution (Using bouncy castle):

    
public static byte[] getEncryptedPassword(String password, byte[] salt) throws NoSuchAlgorithmException, InvalidKeySpecException {
    PKCS5S2ParametersGenerator gen = new PKCS5S2ParametersGenerator(new SHA256Digest());
    gen.init(password.getBytes("UTF-8"), salt.getBytes(), 4096);
    return ((KeyParameter) gen.generateDerivedParameters(256)).getKey();
}
    

    Solution (Java 8 and later):

    public static byte[] getEncryptedPassword(String password, byte[] salt) throws NoSuchAlgorithmException, InvalidKeySpecException {
    KeySpec spec = new PBEKeySpec(password.toCharArray(), salt, 4096, 256 * 8);
    SecretKeyFactory f = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
    return f.generateSecret(spec).getEncoded();
}







References

[1] On Collisions for MD5: Master Thesis by M.M.J. Stevens

[2] Chosen-prefix collisions for MD5 and applications: Paper written by Marc Stevens

Wikipedia: MD5

NIST: Transitioning the Use of Cryptographic Algorithms and Key Lengths

NIST: Recommendation for Password-Based Key Derivation

Stackoverflow: Reliable implementation of PBKDF2-HMAC-SHA256 for Java

CWE-327: Use of a Broken or Risky Cryptographic Algorithm
CWE-328: Use of Weak Hash



        

        

        

    

    
    

        
        

            SHA-1 is a weak hash function
            
        

        
Bug Pattern: WEAK_MESSAGE_DIGEST_SHA1


        
            

The algorithms SHA-1 is not a recommended algorithm for hash password, for signature verification and other
uses. PBKDF2 should be used to hash password for example.



    "SHA-1 for digital signature generation:

    SHA-1 may only be used for digital signature generation where specifically allowed by NIST protocol-specific guidance.
    For all other applications, SHA-1 shall not be used for digital signature generation.

    SHA-1 for digital signature verification:

    For digital signature verification, SHA-1 is allowed for legacy-use.

    [...]

    SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, and SHA-512/256:

    The use of these hash functions is acceptable for all hash function applications."

    - NIST: Transitioning the Use of Cryptographic Algorithms and Key Lengths p.15


    "The main idea of a PBKDF is to slow dictionary or brute force attacks on the passwords by increasing the time
    needed to test each password. An attacker with a list of likely passwords can evaluate the PBKDF using the known
    iteration counter and the salt. Since an attacker has to spend a significant amount of computing time for each try,
    it becomes harder to apply the dictionary or brute force attacks."

- NIST: Recommendation for Password-Based Key Derivation  p.12






    Vulnerable Code:

    
MessageDigest sha1Digest = MessageDigest.getInstance("SHA1");
    sha1Digest.update(password.getBytes());
    byte[] hashValue = sha1Digest.digest();
    

    byte[] hashValue = DigestUtils.getSha1Digest().digest(password.getBytes());







    Solution (Using bouncy castle):

    
public static byte[] getEncryptedPassword(String password, byte[] salt) throws NoSuchAlgorithmException, InvalidKeySpecException {
    PKCS5S2ParametersGenerator gen = new PKCS5S2ParametersGenerator(new SHA256Digest());
    gen.init(password.getBytes("UTF-8"), salt.getBytes(), 4096);
    return ((KeyParameter) gen.generateDerivedParameters(256)).getKey();
}
    

    Solution (Java 8 and later):

    public static byte[] getEncryptedPassword(String password, byte[] salt) throws NoSuchAlgorithmException, InvalidKeySpecException {
    KeySpec spec = new PBEKeySpec(password.toCharArray(), salt, 4096, 256 * 8);
    SecretKeyFactory f = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
    return f.generateSecret(spec).getEncoded();
}







References

Qualys blog: SHA1 Deprecation: What You Need to Know

Google Online Security Blog: Gradually sunsetting SHA-1

NIST: Transitioning the Use of Cryptographic Algorithms and Key Lengths

NIST: Recommendation for Password-Based Key Derivation

Stackoverflow: Reliable implementation of PBKDF2-HMAC-SHA256 for Java

CWE-327: Use of a Broken or Risky Cryptographic Algorithm
CWE-328: Use of Weak Hash



        

        

        

    

    
    

        
        

            DefaultHttpClient with default constructor is not compatible with TLS 1.2
            
        

        
Bug Pattern: DEFAULT_HTTP_CLIENT


        
            


    Vulnerable Code:


HttpClient client = new DefaultHttpClient();







Solution:


Upgrade your implementation to use one of the recommended constructs and configure https.protocols JVM option to include TLSv1.2:







  
Use SystemDefaultHttpClient instead



    Sample Code:


HttpClient client = new SystemDefaultHttpClient();



  
Create an HttpClient based on SSLSocketFactory - get an SSLScoketFactory instance with getSystemSocketFactory() and use this instance for HttpClient creation

  
Create an HttpClient based on SSLConnectionSocketFactory - get an instance with getSystemSocketFactory() and use this instance for HttpClient creation

  
Use HttpClientBuilder - call useSystemProperties() before calling build()



    Sample Code:


HttpClient client = HttpClientBuilder.create().useSystemProperties().build();



  
HttpClients - call createSystem() to create an instance



    Sample Code:


HttpClient client = HttpClients.createSystem();













References

Diagnosing TLS, SSL, and HTTPS



        

        

        

    

    
    

        
        

            Weak SSLContext
            
        

        
Bug Pattern: SSL_CONTEXT


        
            


    Vulnerable Code:


    
SSLContext.getInstance("SSL");







Solution:


Upgrade your implementation to the following, and configure https.protocols JVM option to include TLSv1.2:

SSLContext.getInstance("TLS");








References

Diagnosing TLS, SSL, and HTTPS



        

        

        

    

    
    

        
        

            Message digest is custom
            
        

        
Bug Pattern: CUSTOM_MESSAGE_DIGEST


        
            

Implementing a custom MessageDigest is error-prone.


NIST recommends the use of SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, or SHA-512/256.


    "SHA-1 for digital signature generation:

    SHA-1 may only be used for digital signature generation where specifically allowed by NIST protocol-specific guidance.
    For all other applications, SHA-1 shall not be used for digital signature generation.

    SHA-1 for digital signature verification:

    For digital signature verification, SHA-1 is allowed for legacy-use.

    [...]

    SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, and SHA-512/256:

    The use of these hash functions is acceptable for all hash function applications."

    - NIST: Transitioning the Use of Cryptographic Algorithms and Key Lengths p.15



    Vulnerable Code:


MyProprietaryMessageDigest extends MessageDigest {
    @Override
    protected byte[] engineDigest() {
        [...]
        //Creativity is a bad idea
        return [...];
    }
}







Upgrade your implementation to use one of the approved algorithms. Use an algorithm that is sufficiently strong for your specific security needs.



    Example Solution:


MessageDigest sha256Digest = MessageDigest.getInstance("SHA256");
sha256Digest.update(password.getBytes());







References

NIST Approved Hash Functions

CWE-327: Use of a Broken or Risky Cryptographic Algorithm



        

        

        

    

    
    

        
        

            Tainted filename read
            
        

        
Bug Pattern: FILE_UPLOAD_FILENAME


        
            

The filename provided by the FileUpload API can be tampered with by the client to reference unauthorized files.


For example:




"../../../config/overide_file"


"shell.jsp\u0000expected.gif"




Therefore, such values should not be passed directly to the filesystem API. If acceptable, the application should generate its
own file names and use those. Otherwise, the provided filename should be properly validated to ensure it's properly structured,
contains no unauthorized path characters (e.g., / \), and refers to an authorized file.





References

Securiteam: File upload security recommendations

CWE-22: Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')

WASC-33: Path Traversal

OWASP: Path Traversal

CAPEC-126: Path Traversal




        

        

        

    

    
    

        
        

            Regex DOS (ReDOS)
            
        

        
Bug Pattern: REDOS


        
            


    Regular expressions (Regex) are frequently subject to Denial of Service (DOS) attacks (called ReDOS). This is due to the fact that regex engines
    may take a large amount of time when analyzing certain strings, depending on how the regex is defined.



    For example, for the regex: ^(a+)+$, the input "aaaaaaaaaaaaaaaaX" will cause the regex engine to analyze 65536
different paths.[1] Example taken from OWASP references



Therefore, it is possible that a single request may cause a large amount of computation on the server side.
The problem with this regex, and others like it, is that there are two different ways the same input character can be accepted by the
Regex due to the + (or a *) inside the parenthesis, and the + (or a *) outside the parenthesis. The way this is written, either + could
consume the character 'a'. To fix this, the regex should be rewritten to eliminate the ambiguity. For example, this could simply be
rewritten as: ^a+$, which is presumably what the author meant anyway (any number of a's). Assuming that's what the original
regex meant, this new regex can be evaluated quickly, and is not subject to ReDOS.






References

Sebastian Kubeck's Weblog: Detecting and Preventing ReDoS Vulnerabilities

[1] OWASP: Regular expression Denial of Service

CWE-400: Uncontrolled Resource Consumption ('Resource Exhaustion')



        

        

        

    

    
    

        
        

            XML parsing vulnerable to XXE (XMLStreamReader)
            
        

        
Bug Pattern: XXE_XMLSTREAMREADER


        
            


Attack


XML External Entity (XXE) attacks can occur when an XML parser supports XML entities while processing XML received
from an untrusted source.


Risk 1: Expose local file content (XXE: XML External Entity)




<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [
   <!ENTITY xxe SYSTEM "file:///etc/passwd" > ]>
<foo>&xxe;</foo>



Risk 2: Denial of service (XEE: XML Entity Expansion)



<?xml version="1.0"?>
<!DOCTYPE lolz [
 <!ENTITY lol "lol">
 <!ELEMENT lolz (#PCDATA)>
 <!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
 <!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">
 <!ENTITY lol3 "&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;">
[...]
 <!ENTITY lol9 "&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;">
]>
<lolz>&lol9;</lolz>





Solution



In order to avoid exposing dangerous feature of the XML parser, you can do the following change to the code.





Vulnerable Code:




public void parseXML(InputStream input) throws XMLStreamException {

    XMLInputFactory factory = XMLInputFactory.newFactory();
    XMLStreamReader reader = factory.createXMLStreamReader(input);
    [...]
}







The following snippets show two available solutions. You can set one property or both.




Solution disabling External Entities:




public void parseXML(InputStream input) throws XMLStreamException {

    XMLInputFactory factory = XMLInputFactory.newFactory();
    factory.setProperty(XMLInputFactory.IS_SUPPORTING_EXTERNAL_ENTITIES, false);
    XMLStreamReader reader = factory.createXMLStreamReader(input);
    [...]
}





Solution disabling DTD:




public void parseXML(InputStream input) throws XMLStreamException {

    XMLInputFactory factory = XMLInputFactory.newFactory();
    factory.setProperty(XMLInputFactory.SUPPORT_DTD, false);
    XMLStreamReader reader = factory.createXMLStreamReader(input);
    [...]
}







References


CWE-611: Improper Restriction of XML External Entity Reference ('XXE')

CERT: IDS10-J. Prevent XML external entity attacks

OWASP.org: XML External Entity (XXE) Processing

WS-Attacks.org: XML Entity Expansion

WS-Attacks.org: XML External Entity DOS

WS-Attacks.org: XML Entity Reference Attack

Identifying XML External Entity vulnerability (XXE)


JEP 185: Restrict Fetching of External XML Resources



        

        

        

    

    
    

        
        

            XML parsing vulnerable to XXE (XPathExpression)
            
        

        
Bug Pattern: XXE_XPATH


        
            


Attack


XML External Entity (XXE) attacks can occur when an XML parser supports XML entities while processing XML received
from an untrusted source.


Risk 1: Expose local file content (XXE: XML External Entity)




<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [
   <!ENTITY xxe SYSTEM "file:///etc/passwd" > ]>
<foo>&xxe;</foo>



Risk 2: Denial of service (XEE: XML Entity Expansion)



<?xml version="1.0"?>
<!DOCTYPE lolz [
 <!ENTITY lol "lol">
 <!ELEMENT lolz (#PCDATA)>
 <!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
 <!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">
 <!ENTITY lol3 "&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;">
[...]
 <!ENTITY lol9 "&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;">
]>
<lolz>&lol9;</lolz>





Solution



In order to avoid exposing dangerous feature of the XML parser, you can do the following change to the code.





Vulnerable Code:




DocumentBuilder builder = df.newDocumentBuilder();

XPathFactory xPathFactory = XPathFactory.newInstance();
XPath xpath = xPathFactory.newXPath();
XPathExpression xPathExpr = xpath.compile("/somepath/text()");

xPathExpr.evaluate(new InputSource(inputStream));







The following snippets show two available solutions. You can set one feature or both.




Solution using "Secure processing" mode:



This setting will protect you against Denial of Service attack and remote file access.

DocumentBuilderFactory df = DocumentBuilderFactory.newInstance();
df.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true);
DocumentBuilder builder = df.newDocumentBuilder();

[...]

xPathExpr.evaluate( builder.parse(inputStream) );





Solution disabling DTD:



By disabling DTD, almost all XXE attacks will be prevented.

DocumentBuilderFactory df = DocumentBuilderFactory.newInstance();
spf.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
DocumentBuilder builder = df.newDocumentBuilder();

[...]

xPathExpr.evaluate( builder.parse(inputStream) );







References


CWE-611: Improper Restriction of XML External Entity Reference ('XXE')

CERT: IDS10-J. Prevent XML external entity attacks

OWASP.org: XML External Entity (XXE) Processing

WS-Attacks.org: XML Entity Expansion

WS-Attacks.org: XML External Entity DOS

WS-Attacks.org: XML Entity Reference Attack

Identifying XML External Entity vulnerability (XXE)


XML External Entity (XXE) Prevention Cheat Sheet



        

        

        

    

    
    

        
        

            XML parsing vulnerable to XXE (SAXParser)
            
        

        
Bug Pattern: XXE_SAXPARSER


        
            


Attack


XML External Entity (XXE) attacks can occur when an XML parser supports XML entities while processing XML received
from an untrusted source.


Risk 1: Expose local file content (XXE: XML External Entity)




<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [
   <!ENTITY xxe SYSTEM "file:///etc/passwd" > ]>
<foo>&xxe;</foo>



Risk 2: Denial of service (XEE: XML Entity Expansion)



<?xml version="1.0"?>
<!DOCTYPE lolz [
 <!ENTITY lol "lol">
 <!ELEMENT lolz (#PCDATA)>
 <!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
 <!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">
 <!ENTITY lol3 "&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;">
[...]
 <!ENTITY lol9 "&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;">
]>
<lolz>&lol9;</lolz>





Solution



In order to avoid exposing dangerous feature of the XML parser, you can do the following change to the code.





Vulnerable Code:




SAXParser parser = SAXParserFactory.newInstance().newSAXParser();

parser.parse(inputStream, customHandler);







The following snippets show two available solutions. You can set one feature or both.




Solution using "Secure processing" mode:



This setting will protect you against Denial of Service attack and remote file access.

SAXParserFactory spf = SAXParserFactory.newInstance();
spf.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true);
SAXParser parser = spf.newSAXParser();

parser.parse(inputStream, customHandler);





Solution disabling DTD:



By disabling DTD, almost all XXE attacks will be prevented.

SAXParserFactory spf = SAXParserFactory.newInstance();
spf.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
SAXParser parser = spf.newSAXParser();

parser.parse(inputStream, customHandler);







References


CWE-611: Improper Restriction of XML External Entity Reference ('XXE')

CERT: IDS10-J. Prevent XML external entity attacks

OWASP.org: XML External Entity (XXE) Processing

WS-Attacks.org: XML Entity Expansion

WS-Attacks.org: XML External Entity DOS

WS-Attacks.org: XML Entity Reference Attack

Identifying XML External Entity vulnerability (XXE)


Xerces complete features list



        

        

        

    

    
    

        
        

            XML parsing vulnerable to XXE (XMLReader)
            
        

        
Bug Pattern: XXE_XMLREADER


        
            


Attack


XML External Entity (XXE) attacks can occur when an XML parser supports XML entities while processing XML received
from an untrusted source.


Risk 1: Expose local file content (XXE: XML External Entity)




<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [
   <!ENTITY xxe SYSTEM "file:///etc/passwd" > ]>
<foo>&xxe;</foo>



Risk 2: Denial of service (XEE: XML Entity Expansion)



<?xml version="1.0"?>
<!DOCTYPE lolz [
 <!ENTITY lol "lol">
 <!ELEMENT lolz (#PCDATA)>
 <!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
 <!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">
 <!ENTITY lol3 "&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;">
[...]
 <!ENTITY lol9 "&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;">
]>
<lolz>&lol9;</lolz>





Solution



In order to avoid exposing dangerous feature of the XML parser, you can do the following change to the code.





Vulnerable Code:




XMLReader reader = XMLReaderFactory.createXMLReader();
reader.setContentHandler(customHandler);
reader.parse(new InputSource(inputStream));







The following snippets show two available solutions. You can set one property or both.




Solution using "Secure processing" mode:



This setting will protect you against Denial of Service attack and remote file access.

XMLReader reader = XMLReaderFactory.createXMLReader();
reader.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true);
reader.setContentHandler(customHandler);

reader.parse(new InputSource(inputStream));





Solution disabling DTD:



By disabling DTD, almost all XXE attacks will be prevented.

XMLReader reader = XMLReaderFactory.createXMLReader();
reader.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
reader.setContentHandler(customHandler);

reader.parse(new InputSource(inputStream));







References


CWE-611: Improper Restriction of XML External Entity Reference ('XXE')

CERT: IDS10-J. Prevent XML external entity attacks

OWASP.org: XML External Entity (XXE) Processing

WS-Attacks.org: XML Entity Expansion

WS-Attacks.org: XML External Entity DOS

WS-Attacks.org: XML Entity Reference Attack

Identifying XML External Entity vulnerability (XXE)


Xerces complete features list



        

        

        

    

    
    

        
        

            XML parsing vulnerable to XXE (DocumentBuilder)
            
        

        
Bug Pattern: XXE_DOCUMENT


        
            


Attack


XML External Entity (XXE) attacks can occur when an XML parser supports XML entities while processing XML received
from an untrusted source.


Risk 1: Expose local file content (XXE: XML External Entity)




<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [
   <!ENTITY xxe SYSTEM "file:///etc/passwd" > ]>
<foo>&xxe;</foo>



Risk 2: Denial of service (XEE: XML Entity Expansion)



<?xml version="1.0"?>
<!DOCTYPE lolz [
 <!ENTITY lol "lol">
 <!ELEMENT lolz (#PCDATA)>
 <!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
 <!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">
 <!ENTITY lol3 "&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;">
[...]
 <!ENTITY lol9 "&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;">
]>
<lolz>&lol9;</lolz>





Solution



In order to avoid exposing dangerous feature of the XML parser, you can do the following change to the code.





Vulnerable Code:




DocumentBuilder db = DocumentBuilderFactory.newInstance().newDocumentBuilder();

Document doc = db.parse(input);







The following snippets show two available solutions. You can set one feature or both.




Solution using "Secure processing" mode:



This setting will protect you against Denial of Service attack and remote file access.

DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
dbf.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true);
DocumentBuilder db = dbf.newDocumentBuilder();

Document doc = db.parse(input);





Solution disabling DTD:



By disabling DTD, almost all XXE attacks will be prevented.

DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
dbf.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
DocumentBuilder db = dbf.newDocumentBuilder();

Document doc = db.parse(input);







References


CWE-611: Improper Restriction of XML External Entity Reference ('XXE')

CERT: IDS10-J. Prevent XML external entity attacks

OWASP.org: XML External Entity (XXE) Processing

WS-Attacks.org: XML Entity Expansion

WS-Attacks.org: XML External Entity DOS

WS-Attacks.org: XML Entity Reference Attack

Identifying XML External Entity vulnerability (XXE)


Xerces2 complete features list



        

        

        

    

    
    

        
        

            XML parsing vulnerable to XXE (TransformerFactory)
            
        

        
Bug Pattern: XXE_DTD_TRANSFORM_FACTORY


        
            


Attack


XML External Entity (XXE) attacks can occur when an XML parser supports XML entities while processing XML received
from an untrusted source.


Risk 1: Expose local file content (XXE: XML External Entity)




<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [
   <!ENTITY xxe SYSTEM "file:///etc/passwd" > ]>
<foo>&xxe;</foo>



Risk 2: Denial of service (XEE: XML Entity Expansion)



<?xml version="1.0"?>
<!DOCTYPE lolz [
 <!ENTITY lol "lol">
 <!ELEMENT lolz (#PCDATA)>
 <!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
 <!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">
 <!ENTITY lol3 "&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;">
[...]
 <!ENTITY lol9 "&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;">
]>
<lolz>&lol9;</lolz>





Solution



In order to avoid exposing dangerous feature of the XML parser, you can do the following change to the code.





Vulnerable Code:




Transformer transformer = TransformerFactory.newInstance().newTransformer();
transformer.transform(input, result);







The following snippets show two available solutions. You can set one feature or both.




Solution disabling DTD:



This setting will protect you against remote file access but not denial of service.

TransformerFactory factory = TransformerFactory.newInstance();
factory.setAttribute(XMLConstants.ACCESS_EXTERNAL_DTD, "");
factory.setAttribute(XMLConstants.ACCESS_EXTERNAL_STYLESHEET, "");

Transformer transformer = factory.newTransformer();
transformer.setOutputProperty(OutputKeys.INDENT, "yes");

transformer.transform(input, result);





An empty string denies all access to external references for both attributes.



Solution using "Secure processing" mode:



This setting will protect you against remote file access but not denial of service.

TransformerFactory factory = TransformerFactory.newInstance();
factory.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true);

Transformer transformer = factory.newTransformer();
transformer.setOutputProperty(OutputKeys.INDENT, "yes");

transformer.transform(input, result);







References


CWE-611: Improper Restriction of XML External Entity Reference ('XXE')

CERT: IDS10-J. Prevent XML external entity attacks

OWASP.org: XML External Entity (XXE) Processing

WS-Attacks.org: XML Entity Expansion

WS-Attacks.org: XML External Entity DOS

WS-Attacks.org: XML Entity Reference Attack

Identifying XML External Entity vulnerability (XXE)





        

        

        

    

    
    

        
        

            XSLT parsing vulnerable to XXE (TransformerFactory)
            
        

        
Bug Pattern: XXE_XSLT_TRANSFORM_FACTORY


        
            


Attack


XSLT External Entity (XXE) attacks can occur when an XSLT parser supports external entities while processing XSLT received
from an untrusted source.


Risk: Expose local file content (XXE: XML External Entity)




<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
   <xsl:template match="/">
       <xsl:value-of select="document('/etc/passwd')">
   </xsl:value-of></xsl:template>
</xsl:stylesheet>





Solution



In order to avoid exposing dangerous feature of the XML parser, you can do the following change to the code.





Vulnerable Code:




Transformer transformer = TransformerFactory.newInstance().newTransformer();
transformer.transform(input, result);







The following snippets show two available solutions. You can set one feature or both.



Solution disabling DTD:



This setting will protect you against remote file access but not denial of service.

TransformerFactory factory = TransformerFactory.newInstance();
factory.setAttribute(XMLConstants.ACCESS_EXTERNAL_DTD, "");
factory.setAttribute(XMLConstants.ACCESS_EXTERNAL_STYLESHEET, "");

Transformer transformer = factory.newTransformer();
transformer.setOutputProperty(OutputKeys.INDENT, "yes");

transformer.transform(input, result);





An empty string denies all access to external references for both attributes.



Solution using "Secure processing" mode:



This setting will protect you against remote file access but not denial of service.

TransformerFactory factory = TransformerFactory.newInstance();
factory.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true);

Transformer transformer = factory.newTransformer();
transformer.setOutputProperty(OutputKeys.INDENT, "yes");

transformer.transform(input, result);







References


CWE-611: Improper Restriction of XML External Entity Reference ('XXE')

CERT: IDS10-J. Prevent XML external entity attacks

OWASP.org: XML External Entity (XXE) Processing

WS-Attacks.org: XML Entity Expansion

WS-Attacks.org: XML External Entity DOS

WS-Attacks.org: XML Entity Reference Attack

Identifying XML External Entity vulnerability (XXE)





        

        

        

    

    
    

        
        

            XML schema processing vulnerable to XXE
            
        

        
Bug Pattern: XXE_SCHEMA_FACTORY


        
            


Summary




XML External Entity attacks can occur when an XML SchemaFactory supports access to external entity references or external schema locations while parsing XML Schema Documents.




Sources




Malicious sources include XML Schema Documents containing entity definitions in the Document Type Declaration (DTD) that reference external locations.
Documents can also include references to external schema locations using XML Schema include elements.




External Entity in Document Type Declaration


<?xml version="1.0"?>
<!DOCTYPE schema [
  <!ENTITY entity SYSTEM "file:///etc/passwd">
]>
<schema>&entity;</schema>


External Schema Location


<?xml version="1.0"?>
<schema xmlns="http://www.w3.org/2001/XMLSchema">
  <include schemaLocation="file:///etc/passwd"/>
</schema>


Vulnerabilities




Vulnerable instances of javax.xml.validation.SchemaFactory attempt to resolve XML External Entity references and External Schema Locations in the default configuration.



SchemaFactory schemaFactory = SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);

Schema schema = schemaFactory.newSchema(source);



Solutions




Protecting instances of java.xml.validation.SchemaFactory requires disabling external access or enabling secure processing.




Disabling External Access




The Java API for XML Processing (JAXP) version 1.5 implementing JEP 185 requires implementations to support properties for disabling external access.
Java 7 Update 40 and Java 8 incorporated implementations of JAXP 1.5.
Both ACCESS_EXTERNAL_DTD and ACCESS_EXTERNAL_SCHEMA must be disabled using an empty string to indicate
that no external protocols are allowed.



SchemaFactory schemaFactory = SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);

schemaFactory.setProperty(XMLConstants.ACCESS_EXTERNAL_DTD, "");
schemaFactory.setProperty(XMLConstants.ACCESS_EXTERNAL_SCHEMA, "");

Schema schema = schemaFactory.newSchema(source);



Enabling Secure Processing




JAXP 1.5 and JEP 185 indicate that implementations supporting the secure processing feature flag must restrict external access.
The FEATURE_SECURE_PROCESSING flag restricts external access in supported implementations of JAXP 1.5.



SchemaFactory schemaFactory = SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);

schemaFactory.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true);

Schema schema = schemaFactory.newSchema(source);



References




  
CWE-611: Improper Restriction of XML External Entity Reference

  
OWASP: XML External Entity (XXE) Processing

  
WS-Attacks.org: XML Entity Expansion

  
WS-Attacks.org: XML External Entity DOS

  
WS-Attacks.org: XML Entity Reference Attack

  
Identifying XML External Entity vulnerability (XXE)

  
JEP 185: Restrict Fetching of External XML Resources




        

        

        

    

    
    

        
        

            XML validation vulnerable to XXE
            
        

        
Bug Pattern: XXE_VALIDATOR


        



Summary




XML External Entity attacks can occur when an XML Validator supports access to external entity references or external schema locations while validating malicious sources.




Sources




Malicious sources include XML documents containing entity definitions in the Document Type Declaration (DTD) that reference external locations.
Documents can also include references to external schema locations using XML Schema Instance (XSI) attributes.




External Entity in Document Type Declaration


<?xml version="1.0"?>
<!DOCTYPE document [
  <!ENTITY entity SYSTEM "file:///etc/passwd">
]>
<document>&entity;</document>


External Schema Location


<?xml version="1.0"?>
<document
  xmlns="urn:external"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="urn:external file:///etc/passwd" />


Vulnerabilities




Vulnerable instances of javax.xml.validation.Validator attempt to resolve XML External Entity references and External Schema Locations in the default configuration.



SchemaFactory schemaFactory = SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);
Schema schema = schemaFactory.newSchema();

Validator validator = schema.newValidator();
validator.validate(source);



Solutions




Protecting instances of java.xml.validation.Validator requires disabling external access or enabling secure processing.




Disabling External Access




The Java API for XML Processing (JAXP) version 1.5 implementing JEP 185 requires implementations to support properties for disabling external access.
Java 7 Update 40 and Java 8 incorporated implementations of JAXP 1.5.
Both ACCESS_EXTERNAL_DTD and ACCESS_EXTERNAL_SCHEMA must be disabled using an empty string to indicate
that no external protocols are allowed.



SchemaFactory schemaFactory = SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);
Schema schema = schemaFactory.newSchema();
Validator validator = schema.newValidator();

validator.setProperty(XMLConstants.ACCESS_EXTERNAL_DTD, "");
validator.setProperty(XMLConstants.ACCESS_EXTERNAL_SCHEMA, "");

validator.validate(source);



Enabling Secure Processing




JAXP 1.5 and JEP 185 indicate that implementations supporting the secure processing feature flag must restrict external access.
The FEATURE_SECURE_PROCESSING flag restricts external access in supported implementations of JAXP 1.5.



SchemaFactory schemaFactory = SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);
Schema schema = schemaFactory.newSchema();
Validator validator = schema.newValidator();

validator.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true);

validator.validate(source);



References




  
CWE-611: Improper Restriction of XML External Entity Reference

  
OWASP: XML External Entity (XXE) Processing

  
WS-Attacks.org: XML Entity Expansion

  
WS-Attacks.org: XML External Entity DOS

  
WS-Attacks.org: XML Entity Reference Attack

  
Identifying XML External Entity vulnerability (XXE)

  
JEP 185: Restrict Fetching of External XML Resources




        

        

        

    

    
    

        
        

            Potential XPath Injection
            
        

        
Bug Pattern: XPATH_INJECTION


        
            


XPath injection risks are similar to SQL injection. If the XPath query contains untrusted user input, the complete data source
could be exposed. This could allow an attacker to access unauthorized data or maliciously modify the target XML.






References

WASC-39: XPath Injection

OWASP: Top 10 2013-A1-Injection

CWE-643: Improper Neutralization of Data within XPath Expressions ('XPath Injection')

CERT: IDS09-J. Prevent XPath Injection (archive)

Black Hat Europe 2012: Hacking XPath 2.0

Balisage.net: XQuery Injection



        

        

        

    

    
    

        
        

            Found Struts 1 endpoint
            
        

        
Bug Pattern: STRUTS1_ENDPOINT


        
            

This class is a Struts 1 Action.


Once a request is routed to this controller, a Form object will automatically be instantiated that contains the HTTP parameters.
The use of these parameters should be reviewed to make sure they are used safely.


        

        

        

    

    
    

        
        

            Found Struts 2 endpoint
            
        

        
Bug Pattern: STRUTS2_ENDPOINT


        
            

In Struts 2, the endpoints are Plain Old Java Objects (POJO) which means no Interface/Class needs to be implemented/extended.


When a request is routed to its controller (like the selected class), the supplied HTTP parameters are automatically mapped to setters for
the class. Therefore, all setters of this class should be considered as untrusted input even if the form doesn't include those values.
An attacker can simply provide additional values in the request, and they will be set in the object anyway, as long as that object has
such a setter. The use of these parameters should be reviewed to make sure they are used safely.


        

        

        

    

    
    

        
        

            Found Spring endpoint
            
        

        
Bug Pattern: SPRING_ENDPOINT


        
            

This class is a Spring Controller. All methods annotated with RequestMapping (as well as its shortcut annotations GetMapping, PostMapping, PutMapping, DeleteMapping, and PatchMapping) are reachable remotely.
This class should be analyzed to make sure that remotely exposed methods are safe to expose to potential attackers.


        

        

        

    

    
    

        
        

            Spring CSRF protection disabled
            
        

        
Bug Pattern: SPRING_CSRF_PROTECTION_DISABLED


        
            

Disabling Spring Security's CSRF protection is unsafe for standard web applications.


A valid use case for disabling this protection would be a service exposing state-changing operations
that is guaranteed to be used only by non-browser clients.



    Insecure configuration:


@EnableWebSecurity
public class WebSecurityConfig extends WebSecurityConfigurerAdapter {

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.csrf().disable();
    }
}





References

Spring Security Official Documentation: When to use CSRF protection

OWASP: Cross-Site Request Forgery

OWASP: CSRF Prevention Cheat Sheet

CWE-352: Cross-Site Request Forgery (CSRF)



        

        

        

    

    
    

        
        

            Spring CSRF unrestricted RequestMapping
            
        

        
Bug Pattern: SPRING_CSRF_UNRESTRICTED_REQUEST_MAPPING


        
            

Methods annotated with RequestMapping are by default mapped to all the HTTP request methods.
However, Spring Security's CSRF protection is not enabled by default
for the HTTP request methods GET, HEAD, TRACE, and OPTIONS
(as this could cause the tokens to be leaked).
Therefore, state-changing methods annotated with RequestMapping and not narrowing the mapping
to the HTTP request methods POST, PUT, DELETE, or PATCH
are vulnerable to CSRF attacks.



    Vulnerable Code:


@Controller
public class UnsafeController {

    @RequestMapping("/path")
    public void writeData() {
        // State-changing operations performed within this method.
    }
}





    Solution (Spring Framework 4.3 and later):


@Controller
public class SafeController {

    /**
     * For methods without side-effects use @GetMapping.
     */
    @GetMapping("/path")
    public String readData() {
        // No state-changing operations performed within this method.
        return "";
    }

    /**
     * For state-changing methods use either @PostMapping, @PutMapping, @DeleteMapping, or @PatchMapping.
     */
    @PostMapping("/path")
    public void writeData() {
        // State-changing operations performed within this method.
    }
}





    Solution (Before Spring Framework 4.3):


@Controller
public class SafeController {

    /**
     * For methods without side-effects use either
     * RequestMethod.GET, RequestMethod.HEAD, RequestMethod.TRACE, or RequestMethod.OPTIONS.
     */
    @RequestMapping(value = "/path", method = RequestMethod.GET)
    public String readData() {
        // No state-changing operations performed within this method.
        return "";
    }

    /**
     * For state-changing methods use either
     * RequestMethod.POST, RequestMethod.PUT, RequestMethod.DELETE, or RequestMethod.PATCH.
     */
    @RequestMapping(value = "/path", method = RequestMethod.POST)
    public void writeData() {
        // State-changing operations performed within this method.
    }
}





References

Spring Security Official Documentation: Use proper HTTP verbs (CSRF protection)

OWASP: Cross-Site Request Forgery

OWASP: CSRF Prevention Cheat Sheet

CWE-352: Cross-Site Request Forgery (CSRF)



        

        

        

    

    
    

        
        

            Potential injection (custom)
            
        

        
Bug Pattern: CUSTOM_INJECTION


        
            


The method identified is susceptible to injection. The input should be validated and properly escaped.





    Vulnerable code samples:

    
SqlUtil.execQuery("select * from UserEntity t where id = " + parameterInput);





    Refer to the online wiki for detailed instructions on how to configure custom signatures.




References

WASC-19: SQL Injection

OWASP: Top 10 2013-A1-Injection

OWASP: SQL Injection Prevention Cheat Sheet

OWASP: Query Parameterization Cheat Sheet

CAPEC-66: SQL Injection

CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')



        

        

        

    

    
    

        
        

            Potential SQL Injection
            
        

        
Bug Pattern: SQL_INJECTION


        
            


The input values included in SQL queries need to be passed in safely.
Bind variables in prepared statements can be used to easily mitigate the risk of SQL injection.
Alternatively to prepare statements, each parameter can be escaped manually.




    Vulnerable Code:

    
createQuery("select * from User where id = '"+inputId+"'");






    Solution:


    
import org.owasp.esapi.Encoder;

createQuery("select * from User where id = '"+Encoder.encodeForSQL(inputId)+"'");








References (SQL injection)

WASC-19: SQL Injection

CAPEC-66: SQL Injection

CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')

OWASP: Top 10 2013-A1-Injection

OWASP: SQL Injection Prevention Cheat Sheet

OWASP: Query Parameterization Cheat Sheet




        

        

        

    

    
    

        
        

            Potential SQL Injection with Turbine
            
        

        
Bug Pattern: SQL_INJECTION_TURBINE


        
            


The input values included in SQL queries need to be passed in safely.
Bind variables in prepared statements can be used to easily mitigate the risk of SQL injection.
Turbine API provide a DSL to build query with Java code.




    Vulnerable Code:

    
List<Record> BasePeer.executeQuery( "select * from Customer where id=" + inputId );






    Solution (using Criteria DSL):


    
Criteria c = new Criteria();
c.add( CustomerPeer.ID, inputId );

List<Customer> customers = CustomerPeer.doSelect( c );


    Solution (using specialized method):


Customer customer = CustomerPeer.retrieveByPK( new NumberKey( inputId ) );


    Solution (using OWASP Encoder):


    import org.owasp.esapi.Encoder;

BasePeer.executeQuery("select * from Customer where id = '"+Encoder.encodeForSQL(inputId)+"'");








References (Turbine)

Turbine Documentation: Criteria Howto

References (SQL injection)

WASC-19: SQL Injection

CAPEC-66: SQL Injection

CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')

OWASP: Top 10 2013-A1-Injection

OWASP: SQL Injection Prevention Cheat Sheet

OWASP: Query Parameterization Cheat Sheet




        

        

        

    

    
    

        
        

            Potential SQL/HQL Injection (Hibernate)
            
        

        
Bug Pattern: SQL_INJECTION_HIBERNATE


        
            


The input values included in SQL queries need to be passed in safely.
Bind variables in prepared statements can be used to easily mitigate the risk of SQL injection.
Alternatively to prepare statements, Hibernate Criteria can be used.




    Vulnerable Code:

    
Session session = sessionFactory.openSession();
Query q = session.createQuery("select t from UserEntity t where id = " + input);
q.execute();





    Solution:

    
Session session = sessionFactory.openSession();
Query q = session.createQuery("select t from UserEntity t where id = :userId");
q.setString("userId",input);
q.execute();





    Solution for dynamic queries (with Hibernate Criteria):

    
Session session = sessionFactory.openSession();
Query q = session.createCriteria(UserEntity.class)
    .add( Restrictions.like("id", input) )
    .list();
q.execute();







References (Hibernate)

CWE-564: SQL Injection: Hibernate

Hibernate Documentation: Query Criteria

Hibernate Javadoc: Query Object

HQL for pentesters: Guideline to test if the suspected code is exploitable.


References (SQL injection)

WASC-19: SQL Injection

CAPEC-66: SQL Injection

CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')

OWASP: Top 10 2013-A1-Injection

OWASP: SQL Injection Prevention Cheat Sheet

OWASP: Query Parameterization Cheat Sheet




        

        

        

    

    
    

        
        

            Potential SQL/JDOQL Injection (JDO)
            
        

        
Bug Pattern: SQL_INJECTION_JDO


        
            


The input values included in SQL queries need to be passed in safely.
Bind variables in prepared statements can be used to easily mitigate the risk of SQL injection.




    Vulnerable Code:

    
PersistenceManager pm = getPM();

Query q = pm.newQuery("select * from Users where name = " + input);
q.execute();





    Solution:

    
PersistenceManager pm = getPM();

Query q = pm.newQuery("select * from Users where name = nameParam");
q.declareParameters("String nameParam");
q.execute(input);







References (JDO)

JDO: Object Retrieval

References (SQL injection)

WASC-19: SQL Injection

CAPEC-66: SQL Injection

CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')

OWASP: Top 10 2013-A1-Injection

OWASP: SQL Injection Prevention Cheat Sheet

OWASP: Query Parameterization Cheat Sheet




        

        

        

    

    
    

        
        

            Potential SQL/JPQL Injection (JPA)
            
        

        
Bug Pattern: SQL_INJECTION_JPA


        
            


The input values included in SQL queries need to be passed in safely.
Bind variables in prepared statements can be used to easily mitigate the risk of SQL injection.




    Vulnerable Code:

    
EntityManager pm = getEM();

TypedQuery<UserEntity> q = em.createQuery(
    String.format("select * from Users where name = %s", username),
    UserEntity.class);

UserEntity res = q.getSingleResult();





    Solution:

    
TypedQuery<UserEntity> q = em.createQuery(
    "select * from Users where name = usernameParam",UserEntity.class)
    .setParameter("usernameParam", username);

UserEntity res = q.getSingleResult();







References (JPA)

The Java EE 6 Tutorial: Creating Queries Using the Java Persistence Query Language

References (SQL injection)

WASC-19: SQL Injection

CAPEC-66: SQL Injection

CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')

OWASP: Top 10 2013-A1-Injection

OWASP: SQL Injection Prevention Cheat Sheet

OWASP: Query Parameterization Cheat Sheet




        

        

        

    

    
    

        
        

            Potential JDBC Injection (Spring JDBC)
            
        

        
Bug Pattern: SQL_INJECTION_SPRING_JDBC


        
            


The input values included in SQL queries need to be passed in safely.
Bind variables in prepared statements can be used to easily mitigate the risk of SQL injection.





    Vulnerable Code:

    
JdbcTemplate jdbc = new JdbcTemplate();
int count = jdbc.queryForObject("select count(*) from Users where name = '"+paramName+"'", Integer.class);

    @Value("properties")
private String sql;

public function count() {
    JdcbOperation jdbc = new JdcbOperation();
    int count = jdbc.query(sql);
}





    Solution:

    
JdbcTemplate jdbc = new JdbcTemplate();
int count = jdbc.queryForObject("select count(*) from Users where name = ?", Integer.class, paramName);
    private final static String sql = "select count(*) from Users";

public function count() {
    JdcbOperation jdbc = new JdcbOperation();
    int count = jdbc.query(sql);
}






References (Spring JDBC)

Spring Official Documentation: Data access with JDBC

References (SQL injection)

WASC-19: SQL Injection

CAPEC-66: SQL Injection

CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')

OWASP: Top 10 2013-A1-Injection

OWASP: SQL Injection Prevention Cheat Sheet

OWASP: Query Parameterization Cheat Sheet





        

        

        

    

    
    

        
        

            Potential JDBC Injection
            
        

        
Bug Pattern: SQL_INJECTION_JDBC


        
            


The input values included in SQL queries need to be passed in safely.
Bind variables in prepared statements can be used to easily mitigate the risk of SQL injection.





    Vulnerable Code:

    
Connection conn = [...];
Statement stmt = con.createStatement();
ResultSet rs = stmt.executeQuery("update COFFEES set SALES = "+nbSales+" where COF_NAME = '"+coffeeName+"'");





    Solution:

    
Connection conn = [...];
conn.prepareStatement("update COFFEES set SALES = ? where COF_NAME = ?");
updateSales.setInt(1, nbSales);
updateSales.setString(2, coffeeName);






References (JDBC)

Oracle Documentation: The Java Tutorials > Prepared Statements

References (SQL injection)

WASC-19: SQL Injection

CAPEC-66: SQL Injection

CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')

OWASP: Top 10 2013-A1-Injection

OWASP: SQL Injection Prevention Cheat Sheet

OWASP: Query Parameterization Cheat Sheet





        

        

        

    

    
    

        
        

            Potential Scala Slick Injection
            
        

        
Bug Pattern: SCALA_SQL_INJECTION_SLICK


        
            


The input values included in SQL queries need to be passed in safely.
Bind variables in prepared statements can be used to easily mitigate the risk of SQL injection.





    Vulnerable Code:

    
db.run {
  sql"select * from people where name = '#$value'".as[Person]
}





    Solution:

    
db.run {
  sql"select * from people where name = $value".as[Person]
}






References (SQL injection)

WASC-19: SQL Injection

CAPEC-66: SQL Injection

CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')

OWASP: Top 10 2013-A1-Injection

OWASP: SQL Injection Prevention Cheat Sheet

OWASP: Query Parameterization Cheat Sheet





        

        

        

    

    
    

        
        

            Potential Scala Anorm Injection
            
        

        
Bug Pattern: SCALA_SQL_INJECTION_ANORM


        
            


The input values included in SQL queries need to be passed in safely.
Bind variables in prepared statements can be used to easily mitigate the risk of SQL injection.





    Vulnerable Code:

    
val peopleParser = Macro.parser[Person]("id", "name", "age")

DB.withConnection { implicit c =>
  val people: List[Person] = SQL("select * from people where name = '" + value + "'").as(peopleParser.*)
}





    Solution:

    
val peopleParser = Macro.parser[Person]("id", "name", "age")

DB.withConnection { implicit c =>
  val people: List[Person] = SQL"select * from people where name = $value".as(peopleParser.*)
}






References (SQL injection)

WASC-19: SQL Injection

CAPEC-66: SQL Injection

CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')

OWASP: Top 10 2013-A1-Injection

OWASP: SQL Injection Prevention Cheat Sheet

OWASP: Query Parameterization Cheat Sheet





        

        

        

    

    
    

        
        

            Potential SQL Injection with Vert.x Sql Client
            
        

        
Bug Pattern: SQL_INJECTION_VERTX


        
            


The input values included in SQL queries need to be passed in safely.
Bind variables in prepared statements can be used to easily mitigate the risk of SQL injection.
Vert.x Sql Client API provide a DSL to build query with Java code.




    Vulnerable Code:

    
SqlClient.query( "select * from Customer where id=" + inputId ).execute(ar -> ...);






    Solution (using Prepared Statements):


    
client
    .preparedQuery( "SELECT * FROM users WHERE id=$1" )
    .execute(Tuple.of("julien"))
    .onSuccess(rows -> ...)
    .onFailure(err -> ...);








References (Vert.x Sql Client)

Vertx Database Access Documentation

References (SQL injection)

WASC-19: SQL Injection

CAPEC-66: SQL Injection

CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')

OWASP: Top 10 2013-A1-Injection

OWASP: SQL Injection Prevention Cheat Sheet

OWASP: Query Parameterization Cheat Sheet




        

        

        

    

    
    

        
        

            Potential Android SQL Injection
            
        

        
Bug Pattern: SQL_INJECTION_ANDROID


        
            


The input values included in SQL queries need to be passed in safely.
Bind variables in prepared statements can be used to easily mitigate the risk of SQL injection.





    Vulnerable Code:

    
String query = "SELECT * FROM  messages WHERE uid= '"+userInput+"'" ;
Cursor cursor = this.getReadableDatabase().rawQuery(query,null);





    Solution:

    
String query = "SELECT * FROM  messages WHERE uid= ?" ;
Cursor cursor = this.getReadableDatabase().rawQuery(query,new String[] {userInput});






References (Android SQLite)

InformIT.com: Practical Advice for Building Secure Android Databases in SQLite

Packtpub.com: Knowing the SQL-injection attacks and securing our Android applications from them

Android Database Support (Enterprise Android: Programming Android Database Applications for the Enterprise)

Safe example of Insert, Select, Update and Delete queries provided by Suragch


References (SQL injection)

WASC-19: SQL Injection

CAPEC-66: SQL Injection

CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')

OWASP: Top 10 2013-A1-Injection

OWASP: SQL Injection Prevention Cheat Sheet

OWASP: Query Parameterization Cheat Sheet





        

        

        

    

    
    

        
        

            Potential LDAP Injection
            
        

        
Bug Pattern: LDAP_INJECTION


        
            


Just like SQL, all inputs passed to an LDAP query need to be passed in safely. Unfortunately, LDAP doesn't have prepared statement interfaces like SQL.
Therefore, the primary defense against LDAP injection is strong input validation of any untrusted data before including it in an LDAP query.




    Code at risk:

    
NamingEnumeration<SearchResult> answers = context.search("dc=People,dc=example,dc=com",
        "(uid=" + username + ")", ctrls);






Solution:



Safe evaluation of Java code using "StringUtils" library.


if(StringUtils.isAlphanumeric(username)) {
    NamingEnumeration<SearchResult> answers = context.search("dc=People,dc=example,dc=com",
        "(uid=" + username + ")", ctrls);
}






References

LDAP Injection Prevention Cheat Sheet

OWASP: Top 10 A1:2017-Injection

WASC-29: LDAP Injection

CWE-90: Improper Neutralization of Special Elements used in an LDAP Query ('LDAP Injection')




        

        

        

    

    
    

        
        

            Potential code injection when using Script Engine
            
        

        
Bug Pattern: SCRIPT_ENGINE_INJECTION


        
            


    Dynamic code is being evaluated. A careful analysis of the code construction should be made. Malicious code execution
    could lead to data leakage or operating system compromised.




    If the evaluation of user code is intended, a proper sandboxing should be applied (see references).




Code at risk:




public void runCustomTrigger(String script) {
    ScriptEngineManager factory = new ScriptEngineManager();
    ScriptEngine engine = factory.getEngineByName("JavaScript");

    engine.eval(script); //Bad things can happen here.
}





Solution:



Safe evaluation of JavaScript code using "Cloudbees Rhino Sandbox" library.


public void runCustomTrigger(String script) {
    SandboxContextFactory contextFactory = new SandboxContextFactory();
    Context context = contextFactory.makeContext();
    contextFactory.enterContext(context);
    try {
        ScriptableObject prototype = context.initStandardObjects();
        prototype.setParentScope(null);
        Scriptable scope = context.newObject(prototype);
        scope.setPrototype(prototype);

        context.evaluateString(scope,script, null, -1, null);
    } finally {
        context.exit();
    }
}







References

Cloudbees Rhino Sandbox: Utility to create sandbox with Rhino (block access to all classes)

CodeUtopia.net: Sandboxing Rhino in Java

Remote Code Execution .. by design: Example of malicious payload. The samples given could be used to test sandboxing rules.

CWE-94: Improper Control of Generation of Code ('Code Injection')

CWE-95: Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')




        

        

        

    

    
    

        
        

            Potential code injection when using Spring Expression
            
        

        
Bug Pattern: SPEL_INJECTION


        
            


    A Spring expression is built with a dynamic value. The source of the value(s) should be verified to avoid
    that unfiltered values fall into this risky code evaluation.



Code at risk:




public void parseExpressionInterface(Person personObj,String property) {

        ExpressionParser parser = new SpelExpressionParser();

        //Unsafe if the input is control by the user..
        Expression exp = parser.parseExpression(property+" == 'Albert'");

        StandardEvaluationContext testContext = new StandardEvaluationContext(personObj);
        boolean result = exp.getValue(testContext, Boolean.class);
[...]







    References

    CWE-94: Improper Control of Generation of Code ('Code Injection')

    CWE-95: Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')

    Spring Expression Language (SpEL) - Official Documentation

    Minded Security: Expression Language Injection

    Remote Code Execution .. by design: Example of malicious payload. The samples given could be used to test sandboxing rules.

    Spring Data-Commons: (CVE-2018-1273)

    Spring OAuth2: CVE-2018-1260




        

        

        

    

    
    

        
        

            Potential code injection when using Expression Language (EL)
            
        

        
Bug Pattern: EL_INJECTION


        
            


    An expression is built with a dynamic value. The source of the value(s) should be verified to avoid
    that unfiltered values fall into this risky code evaluation.



Code at risk:




public void evaluateExpression(String expression) {
    FacesContext context = FacesContext.getCurrentInstance();
    ExpressionFactory expressionFactory = context.getApplication().getExpressionFactory();
    ELContext elContext = context.getELContext();
    ValueExpression vex = expressionFactory.createValueExpression(elContext, expression, String.class);
    return (String) vex.getValue(elContext);
}







    References

    Minded Security: Abusing EL for executing OS commands

    The Java EE 6 Tutorial: Expression Language

    CWE-94: Improper Control of Generation of Code ('Code Injection')

    CWE-95: Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')

    Minded Security: Expression Language Injection

    Dan Amodio's blog: Remote Code with Expression Language Injection

    Remote Code Execution .. by design: Example of malicious payload. The samples given could be used to test sandboxing rules.




        

        

        

    

    
    

        
        

            Potential code injection in Seam logging call
            
        

        
Bug Pattern: SEAM_LOG_INJECTION


        
            


    Seam Logging API support an expression language to introduce bean property to log messages. The expression language can
    also be the source to unwanted code execution.




    In this context, an expression is built with a dynamic value. The source of the value(s) should be verified to avoid
    that unfiltered values fall into this risky code evaluation.



Code at risk:




public void logUser(User user) {
    log.info("Current logged in user : " + user.getUsername());
    //...
}




Solution:




public void logUser(User user) {
    log.info("Current logged in user : #0", user.getUsername());
    //...
}







    References

    JBSEAM-5130: Issue documenting the risk

    JBoss Seam: Logging (Official documentation)

    The Java EE 6 Tutorial: Expression Language

    CWE-94: Improper Control of Generation of Code ('Code Injection')

    CWE-95: Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')





        

        

        

    

    
    

        
        

            Potential code injection when using OGNL expression
            
        

        
Bug Pattern: OGNL_INJECTION


        
            


    A expression is built with a dynamic value. The source of the value(s) should be verified to avoid
    that unfiltered values fall into this risky code evaluation.



Code at risk:




public void getUserProperty(String property) {
  [...]
  //The first argument is the dynamic expression.
  return ognlUtil.getValue("user."+property, ctx, root, String.class);
}





Solution:



In general, method evaluating OGNL expression should not receive user input. It is intended to be used in static configurations.






    References

    HP Enterprise: Struts 2 OGNL Expression Injections by Alvaro MuÃ±oz

    Gotham Digital Science: An Analysis Of CVE-2017-5638

    Apache Struts2: Vulnerability S2-016

    Apache Struts 2 Documentation: OGNL

    CWE-94: Improper Control of Generation of Code ('Code Injection')




        

        

        

    

    
    

        
        

            Potential code injection when using GroovyShell
            
        

        
Bug Pattern: GROOVY_SHELL


        
            


    A expression is built with a dynamic value. The source of the value(s) should be verified to avoid
    that unfiltered values fall into this risky code evaluation.



Code at risk:




public void evaluateScript(String script) {
  GroovyShell shell = new GroovyShell();
  shell.evaluate(script);
}





Solution:



In general, method evaluating Groovy expression should not receive user input from low privilege users.






    References

    Hacking Jenkins Part 2 - Abusing Meta Programming for Unauthenticated RCE! by Orange Tsai

    Jenkins RCE payloads by Orange Tsai

    POC for CVE-2019-1003001 by Adam Jordan

    Various payloads of exploiting Groovy code evaluation

    CWE-94: Improper Control of Generation of Code ('Code Injection')




        

        

        

    

    
    

        
        

            Potential HTTP Response Splitting
            
        

        
Bug Pattern: HTTP_RESPONSE_SPLITTING


        
            


    When an HTTP request contains unexpected CR and LF characters, the server may respond with an output stream
    that is interpreted as two different HTTP responses (instead of one).
    An attacker can control the second response and mount attacks such as cross-site scripting and cache poisoning attacks.
    According to OWASP, the issue has been fixed in virtually all modern Java EE application servers, but it is still better to validate the input.
    If you are concerned about this risk, you should test on the platform of concern to see
    if the underlying platform allows for CR or LF characters to be injected into headers.
    This weakness is reported with low priority because it requires the web container to be vulnerable.






Code at risk:


String author = request.getParameter(AUTHOR_PARAMETER);
// ...
Cookie cookie = new Cookie("author", author);
response.addCookie(cookie);







    References

    OWASP: HTTP Response Splitting

    CWE-113: Improper Neutralization of CRLF Sequences in HTTP Headers ('HTTP Response Splitting')
    CWE-93: Improper Neutralization of CRLF Sequences ('CRLF Injection')





        

        

        

    

    
    

        
        

            Potential CRLF Injection for logs
            
        

        
Bug Pattern: CRLF_INJECTION_LOGS


        
            


    When data from an untrusted source is put into a logger and not neutralized correctly,
    an attacker could forge log entries or include malicious content.
    Inserted false entries could be used to skew statistics, distract the administrator
    or even to implicate another party in the commission of a malicious act.
    If the log file is processed automatically, the attacker can render the file unusable
    by corrupting the format of the file or injecting unexpected characters.
    An attacker may also inject code or other commands into the log file and take advantage
    of a vulnerability in the log processing utility (e.g. command injection or XSS).






Code at risk:


String val = request.getParameter("user");
String metadata = request.getParameter("metadata");
[...]
if(authenticated) {
    log.info("User " + val + " (" + metadata + ") was authenticated successfully");
}
else {
    log.info("User " + val + " (" + metadata + ") was not authenticated");
}


A malicious user could send the metadata parameter with the value: "Firefox) was authenticated successfully\r\n[INFO] User bbb (Internet Explorer".




Solution:



You can manually sanitize each parameter.

log.info("User " + val.replaceAll("[\r\n]","") + " (" + userAgent.replaceAll("[\r\n]","") + ") was not authenticated");







You can also configure your logger service to replace new line for all message events. Here is sample configuration for LogBack using the replace function.

<pattern>%-5level - %replace(%msg){'[\r\n]', ''}%n</pattern>







Finally, you can use a logger implementation that replace new line by spaces.
The project OWASP Security Logging has an implementation for Logback and Log4j.







    References

    CWE-117: Improper Output Neutralization for Logs

    CWE-93: Improper Neutralization of CRLF Sequences ('CRLF Injection')

    CWE-93: Improper Neutralization of CRLF Sequences ('CRLF Injection')

    OWASP Security Logging





        

        

        

    

    
    

        
        

            Potential external control of configuration
            
        

        
Bug Pattern: EXTERNAL_CONFIG_CONTROL


        
            


    Allowing external control of system settings can disrupt service or cause an application
    to behave in unexpected, and potentially malicious ways.
    An attacker could cause an error by providing a nonexistent catalog name
    or connect to an unauthorized portion of the database.






Code at risk:


conn.setCatalog(request.getParameter("catalog"));







    References

    CWE-15: External Control of System or Configuration Setting




        

        

        

    

    
    

        
        

            Bad hexadecimal concatenation
            
        

        
Bug Pattern: BAD_HEXA_CONVERSION


        
            

When converting a byte array containing a hash signature to a human readable string, a conversion mistake can be made if
the array is read byte by byte. The following sample illustrates the use of the method Integer.toHexString() which will trim any leading zeroes
from each byte of the computed hash value.

MessageDigest md = MessageDigest.getInstance("SHA-256");
byte[] resultBytes = md.digest(password.getBytes("UTF-8"));

StringBuilder stringBuilder = new StringBuilder();
for(byte b :resultBytes) {
    stringBuilder.append( Integer.toHexString( b & 0xFF ) );
}

return stringBuilder.toString();





This mistake weakens the hash value computed since it introduces more collisions.
For example, the hash values "0x0679" and "0x6709" would both output as "679" for the above function.





In this situation, the method Integer.toHexString() should be replaced with String.format() as follows:

stringBuilder.append( String.format( "%02X", b ) );







References

CWE-704: Incorrect Type Conversion or Cast



        

        

        

    

    
    

        
        

            Hazelcast symmetric encryption
            
        

        
Bug Pattern: HAZELCAST_SYMMETRIC_ENCRYPTION


        
            

The network communications for Hazelcast is configured to use a symmetric cipher (probably DES or Blowfish).


Those ciphers alone do not provide integrity or secure authentication. The use of asymmetric encryption is preferred.





References

WASC-04: Insufficient Transport Layer Protection

Hazelcast Documentation: Encryption

CWE-326: Inadequate Encryption Strength
CWE-327: Use of a Broken or Risky Cryptographic Algorithm



        

        

        

    

    
    

        
        

            NullCipher is insecure
            
        

        
Bug Pattern: NULL_CIPHER


        
            


The NullCipher is rarely used intentionally in production applications. It implements the Cipher interface by returning ciphertext
identical to the supplied plaintext. In a few contexts, such as testing, a NullCipher may be appropriate.




    Vulnerable Code:


Cipher doNothingCihper = new NullCipher();
[...]
//The ciphertext produced will be identical to the plaintext.
byte[] cipherText = c.doFinal(plainText);





    Solution:

    Avoid using the NullCipher. Its accidental use can introduce a significant confidentiality risk.






Reference

CWE-327: Use of a Broken or Risky Cryptographic Algorithm



        

        

        

    

    
    

        
        

            Unencrypted Socket
            
        

        
Bug Pattern: UNENCRYPTED_SOCKET


        
            


The communication channel used is not encrypted. The traffic could be read by an attacker intercepting the network traffic.




Vulnerable Code:

Plain socket (Cleartext communication):

Socket soc = new Socket("www.google.com",80);





Solution:

SSL Socket (Secure communication):

Socket soc = SSLSocketFactory.getDefault().createSocket("www.google.com", 443);




Beyond using an SSL socket, you need to make sure your use of SSLSocketFactory does all the appropriate certificate validation checks to
make sure you are not subject to man-in-the-middle attacks. Please read the OWASP Transport Layer Protection Cheat Sheet for details on how
to do this correctly.






References

OWASP: Top 10 2010-A9-Insufficient Transport Layer Protection

OWASP: Top 10 2013-A6-Sensitive Data Exposure

OWASP: Transport Layer Protection Cheat Sheet

WASC-04: Insufficient Transport Layer Protection

CWE-319: Cleartext Transmission of Sensitive Information



        

        

        

    

    
    

        
        

            Unencrypted Server Socket
            
        

        
Bug Pattern: UNENCRYPTED_SERVER_SOCKET


        
            


The communication channel used is not encrypted. The traffic could be read by an attacker intercepting the network traffic.




Vulnerable Code:

Plain server socket (Cleartext communication):

ServerSocket soc = new ServerSocket(1234);





Solution:

SSL Server Socket (Secure communication):

ServerSocket soc = SSLServerSocketFactory.getDefault().createServerSocket(1234);




Beyond using an SSL server socket, you need to make sure your use of SSLServerSocketFactory does all the appropriate certificate validation checks to
make sure you are not subject to man-in-the-middle attacks. Please read the OWASP Transport Layer Protection Cheat Sheet for details on how
to do this correctly.






References

OWASP: Top 10 2010-A9-Insufficient Transport Layer Protection

OWASP: Top 10 2013-A6-Sensitive Data Exposure

OWASP: Transport Layer Protection Cheat Sheet

WASC-04: Insufficient Transport Layer Protection

CWE-319: Cleartext Transmission of Sensitive Information



        

        

        

    

    
    

        
        

            DES is insecure
            
        

        
Bug Pattern: DES_USAGE


        
            


DES is considered strong ciphers for modern applications. Currently, NIST recommends the
usage of AES block ciphers instead of DES.




    Example weak code:

Cipher c = Cipher.getInstance("DES/ECB/PKCS5Padding");
c.init(Cipher.ENCRYPT_MODE, k, iv);
byte[] cipherText = c.doFinal(plainText);





    Example solution:
    
Cipher c = Cipher.getInstance("AES/GCM/NoPadding");
c.init(Cipher.ENCRYPT_MODE, k, iv);
byte[] cipherText = c.doFinal(plainText);







References

NIST Withdraws Outdated Data Encryption Standard

CWE-326: Inadequate Encryption Strength
CWE-327: Use of a Broken or Risky Cryptographic Algorithm



        

        

        

    

    
    

        
        

            DESede is insecure
            
        

        
Bug Pattern: TDES_USAGE


        
            


Triple DES (also known as 3DES or DESede) is considered strong ciphers for modern applications. Currently, NIST recommends the
usage of AES block ciphers instead of 3DES.




    Example weak code:

Cipher c = Cipher.getInstance("DESede/ECB/PKCS5Padding");
c.init(Cipher.ENCRYPT_MODE, k, iv);
byte[] cipherText = c.doFinal(plainText);





    Example solution:
    
Cipher c = Cipher.getInstance("AES/GCM/NoPadding");
c.init(Cipher.ENCRYPT_MODE, k, iv);
byte[] cipherText = c.doFinal(plainText);







References

NIST Withdraws Outdated Data Encryption Standard

CWE-326: Inadequate Encryption Strength



        

        

        

    

    
    

        
        

            RSA with no padding is insecure
            
        

        
Bug Pattern: RSA_NO_PADDING


        
            


The software uses the RSA algorithm but does not incorporate Optimal Asymmetric Encryption Padding (OAEP), which might weaken the encryption.




Vulnerable Code:


Cipher.getInstance("RSA/NONE/NoPadding")





Solution:

The code should be replaced with:


Cipher.getInstance("RSA/ECB/OAEPWithMD5AndMGF1Padding")







References

CWE-780: Use of RSA Algorithm without OAEP

Root Labs: Why RSA encryption padding is critical



        

        

        

    

    
    

        
        

            Hard coded password
            
        

        
Bug Pattern: HARD_CODE_PASSWORD


        
            


Passwords should not be kept in the source code. The source code can be widely shared in an enterprise environment, and is
certainly shared in open source. To be managed safely, passwords and secret keys should be stored in separate configuration files or keystores.
(Hard coded keys are reported separately by Hard Coded Key pattern)






Vulnerable Code:



private String SECRET_PASSWORD = "letMeIn!";

Properties props = new Properties();
props.put(Context.SECURITY_CREDENTIALS, "p@ssw0rd");







References

CWE-259: Use of Hard-coded Password



        

        

        

    

    
    

        
        

            Hard coded key
            
        

        
Bug Pattern: HARD_CODE_KEY


        
            


Cryptographic keys should not be kept in the source code. The source code can be widely shared in an enterprise environment, and is
certainly shared in open source. To be managed safely, passwords and secret keys should be stored in separate configuration files or keystores.
(Hard coded passwords are reported separately by the Hard coded password pattern)






Vulnerable Code:



byte[] key = {1, 2, 3, 4, 5, 6, 7, 8};
SecretKeySpec spec = new SecretKeySpec(key, "AES");
Cipher aes = Cipher.getInstance("AES");
aes.init(Cipher.ENCRYPT_MODE, spec);
return aesCipher.doFinal(secretData);







References

CWE-321: Use of Hard-coded Cryptographic Key




        

        

        

    

    
    

        
        

            Unsafe hash equals
            
        

        
Bug Pattern: UNSAFE_HASH_EQUALS


        
            


An attacker might be able to detect the value of the secret hash due to the exposure of comparison timing. When the
functions Arrays.equals() or String.equals() are called, they will exit earlier if fewer
bytes are matched.






Vulnerable Code:



String actualHash = ...

if(userInput.equals(actualHash)) {
    ...
}




Solution:



String actualHash = ...

if(MessageDigest.isEqual(userInput.getBytes(),actualHash.getBytes())) {
    ...
}







References

CWE-203: Information Exposure Through DiscrepancyKey




        

        

        

    

    
    

        
        

            Struts Form without input validation
            
        

        
Bug Pattern: STRUTS_FORM_VALIDATION


        
            


Form inputs should have minimal input validation. Preventive validation helps provide defense in depth against a variety of risks.




Validation can be introduced by implementing a validate method.

public class RegistrationForm extends ValidatorForm {

    private String name;
    private String email;

    [...]

    public ActionErrors validate(ActionMapping mapping, HttpServletRequest request) {
        //Validation code for name and email parameters passed in via the HttpRequest goes here
    }
}








References

CWE-20: Improper Input Validation

CWE-106: Struts: Plug-in Framework not in Use



        

        

        

    

    
    

        
        

            XSSRequestWrapper is a weak XSS protection
            
        

        
Bug Pattern: XSS_REQUEST_WRAPPER


        
            


An implementation of HttpServletRequestWrapper called XSSRequestWrapper was published through
various blog sites. [1]
[2]




The filtering is weak for a few reasons:




It covers only parameters not headers and side-channel inputs


The chain of replace functions can be bypassed easily (see example below)


It's a black list of very specific bad patterns (rather than a white list of good/valid input)








Example of bypass:



<scrivbscript:pt>alert(1)</scrivbscript:pt>


The previous input will be transformed into "<script>alert(1)</script>".
The removal of "vbscript:" is after the replacement of "<script>.*</script>".




For stronger protection, choose a solution that encodes characters automatically in the view (template or JSP) following
the XSS protection rules defined in the OWASP XSS Prevention Cheat Sheet.






References

WASC-8: Cross Site Scripting

OWASP: XSS Prevention Cheat Sheet

OWASP: Top 10 2013-A3: Cross-Site Scripting (XSS)

CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')



        

        

        

    

    
    

        
        

            Blowfish usage with short key
            
        

        
Bug Pattern: BLOWFISH_KEY_SIZE


        
            


The Blowfish cipher supports key sizes from 32 bits to 448 bits. A small key size makes the ciphertext vulnerable to brute force attacks.
At least 128 bits of entropy should be used when generating the key if the use of Blowfish is required.




If the algorithm can be changed, the AES block cipher should be used instead.




Vulnerable Code:


KeyGenerator keyGen = KeyGenerator.getInstance("Blowfish");
keyGen.init(64);





Solution:


KeyGenerator keyGen = KeyGenerator.getInstance("Blowfish");
keyGen.init(128);







References

Blowfish (cipher)

CWE-326: Inadequate Encryption Strength



        

        

        

    

    
    

        
        

            RSA usage with short key
            
        

        
Bug Pattern: RSA_KEY_SIZE


        
            


    The NIST recommends the use of 2048 bits and higher keys for the RSA algorithm.



    "Digital Signature Verification | RSA: 1024 ≤ len(n) < 2048 | Legacy-use"

    "Digital Signature Verification | RSA: len(n) ≥ 2048 | Acceptable"

    - NIST: Recommendation for Transitioning the Use of Cryptographic Algorithms and Key Lengths p.7



Vulnerable Code:


KeyPairGenerator keyGen = KeyPairGenerator.getInstance("RSA");
keyGen.initialize(512);






Solution:

The KeyPairGenerator creation should be as follows with at least 2048 bit key size.


KeyPairGenerator keyGen = KeyPairGenerator.getInstance("RSA");
keyGen.initialize(2048);








References

NIST: Latest publication on key management

NIST: Recommendation for Transitioning the Use of Cryptographic Algorithms and Key Lengths p.7

Wikipedia: Asymmetric algorithm key lengths

CWE-326: Inadequate Encryption Strength

Keylength.com (BlueKrypt): Aggregate key length recommendations.



        

        

        

    

    
    

        
        

            Unvalidated Redirect
            
        

        
Bug Pattern: UNVALIDATED_REDIRECT


        
            


    Unvalidated redirects occur when an application redirects a user to a destination URL specified by a user supplied
    parameter that is not validated. Such vulnerabilities can be used to facilitate phishing attacks.




    Scenario

    1. A user is tricked into visiting the malicious URL: http://website.com/login?redirect=http://evil.vvebsite.com/fake/login

    2. The user is redirected to a fake login page that looks like a site they trust. (http://evil.vvebsite.com/fake/login)

    3. The user enters his credentials.

    4. The evil site steals the user's credentials and redirects him to the original website.

    

    This attack is plausible because most users don't double check the URL after the redirection. Also, redirection to
    an authentication page is very common.




    Vulnerable Code:

    
protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
    [...]
    resp.sendRedirect(req.getParameter("redirectUrl"));
    [...]
}





    Solution/Countermeasures:

    


        
Don't accept redirection destinations from users

        
Accept a destination key, and use it to look up the target (legal) destination

        
Accept only relative paths

        
White list URLs (if possible)

        
Validate that the beginning of the URL is part of a white list

    








References

WASC-38: URL Redirector Abuse

OWASP: Top 10 2013-A10: Unvalidated Redirects and Forwards

OWASP: Unvalidated Redirects and Forwards Cheat Sheet

CWE-601: URL Redirection to Untrusted Site ('Open Redirect')


            
        

        

        

    

    
    

        
        

            Unvalidated Redirect (Play Framework)
            
        

        
Bug Pattern: PLAY_UNVALIDATED_REDIRECT


        
            


    Unvalidated redirects occur when an application redirects a user to a destination URL specified by a user supplied
    parameter that is not validated. Such vulnerabilities can be used to facilitate phishing attacks.




    Scenario

    1. A user is tricked into visiting the malicious URL: http://website.com/login?redirect=http://evil.vvebsite.com/fake/login

    2. The user is redirected to a fake login page that looks like a site they trust. (http://evil.vvebsite.com/fake/login)

    3. The user enters his credentials.

    4. The evil site steals the user's credentials and redirects him to the original website.

    

    This attack is plausible because most users don't double check the URL after the redirection. Also, redirection to
    an authentication page is very common.




    Vulnerable Code:

    
def login(redirectUrl:String) = Action {
    [...]
    Redirect(url)
}





    Solution/Countermeasures:

    


        
Don't accept redirection destinations from users

        
Accept a destination key, and use it to look up the target (legal) destination

        
Accept only relative paths

        
White list URLs (if possible)

        
Validate that the beginning of the URL is part of a white list

    








References

WASC-38: URL Redirector Abuse

OWASP: Top 10 2013-A10: Unvalidated Redirects and Forwards

OWASP: Unvalidated Redirects and Forwards Cheat Sheet

CWE-601: URL Redirection to Untrusted Site ('Open Redirect')


            
        

        

        

    

    
    

        
        

            Spring Unvalidated Redirect
            
        

        
Bug Pattern: SPRING_UNVALIDATED_REDIRECT


        
            


    Unvalidated redirects occur when an application redirects a user to a destination URL specified by a user supplied
    parameter that is not validated. Such vulnerabilities can be used to facilitate phishing attacks.




    Scenario

    1. A user is tricked into visiting the malicious URL: http://website.com/login?redirect=http://evil.vvebsite.com/fake/login

    2. The user is redirected to a fake login page that looks like a site they trust. (http://evil.vvebsite.com/fake/login)

    3. The user enters his credentials.

    4. The evil site steals the user's credentials and redirects him to the original website.

    

    This attack is plausible because most users don't double check the URL after the redirection. Also, redirection to
    an authentication page is very common.




    Vulnerable Code:

    
@RequestMapping("/redirect")
public String redirect(@RequestParam("url") String url) {
    [...]
    return "redirect:" + url;
}





    Solution/Countermeasures:

    


        
Don't accept redirection destinations from users

        
Accept a destination key, and use it to look up the target (legal) destination

        
Accept only relative paths

        
White list URLs (if possible)

        
Validate that the beginning of the URL is part of a white list

    








References

WASC-38: URL Redirector Abuse

OWASP: Top 10 2013-A10: Unvalidated Redirects and Forwards

OWASP: Unvalidated Redirects and Forwards Cheat Sheet

CWE-601: URL Redirection to Untrusted Site ('Open Redirect')


            
        

        

        

    

    
    

        
        

            Unexpected property leak
            
        

        
Bug Pattern: ENTITY_LEAK


        
            


    Persistent objects should never be returned by APIs. They might lead to leaking business logic over the UI, unauthorized tampering of
    persistent objects in database.




    Vulnerable Code:


@javax.persistence.Entity
class UserEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String username;

    private String password;
}

[...]
@Controller
class UserController {

    @GetMapping("/user/{id}")
    public UserEntity getUser(@PathVariable("id") String id) {

        return userService.findById(id).get(); //Return the user entity with ALL fields.
    }

}






    Solution/Countermeasures:

    


        
Data transfer objects should be used instead including only the parameters needed as input/response to/from the API.

        
Sensitive parameters should be removed properly before transferring to UI.

        
Data should be persisted in database only after proper sanitization checks.

    






    Spring MVC Solution:

    In Spring specifically, you can apply the following solution to allow or disallow specific fields.

        
@Controller
class UserController {

   @InitBinder
   public void initBinder(WebDataBinder binder, WebRequest request)
   {
      binder.setAllowedFields(["username","firstname","lastname"]);
   }

}
    






References

OWASP Top 10-2017 A3: Sensitive Data Exposure

OWASP Cheat Sheet: Mass Assignment

CWE-212: Improper Cross-boundary Removal of Sensitive Data

CWE-213: Intentional Information Exposure






            
        

        

        

    

    
    

        
        

            Mass assignment
            
        

        
Bug Pattern: ENTITY_MASS_ASSIGNMENT


        
            


    Software frameworks sometime allow developers to automatically bind HTTP request parameters into program code variables or objects 
    to make using that framework easier on developers. This can sometimes cause harm.




    Attackers can sometimes use this methodology to create new parameters that the developer never intended which in turn creates or 
    overwrites new variable or objects in program code that was not intended.




    Vulnerable Code:


@javax.persistence.Entity
class UserEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String username;

    private String password;

    private Long role;
}

[...]
@Controller
class UserController {

    @PutMapping("/user/")
    @ResponseStatus(value = HttpStatus.OK)
    public void update(UserEntity user) {

        userService.save(user); //ALL fields from the user can be altered
    }

}






    General Guidelines:

    


        
Data transfer objects should be used instead including only the parameters needed as input/response to/from the API.

        
Sensitive parameters should be removed properly before transferring to UI.

        
Data should be persisted in database only after proper sanitization checks.

    






    Spring MVC Solution:

    In Spring specifically, you can apply the following solution to allow or disallow specific fields.



With whitelist:

        
@Controller
class UserController {

   @InitBinder
   public void initBinder(WebDataBinder binder, WebRequest request)
   {
      binder.setAllowedFields(["username","password"]);
   }

}
    


With a blacklist:

    @Controller
class UserController {

   @InitBinder
   public void initBinder(WebDataBinder binder, WebRequest request)
   {
      binder.setDisallowedFields(["role"]);
   }

}
    






References

OWASP Cheat Sheet: Mass Assignment

CWE-915: Improperly Controlled Modification of Dynamically-Determined Object Attributes



            
        

        

        

    

    
    

        
        

            Dynamic JSP inclusion
            
        

        
Bug Pattern: JSP_INCLUDE


        
            

The inclusion of JSP file allow the entry of dynamic value. It may allow an attacker to control the JSP page included.
If this is the case, an attacker will try to include a file on disk that he controls. By including arbitrary files, the
attacker gets the ability to execute any code.




    Vulnerable Code:
    
<jsp:include page="${param.secret_param}" />





    Solution:
    
<c:if test="${param.secret_param == 'page1'}">
    <jsp:include page="page1.jsp" />
</c:if>







References

InfosecInstitute: File Inclusion Attacks

WASC-05: Remote File Inclusion

CWE-917: Improper Neutralization of Special Elements used in an Expression Language Statement ('Expression Language Injection')



            
        

        

        

    

    
    

        
        

            Dynamic variable in Spring expression
            
        

        
Bug Pattern: JSP_SPRING_EVAL


        
            

A Spring expression is built with a dynamic value. The source of the value(s) should be verified to avoid that unfiltered values fall into this risky code evaluation.




    Vulnerable Code:
    
<%@ taglib prefix="spring" uri="http://www.springframework.org/tags" %>

<spring:eval expression="${param.lang}" var="lang" />
    

    <%@ taglib prefix="spring" uri="http://www.springframework.org/tags" %>

<spring:eval expression="'${param.lang}'=='fr'" var="languageIsFrench" />





    Solution:
    
<c:set var="lang" value="${param.lang}"/>
    

    <c:set var="languageIsFrench" value="${param.lang == 'fr'}"/>







References

    CWE-94: Improper Control of Generation of Code ('Code Injection')

    CWE-95: Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection')

    CWE-917: Improper Neutralization of Special Elements used in an Expression Language Statement ('Expression Language Injection')



            
        

        

        

    

    
    

        
        

            Escaping of special XML characters is disabled
            
        

        
Bug Pattern: JSP_JSTL_OUT


        
            

A potential XSS was found. It could be used to execute unwanted JavaScript in a client's browser. (See references)




    Vulnerable Code:
    
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<c:out value="${param.test_param}" escapeXml="false"/>





    Solution:
    
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<c:out value="${param.test_param}"/>







References

WASC-8: Cross Site Scripting

OWASP: XSS Prevention Cheat Sheet

OWASP: Top 10 2013-A3: Cross-Site Scripting (XSS)

CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')

JSTL Javadoc: Out tag



            
        

        

        

    

    
    

        
        

            Potential XSS in JSP
            
        

        
Bug Pattern: XSS_JSP_PRINT


        
            

A potential XSS was found. It could be used to execute unwanted JavaScript in a client's browser. (See references)




    Vulnerable Code:
    
<%
String taintedInput = (String) request.getAttribute("input");
%>
[...]
<%= taintedInput %>





    Solution:
    
<%
String taintedInput = (String) request.getAttribute("input");
%>
[...]
<%= Encode.forHtml(taintedInput) %>
    





The best defense against XSS is context sensitive output encoding like the example above. There are typically 4 contexts to consider:
HTML, JavaScript, CSS (styles), and URLs. Please follow the XSS protection rules defined in the OWASP XSS Prevention Cheat Sheet,
which explains these defenses in significant detail.






References

WASC-8: Cross Site Scripting

OWASP: XSS Prevention Cheat Sheet

OWASP: Top 10 2013-A3: Cross-Site Scripting (XSS)

CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')

OWASP Java Encoder



            
        

        

        

    

    
    

        
        

            Potential XSS in Servlet
            
        

        
Bug Pattern: XSS_SERVLET


        
            


A potential XSS was found. It could be used to execute unwanted JavaScript in a client's browser. (See references)




    Vulnerable Code:

protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
    String input1 = req.getParameter("input1");
    [...]
    resp.getWriter().write(input1);
}





    Solution:

protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
    String input1 = req.getParameter("input1");
    [...]
    resp.getWriter().write(Encode.forHtml(input1));
}





The best defense against XSS is context sensitive output encoding like the example above. There are typically 4 contexts to consider:
HTML, JavaScript, CSS (styles), and URLs. Please follow the XSS protection rules defined in the OWASP XSS Prevention Cheat Sheet,
which explains these defenses in significant detail.



Note that this XSS in Servlet rule looks for similar issues, but looks for them in a different way than the existing
'XSS: Servlet reflected cross site scripting vulnerability' and 'XSS: Servlet reflected cross site scripting vulnerability in error page' rules in FindBugs.






References

WASC-8: Cross Site Scripting

OWASP: XSS Prevention Cheat Sheet

OWASP: Top 10 2013-A3: Cross-Site Scripting (XSS)

CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')

OWASP Java Encoder



            
        

        

        

    

    
    

        
        

            XMLDecoder usage
            
        

        
Bug Pattern: XML_DECODER


        
            


    XMLDecoder should not be used to parse untrusted data. Deserializing user input can lead to arbitrary code execution.
    This is possible because XMLDecoder supports arbitrary method invocation. This capability is intended to call setter methods,
    but in practice, any method can be called.




    Malicious XML example:


<?xml version="1.0" encoding="UTF-8" ?>
<java version="1.4.0" class="java.beans.XMLDecoder">
  <object class="java.io.PrintWriter">
    <string>/tmp/Hacked.txt</string>
    <void method="println">
      <string>Hello World!</string>
    </void>
    <void method="close"/>
  </object>
</java>



The XML code above will cause the creation of a file with the content "Hello World!".




    Vulnerable Code:

    
XMLDecoder d = new XMLDecoder(in);
try {
    Object result = d.readObject();
}
[...]





Solution:

The solution is to avoid using XMLDecoder to parse content from an untrusted source.






References

Dinis Cruz Blog: Using XMLDecoder to execute server-side Java Code on a Restlet application

RedHat blog : Java deserialization flaws: Part 2, XML deserialization

CWE-20: Improper Input Validation
CWE-502: Deserialization of Untrusted Data


            
        

        

        

    

    
    

        
        

            Static IV
            
        

        
Bug Pattern: STATIC_IV


        
            


    Initialization vector must be regenerated for each message to be encrypted.



Vulnerable Code:




private static byte[] IV = new byte[16] {(byte)0,(byte)1,(byte)2,[...]};

public void encrypt(String message) throws Exception {

    IvParameterSpec ivSpec = new IvParameterSpec(IV);
[...]


Solution:




public void encrypt(String message) throws Exception {

    byte[] iv = new byte[16];
    new SecureRandom().nextBytes(iv);

    IvParameterSpec ivSpec = new IvParameterSpec(iv);
[...]








References

Wikipedia: Initialization vector

CWE-329: Not Using a Random IV with CBC Mode

Encryption - CBC Mode IV: Secret or Not?


            
        

        

        

    

    
    

        
        

            ECB mode is insecure
            
        

        
Bug Pattern: ECB_MODE


        
            

An authentication cipher mode which provides better confidentiality of the encrypted data should be used instead of Electronic Code Book (ECB) mode,
which does not provide good confidentiality. Specifically, ECB mode produces the same output for the same input each time. So,
for example, if a user is sending a password, the encrypted value is the same each time. This allows an attacker to intercept
and replay the data.



To fix this, something like Galois/Counter Mode (GCM) should be used instead.




Code at risk:
    
Cipher c = Cipher.getInstance("AES/ECB/NoPadding");
c.init(Cipher.ENCRYPT_MODE, k, iv);
byte[] cipherText = c.doFinal(plainText);





    Solution:
    
Cipher c = Cipher.getInstance("AES/GCM/NoPadding");
c.init(Cipher.ENCRYPT_MODE, k, iv);
byte[] cipherText = c.doFinal(plainText);







References

Wikipedia: Authenticated encryption

NIST: Authenticated Encryption Modes

Wikipedia: Block cipher modes of operation

NIST: Recommendation for Block Cipher Modes of Operation
CWE-327: Use of a Broken or Risky Cryptographic Algorithm




        

        

        

    

    
    

        
        

            Cipher is susceptible to Padding Oracle
            
        

        
Bug Pattern: PADDING_ORACLE


        
            


    This specific mode of CBC with PKCS5Padding is susceptible to padding oracle attacks. An adversary could potentially decrypt the
    message if the system exposed the difference between plaintext with invalid padding or valid padding. The distinction between
    valid and invalid padding is usually revealed through distinct error messages being returned for each condition.




    Code at risk:
    
Cipher c = Cipher.getInstance("AES/CBC/PKCS5Padding");
c.init(Cipher.ENCRYPT_MODE, k, iv);
byte[] cipherText = c.doFinal(plainText);





    Solution:
    
Cipher c = Cipher.getInstance("AES/GCM/NoPadding");
c.init(Cipher.ENCRYPT_MODE, k, iv);
byte[] cipherText = c.doFinal(plainText);







    References

    Padding Oracles for the masses (by Matias Soler)

    Wikipedia: Authenticated encryption

    NIST: Authenticated Encryption Modes

    CAPEC: Padding Oracle Crypto Attack

    CWE-696: Incorrect Behavior Order
    CWE-326: Inadequate Encryption Strength



        

        

        

    

    
    

        
        

            Cipher with no integrity
            
        

        
Bug Pattern: CIPHER_INTEGRITY


        
            


    The ciphertext produced is susceptible to alteration by an adversary. This mean that the cipher provides no way to detect that the
    data has been tampered with. If the ciphertext can be controlled by an attacker, it could be altered without detection.




    The solution is to use a cipher that includes a Hash based Message Authentication Code (HMAC) to sign the data. Combining a HMAC function to the
    existing cipher is prone to error [1]. Specifically,
    it is always recommended that you be able to verify the HMAC first, and only if the data is unmodified, do you then perform any cryptographic
    functions on the data.



The following modes are vulnerable because they don't provide a HMAC:

    - CBC

    - OFB

    - CTR

    - ECB


    The following snippets code are some examples of vulnerable code.


    Code at risk:

    AES in CBC mode


    
Cipher c = Cipher.getInstance("AES/CBC/PKCS5Padding");
c.init(Cipher.ENCRYPT_MODE, k, iv);
byte[] cipherText = c.doFinal(plainText);
    

    Triple DES with ECB mode


Cipher c = Cipher.getInstance("DESede/ECB/PKCS5Padding");
c.init(Cipher.ENCRYPT_MODE, k, iv);
byte[] cipherText = c.doFinal(plainText);





    Solution:
    
Cipher c = Cipher.getInstance("AES/GCM/NoPadding");
c.init(Cipher.ENCRYPT_MODE, k, iv);
byte[] cipherText = c.doFinal(plainText);





In the example solution above, the GCM mode introduces an HMAC into the resulting encrypted data, providing integrity of the result.






    References

    Wikipedia: Authenticated encryption

    NIST: Authenticated Encryption Modes

    Moxie Marlinspike's blog: The Cryptographic Doom Principle

    CWE-353: Missing Support for Integrity Check



        

        

        

    

    
    

        
        

            Use of ESAPI Encryptor
            
        

        
Bug Pattern: ESAPI_ENCRYPTOR


        
            


    The ESAPI has a small history of vulnerabilities within the cryptography component. Here is a quick validation list to
    make sure the Authenticated Encryption is working as expected.



1. Library Version



    This issue is corrected in ESAPI version 2.1.0. Versions <= 2.0.1 are vulnerable to a MAC bypass (CVE-2013-5679).





    For Maven users, the plugin versions can be called using the
    following command. The effective version of ESAPI will be available in the output.

    
$ mvn versions:display-dependency-updates
    
Output:

    [...]
[INFO] The following dependencies in Dependencies have newer versions:
[INFO]   org.slf4j:slf4j-api ................................... 1.6.4 -> 1.7.7
[INFO]   org.owasp.esapi:esapi ................................. 2.0.1 -> 2.1.0
[...]
    





    or by looking at the configuration directly.

    
<dependency>
    <groupId>org.owasp.esapi</groupId>
    <artifactId>esapi</artifactId>
    <version>2.1.0</version>
</dependency>





    For Ant users, the jar used should be esapi-2.1.0.jar.



2. Configuration:

    

    The library version 2.1.0 is still vulnerable to key size being changed in the ciphertext definition (CVE-2013-5960). Some precautions need to be taken.

    

    

The cryptographic configuration of ESAPI can also be vulnerable if any of these elements are present:

    Insecure configuration:

    Encryptor.CipherText.useMAC=false

Encryptor.EncryptionAlgorithm=AES
Encryptor.CipherTransformation=AES/CBC/PKCS5Padding

Encryptor.cipher_modes.additional_allowed=CBC
    






    


    Secure configuration:

    #Needed
Encryptor.CipherText.useMAC=true

#Needed to have a solid auth. encryption
Encryptor.EncryptionAlgorithm=AES
Encryptor.CipherTransformation=AES/GCM/NoPadding

#CBC mode should be removed to avoid padding oracle
Encryptor.cipher_modes.additional_allowed=
    








    References

    ESAPI Security bulletin 1 (CVE-2013-5679)

    Vulnerability Summary for CVE-2013-5679

    Synactiv: Bypassing HMAC validation in OWASP ESAPI symmetric encryption

    CWE-310: Cryptographic Issues

    ESAPI-dev mailing list: Status of CVE-2013-5960




        

        

        

    

    
    

        
        

            External file access (Android)
            
        

        
Bug Pattern: ANDROID_EXTERNAL_FILE_ACCESS


        
            


    The application write data to external storage (potentially SD card). There are multiple security implication to this
    action. First, file store on SD card will be accessible to the application having the
    READ_EXTERNAL_STORAGE permission.
    Also, if the data persisted contains confidential information about the user, encryption would be needed.




    Code at risk:


file file = new File(getExternalFilesDir(TARGET_TYPE), filename);
fos = new FileOutputStream(file);
fos.write(confidentialData.getBytes());
fos.flush();






    Better alternative:


fos = openFileOutput(filename, Context.MODE_PRIVATE);
fos.write(string.getBytes());








    References

    Android Official Doc: Security Tips

    CERT: DRD00-J: Do not store sensitive information on external storage [...]

    Android Official Doc: Using the External Storage

    OWASP Mobile Top 10 2014-M2: Insecure Data Storage

    CWE-276: Incorrect Default Permissions
    CWE-312: Cleartext Storage of Sensitive Information



        

        

        

    

    
    

        
        

            Broadcast (Android)
            
        

        
Bug Pattern: ANDROID_BROADCAST


        
            


    Broadcast intents can be listened by any application with the appropriate permission. It is suggested to avoid transmitting
    sensitive information when possible.




    Code at risk:


Intent i = new Intent();
i.setAction("com.insecure.action.UserConnected");
i.putExtra("username", user);
i.putExtra("email", email);
i.putExtra("session", newSessionId);

this.sendBroadcast(v1);








    Solution (if possible):


Intent i = new Intent();
i.setAction("com.secure.action.UserConnected");

sendBroadcast(v1);








    Configuration (receiver)[1] Source: StackOverflow:


<manifest ...>

    <!-- Permission declaration -->
    <permission android:name="my.app.PERMISSION" />

    <receiver
        android:name="my.app.BroadcastReceiver"
        android:permission="my.app.PERMISSION"> <!-- Permission enforcement -->
        <intent-filter>
            <action android:name="com.secure.action.UserConnected" />
        </intent-filter>
    </receiver>

    ...
</manifest>






    Configuration (sender)[1] Source: StackOverflow:


<manifest>
    <!-- We declare we own the permission to send broadcast to the above receiver -->
    <uses-permission android:name="my.app.PERMISSION"/>

    <!-- With the following configuration, both the sender and the receiver apps need to be signed by the same developer certificate. -->
    <permission android:name="my.app.PERMISSION" android:protectionLevel="signature"/>
</manifest>








    References

    CERT: DRD03-J. Do not broadcast sensitive information using an implicit intent

    Android Official Doc: BroadcastReceiver (Security)

    Android Official Doc: Receiver configuration (see android:permission)

    [1] StackOverflow: How to set permissions in broadcast sender and receiver in android

    CWE-276: Incorrect Default Permissions

    CWE-925: Improper Verification of Intent by Broadcast Receiver

    CWE-927: Use of Implicit Intent for Sensitive Communication



        

        

        

    

    
    

        
        

            World writable file (Android)
            
        

        
Bug Pattern: ANDROID_WORLD_WRITABLE


        
            


    The file written in this context is using the creation mode MODE_WORLD_READABLE. It might not be the
    expected behavior to expose the content being written.




    Code at risk:


fos = openFileOutput(filename, MODE_WORLD_READABLE);
fos.write(userInfo.getBytes());








    Solution (using MODE_PRIVATE):


fos = openFileOutput(filename, MODE_PRIVATE);






    Solution (using local SQLite Database):


Using a local SQLite database is probably the best solution to store structured data. Make sure the database file is not
create on external storage. See references below for implementation guidelines.






    References

    CERT: DRD11-J. Ensure that sensitive data is kept secure

    Android Official Doc: Security Tips

    Android Official Doc: Context.MODE_PRIVATE

    vogella.com: Android SQLite database and content provider - Tutorial

    vogella.com: Android SQLite database and content provider - Tutorial

    OWASP Mobile Top 10 2014-M2: Insecure Data Storage

    CWE-276: Incorrect Default Permissions
    CWE-312: Cleartext Storage of Sensitive Information



        

        

        

    

    
    

        
        

            WebView with geolocation activated (Android)
            
        

        
Bug Pattern: ANDROID_GEOLOCATION


        
            


    It is suggested to ask the user for a confirmation about obtaining its geolocation.




    Code at risk:


webView.setWebChromeClient(new WebChromeClient() {
    @Override
    public void onGeolocationPermissionsShowPrompt(String origin, GeolocationPermissions.Callback callback) {
        callback.invoke(origin, true, false);
    }
});






    Suggested code:


    Limit the sampling of geolocation and ask the user for confirmation.

webView.setWebChromeClient(new WebChromeClient() {
    @Override
    public void onGeolocationPermissionsShowPrompt(String origin, GeolocationPermissions.Callback callback) {
        callback.invoke(origin, true, false);

        //Ask the user for confirmation
    }
});








    References

    CERT: DRD15-J. Consider privacy concerns when using Geolocation API

    Wikipedia: W3C Geolocation API

    W3C: Geolocation Specification

    CWE-359: Exposure of Private Personal Information to an Unauthorized Actor



        

        

        

    

    
    

        
        

            WebView with JavaScript enabled (Android)
            
        

        
Bug Pattern: ANDROID_WEB_VIEW_JAVASCRIPT


        
            


    Enabling JavaScript for the WebView means that it is now susceptible to XSS. The page render should be inspected
    for potential reflected XSS, stored XSS and DOM XSS.


WebView myWebView = (WebView) findViewById(R.id.webView);
WebSettings webSettings = myWebView.getSettings();
webSettings.setJavaScriptEnabled(true);







    Code at risk:

Enabling JavaScript is not a bad practice. It just means that the backend code need to be audited for potential XSS.
The XSS can also be introduced client-side with DOM XSS.

function updateDescription(newDescription) {
    $("#userDescription").html("<p>"+newDescription+"</p>");
}








    References

    Issue: Using setJavaScriptEnabled can introduce XSS vulnerabilities

    Android Official Doc: WebView

    WASC-8: Cross Site Scripting

    OWASP: XSS Prevention Cheat Sheet

    OWASP: Top 10 2013-A3: Cross-Site Scripting (XSS)

    CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')



        

        

        

    

    
    

        
        

            WebView with JavaScript interface (Android)
            
        

        
Bug Pattern: ANDROID_WEB_VIEW_JAVASCRIPT_INTERFACE


        
            


    The use of JavaScript Interface could expose the WebView to risky API. If an XSS is triggered in the WebView, the class
    could be called by the malicious JavaScript code.





    Code at risk:

    
WebView myWebView = (WebView) findViewById(R.id.webView);

myWebView.addJavascriptInterface(new FileWriteUtil(this), "fileWriteUtil");

WebSettings webSettings = myWebView.getSettings();
webSettings.setJavaScriptEnabled(true);

[...]
class FileWriteUtil {
    Context mContext;

    FileOpenUtil(Context c) {
        mContext = c;
    }

    public void writeToFile(String data, String filename, String tag) {
        [...]
    }
}
    







    References

    Android Official Doc: WebView.addJavascriptInterface()

    CWE-285: Improper Authorization
    CWE-749: Exposed Dangerous Method or Function



        

        

        

    

    
    

        
        

            Cookie without the secure flag
            
        

        
Bug Pattern: INSECURE_COOKIE


        
            


A new cookie is created without the Secure flag set.
The Secure flag is a directive to the browser to make sure that the cookie is not sent for insecure
communication (http://).





Code at risk:


Cookie cookie = new Cookie("userName",userName);
response.addCookie(cookie);







Solution (Specific configuration):


Cookie cookie = new Cookie("userName",userName);
cookie.setSecure(true); // Secure flag
cookie.setHttpOnly(true);







Solution (Servlet 3.0 configuration):


<web-app xmlns="http://java.sun.com/xml/ns/javaee" version="3.0">
[...]
<session-config>
 <cookie-config>
  <http-only>true</http-only>
  <secure>true</secure>
 </cookie-config>
</session-config>
</web-app>








Reference

CWE-614: Sensitive Cookie in HTTPS Session Without 'Secure' Attribute

CWE-315: Cleartext Storage of Sensitive Information in a Cookie

CWE-311: Missing Encryption of Sensitive Data

OWASP: Secure Flag

Rapid7: Missing Secure Flag From SSL Cookie



        

        

        

    

    
    

        
        

            Cookie without the HttpOnly flag
            
        

        
Bug Pattern: HTTPONLY_COOKIE


        
            


A new cookie is created without the HttpOnly flag set.
The HttpOnly flag is a directive to the browser to make sure that the cookie can not be red by
malicious script. When a user is the target of a "Cross-Site Scripting", the attacker would benefit greatly from getting
the session id for example.





Code at risk:


Cookie cookie = new Cookie("email",userName);
response.addCookie(cookie);







Solution (Specific configuration):


Cookie cookie = new Cookie("email",userName);
cookie.setSecure(true);
cookie.setHttpOnly(true); //HttpOnly flag







Solution (Servlet 3.0 configuration):


<web-app xmlns="http://java.sun.com/xml/ns/javaee" version="3.0">
[...]
<session-config>
 <cookie-config>
  <http-only>true</http-only>
  <secure>true</secure>
 </cookie-config>
</session-config>
</web-app>








Reference

Coding Horror blog: Protecting Your Cookies: HttpOnly

OWASP: HttpOnly

Rapid7: Missing HttpOnly Flag From Cookie
CWE-1004: Sensitive Cookie Without 'HttpOnly' Flag




        

        

        

    

    
    

        
        

            Object deserialization is used
            
        

        
Bug Pattern: OBJECT_DESERIALIZATION


        
            


    Object deserialization of untrusted data can lead to remote code execution, if there is a class in classpath that allows
    the trigger of malicious operation.




    Libraries developers tend to fix class that provided potential malicious trigger. There are still classes that are
    known to trigger Denial of Service[1].




    Deserialization is a sensible operation that has a great history of vulnerabilities. The web application might
    become vulnerable as soon as a new vulnerability is found in the Java Virtual Machine[2] [3].





Code at risk:


public UserData deserializeObject(InputStream receivedFile) throws IOException, ClassNotFoundException {

    try (ObjectInputStream in = new ObjectInputStream(receivedFile)) {
        return (UserData) in.readObject();
    }
}







Solutions:




Avoid deserializing object provided by remote users.






References

CWE-502: Deserialization of Untrusted Data

Deserialization of untrusted data

Serialization and Deserialization 

A tool for generating payloads that exploit unsafe Java object deserialization

[1] Example of Denial of Service using the class java.util.HashSet

[2] OpenJDK: Deserialization issue in ObjectInputStream.readSerialData() (CVE-2015-2590)

[3] Rapid7: Sun Java Calendar Deserialization Privilege Escalation (CVE-2008-5353)



        

        

        

    

    
    

        
        

            Unsafe Jackson deserialization configuration
            
        

        
Bug Pattern: JACKSON_UNSAFE_DESERIALIZATION


        
            

When the Jackson databind library is used incorrectly the deserialization of untrusted data can lead to remote code execution, if there is a class in classpath that allows the trigger of malicious operation.




Solutions:




Explicitly define what types and subtypes you want to be available when using polymorphism through JsonTypeInfo.Id.NAME.
Also, never call ObjectMapper.enableDefaultTyping (and then readValue a type that holds an Object or Serializable or Comparable or a known deserialization type).





Code at risk:


public class Example {
    static class ABean {
        public int id;
        public Object obj;
    }

    static class AnotherBean {
        @JsonTypeInfo(use = JsonTypeInfo.Id.CLASS) // or JsonTypeInfo.Id.MINIMAL_CLASS
        public Object obj;
    }

    public void example(String json) throws JsonMappingException {
         ObjectMapper mapper = new ObjectMapper();
         mapper.enableDefaultTyping();
         mapper.readValue(json, ABean.class);
    }

    public void exampleTwo(String json) throws JsonMappingException {
         ObjectMapper mapper = new ObjectMapper();
         mapper.readValue(json, AnotherBean.class);
    }

}







References

Jackson Deserializer security vulnerability

Java Unmarshaller Security - Turning your data into code execution

CWE-502: Deserialization of Untrusted Data




        

        

        

    

    
    

        
        

            This class could be used as deserialization gadget
            
        

        
Bug Pattern: DESERIALIZATION_GADGET


        
            


Deserialization gadget are class that could be used by an attacker to take advantage of a remote API using Native Serialization.
This class is either adding custom behavior to deserialization with the readObject method (Serializable) or can be called
 from a serialized object (InvocationHandler).




This detector is intended to be used mostly by researcher. The real issue is using deserialization for remote operation.
Removing gadget is a hardening practice to reduce the risk of being exploited.




References

CWE-502: Deserialization of Untrusted Data

Deserialization of untrusted data

Serialization and Deserialization 

A tool for generating payloads that exploit unsafe Java object deserialization

[1] Example of Denial of Service using the class java.util.HashSet

[2] OpenJDK: Deserialization issue in ObjectInputStream.readSerialData() (CVE-2015-2590)

[3] Rapid7: Sun Java Calendar Deserialization Privilege Escalation (CVE-2008-5353)



        

        

        

    

    
    

        
        

            Trust Boundary Violation
            
        

        
Bug Pattern: TRUST_BOUNDARY_VIOLATION


        
            


    "A trust boundary can be thought of as line drawn through a program. On one side of the line, data is untrusted.
    On the other side of the line, data is assumed to be trustworthy. The purpose of validation logic is to allow data
    to safely cross the trust boundary - to move from untrusted to trusted. A trust boundary violation occurs when a
    program blurs the line between what is trusted and what is untrusted. By combining trusted and untrusted data in the
    same data structure, it becomes easier for programmers to mistakenly trust unvalidated data." [1]





Code at risk:


public void doSomething(HttpServletRequest req, String activateProperty) {
    //..

    req.getSession().setAttribute(activateProperty,"true");

}



public void loginEvent(HttpServletRequest req, String userSubmitted) {
    //..

    req.getSession().setAttribute("user",userSubmitted);
}







Solution:




The solution would be to add validation prior setting a new session attribute. When possible, prefer data from
safe location rather than using direct user input.






References

[1] CWE-501: Trust Boundary Violation

OWASP : Trust Boundary Violation



        

        

        

    

    
    

        
        

            A malicious XSLT could be provided to the JSP tag
            
        

        
Bug Pattern: JSP_XSLT


        
            


    "XSLT (Extensible Stylesheet Language Transformations) is a language for transforming XML documents into other XML documents".[1]

    It is possible to attach malicious behavior to those style sheets. Therefore, if an attacker can control the content or the source of the
    style sheet, he might be able to trigger remote code execution.[2]




Code at risk:


<x:transform xml="${xmlData}" xslt="${xsltControlledByUser}" />






Solution:




The solution would be to make sure the style sheet is loaded from a safe sources and make sure that vulnerabilities such as
Path traversal [3][4] are not possible.




References

[1] Wikipedia: XSLT (Extensible Stylesheet Language Transformations)

Offensive XSLT by Nicolas Grégoire

[2] From XSLT code execution to Meterpreter shells by Nicolas Grégoire

XSLT Hacking Encyclopedia by Nicolas Grégoire

Acunetix.com : The hidden dangers of XSLTProcessor - Remote XSL injection

w3.org XSL Transformations (XSLT) Version 1.0 : w3c specification

[3] WASC: Path Traversal

[4] OWASP: Path Traversal

CWE-94: Improper Control of Generation of Code ('Code Injection')



            
        

        

        

    

    
    

        
        

            A malicious XSLT could be provided
            
        

        
Bug Pattern: MALICIOUS_XSLT


        
            


    "XSLT (Extensible Stylesheet Language Transformations) is a language for transforming XML documents into other XML documents".[1]

    It is possible to attach malicious behavior to those style sheets. Therefore, if an attacker can control the content or the source of the
    style sheet, he might be able to trigger remote code execution.[2]




Code at risk:


Source xslt = new StreamSource(new FileInputStream(inputUserFile)); //Dangerous source

Transformer transformer = TransformerFactory.newInstance().newTransformer(xslt);

Source text = new StreamSource(new FileInputStream("/data_2_process.xml"));
transformer.transform(text, new StreamResult(...));






Solution:




The solution is to enable the secure processing mode which will block potential reference to Java classes such as java.lang.Runtime.


TransformerFactory factory = TransformerFactory.newInstance();
factory.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true);
Source xslt  = new StreamSource(new FileInputStream(inputUserFile));

Transformer transformer = factory.newTransformer(xslt);




Alternatively, make sure the style sheet is loaded from a safe sources and make sure that vulnerabilities such as
Path traversal [3][4] are not possible.




References

[1] Wikipedia: XSLT (Extensible Stylesheet Language Transformations)

Offensive XSLT by Nicolas Grégoire

[2] From XSLT code execution to Meterpreter shells by Nicolas Grégoire

XSLT Hacking Encyclopedia by Nicolas Grégoire

Acunetix.com : The hidden dangers of XSLTProcessor - Remote XSL injection

w3.org XSL Transformations (XSLT) Version 1.0 : w3c specification

[3] WASC: Path Traversal

[4] OWASP: Path Traversal

CWE-94: Improper Control of Generation of Code ('Code Injection')



            
        

        

        

    

    
    

        
        

            Potential information leakage in Scala Play
            
        

        
Bug Pattern: SCALA_SENSITIVE_DATA_EXPOSURE


        
            


    Applications can unintentionally leak information about their configuration, internal workings, or violate privacy through a
    variety of application problems. [1] Pages that provide different responses based on the validity of the data can
    lead to Information Leakage; specifically when data deemed confidential is being revealed as a result of the web application's
    design. [2]




    Examples of sensitive data includes (but is not limited to): API keys, passwords, product versions or environment configurations.




Code at risk:


def doGet(value:String) = Action {
  val configElement = configuration.underlying.getString(value)

  Ok("Hello "+ configElement +" !")
}





    Application configuration elements should not be sent in the response content and users should not be allowed to control which
    configuration elements will be used by the code.


References

OWASP: Top 10 2013-A6-Sensitive Data Exposure

[1] OWASP: Top 10 2007-Information Leakage and Improper Error Handling

[2] WASC-13: Information Leakage

CWE-200: Information Exposure




            
        

        

        

    

    
    

        
        

            Scala Play Server-Side Request Forgery (SSRF)
            
        

        
Bug Pattern: SCALA_PLAY_SSRF


        
            


    Server-Side Request Forgery occur when a web server executes a request to a user supplied destination
    parameter that is not validated. Such vulnerabilities could allow an attacker to access internal services
    or to launch attacks from your web server.




    Vulnerable Code:

def doGet(value:String) = Action {
    WS.url(value).get().map { response =>
        Ok(response.body)
    }
}





    Solution/Countermeasures:

    


        
Don't accept request destinations from users

        
Accept a destination key, and use it to look up the target (legal) destination

        
White list URLs (if possible)

        
Validate that the beginning of the URL is part of a white list

    








References

CWE-918: Server-Side Request Forgery (SSRF)

Understanding Server-Side Request Forgery



            

        

        

    

    
    

        
        

            URLConnection Server-Side Request Forgery (SSRF) and File Disclosure
            
        

        
Bug Pattern: URLCONNECTION_SSRF_FD


        
            


    Server-Side Request Forgery occur when a web server executes a request to a user supplied destination
    parameter that is not validated. Such vulnerabilities could allow an attacker to access internal services
    or to launch attacks from your web server.




    URLConnection can be used with file:// protocol or other protocols to access local filesystem and potentially other services.



    Vulnerable Code:

new URL(String url).openConnection()


new URL(String url).openStream()


new URL(String url).getContent()






    Solution/Countermeasures:

    


        
Don't accept URL destinations from users

        
Accept a destination key, and use it to look up the target destination associate with the key

        
White list URLs (if possible)

        
Validate that the beginning of the URL is part of a white list

    








References

CWE-918: Server-Side Request Forgery (SSRF)

Understanding Server-Side Request Forgery

CWE-73: External Control of File Name or Path

Abusing jar:// downloads



            

        

        

    

    
    

        
        

            Potential XSS in Scala Twirl template engine
            
        

        
Bug Pattern: SCALA_XSS_TWIRL


        
            


A potential XSS was found. It could be used to execute unwanted JavaScript in a client's browser. (See references)




    Vulnerable Code:

@(value: Html)

@value





    Solution:

@(value: String)

@value





The best defense against XSS is context sensitive output encoding like the example above. There are typically 4 contexts to consider:
HTML, JavaScript, CSS (styles), and URLs. Please follow the XSS protection rules defined in the OWASP XSS Prevention Cheat Sheet,
which explains these defenses in significant detail.






References

WASC-8: Cross Site Scripting

OWASP: XSS Prevention Cheat Sheet

OWASP: Top 10 2013-A3: Cross-Site Scripting (XSS)

CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')

OWASP Java Encoder



            
        

        

        

    

    
    

        
        

            Potential XSS in Scala MVC API engine
            
        

        
Bug Pattern: SCALA_XSS_MVC_API


        
            


A potential XSS was found. It could be used to execute unwanted JavaScript in a client's browser. (See references)




    Vulnerable Code:

def doGet(value:String) = Action {
    Ok("Hello " + value + " !").as("text/html")
  }





    Solution:

def doGet(value:String) = Action {
    Ok("Hello " + Encode.forHtml(value) + " !")
  }





The best defense against XSS is context sensitive output encoding like the example above. There are typically 4 contexts to consider:
HTML, JavaScript, CSS (styles), and URLs. Please follow the XSS protection rules defined in the OWASP XSS Prevention Cheat Sheet,
which explains these defenses in significant detail.






References

WASC-8: Cross Site Scripting

OWASP: XSS Prevention Cheat Sheet

OWASP: Top 10 2013-A3: Cross-Site Scripting (XSS)

CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')

OWASP Java Encoder



            
        

        

        

    

    
    

        
        

            Potential template injection with Velocity
            
        

        
Bug Pattern: TEMPLATE_INJECTION_VELOCITY


        
            


Velocity template engine is powerful. It is possible to add logic including condition statements, loops and external calls.
It is not designed to be a sandbox to templating operations. A malicious user in control of a template can run malicious code
on the server-side. Velocity templates should be seen as scripts.




    Vulnerable Code:

[...]

Velocity.evaluate(context, swOut, "test", userInput);





    Solution:


Avoid letting end users manipulate templates with Velocity. If you need to expose template editing to your users,
prefer logic-less template engines such as Handlebars or Moustache (See references).






References

PortSwigger: Server-Side Template Injection 

Handlebars.java

CWE-94: Improper Control of Generation of Code ('Code Injection')



            
        

        

        

    

    
    

        
        

            Potential template injection with Freemarker
            
        

        
Bug Pattern: TEMPLATE_INJECTION_FREEMARKER


        
            


Freemarker template engine is powerful. It is possible to add logic including condition statements, loops and external calls.
It is not design to be sandbox to templating operations. A malicious user in control of a template can run malicious code
on the server-side. Freemarker templates should be seen as scripts.




    Vulnerable Code:

Template template = cfg.getTemplate(inputTemplate);
[...]
template.process(data, swOut);





    Solution:


Avoid letting end users manipulate templates with Freemarker. If you need to expose template editing to your users,
prefer logic-less template engines such as Handlebars or Moustache (See references).






References

PortSwigger: Server-Side Template Injection

Handlebars.java

CWE-94: Improper Control of Generation of Code ('Code Injection')



            
        

        

        

    

    
    

        
        

            Potential template injection with Pebble
            
        

        
Bug Pattern: TEMPLATE_INJECTION_PEBBLE


        
            


Pebble template engine is powerful. It is possible to add logic including condition statements, loops and external calls.
It is not design to be sandbox to templating operations. A malicious user in control of a template can run malicious code
on the server-side. Pebble templates should be seen as scripts.




    Vulnerable Code:

PebbleTemplate compiledTemplate = engine.getLiteralTemplate(inputFile);
[...]
compiledTemplate.evaluate(writer, context);





    Solution:


Avoid letting end users manipulate templates with Pebble. If you need to expose template editing to your users,
prefer logic-less template engines such as Handlebars or Moustache (See references).






References

Server Side Template Injection – on the example of Pebble by Michał Bentkowski

PortSwigger: Server-Side Template Injection

Handlebars.java

CWE-94: Improper Control of Generation of Code ('Code Injection')



            
        

        

        

    

    
    

        
        

            Overly permissive CORS policy
            
        

        
Bug Pattern: PERMISSIVE_CORS


        
            


Prior to HTML5, Web browsers enforced the Same Origin Policy which ensures that in order for JavaScript to access the contents of a Web page, both the JavaScript and the Web page must originate from the same domain. Without the Same Origin Policy, a malicious website could serve up JavaScript that loads sensitive information from other websites using a client's credentials, cull through it, and communicate it back to the attacker. HTML5 makes it possible for JavaScript to access data across domains if a new HTTP header called Access-Control-Allow-Origin is defined. With this header, a Web server defines which other domains are allowed to access its domain using cross-origin requests. However, caution should be taken when defining the header because an overly permissive CORS policy will allow a malicious application to communicate with the victim application in an inappropriate way, leading to spoofing, data theft, relay and other attacks.




    Vulnerable Code:

response.addHeader("Access-Control-Allow-Origin", "*");





    Solution:


Avoid using * as the value of the Access-Control-Allow-Origin header, which indicates that the application's data is accessible to JavaScript running on any domain.






References

W3C Cross-Origin Resource Sharing

Enable Cross-Origin Resource Sharing

CWE-942: Permissive Cross-domain Policy with Untrusted Domains



        

        

        

    

    
    

        
        

            Anonymous LDAP bind
            
        

        
Bug Pattern: LDAP_ANONYMOUS


        
            


Without proper access control, executing an LDAP statement that contains a user-controlled value can allow an attacker to abuse poorly configured LDAP context.
All LDAP queries executed against the context will be performed without authentication and access control.
An attacker may be able to manipulate one of these queries in an unexpected way to gain access to records that would otherwise be protected by the directory's access control mechanism.




    Vulnerable Code:

...
env.put(Context.SECURITY_AUTHENTICATION, "none");
DirContext ctx = new InitialDirContext(env);
...





    Solution:


Consider other modes of authentication to LDAP and ensure proper access control mechanism.







References

Ldap Authentication Mechanisms



            
        

        

        

    

    
    

        
        

            LDAP Entry Poisoning
            
        

        
Bug Pattern: LDAP_ENTRY_POISONING


        
            


JNDI API support the binding of serialize object in LDAP directories. If certain attributes are presented, the deserialization
of object will be made in the application querying the directory (See Black Hat USA 2016 white paper for details).
Object deserialization should be consider a risky operation that can lead to remote code execution.




The exploitation of the vulnerability will be possible if the attacker has an entry point in an LDAP base query, by adding
attributes to an existing LDAP entry or by configuring the application to use a malicious LDAP server.




    Vulnerable Code:

DirContext ctx = new InitialDirContext();
//[...]

ctx.search(query, filter,
        new SearchControls(scope, countLimit, timeLimit, attributes,
            true, //Enable object deserialization if bound in directory
            deref));






    Solution:

DirContext ctx = new InitialDirContext();
//[...]

ctx.search(query, filter,
        new SearchControls(scope, countLimit, timeLimit, attributes,
            false, //Disable
            deref));








References

Black Hat USA 2016: A Journey From JNDI/LDAP Manipulation to Remote Code Execution Dream Land
(slides & video) by Alvaro Muñoz and Oleksandr Mirosh

HP Enterprise: Introducing JNDI Injection and LDAP Entry Poisoning by Alvaro Muñoz

TrendMicro: How The Pawn Storm Zero-Day Evaded Java's Click-to-Play Protection by Jack Tang
CWE-90: Improper Neutralization of Special Elements used in an LDAP Query ('LDAP Injection')



            
        

        

        

    

    
    

        
        

            Persistent Cookie Usage
            
        

        
Bug Pattern: COOKIE_PERSISTENT


        
            


Storing sensitive data in a persistent cookie for an extended period can lead to a breach of confidentiality or account compromise.




    Explanation:

If private information is stored in persistent cookies, attackers have a larger time window in which to steal this data - especially since persistent cookies are often set to expire in the distant future. Persistent cookies are generally stored in a text file on the client and an attacker with access to the victim's machine can steal this information.

Persistent cookies are often used to profile users as they interact with a site. Depending on what is done with this tracking data, it is possible to use persistent cookies to violate users' privacy.




    Vulnerable Code: The following code sets a cookie to expire in 1 year.


[...]
Cookie cookie = new Cookie("email", email);
cookie.setMaxAge(60*60*24*365);
[...]





    Solution:




    
Use persistent cookies only if necessary and limit their maximum age.

    
Don't use persistent cookies for sensitive data.










References

Class Cookie setMaxAge documentation

CWE-539: Information Exposure Through Persistent Cookies



            
        

        

        

    

    
    

        
        

            URL rewriting method
            
        

        
Bug Pattern: URL_REWRITING


        
            


The implementation of this method includes the logic to determine whether the session ID needs to be encoded in the URL.

URL rewriting has significant security risks. Since session ID appears in the URL, it may be easily seen by third parties. Session ID in the URL can be disclosed in many ways, for example:




    
Log files,

    
The browser history,

    
By copy-and-pasting it into an e-mail or posting,

    
The HTTP Referrer.








    Vulnerable Code:


out.println("Click <a href=" +
                res.encodeURL(HttpUtils.getRequestURL(req).toString()) +
                ">here</a>");





    Solution:

Avoid using those methods. If you are looking to encode a URL String or form parameters do not confuse the URL rewriting methods with the URLEncoder class.






References

OWASP Top 10 2010-A3-Broken Authentication and Session Management

CWE-601: URL Redirection to Untrusted Site ('Open Redirect')



            
        

        

        

    

    
    

        
        

            Insecure SMTP SSL connection
            
        

        
Bug Pattern: INSECURE_SMTP_SSL


        
            


Server identity verification is disabled when making SSL connections. Some email libraries that enable SSL connections do not verify the server certificate by default. This is equivalent to trusting all certificates.
When trying to connect to the server, this application would readily accept a certificate issued to "victim.com".
The application would now potentially leak sensitive user information on a broken SSL connection to the victim server.




    Vulnerable Code:


...
Email email = new SimpleEmail();
email.setHostName("smtp.servermail.com");
email.setSmtpPort(465);
email.setAuthenticator(new DefaultAuthenticator(username, password));
email.setSSLOnConnect(true);
email.setFrom("user@gmail.com");
email.setSubject("TestMail");
email.setMsg("This is a test mail ... :-)");
email.addTo("foo@bar.com");
email.send();
...





    Solution:

Please add the following check to verify the server certificate:

email.setSSLCheckServerIdentity(true);







References

CWE-297: Improper Validation of Certificate with Host Mismatch



            
        

        

        

    

    
    

        
        

            AWS Query Injection
            
        

        
Bug Pattern: AWS_QUERY_INJECTION


        
            


Constructing SimpleDB queries containing user input can allow an attacker to view unauthorized records.

The following example dynamically constructs and executes a SimpleDB SELECT query allowing the user to specify the productCategory. The attacker can modify the query, bypass the required authentication for customerID and view records matching any customer.




    Vulnerable Code:


...
String customerID = getAuthenticatedCustomerID(customerName, customerCredentials);
String productCategory = request.getParameter("productCategory");
...
AmazonSimpleDBClient sdbc = new AmazonSimpleDBClient(appAWSCredentials);
String query = "select * from invoices where productCategory = '"
            + productCategory + "' and customerID = '"
            + customerID + "' order by '"
            + sortColumn + "' asc";
SelectResult sdbResult = sdbc.select(new SelectRequest(query));






    Solution:

This issue is analogical to SQL Injection. Sanitize user input before using it in a SimpleDB query.






References

CWE-943: Improper Neutralization of Special Elements in Data Query Logic



            
        

        

        

    

    
    

        
        

            JavaBeans Property Injection
            
        

        
Bug Pattern: BEAN_PROPERTY_INJECTION


        
            


An attacker can set arbitrary bean properties that can compromise system integrity.
Bean population functions allow to set a bean property or a nested property.
An attacker can leverage this functionality to access special bean properties like class.classLoader that will allow him to override system properties and potentially execute arbitrary code.




    Vulnerable Code:


MyBean bean = ...;
HashMap map = new HashMap();
Enumeration names = request.getParameterNames();
while (names.hasMoreElements()) {
    String name = (String) names.nextElement();
    map.put(name, request.getParameterValues(name));
}
BeanUtils.populate(bean, map);





    Solution:

Avoid using user controlled values to populate Bean property names.






References

CWE-15: External Control of System or Configuration Setting



            
        

        

        

    

    
    

        
        

            Struts File Disclosure
            
        

        
Bug Pattern: STRUTS_FILE_DISCLOSURE


        
            


Constructing a server-side redirect path with user input could allow an attacker to download application binaries (including application classes or jar files) or view arbitrary files within protected directories.

An attacker may be able to forge a request parameter to match sensitive file locations. For example, requesting "http://example.com/?returnURL=WEB-INF/applicationContext.xml" would display the application's applicationContext.xml file. The attacker would be able to locate and download the applicationContext.xml referenced in the other configuration files, and even class files or jar files, obtaining sensitive information and launching other types of attacks.




    Vulnerable Code:


...
String returnURL = request.getParameter("returnURL");
Return new ActionForward(returnURL);
...





    Solution:

Avoid constructing server-side redirects using user controlled input.






References

CWE-552: Files or Directories Accessible to External Parties



            
        

        

        

    

    
    

        
        

            Spring File Disclosure
            
        

        
Bug Pattern: SPRING_FILE_DISCLOSURE


        
            


Constructing a server-side redirect path with user input could allow an attacker to download application binaries (including application classes or jar files) or view arbitrary files within protected directories.

An attacker may be able to forge a request parameter to match sensitive file locations. For example, requesting "http://example.com/?returnURL=WEB-INF/applicationContext.xml" would display the application's applicationContext.xml file. The attacker would be able to locate and download the applicationContext.xml referenced in the other configuration files, and even class files or jar files, obtaining sensitive information and launching other types of attacks.




    Vulnerable Code:


...
String returnURL = request.getParameter("returnURL");
return new ModelAndView(returnURL);
...





    Solution:

Avoid constructing server-side redirects using user controlled input.






References

CWE-552: Files or Directories Accessible to External Parties



            
        

        

        

    

    
    

        
        

            RequestDispatcher File Disclosure
            
        

        
Bug Pattern: REQUESTDISPATCHER_FILE_DISCLOSURE


        
            


Constructing a server-side redirect path with user input could allow an attacker to download application binaries (including application classes or jar files) or view arbitrary files within protected directories.

An attacker may be able to forge a request parameter to match sensitive file locations. For example, requesting "http://example.com/?jspFile=../applicationContext.xml%3F" would display the application's applicationContext.xml file. The attacker would be able to locate and download the applicationContext.xml referenced in the other configuration files, and even class files or jar files, obtaining sensitive information and launching other types of attacks.




    Vulnerable Code:


...
String jspFile = request.getParameter("jspFile");
request.getRequestDispatcher("/WEB-INF/jsps/" + jspFile + ".jsp").include(request, response);
...





    Solution:

Avoid constructing server-side redirects using user controlled input.






References

CWE-552: Files or Directories Accessible to External Parties



            
        

        

        

    

    
    

        
        

            Format String Manipulation
            
        

        
Bug Pattern: FORMAT_STRING_MANIPULATION


        
            


Allowing user input to control format parameters could enable an attacker to cause exceptions to be thrown or leak information.

Attackers may be able to modify the format string argument, such that an exception is thrown. If this exception is left uncaught, it may crash the application. Alternatively, if sensitive information is used within the unused arguments, attackers may change the format string to reveal this information.

The example code below lets the user specify the decimal points to which it shows the balance. The user can in fact specify anything causing an exception to be thrown which could lead to application failure. Even more critical within this example, if an attacker can specify the user input "2f %3$s %4$.2", the format string would be "The customer: %s %s has the balance %4$.2f %3$s %4$.2". This would then lead to the sensitive accountNo to be included within the resulting string.




    Vulnerable Code:


Formatter formatter = new Formatter(Locale.US);
String format = "The customer: %s %s has the balance %4$." + userInput + "f";
formatter.format(format, firstName, lastName, accountNo, balance);





    Solution:

Avoid using user controlled values in the format string argument.






References

CWE-134: Use of Externally-Controlled Format String



            
        

        

        

    

    
    

        
        

            HTTP Parameter Pollution
            
        

        
Bug Pattern: HTTP_PARAMETER_POLLUTION


        
            


Concatenating unvalidated user input into a URL can allow an attacker to override the value of a request parameter. Attacker may be able to override existing parameter values, inject a new parameter or exploit variables out of a direct reach. HTTP Parameter Pollution (HPP) attacks consist of injecting encoded query string delimiters into other existing parameters. If a web application does not properly sanitize the user input, a malicious user may compromise the logic of the application to perform either client-side or server-side attacks.

In the following example the programmer has not considered the possibility that an attacker could provide a parameter lang such as en&user_id=1, which would enable him to change the user_id at will.




    Vulnerable Code:


String input = request.getParameter("lang");
GetMethod get = new GetMethod("http://www.host.com/viewDetails");
get.setQueryString("lang=" + input + "&user_id=" + userId);
get.execute();


    Solution:

You can either encode user input before placing it in HTTP parameters or use the
UriBuilder class
from Apache HttpClient.

URIBuilder uriBuilder = new URIBuilder("http://www.host.com/viewDetails");
uriBuilder.addParameter("lang", input);
uriBuilder.addParameter("user_id", userId);

HttpGet httpget = new HttpGet(uriBuilder.build().toString()); //OK








References

CAPEC-460: HTTP Parameter Pollution (HPP)
CWE-235: Improper Handling of Extra Parameters



            
        

        

        

    

    
    

        
        

            Information Exposure Through An Error Message
            
        

        
Bug Pattern: INFORMATION_EXPOSURE_THROUGH_AN_ERROR_MESSAGE


        
            


The sensitive information may be valuable information on its own (such as a password), or it may be useful for launching other, more deadly attacks. If an attack fails, an attacker may use error information provided by the server to launch another more focused attack. For example, an attempt to exploit a path traversal weakness (CWE-22) might yield the full pathname of the installed application. In turn, this could be used to select the proper number of ".." sequences to navigate to the targeted file. An attack using SQL injection (CWE-89) might not initially succeed, but an error message could reveal the malformed query, which would expose query logic and possibly even passwords or other sensitive information used within the query.




    Vulnerable Code:


try {
  out = httpResponse.getOutputStream()
} catch (Exception e) {
  e.printStackTrace(out);
}





References

CWE-209: Information Exposure Through an Error Message

CWE-211: Information Exposure Through Externally-Generated Error Message



            
        

        

        

    

    
    

        
        

            SMTP Header Injection
            
        

        
Bug Pattern: SMTP_HEADER_INJECTION


        
            


Simple Mail Transfer Protocol (SMTP) is a text based protocol used for email delivery.
Like with HTTP, headers are separate by new line separator.
If user input is place in a header line, the application should remove
or replace new line characters (CR / LF).
You should use a safe wrapper such as Apache Common Email
and Simple Java Mail which filter special characters that can lead to header injection.



    Vulnerable Code:




Message message = new MimeMessage(session);
message.setFrom(new InternetAddress("noreply@your-organisation.com"));
message.setRecipients(Message.RecipientType.TO, new InternetAddress[] {new InternetAddress("target@gmail.com")});
message.setSubject(usernameDisplay + " has sent you notification"); //Injectable API
message.setText("Visit your ACME Corp profile for more info.");
Transport.send(message);




    Solution


Use Apache Common Email or Simple Java Mail.




References

OWASP SMTP Injection

CWE-93: Improper Neutralization of CRLF Sequences ('CRLF Injection')

Commons Email: User Guide

Simple Java Mail Website

StackExchange InfoSec: What threats come from CRLF in email generation?



            
        

        

        

    

    
    

        
        

            Enabling extensions in Apache XML RPC server or client.
            
        

        
Bug Pattern: RPC_ENABLED_EXTENSIONS


        
            


Enabling extensions in Apache XML RPC server or client can lead to deserialization vulnerability which would allow an
attacker to execute arbitrary code.


It's recommended not to use setEnabledForExtensions method of org.apache.xmlrpc.client.XmlRpcClientConfigImpl or org.apache.xmlrpc.XmlRpcConfigImpl.
By default, extensions are disabled both on the client and the server.





References


0ang3el's Blog: Beware of WS-XMLRPC library in your Java App

CVE-2016-5003 vulnerability reference



            
        

        

        

    

    
    

        
        

            Disabling HTML escaping put the application at risk for XSS
            
        

        
Bug Pattern: WICKET_XSS1


        
            


Disabling HTML escaping put the application at risk for Cross-Site Scripting (XSS).




Vulnerable Code:


add(new Label("someLabel").setEscapeModelStrings(false));







References


Wicket models and forms - Reference Documentation

WASC-8: Cross Site Scripting

OWASP: XSS Prevention Cheat Sheet

OWASP: Top 10 2013-A3: Cross-Site Scripting (XSS)

CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')




            
        

        

        

    

    
    

        
        

            Ignoring XML comments in SAML may lead to authentication bypass
            
        

        
Bug Pattern: SAML_IGNORE_COMMENTS


        
            


Security Assertion Markup Language (SAML) is a single sign-on protocol that that used XML.
The SAMLResponse message include statements that describe the authenticated user.
If a user manage to place XML comments (<!-- -->), it may caused issue in the way the parser extract literal value.





    For example, let's take the following XML section:
    
<saml:Subject><saml:NameID>admin@domain.com<!---->.evil.com</saml:NameID></saml:Subject>

    The user identity is "admin@domain.com<!---->.evil.com" but it is in fact a text node "admin@domain.com", a comment "" and a text node ".evil.com".
    When extracting the NameID, the service provider implementation might take first text node or the last one.






Vulnerable Code:


@Bean
ParserPool parserPool1() {
    BasicParserPool pool = new BasicParserPool();
    pool.setIgnoreComments(false);
    return pool;
}







Solution:


@Bean
ParserPool parserPool1() {
    BasicParserPool pool = new BasicParserPool();
    pool.setIgnoreComments(true);
    return pool;
}








References

Duo Finds SAML Vulnerabilities Affecting Multiple Implementations

Spring Security SAML and this week's SAML Vulnerability






            
        

        

        

    

    
    

        
        

            Overly permissive file permission
            
        

        
Bug Pattern: OVERLY_PERMISSIVE_FILE_PERMISSION


        
            


It is generally a bad practices to set overly permissive file permission such as read+write+exec for all users.
If the file affected is a configuration, a binary, a script or sensitive data, it can lead to privilege escalation or information leakage.




It is possible that another service, running on the same host as your application, gets compromised.
Services typically run under a different user. A compromised service account could be used to read your configuration, add execution instruction to scripts or alter the data file.
To limite the damage from other services or local users, you should limit the permission of your application files.





Vulnerable Code 1 (symbolic notation):


Files.setPosixFilePermissions(configPath, PosixFilePermissions.fromString("rw-rw-rw-"));







Solution 1 (symbolic notation):


Files.setPosixFilePermissions(configPath, PosixFilePermissions.fromString("rw-rw----"));








Vulnerable Code 2 (Object-oriented implementation):


Set<PosixFilePermission> perms = new HashSet<>();
perms.add(PosixFilePermission.OWNER_READ);
perms.add(PosixFilePermission.OWNER_WRITE);
perms.add(PosixFilePermission.OWNER_EXECUTE);

perms.add(PosixFilePermission.GROUP_READ);
perms.add(PosixFilePermission.GROUP_WRITE);
perms.add(PosixFilePermission.GROUP_EXECUTE);

perms.add(PosixFilePermission.OTHERS_READ);
perms.add(PosixFilePermission.OTHERS_WRITE);
perms.add(PosixFilePermission.OTHERS_EXECUTE);







Solution 2 (Object-oriented implementation):


Set<PosixFilePermission> perms = new HashSet<>();
perms.add(PosixFilePermission.OWNER_READ);
perms.add(PosixFilePermission.OWNER_WRITE);
perms.add(PosixFilePermission.OWNER_EXECUTE);

perms.add(PosixFilePermission.GROUP_READ);
perms.add(PosixFilePermission.GROUP_WRITE);
perms.add(PosixFilePermission.GROUP_EXECUTE);







References

CWE-732: Incorrect Permission Assignment for Critical Resource

A guide to Linux Privilege Escalation

File system permissions




            
        

        

        

    

    
    

        
        

            Improper handling of Unicode transformations
            
        

        
Bug Pattern: IMPROPER_UNICODE


        
            


Unexpected behavior in unicode transformations can sometimes lead to bugs, some of them affecting software security.
A code that applies the uppercase transformation to two strings could mistakenly interpret both strings as being equal.





In the code bellow, the string "ADM\u0131N" would cause the condition to be true.
When the uppercase transformation is applied, the character `\u0131` will become '\u0049' (I).
It can be an issue if the developer only one user to be "ADMIN".


if(username.toUpperCase().equals("ADMIN")) {
  //...
}







Similar characters transformations can occur with normalization functions.
In the code bellow, the string "BAC\u212AUP" would cause the condition to be true.
When the normalization transformation is applied, the character `\u212A` will become '\u004B' (K).


if(Normalizer.normalize(input, Normalizer.Form.NFC).equals("BACKUP")) {
  //...
}







References

Unicode for Security Professionals

Unicode Security Guide: Character Transformations

CWE-176: Improper Handling of Unicode Encoding

Unicode: Unicode Security Considerations




            
        

        

        

    

    
    

        
        

            String is modified after validation and not before it
            
        

        
Bug Pattern: MODIFICATION_AFTER_VALIDATION


        
            


A string must not be modified after validation because it may allow an attacker to bypass validation using a tricky
string which becomes malicious after the modification. For example, a program may filter out the ⟨script⟩ tags from
HTML input to avoid cross-site scripting (XSS) and other vulnerabilities. If non-character code points  are deleted
from the input following validation, an attacker may pass the string "⟨scr"+"\uFDEF"+"ipt⟩" so that the validation
check fails to detect the ⟨script⟩ tag, but the subsequent removal of the non-character code pont creates a ⟨script⟩
tag in the input:

Pattern pattern = Pattern.compile("<script>");
Matcher matcher = pattern.matcher(s);
if (matcher.find()) {
  throw new IllegalArgumentException("Invalid input");
}

s = s.replaceAll("[\\p{Cn}]", "");







The proper way is to perform the modification before the validation so the passed string is first changed to ⟨script⟩
which fails to be validated:

s = s.replaceAll("[\\p{Cn}]", "\uFFFD");
Pattern pattern = Pattern.compile("<script>");
Matcher matcher = pattern.matcher(s);
if (matcher.find()) {
  throw new IllegalArgumentException("Invalid input");
}







References

CERT: IDS11-J. Perform any string modifications before validation

CWE-179: Incorrect Behavior Order: Early Validation

CWE-182: Collapse of Data into Unsafe Value




            
        

        

        

    

    
    

        
        

            String is normalized after validation and not before it
            
        

        
Bug Pattern: NORMALIZATION_AFTER_VALIDATION


        
            


A string must not be normalized after validation because it may allow an attacker to bypass validation using a tricky
string which becomes malicious after the normalization. For example, a program may filter out the ⟨script⟩ tags from
HTML input to avoid cross-site scripting (XSS) and other vulnerabilities. However, in unicode, the same string can have
many different representations. For example, \uFE64 is normalized to ⟨ and \uFE65 is normalized to ⟩. Thus,
if an attacker passes the string "\uFE64" + "script" + "\uFE65" the validation check fails to detect the ⟨script⟩ tag,
but thereafter the string is normalized to the ⟨script⟩ tag in the input:

Pattern pattern = Pattern.compile("[<>]"); // Check for angle brackets
Matcher matcher = pattern.matcher(s);
if (matcher.find()) {
  throw new IllegalStateException();
}
s = Normalizer.normalize(s, Form.NFKC);







The proper way is to do the normalization before the validation so the passed string is first changed to ⟨script⟩
which fails to be validated:

s = Normalizer.normalize(s, Form.NFKC);
Pattern pattern = Pattern.compile("[<>]");
Matcher matcher = pattern.matcher(s);
if (matcher.find()) {
  throw new IllegalStateException();
}







References

CERT: IDS01-J. Normalize strings before validating them

CWE-179: Incorrect Behavior Order: Early Validation

CWE-180: Incorrect Behavior Order: Validate Before Canonicalize

CWE-289: Authentication Bypass by Alternate Name




            
        

        

        

    

    
    

        
        

            Dangerous combination of permissions granted
            
        

        
Bug Pattern: DANGEROUS_PERMISSION_COMBINATION


        
            


Certain combinations of permissions can produce significant capability increases and should not be granted. Granting
ReflectPermission on the target suppressAccessChecks is dangerous in that information (possibly confidential) and
methods normally unavailable would be accessible to malicious code. Similarly, the permission
java.lang.RuntimePermission applied to target createClassLoader grants code the permission to create a
ClassLoader object.
This is extremely dangerous, because malicious applications that can instantiate their own class loaders could
then load their own rogue classes into the system. These newly loaded classes could be placed into any protection
domain by the class loader, thereby automatically granting the classes the permissions for that domain.






Dangerous permission combinations:



PermissionCollection pc = super.getPermissions(cs);
pc.add(new ReflectPermission("suppressAccessChecks"));




PermissionCollection pc = super.getPermissions(cs);
pc.add(new RuntimePermission("createClassLoader"));







References

CERT: ENV03-J. Do not grant dangerous combinations of permissions

CWE-732: Incorrect Permission Assignment for Critical Resource



            
        

        

        

    

    
    

        
        

            An unsafe string is potentially injected into an XML string
            
        

        
Bug Pattern: POTENTIAL_XML_INJECTION


        
        


Unsafe strings (e.g. from a user input) may contain XML tags. If such a string is inserted into an XML document then it
may change its structure to a valid but semantically different document. To prevent this unsafe strings must b
sanitized first.





Example:


An XML document may look like this:



⟨product⟩
    ⟨name⟩Cell Phone⟨/name⟩
    ⟨price⟩800⟨/price⟩
    ⟨amount⟩1⟨/amount⟩
⟨/product⟩




An attacker may put the following string to the field "amount":


1⟨/amount⟩⟨price⟩1⟨/price⟩⟨amount⟩1




If the XML parser works in a way that the second price overwrites the first one then the attacker may buy the cell
phone for 1 singe dollar.





References

IDS16-J. Prevent XML Injection



        
        

        

        

    

    
        


        


            

                
Languages:

                

                    
English

                    
Japanese

                

            

        

    










    

        

            Find Security Bugs 1.14.0
            ·
            Created by Philippe Arteau
        

        

            Licensed under LGPL
        

    













    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-34839255-2']);
    _gaq.push(['_trackPageview']);

    (function () {
        var ga = document.createElement('script');
        ga.type = 'text/javascript';
        ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(ga, s);
    })();
