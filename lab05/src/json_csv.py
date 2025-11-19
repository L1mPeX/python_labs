import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл (список словарей) в CSV
    Записывает CSV в utf-8
    Проверяет ошибки
    """
    json_file = Path(json_path)
    csv_file = Path(csv_path)
    if not json_file.is_file():
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")

    with json_file.open(encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Ошибка разбора JSON: {e}")

    if not isinstance(data, list) or not data:
        raise ValueError("JSON должен быть непустым списком объектов")

    for i, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(f"Элемент {i} в JSON не является словарём")

    keys = list(data[0].keys())

    with csv_file.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for row in data:
            full_row = {k: row.get(k, "") for k in keys}
            writer.writerow(full_row)

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV-файл в JSON (список словарей)
    Входной CSV должен иметь заголовок
    Записывает JSON в utf-8 с отступами и utf-8 символами
    Проверяет ошибки
    """
    csv_file = Path(csv_path)
    json_file = Path(json_path)
    if not csv_file.is_file():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")

    with csv_file.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("CSV файл пустой или не имеет заголовка")

        data = list(reader)
        if not data:
            raise ValueError("CSV файл не содержит данных")

    with json_file.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
