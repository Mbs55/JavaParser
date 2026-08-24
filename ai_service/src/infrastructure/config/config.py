from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    app_name:str="JavaAnalyzer"
    api_prefix:str=""
    model_config=SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )
    model_llm:str
    model_embed:str
    ollama_host:str
@lru_cache
def get_settings()->Settings:
    return Settings()
