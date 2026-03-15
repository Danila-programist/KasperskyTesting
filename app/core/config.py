from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Конфигурация приложения.

    Значения могут загружаться:
    - из переменных окружения
    - из .env файла
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

    FILE_STORAGE_PATH: Path = Path("tmp/uploads")

    @property
    def upload_dir(self) -> Path:
        """
        Возвращает директорию загрузки и создаёт её при необходимости
        """
        self.FILE_STORAGE_PATH.mkdir(parents=True, exist_ok=True)
        return self.FILE_STORAGE_PATH


settings = Settings()