from pydantic import BaseModel, BaseSettings, SecretStr, FilePath


class WordSettings(BaseModel):
    wordfile: FilePath
    min: int = 2
    max: int = 8
    default: int = 3
    prefixes_suffixed_by_default: bool = True
    separators_by_default: bool = True


class Redis(BaseModel):
    host: str
    port: int = 6379
    db_num: int = 0


class Settings(BaseSettings):
    bot_token: SecretStr
    redis: Redis
    words: WordSettings

    class Config:
        env_nested_delimiter = '__'


settings = Settings()
