from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Basic Auth App"
    secret_key: str = "change-me"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30


settings = Settings()
