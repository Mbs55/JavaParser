from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    app_name:str="JavaAnalyzer"
    api_prefix:str=""
    model_name:str="qwen2.5:7b"
    model_url:str="http://localhost:11434"
    model_config=SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )
@lru_cache
def get_settings()->Settings:
    return Settings()
