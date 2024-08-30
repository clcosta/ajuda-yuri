from pathlib import Path
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    BASE_PATH: Path = Path(__file__).parent.parent.parent

    model_config = SettingsConfigDict(
        env_file=BASE_PATH / '.env', env_file_encoding='utf-8', extra='ignore'
    )

    DATABASE_URL: str = 'sqlite:///db.sqlite3'
    DEBUG: bool = False

    @field_validator('DATABASE_URL')
    def check_database_url(cls, value):   # pragma: no coverage
        if 'postgresql' in value and 'psycopg' not in value:
            raise ValueError(
                'DATABASE_URL must be a valid SQLAlchemy (psycopg) postgresql URL'
            )
        return value
