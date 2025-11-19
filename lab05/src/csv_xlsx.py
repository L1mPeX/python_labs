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
