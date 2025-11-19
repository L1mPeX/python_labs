from pathlib import Path
import csv
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Прочитать весь текст из файла с заданной кодировкой (UTF-8 по умолчанию).
    Если нужно, укажите другую кодировку, например, encoding="cp1251".
    Исключения FileNotFoundError и UnicodeDecodeError не подавляются.
    """
    p = Path(path)
    return p.read_text(encoding=encoding)

def write_csv(rows: list[tuple | list], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    """
    Записать строки в CSV-файл с разделителем запятой.
    Если указан header, он записывается первой строкой.
    Проверяет одинаковую длину всех строк, иначе вызывает ValueError.
    Создаёт/перезаписывает файл.
    """
    if not rows and header is None:
        # Пустой файл
        with open(path, "w", encoding="utf-8", newline="") as f:
            pass
        return
    if rows:
        length = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != length:
                raise ValueError(f"Row {i} length {len(row)} != first row length {length}")
    p = Path(path)
    ensure_parent_dir(p)
    with p.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(header)
        writer.writerows(rows)

def ensure_parent_dir(path: str | Path) -> None:
    """Создать родительские директории для файла, если их нет."""
    p = Path(path)
    if parent := p.parent:
        parent.mkdir(parents=True, exist_ok=True)
