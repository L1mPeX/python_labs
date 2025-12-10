#!/bin/bash

# Тесты для ЛР9: класс Group (CRUD + stats)
# Запуск: bash src/tests.sh  (из папки src)

set -e  # выход при ошибке

echo "=== ЛР9: Тесты класса Group ==="
echo

# пути (относительно src/)
CSV_FILE="../data/students.csv"
TEST_PY="temp_test.py"

# очистка
rm -rf ../data "$TEST_PY"
mkdir -p ../data

# Функция для запуска Python-теста с прямым импортом
run_test() {
    cat > "$TEST_PY" << 'EOF'
import sys
sys.path.insert(0, ".")
from models import Student
from group import Group
from datetime import date
EOF
    cat >> "$TEST_PY" << EOF
$1
EOF
    python3 "$TEST_PY"
}

echo "1. Создание пустого CSV..."
run_test "
g = Group('$CSV_FILE')
print('✓ CSV создан с заголовком')
" && echo "✓ Тест 1 OK" || echo "✗ Тест 1 ОШИБКА"

echo
echo "2. Добавление студентов..."
run_test "
g = Group('$CSV_FILE')
g.add(Student('Иванов Иван', date(2003,10,10), 'БИВТ-21-1', 4.3))
g.add(Student('Петров Пётр', date(2004,5,12), 'БИВТ-21-2', 3.9))
print('✓ Добавлено 2 студента')
" && echo "✓ Тест 2 OK" || echo "✗ Тест 2 ОШИБКА"

echo
echo "3. list() — проверка списка..."
run_test "
g = Group('$CSV_FILE')
students = g.list()
print(f'Найдено: {len(students)} студентов')
for s in students:
    print(f'  {s.fio}: GPA={s.gpa}')
" && echo "✓ Тест 3 OK" || echo "✗ Тест 3 ОШИБКА"

echo
echo "4. find('Иван')..."
run_test "
g = Group('$CSV_FILE')
found = g.find('Иван')
print(f'Найдено по \"Иван\": {len(found)}')
" && echo "✓ Тест 4 OK" || echo "✗ Тест 4 ОШИБКА"

echo
echo "5. stats() — статистика..."
run_test "
g = Group('$CSV_FILE')
stats = g.stats()
print(f'Студентов: {stats[\"count\"]}')
print(f'Средний GPA: {stats[\"avg_gpa\"]:.2f}')
print(f'Группы: {stats[\"groups\"]}')
" && echo "✓ Тест 5 OK" || echo "✗ Тест 5 ОШИБКА"

echo
echo "6. update() — GPA Иванова -> 4.5..."
run_test "
g = Group('$CSV_FILE')
updated = g.update('Иванов Иван', gpa=4.5)
print(f'Обновлено: {updated}')
print(f'Новый GPA Иванова: {g.list()[0].gpa}')
" && echo "✓ Тест 6 OK" || echo "✗ Тест 6 ОШИБКА"

echo
echo "7. remove() — удаляем Петрова..."
run_test "
g = Group('$CSV_FILE')
removed = g.remove('Петров Пётр')
print(f'Удалено: {removed}')
print(f'Осталось: {len(g.list())}')
" && echo "✓ Тест 7 OK" || echo "✗ Тест 7 ОШИБКА"

echo
echo "=== Все тесты ✓ УСПЕШНО ==="
echo "CSV создан: $CSV_FILE"
echo "Содержимое:"
cat "$CSV_FILE"
rm -f "$TEST_PY"
