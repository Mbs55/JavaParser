from src.infrastructure.models.interface.llmService import LlmService
from ollama import chat,ChatResponse,Client
from src.api.schemas.analyze import AnalyzeRequest,AnalyzeResponse
import json
import chromadb
import os
from fastapi.concurrency import run_in_threadpool
MODEL_EMBED="nomic-embed-text"
MODEL_LLM="qwen2.5"
class model(LlmService):
    # async def prompt(self,req:AnalyzeRequest)->AnalyzeResponse:
    #     METHOD=req.method
    #     prompt=METHOD
    #     Host:str=os.getenv("OLLAMA_HOST")
    #     client=Client(host=Host)
    #     response:ChatResponse=await run_in_threadpool(
    #         client.chat,model=MODEL_LLM,
    #         messages=[{"role":"user","content":prompt}],stream=False
    #     )
    #     print(prompt)
    #     result=json.loads(response.message.content)
    #     return AnalyzeResponse(**result)
    client_db=chromadb.Client()
    collection=client_db.create_collection(name='')
