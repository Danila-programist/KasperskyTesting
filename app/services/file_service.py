import uuid

from fastapi import UploadFile

from app.infrastructure.file_storage import FileStorage


class FileService:

    @staticmethod
    async def save_upload_file(file: UploadFile) -> str:
        """
        Валидирует файл и сохраняет его через storage слой
        """

        if not file.filename or not file.filename.lower().endswith(".txt"):
            raise ValueError("Разрешены только .txt файлы")

        file_id: str = str(uuid.uuid4())
        filename: str = f"{file_id}_{file.filename}"

        file_path: str = await FileStorage.save_file(file, filename)

        return file_path