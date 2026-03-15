from pathlib import Path

from celery import Celery

from app.services.text_analyzer_service import TextAnalyzerService
from app.services.excel_export_service import ExcelExportService

celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/1"
)

@celery_app.task
def process_report_file(file_path: str, output_dir: str):
    file_path = Path(file_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    stats = TextAnalyzerService.analyze_file(file_path)

    output_file = output_dir / f"{file_path.stem}.xlsx"
    ExcelExportService.export_stats(stats, output_file)

    return str(output_file)