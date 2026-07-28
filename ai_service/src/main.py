from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes.health import router as health_router
from src.api.routes.analyze import router as analyze_router
from src.infrastructure.config.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    description="Java vulnerabilities analyzer",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router,prefix=settings.api_prefix)
app.include_router(analyze_router)


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "service": settings.app_name,
        "status": "running"
    }
