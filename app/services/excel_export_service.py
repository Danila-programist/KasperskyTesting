from pathlib import Path

from openpyxl import Workbook


class ExcelExportService:
    @staticmethod
    def export_stats(result: dict, output_path: Path) -> None:
        """
        Экспортирует статистику в Excel файл.
        """
        wb = Workbook(write_only=True)
        ws = wb.create_sheet(title="Статистика")
        ws.append(["Словоформа", "Всего", "По строкам"])

        per_line_str = ",".join(str(x) for x in result["per_line"])

        ws.append([result["word"], result["total"], per_line_str])

        wb.save(output_path)
