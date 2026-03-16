from collections import defaultdict
from typing import Dict
from pathlib import Path
import re

from pymystem3 import Mystem


class TextAnalyzerService:
    mystem = Mystem()  # инициализация движка Mystem

    @staticmethod
    def normalize_word(word: str) -> str:
        """
        Лемматизация слова с помощью Mystem
        """
        lemma = TextAnalyzerService.mystem.lemmatize(word)
        return lemma[0] if lemma else word

    @staticmethod
    def analyze_file(file_path: Path) -> Dict:
        """
        Возвращает статистику:
        - total: общее количество словоформы в документе
        - per_line: разреженное представление {line_index: count}
        - total_lines: количество строк в файле
        """
        stats: Dict[str, dict] = defaultdict(lambda: {"total": 0, "per_line": {}})
        total_lines = 0

        with open(file_path, "r", encoding="utf-8") as f:
            for line_idx, line in enumerate(f):
                total_lines = line_idx + 1
                tokens = re.findall(r"[A-Za-zА-Яа-яЁё]+", line)
                if not tokens:
                    continue

                counts = defaultdict(int)
                for raw in tokens:
                    w = TextAnalyzerService.normalize_word(raw.lower())
                    if w:
                        counts[w] += 1

                for w, c in counts.items():
                    stats[w]["total"] += c
                    stats[w]["per_line"][line_idx] = c

        return {"stats": stats, "total_lines": total_lines}