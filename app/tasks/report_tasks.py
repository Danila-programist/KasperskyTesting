from pathlib import Path

from celery import Celery

from app.services.text_analyzer_service import TextAnalyzerService
from app.services.excel_export_service import ExcelExportService
from app.core.config import settings

celery_app = Celery("tasks")

celery_app.conf.update(
    broker_url=settings.CELERY_BROKER_URL,
    result_backend=settings.CELERY_RESULT_BACKEND,
)

@celery_app.task
def process_report_file(file_path: str, output_dir: str):
    file_path_obj = Path(file_path)
    output_dir_obj = Path(output_dir)
    output_dir_obj.mkdir(parents=True, exist_ok=True)

    try:
        stats = TextAnalyzerService.analyze_file(file_path_obj)

        output_file = output_dir_obj / f"{file_path_obj.stem}.xlsx"
        ExcelExportService.export_stats(stats, output_file)

        return str(output_file)
    finally:
        try:
            file_path_obj.unlink(missing_ok=True)
        except Exception:
            pass
        