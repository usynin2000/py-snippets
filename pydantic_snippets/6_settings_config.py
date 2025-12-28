from pydantic import BaseModel, Field, field_validator
from pydantic_settings import BaseSettings

# Example 1: Setting up application (can be downloaded from .env)

class DatabaseSettings(BaseSettings):
    db_host: str = Field(default="localhost", alias="DATABSE_HOST")
    db_port: int = Field(default=5432, alias="DATABASE_PORT")
    db_name: str = Field(default="myapp", alias="DATABASE_NAME")
    db_user: str = Field(default="user", alias="DATABASE_USER")
    db_password: str = Field(default="", alias="DATABASE_PASSWORD")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
    
    @property
    def connection_string(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


# Example 2: Settings with validation
class AppSettings(BaseSettings):
    app_name: str = "MyApp"
    debug: bool = False
    api_key: str
    max_connections: int = Field(default=100, ge=1, le=1000)
    timeout: float = Field(default=30.0, gt=0)
    allowed_hosts: list[str] = ["localhost", "127.0.0.1"]

    @field_validator("api_key")
    @classmethod
    def validate_api_key(cls, v: str) -> str:
        if len(v) < 32:
            raise ValueError("API KEY should be more than 32 chars")
        return v
    
    class Config:
        env_file = ".env"
    


if __name__ == "__main__":
    try:
        db_settings = DatabaseSettings(
            db_host="localhost",
            db_user="admin",
            db_password="secret123"
        )
        print("DB:")
        print(f"Connection string: {db_settings.connection_string}\n")
    except Exception as e:
        print(f"Error DB settings: {e}\n")


    try:
        app_settings = AppSettings(
            api_key="a" * 32,
            debug=True,
            max_connections=50
        )
        print("Application settings:")
        print(f"App: {app_settings.app_name}")
        print(f"Debug: {app_settings.debug}")
        print(f"Max connections: {app_settings.max_connections}")
        print(f"Allowed hosts: {app_settings.allowed_hosts}")
    except Exception as e:
        print(f"Error APP settings: {e}")