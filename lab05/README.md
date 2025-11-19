# Лабораторная работа № 5

## JSON и конвертации (JSON↔CSV, CSV→XLSX)

csv_xlsx.py
```python
from pathlib import Path
import csv
import openpyxl

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX через openpyxl
    Первая строка - заголовок. Лист Sheet1
    Ширина колонок авто по содержимому
    """
    csv_file = Path(csv_path)
    xlsx_file = Path(xlsx_path)
    if not csv_file.is_file():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    with csv_file.open(encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)
        if not rows:
            raise ValueError("CSV файл пуст")

        for row in rows:
            ws.append(row)

    for col_idx, column_cells in enumerate(ws.columns, start=1):
        max_length = 8 # ну почему бы и нет?, а то колонки на миллиметр не особо приятно смотреть
        for cell in column_cells:
            try:
                value = str(cell.value)
            except Exception:
                value = ""
            if value:
                max_length = max(max_length, len(value))
        ws.column_dimensions[openpyxl.utils.get_column_letter(col_idx)].width = max_length + 2

    wb.save(xlsx_file)
```

json_csv.py
```python
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
```

Тесты запускаются по скрипту tests.sh:
![Скриншот 1](./materials/imgage.png)

## Лицензия <a name="license"></a>

[![License: CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
Проект доступен с открытым исходным кодом на условиях [Лицензии CC BY-NC-SA 4.0](./LICENSE).

_Авторские права 2025 Андрей Казарин_
