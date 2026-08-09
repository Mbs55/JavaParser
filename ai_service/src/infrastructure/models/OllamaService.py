from src.infrastructure.models.interface.llmService import LlmService
from ollama import chat,ChatResponse,Client
from src.api.schemas.analyze import AnalyzeRequest,AnalyzeResponse,MethodInfo,ClassInfo
import json
import chromadb
import os
from fastapi.concurrency import run_in_threadpool
from dotenv import load_dotenv
from pathlib import Path
from src.infrastructure.chunking.chunkingService import chunking_rag_docs
import asyncio

load_dotenv()
MODEL_LLM=os.getenv('MODEL_LLM')
MODEL_EMBED=os.getenv('MODEL_EMBED')
OLLAMA_HOST=os.getenv("OLLAMA_HOST")
class model(LlmService):
    def __init__(self):
        self.model=MODEL_LLM
        self.embedModel=MODEL_EMBED
        self.Host:str=OLLAMA_HOST
        self.client=Client(host=self.Host)
        self.client_db=chromadb.PersistentClient(path="./chroma_db")
        self.collection=self.client_db.get_or_create_collection(name='docs')
        self.chunks=chunking_rag_docs()

    async def prompt(self,req:MethodInfo)->list[AnalyzeResponse]:
            
            prompt=""""
            You are a senior Java Application Security Engineer.
            
            Analyze the following Java method.
            
            ============================
            
            Method metadata:
            
            -Name: {req.name}
            -Id: {req.id}
            -Existing in class: {req.className}
            -Existing in package: {req.packageName}
            
            ============================
            
            Java Source
            
            {req.sourceCode}
            
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
            """
            response:ChatResponse=await run_in_threadpool(
                self.client.chat,model=self.model,
                messages=[{"role":"user","content":prompt}],stream=False
            )
            result=json.loads(response.message.content)
            return AnalyzeResponse(**result)

    async def embed(self,txt:str):
                response = await run_in_threadpool(
                self.client.embed,
                model=self.embedModel,
                input=txt
                )
                return response["embeddings"]
        
    async def store(self):
               for i,chunk in enumerate(self.chunks):
                      response=await self.embed(chunk)
                      await run_in_threadpool(
                             self.collection.add,
                             ids=[str(i)],
                             documents=chunk,
                             embeddings=response[0]
                            )
                      if i%100==0:
                             print(f"{i} stored chunks")  
                      print(response[0])
               
    def check(self):
        print(self.client_db.list_collections())

    def query(self,req:MethodInfo):
           queryString="""
        {}
        """



s="""
cwe 502
"""

m=model()
response = asyncio.run(m.embed(s))
result=m.collection.query(
    query_embeddings=[response[0]],n_results=5
)
print(result)
        
