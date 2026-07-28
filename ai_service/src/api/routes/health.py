from fastapi import APIRouter
router=APIRouter(prefix="/AIService",tags=["AIService"])
@router.get('/health')
def health():
    return {"message":"health ok"}
