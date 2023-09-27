from enum import Enum

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

load_dotenv()


class Environment(str, Enum):
    DEV = "dev"
    HML = "hml"
    PRD = "prd"
    UNITTEST = "unnitest"


class Settings(BaseSettings):
    ENV: Environment = Environment.PRD
    APP: str = Field(..., env="APP")
    BASE_PATH: str = Field(..., env="BASE_PATH")
    HOST: str = Field("0.0.0.0", env="HOST")  # nosec
    PORT: int = Field(8888, env="PORT")


deploy_settings = Settings()
