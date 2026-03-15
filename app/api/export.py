from fastapi import APIRouter, UploadFile, File, HTTPException, status
from fastapi.responses import JSONResponse

from app.services.file_service import FileService

from app.tasks.report_tasks import process_report_file
from app.core.config import settings

router_file = APIRouter()


@router_file.post("/public/upload/export")
async def export_report(file: UploadFile = File(...)):
    """
    Endpoint принимает файл и передает его в сервисный слой для дальнейшей обработки в Celery worker.
    """

    try:
        file_path = await FileService.save_upload_file(file)
    except ValueError as exp:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exp)
        )
    except Exception as exp:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exp)
        )

    process_report_file.delay(
        str(file_path),
        str(settings.upload_dir / "reports")
    )

    return JSONResponse(
        content={
            "message": "Файл успешно загружен",
            "file_path": file_path
        }
    )