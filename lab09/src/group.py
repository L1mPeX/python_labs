import csv
from pathlib import Path
from typing import List, Dict, Any
from datetime import date

from models import Student


CSV_HEADER = ["fio", "birthdate", "group", "gpa"]


class Group:
    def __init__(self, storage_path: str) -> None:
        self.path = Path(storage_path)
        self._ensure_storage_exists()


    def _ensure_storage_exists(self) -> None:
        """Создаёт CSV с заголовком, если файла нет или он пустой."""
        if not self.path.exists() or self.path.stat().st_size == 0:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self.path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=CSV_HEADER)
                writer.writeheader()

    def _read_all_dicts(self) -> List[Dict[str, str]]:
        """Возвращает все строки в виде словарей."""
        self._ensure_storage_exists()
        with self.path.open("r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames != CSV_HEADER:
                raise ValueError(f"Неверный заголовок CSV: {reader.fieldnames}")
            return list(reader)

    def _write_all_dicts(self, rows: List[Dict[str, Any]]) -> None:
        """Перезаписывает CSV всеми строками."""
        with self.path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_HEADER)
            writer.writeheader()
            writer.writerows(rows)

    def list(self) -> List[Student]:
        """Возвращает всех студентов как список Student."""
        rows = self._read_all_dicts()
        students: List[Student] = []
        for r in rows:
            student = Student.from_dict(r)
            students.append(student)
        return students

    def add(self, student: Student) -> None:
        """Добавляет нового студента в CSV."""
        self._ensure_storage_exists()
        with self.path.open("a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_HEADER)
            writer.writerow(student.to_dict())

    def find(self, substr: str) -> List[Student]:
        """Находит студентов по подстроке в fio (регистр игнорируется)."""
        substr_lower = substr.lower()
        result: List[Student] = []
        for student in self.list():
            if substr_lower in student.fio.lower():
                result.append(student)
        return result

    def remove(self, fio: str) -> int:
        """
        Удаляет все записи с заданным fio.
        Возвращает количество удалённых записей.
        """
        rows = self._read_all_dicts()
        new_rows: List[Dict[str, Any]] = []
        removed = 0
        for r in rows:
            if r["fio"] == fio:
                removed += 1
            else:
                new_rows.append(r)
        if removed:
            self._write_all_dicts(new_rows)
        return removed

    def update(self, fio: str, **fields: Any) -> int:
        """
        Обновляет записи с заданным fio.
        Допустимые поля: fio, birthdate, group, gpa.
        Возвращает количество обновлённых записей.
        """
        allowed = set(CSV_HEADER)
        rows = self._read_all_dicts()
        updated = 0

        for r in rows:
            if r["fio"] != fio:
                continue
            for key, value in fields.items():
                if key not in allowed:
                    raise ValueError(f"Неизвестное поле: {key}")
                r[key] = str(value)
            updated += 1

        if updated:
            self._write_all_dicts(rows)
        return updated

    def stats(self) -> Dict[str, Any]:
        """Собирает статистику по группе."""
        students = self.list()
        if not students:
            return {
                "count": 0,
                "min_gpa": None,
                "max_gpa": None,
                "avg_gpa": None,
                "groups": {},
                "top_5_students": [],
            }

        gpas = [float(s.gpa) for s in students]
        count = len(students)
        min_gpa = min(gpas)
        max_gpa = max(gpas)
        avg_gpa = sum(gpas) / count

        groups: Dict[str, int] = {}
        for s in students:
            groups[s.group] = groups.get(s.group, 0) + 1

        sorted_by_gpa = sorted(students, key=lambda s: float(s.gpa), reverse=True)
        top_5 = [{"fio": s.fio, "gpa": float(s.gpa)} for s in sorted_by_gpa[:5]]

        return {
            "count": count,
            "min_gpa": min_gpa,
            "max_gpa": max_gpa,
            "avg_gpa": avg_gpa,
            "groups": groups,
            "top_5_students": top_5,
        }
