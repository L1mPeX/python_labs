#!/bin/bash

# Тесты для ЛР8 (модуль Student и сериализация)

SRC_DIR="src/"
DATA_DIR="data/"
PYTHON="python3"

# Проверка существования требуемых файлов
if [[ ! -f "$SRC_DIR/models.py" || ! -f "$SRC_DIR/serialise.py" ]]; then
  echo "Ошибка: Отсутствуют необходимые файлы src/models.py или src/serialise.py"
  exit 1
fi

if [[ ! -d "$DATA_DIR" ]]; then
  mkdir -p "$DATA_DIR"
fi

# Тест 1: Создание объекта Student с корректными данными (ожидается успех)
echo "Тест 1: Создание объекта Student с валидными данными... "
$PYTHON - <<END
from src.models import Student
try:
    s = Student("Иванов Иван Иваныч", "2000-01-02", "SE-01", 4.0)
    print("PASS")
except Exception as e:
    print("FAIL:", e)
    exit(1)
END

# Тест 2: Валидация даты в неправильном формате (ожидается ошибка)
echo "Тест 2: Валидация неверного формата даты (ожидается ValueError)..."
$PYTHON - <<END
from src.models import Student
try:
    s = Student("Иванов Иван", "2000/01/02", "SE-01", 4.0)
    print("FAIL: Ошибка не выброшена")
    exit(1)
except ValueError:
    print("PASS")
END

# Тест 3: Валидация GPA вне диапазона (ожидается ошибка)
echo "Тест 3: Валидация gpa = 6.0 (ожидается ValueError)..."
$PYTHON - <<END
from src.models import Student
try:
    s = Student("Иванов Иван", "2000-01-02", "SE-01", 6.0)
    print("FAIL: Ошибка не выброшена")
    exit(1)
except ValueError:
    print("PASS")
END

# Тест 4: Сериализация и десериализация списка студентов
echo "Тест 4: Сериализация и десериализация..."
$PYTHON - <<END
import os
from src.models import Student
from src.serialise import students_to_json, students_from_json

test_file = "$DATA_DIR/test_students.json"

students = [
    Student("Иванов Иван", "2000-01-02", "SE-01", 3.5),
    Student("Петров Петр", "1999-12-31", "SE-02", 4.2),
]

try:
    students_to_json(students, test_file)
    loaded = students_from_json(test_file)
    if len(loaded) != len(students):
        raise AssertionError("Размер загруженного списка не совпадает")
    if any(s.fio != o.fio for s, o in zip(students, loaded)):
        raise AssertionError("ФИО студентов не совпадают после десериализации")
    print("PASS")
finally:
    if os.path.exists(test_file):
        os.remove(test_file)
END

echo "Все тесты завершены."
