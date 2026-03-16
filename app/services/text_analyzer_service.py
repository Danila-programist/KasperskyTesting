from typing import Dict, Set, List
from pathlib import Path
import re

class TextAnalyzerService:
    TARGET_FORMS: Set[str] = {"житель", "жителем"}
    TARGET_LEMMA: str = "житель"

    @classmethod
    def analyze_file(cls, file_path: Path) -> Dict:
        """
        Анализирует файл и собирает статистику для форм "житель" и "жителем",
        объединяя их в одну статистику для слова "житель".

        Returns:
            Dict с полями:
            - total: общее количество упоминаний
            - per_line: список количества упоминаний по строкам
            - total_lines: общее количество строк
            - word: строка с целевыми формами через запятую
        """

        total_count: int = 0
        line_counts: List[int] = [] 

        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:

                words: List[str] = re.findall(r"[А-Яа-яЁё]+", line.lower()) # извлечение слов из строки

                if not words:
                    line_counts.append(0)
                    continue

                line_count = 0

                for word in words:
                    if word in cls.TARGET_FORMS:  
                        line_count += 1

                line_counts.append(line_count)
                total_count += line_count

        words_str: str = ", ".join(sorted(cls.TARGET_FORMS)) 

        return {
            "total": total_count,
            "per_line": line_counts,
            "total_lines": len(line_counts),
            "word": words_str  
        }