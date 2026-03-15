from pathlib import Path

import aiofiles
from fastapi import UploadFile


UPLOAD_DIR = Path("tmp/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


class FileStorage:

    @staticmethod
    async def save_file(file: UploadFile, filename: str) -> str:
        """
        Сохраняет файл на диск чанками
        """

        file_path = UPLOAD_DIR / filename

        async with aiofiles.open(file_path, "wb") as buffer:
            while chunk := await file.read(1024 * 1024):
                await buffer.write(chunk)

        return str(file_path)