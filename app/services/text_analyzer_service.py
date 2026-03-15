# app/services/text_analyzer_service.py
from collections import defaultdict
import pymorphy2
from pathlib import Path

class TextAnalyzerService:
    morph = pymorphy2.MorphAnalyzer()

    @staticmethod
    def normalize_word(word: str) -> str:
        return TextAnalyzerService.morph.parse(word)[0].normal_form

    @staticmethod
    def analyze_file(file_path: Path):
        stats = defaultdict(lambda: {"total": 0, "per_line": []})

        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                words = [TextAnalyzerService.normalize_word(w) for w in line.split()]
                counts = defaultdict(int)
                for w in words:
                    counts[w] += 1
                # обновляем stats
                for w, c in counts.items():
                    stats[w]["total"] += c
                # для всех словоформ добавляем 0 если не встречалось в строке
                for w in stats.keys():
                    stats[w]["per_line"].append(counts.get(w, 0))
        return stats