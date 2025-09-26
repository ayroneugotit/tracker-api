from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_RECONNECT_ATTEMPTS: int = 5

    MONGODB_APPNAME: str
    MONGODB_DBNAME: str
    MONGODB_USERNAME: str
    MONGODB_PASSWORD: str

    @property
    def MONGODB_URI(self) -> str:
        return f"mongodb+srv://{self.MONGODB_USERNAME}:{self.MONGODB_PASSWORD}@development.uznajdu.mongodb.net/{self.MONGODB_DBNAME}?retryWrites=true&w=majority&appName={self.MONGODB_APPNAME}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
