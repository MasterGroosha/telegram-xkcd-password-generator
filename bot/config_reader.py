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
    host: Optional[str]
    port: int = 6379
    db_num: int = 0


class Settings(BaseSettings):
    bot_token: SecretStr
    redis: Optional[Redis]
    storage_mode: str
    words: WordSettings

    @validator("storage_mode")
    def validate_storage_mode(cls, v: str, values):
        v = v.lower()
        if v not in {"memory", "redis"}:
            raise ValueError("Only 'memory' and 'redis' values are allowed.")
        if v == "redis" and (not values.get("redis") or not values.get("redis", {}).get("host")):
            raise ValueError("Backend mode 'redis' selected, but no host is provided; set it via REDIS__HOST variable.")
        return v

    class Config:
        env_nested_delimiter = '__'


settings = Settings()
