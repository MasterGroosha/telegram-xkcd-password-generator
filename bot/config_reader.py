from typing import Optional

from pydantic import BaseModel, BaseSettings, SecretStr, FilePath, validator


class WordSettings(BaseModel):
    wordfile: FilePath
    min: int = 2
    max: int = 8
    default: int = 3
    prefixes_suffixes_by_default: bool = True
    separators_by_default: bool = True


class Redis(BaseModel):
    host: str = "127.0.0.1"
    port: int = 6379
    db_num: int = 0


class Settings(BaseSettings):
    bot_token: SecretStr
    redis: Optional[Redis]
    storage_mode: str
    words: WordSettings

    @validator("storage_mode")
    def validate_storage_mode(cls, v: str):
        v = v.lower()
        if v not in {"memory", "redis"}:
            raise ValueError("Only 'memory' and 'redis' values are allowed")
        return v

    class Config:
        env_nested_delimiter = '__'


settings = Settings()
