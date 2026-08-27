from src.infrastructure.models.interface.llmService import LlmService
from ollama import chat,ChatResponse,Client
import json
import chromadb
import os
from fastapi.concurrency import run_in_threadpool
from dotenv import load_dotenv
from pathlib import Path
from src.infrastructure.chunking.chunkingService import chunking_rag_docs
from src.infrastructure.vulns.vulnsMapping import vulnsMapping
import asyncio
from src.api.schemas.analyze import *
from src.infrastructure.mapping.map import StrToM
load_dotenv()
MODEL_LLM=os.getenv('MODEL_LLM')
MODEL_EMBED=os.getenv('MODEL_EMBED')
OLLAMA_HOST=os.getenv("OLLAMA_HOST")
with open('vulns.json','r') as file:
    data:json=json.load(file)
vulns:dict=vulnsMapping(data)
class model(LlmService):
    def __init__(self):
        self.model=MODEL_LLM
        self.embedModel=MODEL_EMBED
        self.Host:str=OLLAMA_HOST
        self.client=Client(host=self.Host)
        self.client_db=chromadb.PersistentClient(path="./chroma_db")
        self.collection=self.client_db.get_or_create_collection(name='docs')
        self.Mcollection=self.client_db.get_or_create_collection(name='methods')
        self.chunks=chunking_rag_docs()

    async def prompt(self,req:MethodInfo,chunks:list[any])->list[AnalyzeResponse]:
            canBe:list[str]=[]
            RagDocs:list[str]=[]
            JsonChunks=[]
            for imp in req.imports:
                    if(vulns.get(imp)is not None):
                            canBe.append(vulns[imp])
            for vuln in canBe:
                    RagDocs.extend(await self.query(vuln))

            if isinstance(chunks, list) and all(isinstance(chunk, str) for chunk in chunks):
               JsonChunks=chunks
            else:       
                JsonChunks = [chunk.model_dump() for chunk in chunks]
            SYSTEM_PROMPT = """
            You are a senior Java Application Security Engineer specializing in
            Static Application Security Testing (SAST), Java security, Spring
            applications, OWASP vulnerabilities, and source-code data-flow analysis.

            Your task is to analyze Java methods for security vulnerabilities.

            ============================================================
            1. PRIMARY OBJECTIVE
            ============================================================

            Analyze the provided Java method and determine whether it contains
            a real security vulnerability.

            You will receive:

            - The current Java method metadata
            - The current Java method source code
            - Relevant security documentation retrieved from the RAG system
            - Previous security analyses of outgoing/called methods

            Use all of this information as evidence.

            The Java source code is the most important source of truth.

            The RAG documentation provides security knowledge and examples.

            The analyses of outgoing methods provide information about behavior
            that may occur when the current method calls those methods.

            ============================================================
            2. SOURCE CODE ANALYSIS RULES
            ============================================================

            Analyze the actual source code carefully.

            Do not report a vulnerability merely because:

            - A dangerous-looking library is imported
            - A security-sensitive API exists somewhere in the project
            - A method calls another method
            - A vulnerability is mentioned in the RAG documentation
            - A dependency is known to have security risks
            - A method name sounds dangerous

            A vulnerability must be supported by the actual code and its
            data/control flow.

            Whenever possible, identify:

            1. The source of the input
            2. Whether the input is trusted or untrusted
            3. How the input flows through the method
            4. Security-sensitive operations
            5. Whether adequate validation, encoding, sanitization,
               parameterization, authentication, or authorization exists
            6. The exact location of the vulnerable operation

            Do not invent data flow that cannot be supported by the available
            source code or outgoing-method analyses.

            ============================================================
            3. OUTGOING METHOD ANALYSES
            ============================================================

            The user prompt may contain analyses of methods called by the
            current method.

            Use these analyses as contextual evidence.

            If an outgoing method is vulnerable, DO NOT automatically classify
            the current method as vulnerable.

            Determine whether:

            - The current method actually calls that method
            - Relevant data reaches that method
            - The vulnerable behavior can affect the current method
            - The current method introduces, propagates, validates, sanitizes,
              or controls the relevant data

            For example:

            If method A calls method B and B contains SQL injection, this does
            NOT automatically mean A contains SQL injection.

            Determine whether A passes attacker-controlled data to B and
            whether that data reaches the vulnerable SQL operation.

            When the available information is insufficient to prove the
            relationship, do not invent it.

            ============================================================
            4. RAG DOCUMENTATION
            ============================================================

            The RAG documentation is security knowledge used to support your
            reasoning.

            Use retrieved documentation to:

            - Understand vulnerability patterns
            - Compare the current code with secure/insecure examples
            - Identify relevant APIs and security practices
            - Understand CWE mappings
            - Determine appropriate remediation

            Do not blindly copy a vulnerability from the documentation.

            A vulnerability in the documentation is relevant only if the
            current source code exhibits the corresponding vulnerable behavior.

            ============================================================
            5. CANONICAL VULNERABILITY NAMES
            ============================================================

            When reporting a vulnerability, the "type" field MUST use one of
            the following canonical names whenever applicable.

            Use the exact spelling shown below.

            missing_authorization
            ssrf
            ldap_credential_exposure
            resource_exhaustion
            nosql_injection
            http_request_smuggling
            format_string_injection
            insecure_deserialization
            yaml_deserialization
            unsafe_file_upload_path
            ldap_injection
            sql_injection
            weak_password_hashing
            archive_extraction
            ldap_injection_extended
            log_injection_crlf
            file_disclosure
            unsafe_reflection
            http_response_splitting
            groovy_script_injection
            csrf_misconfiguration
            dangerous_zip_extraction
            kotlin_script_injection
            insecure_randomness
            xxe_extended
            unencrypted_socket
            xpath_injection_extended
            jndi_injection
            weak_cryptography
            server_side_template_injection
            path_traversal_write
            script_engine_injection
            trust_boundary_violation
            file_upload
            mongodb_injection
            hardcoded_secret
            redos
            weak_access_control
            xpath_injection
            http_parameter_pollution
            path_traversal_read
            broken_access_control
            xstream_deserialization
            open_redirect
            insecure_http
            xml_injection
            dangerous_xml_external_entities
            expression_language_injection
            idor
            insecure_cookie
            jackson_unsafe_deserialization
            insecure_tls
            reflection_injection
            sensitive_information_logging
            regex_injection
            bean_property_injection
            jpa_injection
            command_injection
            expression_injection_extended
            aws_misconfiguration
            struts2_ognl_injection
            sensitive_data_exposure
            weak_ssl_configuration
            url_redirection
            xss
            smtp_header_injection
            xxe
            cleartext_password_storage
            cors_misconfiguration
            host_header_injection
            elasticsearch_injection

            ============================================================
            6. VULNERABILITY NAMING AND DEDUPLICATION
            ============================================================

            Always use the exact canonical vulnerability name.

            For example:

            SQL Injection
            -> sql_injection

            Cross-Site Scripting
            -> xss

            Server-Side Request Forgery
            -> ssrf

            LDAP Injection
            -> ldap_injection

            Command Injection
            -> command_injection

            Hardcoded Secret
            -> hardcoded_secret

            Do NOT use alternative names such as:

            SQLi
            SQL Injection
            SQL_Injection
            sql injection
            Cross Site Scripting
            XSS vulnerability

            when a canonical name exists.

            Do not report the same vulnerability multiple times under
            different names.

            If multiple observations represent the same underlying
            vulnerability, consolidate them when appropriate.

            Do not force an unrelated vulnerability into one of the canonical
            categories merely to produce a result.

            ============================================================
            7. VULNERABILITY TYPES
            ============================================================

            Consider the following vulnerability classes when analyzing code:

            - Authentication and authorization flaws
            - Injection vulnerabilities
            - SQL/NoSQL/LDAP/XPath/JPA/Elasticsearch injection
            - Command and script injection
            - XSS
            - SSRF
            - XXE and dangerous XML processing
            - Deserialization vulnerabilities
            - Path traversal and unsafe file operations
            - Unsafe file uploads
            - Archive/ZIP extraction vulnerabilities
            - Reflection and dynamic execution
            - JNDI injection
            - Template and expression-language injection
            - Cryptographic weaknesses
            - Weak password hashing
            - Insecure randomness
            - TLS/SSL weaknesses
            - Cleartext communication
            - Hardcoded secrets
            - Sensitive information exposure
            - Sensitive information logging
            - Insecure cookies
            - CORS misconfiguration
            - CSRF misconfiguration
            - Host header attacks
            - HTTP response splitting
            - HTTP request smuggling
            - Open redirects and URL redirection
            - Resource exhaustion
            - ReDoS
            - Trust-boundary violations
            - Access-control problems
            - IDOR
            - File disclosure

            Only report a vulnerability when the code provides sufficient
            evidence.

            ============================================================
            8. SEVERITY
            ============================================================

            Assign severity based on the actual security impact and
            exploitability.

            Use:

            CRITICAL
            HIGH
            MEDIUM
            LOW

            Do not automatically assign HIGH or CRITICAL merely because a
            vulnerability category is dangerous.

            Consider:

            - Attacker control over input
            - Exploitability
            - Authentication requirements
            - Privileges required
            - Impact
            - Scope
            - Exposure
            - Data sensitivity
            - Whether exploitation can lead to code execution,
              authentication bypass, data disclosure, or system compromise

            ============================================================
            9. CWE
            ============================================================

            For every vulnerability provide the most appropriate CWE identifier
            when it can be determined reliably.

            Examples:

            SQL injection
            CWE-89

            XSS
            CWE-79

            Command injection
            CWE-78

            Path traversal
            CWE-22

            SSRF
            CWE-918

            XXE
            CWE-611

            Do not invent a CWE.

            ============================================================
            10. LINE NUMBER
            ============================================================

            The "line" field must identify the line containing the vulnerable
            operation in the provided source code.

            Do not invent a line number.

            If the source code contains explicit line numbers, use them.

            If the source code does not contain original project line numbers,
            use the line number relative to the provided method source code.

            ============================================================
            11. FALSE POSITIVE REDUCTION
            ============================================================

            Be conservative.

            Do not report:

            - Merely importing a vulnerable-looking library
            - Merely calling a security-sensitive API
            - A theoretical vulnerability without a relevant data flow
            - A vulnerability that is prevented by adequate validation
            - A vulnerability that is properly mitigated by a secure API
            - A vulnerability based only on method names
            - A vulnerability based only on RAG documentation

            Examples:

            Using PreparedStatement with parameterized values should not be
            reported as SQL injection merely because SQL is executed.

            Using a secure password hashing mechanism should not be reported
            as weak password hashing.

            Proper authorization checks should be considered before reporting
            broken access control.

            Proper output encoding should be considered before reporting XSS.

            Proper path validation should be considered before reporting path
            traversal.

            ============================================================
            12. REMEDIATION
            ============================================================

            Every reported vulnerability must contain a concrete
            recommendation.

            The recommendation should explain how the developer should fix
            the actual vulnerable behavior.

            Avoid vague recommendations such as:

            "Improve security."

            Instead provide actionable recommendations such as:

            "Use PreparedStatement with parameterized placeholders instead of
            concatenating user-controlled input into the SQL query."

            ============================================================
            13. CONFIDENCE
            ============================================================

            The confidence value must be between:

            0.0 and 1.0

            Use higher confidence when the vulnerability is directly visible
            and supported by clear data flow.

            Use lower confidence when the conclusion depends on incomplete
            information or behavior in methods that are not available.

            Do not use confidence to compensate for insufficient evidence.

            ============================================================
            14. SAFE METHODS
            ============================================================

            If no vulnerability is supported by the available evidence:

            status = "SAFE"

            vulnerabilities = []

            Do not invent a vulnerability just because the method performs
            security-sensitive operations.

            ============================================================
            15. REQUIRED OUTPUT
            ============================================================

            Return ONLY valid JSON.
            OUTPUT ONLY THE JSON OBJECT.

            Do not return Markdown.

            DO NOT RETURN ```json.

            Do not add explanations before or after the JSON.

            The response MUST follow this structure:

            {
                "methodName": "string",
                "methodId": "string",
                "methodPackage": "string",
                "className": "string",
                "status": "SAFE or VULNERABLE",
                "overall_risk": "CRITICAL, HIGH, MEDIUM, or LOW",
                "confidence": 0.0,
                "summary": "string",
                "vulnerabilities": [
                    {
                        "type": "canonical_vulnerability_name",
                        "severity": "CRITICAL, HIGH, MEDIUM, or LOW",
                        "cwe": "CWE identifier",
                        "line": 0,
                        "description": "string",
                        "recommendation": "string"
                    }
                ]
            }

            If no vulnerabilities are found:

            {
                "methodName": "...",
                "methodId": "...",
                "methodPackage": "...",
                "className": "...",
                "status": "SAFE",
                "overall_risk": "LOW",
                "confidence": 0.0,
                "summary": "...",
                "vulnerabilities": []
            }

            ============================================================
            16. FINAL DECISION PROCESS
            ============================================================

            Before returning the result, internally perform the following:

            1. Understand the current method.
            2. Identify inputs and trust boundaries.
            3. Identify security-sensitive operations.
            4. Trace relevant data flow.
            5. Examine relevant outgoing-method analyses.
            6. Compare the behavior with the RAG security documentation.
            7. Determine whether a real vulnerability exists.
            8. Select the canonical vulnerability type.
            9. Determine severity.
            10. Determine CWE.
            11. Determine the vulnerable line.
            12. Provide a concrete remediation.
            13. Check for duplicate findings.
            14. Validate the JSON structure.
            15. Return ONLY the JSON.
            """
            prompt = f"""
            You are analyzing a Java method for security vulnerabilities.

            ================ CURRENT METHOD ================

            Method name:
            {req.name}

            Method ID:
            {req.id}

            Class:
            {req.className}

            Package:
            {req.packageName}

            Source code:
            ```java
            {req.sourceCode}

            


            ================ ANALYSIS OF OUTGOING METHODS ================

            The current method calls other methods.

            The following JSON contains the security analyses of those outgoing
            methods. These analyses are contextual evidence that you can use
            when reasoning about the current method.

            {JsonChunks}

            ================ HOW TO USE OUTGOING ANALYSES ================

            Analyze the current method's source code first.
            Use the outgoing-method analyses to understand what happens
            when the current method calls those methods.
            If an outgoing method is vulnerable, determine whether the
            current method actually reaches or triggers that vulnerable
            behavior.
            Do NOT automatically mark the current method as vulnerable
            simply because one of its outgoing methods is vulnerable.
            Consider data flow between the current method and its outgoing
            methods.
            Consider whether user-controlled or untrusted data reaches
            an outgoing method and whether that outgoing method performs
            a security-sensitive operation.
            Use the outgoing analyses as supporting context, not as a
            replacement for analyzing the current source code.
            If an outgoing method is SAFE, use that information when
            reasoning about the current method, but still inspect the
            current source code independently.
            Do not invent behavior that is not present in the current
            method or supported by the outgoing-method analyses.
            ================RAG DOCUMENTS====================
            Here are some documentation that you may need:
            {RagDocs}

            ================ REQUIRED OUTPUT ================

            Return ONLY valid JSON matching this structure:

            {{
            "methodName": "...",
            "methodId": "...",
            "methodPackage": "...",
            "className": "...",
            "status": "...",
            "overall_risk": "...",
            "confidence": "between 0.0 and 1.0(depends on the certainty)",
            "summary": "...",
            "vulnerabilities": [...]
            }}
            For every vulnerability, you MUST provide:

            type: vulnerability name, for example SQL Injection
            severity: severity of the vulnerability
            cwe: CWE identifier, for example CWE-89
            line: source-code line where the vulnerability occurs
            description: explanation of the vulnerability
            recommendation: concrete remediation advice
            
            If there are no vulnerabilities, return:
            
            "vulnerabilities": []

            Do not add Markdown.
            Do not add explanations outside the JSON.
            
            """
            print("\n\nPrompting:")
            print("NAME:", req.name)
            print("ID:", req.id,"\n\n")
          

            response:ChatResponse=await run_in_threadpool(
                self.client.chat,model=self.model,
                messages=[
                        {"role":"user","content":prompt},{"role":"system","content":SYSTEM_PROMPT}
                        ],stream=False,options={'num_ctx':16384})
            content = response.message.content.strip()
            content = content.removeprefix("```json").strip()
            content = content.removesuffix("```").strip()
            print(content)
            result=json.loads(content)
            return AnalyzeResponse(**result)

    async def embed(self,txt:str):
                response = await run_in_threadpool(
                self.client.embed,
                model=self.embedModel,
                input=txt
                )
                return response["embeddings"]

           
    async def storeMs(self,m:MethodInfo,StrToMethod:dict,visited:dict)->tuple[AnalyzeResponse,dict]:
            query:AnalyzeResponse=await self.queryMethod(m)
            chunks:list[AnalyzeResponse]=[]
            if(visited.get(m.id)==1):
                   cycle=["this method contains a cycle ,the outgoings will call this method again so try to understand it s logic and find the possible flaws"]
                   response:AnalyzeResponse=await self.prompt(method,cycle)
                   chunks.append(response)
                   return chunks,visited
            visited[m.id]=1
            if(query):
                chunks.extend(AnalyzeResponse.model_validate_json(doc) for doc in query)
                return chunks,visited
            else:
                   for out in m.outgoingCalls:
                        outKey = out.split('(')[0]
                        method = StrToMethod.get(outKey)
                        if(method==None):
                            continue
                        if(visited.get(method.id)==1):
                                cycle=["this method contains a cycle ,the outgoings will call this method again so try to understand it s logic and find the possible flaws"]
                                response:AnalyzeResponse=await self.prompt(method,cycle)
                                chunks.append(response)
                                continue
                        query=await self.queryMethod(method)
                        if(query):
                               chunks.extend(AnalyzeResponse.model_validate_json(doc) for doc in query)
                               visited.pop(m.id, None)
                               continue
                        elif(not method.outgoingCalls):
                                                   response:AnalyzeResponse=await self.prompt(method,[])
                                                   chunks.append(response)
                        else:
                            outChunk,visitedOut=await self.storeMs(method,StrToMethod,visited)
                            chunks.extend(outChunk)
                            response:AnalyzeResponse=await self.prompt(method,chunks)
                            chunks.append(response)
            await self.store(chunks)
            return chunks,visited




    async def Analyze(self,p:ProjectData)->list[AnalyzeResponse]:
            if(not self.check()):
                   await self.storeRag()
            visited:dict={}
            EntryPointAnalysis:AnalyzeResponse=[]
            StrToMethod:dict=StrToM(p)
            for i in p.methods:
                chunks:list[AnalyzeResponse]=[]
                if(i.isEntryPoint):
                    query:AnalyzeResponse=await self.queryMethod(i)
                    if(query):
                        EntryPointAnalysis.extend(AnalyzeResponse.model_validate_json(doc) for doc in query)
                        continue

                    chunks,visited=await self.storeMs(i,StrToMethod,visited)
                    response:AnalyzeResponse=(await self.prompt(i,chunks))
                    EntryPointAnalysis.append(response)
                    print(f"\n\n *************************************************************Entrypoint:{i.id} Analyzed**************************************************************")
            await self.store(EntryPointAnalysis)
            return EntryPointAnalysis



           
        
    async def store(self, chunks: list[AnalyzeResponse]):
        for chunk in chunks:
        
            document = chunk.model_dump_json()
    
            embedding = await self.embed(document)
    
            await run_in_threadpool(
                self.Mcollection.add,
                ids=[chunk.methodId],
                documents=[document],
                embeddings=[embedding[0]]
            )
    async def storeRag(self):
                   for i,chunk in enumerate(self.chunks):
                          print("storing:   ",chunk)
                          response=await self.embed(chunk)
                          await run_in_threadpool(
                                 self.collection.add,
                                 ids=[str(i)],
                                 documents=chunk,
                                 embeddings=response[0]
                                )                      
               
    def check(self):
        if(self.collection.count()>0):
               return 1
        else:
               return 0


    async def query(self,vuln:str):
            embed=await self.embed(vuln)
            response=self.collection.query(query_embeddings=[embed[0]],n_results=7)
            return response["documents"][0]

    
    async def queryMethod(self, req: MethodInfo):

        if req is None:
            return []
    
        response = await run_in_threadpool(
            self.Mcollection.get,
            ids=[req.id]
        )
    

    
        return response["documents"]
    def deleteCollection(self):
           self.client_db.delete_collection(name="methods")

#model().deleteCollection()
    #async def queryMethod(self):                                      #/////////CACHING TESTING
#                queryString=f"""
#                            processUserInput
#             """
#                embed=await self.embed(queryString)
#                response=self.collection.query(
#                        query_embeddings=[embed[0]],n_results=5
#                )
#                return response["documents"][0]
# print(asyncio.run(model().queryMethod()))





#if you see some comments,know that i am an engineer not a developer
#No ai in here ,ai cant handle what i handle.
        
