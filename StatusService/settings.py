import os
from pathlib import Path
from tempfile import gettempdir

from dotenv import load_dotenv, find_dotenv
from pydantic import BaseSettings
from yarl import URL

TEMP_DIR = Path(gettempdir())
load_dotenv(find_dotenv())


class Settings(BaseSettings):
    """Application settings."""

    # host: str = "0.0.0.0"
    host: str = "127.0.0.1"
    port: int = 8000
    # quantity of workers for uvicorn
    workers_count: int = 1
    # Enable uvicorn reloading
    reload: bool = False
    db_host: str = os.environ.get('DB_HOST')
    db_port: int = 5432
    db_user: str = os.environ.get('DB_USER')
    db_pass: str = os.environ.get('DB_PASSWORD')
    db_base: str = os.environ.get('DB_NAME')
    db_echo: bool = False

    @property
    def db_url(self) -> URL:
        """
        Assemble database URL from settings.

        :return: database URL.
        """
        self.db_host: str = os.environ.get('DB_HOST')
        self.db_port: int = 5432
        self.db_user: str = os.environ.get('DB_USER')
        self.db_pass: str = os.environ.get('DB_PASSWORD')
        self.db_base: str = os.environ.get('DB_NAME')


        return URL.build(
            scheme="postgres",
            host=self.db_host,
            port=self.db_port,
            user=self.db_user,
            password=self.db_pass,
            path=f"/{self.db_base}",
        )

    class Config:
        env_file = ".env"
        env_prefix = "STATUSSERVICE_"
        env_file_encoding = "utf-8"


settings = Settings()
