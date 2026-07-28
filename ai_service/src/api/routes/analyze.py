from fastapi import APIRouter,Depends
from src.api.schemas.analyze import AnalyzeResponse,AnalyzeRequest
from  src.infrastructure.models.OllamaService import model
from src.api.dependencies.model import get_model
router=APIRouter(prefix="/AIService",tags=["AIService"])
llm=model()
@router.post("/analyze",response_model=AnalyzeResponse)
async def analyze(method:AnalyzeRequest,Llm:model=Depends(get_model))->AnalyzeResponse:
     response=await Llm.prompt(method)
     return response
    






