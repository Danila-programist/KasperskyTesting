from pathlib import Path
from typing import cast

from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet


class ExcelExportService:

    @staticmethod
    def export_stats(result: dict, output_path: Path):
        wb = Workbook(write_only=True)
        ws = wb.create_sheet()
        ws.append(["Словоформа", "Всего", "По строкам"])

        stats = result["stats"]
        total_lines = result["total_lines"]

        for word, data in stats.items():
            per_line_map = data["per_line"]
            per_line = ",".join(str(per_line_map.get(i, 0)) for i in range(total_lines))
            ws.append([word, data["total"], per_line])

        wb.save(output_path)
        return output_path