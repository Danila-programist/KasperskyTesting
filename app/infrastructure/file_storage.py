from pathlib import Path

import aiofiles
from fastapi import UploadFile

from app.core.config import settings   


class FileStorage:

    @staticmethod
    async def save_file(file: UploadFile, filename: str) -> str:
        """
        Сохраняет файл на диск чанками
        """

        upload_dir: Path = settings.upload_dir

        file_path = upload_dir / filename

        async with aiofiles.open(file_path, "wb") as buffer:
            while chunk := await file.read(settings.FILE_CHUNK_SIZE):
                await buffer.write(chunk)

        return str(file_path)