from fastapi import APIRouter,Depends
from src.api.schemas.analyze import AnalyzeResponse,ProjectData
from  src.infrastructure.models.OllamaService import model
from src.api.dependencies.model import get_model
router=APIRouter(prefix="/AIService",tags=["AIService"])
llm=model()
@router.post("/analyze",response_model=list[AnalyzeResponse])
async def analyze(Project:ProjectData,Llm:model=Depends(get_model))->list[AnalyzeResponse]:
     response=await Llm.Analyze(Project)
     print(response)
     return response
    






