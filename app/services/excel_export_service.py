from pathlib import Path

from openpyxl import Workbook


class ExcelExportService:

    @staticmethod
    def export_stats(stats: dict, output_path: Path):
        wb = Workbook()
        ws = wb.active
        ws.append(["Словоформа", "Всего", "По строкам"])

        for word, data in stats.items():
            per_line = ",".join(map(str, data["per_line"]))
            ws.append([word, data["total"], per_line])

        wb.save(output_path)
        return output_path