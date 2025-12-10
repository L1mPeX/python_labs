import json
from typing import List
from src.models import Student


def students_to_json(students: List[Student], path: str) -> None:
    """
    Сохраняет список студентов в JSON файл.

    :param students: список объектов Student
    :param path: путь к файлу для записи
    """
    with open(path, "w", encoding="utf-8") as f:
        json.dump([s.to_dict() for s in students], f, ensure_ascii=False, indent=2)


def students_from_json(path: str) -> List[Student]:
    """
    Загружает список студентов из JSON файла.

    :param path: путь к JSON файлу
    :return: список объектов Student
    """
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    # Валидация и создание объектов
    return list(map(lambda d: Student.from_dict(d), data))
