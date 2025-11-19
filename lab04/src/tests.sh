#!/bin/bash
set -e

echo "Создаем тестовый файл data/lab04/input.txt для ЛР4..."
cat > ../data/lab04/input.txt << EOF
Привет, мир! Привет!!! 🏧 🚮
EOF

echo "Создаем тестовый файл data/lab04/a.txt..."
cat > ../data/lab04/a.txt << EOF
Привет мир
EOF

echo "Создаем тестовый файл data/lab04/b.txt..."
cat > ../data/lab04/b.txt << EOF
Привет, привет!
EOF

echo "Запускаем скрипт ЛР4 и проверяем output report.csv..."
python3 text_report.py --in ../data/lab04/input.txt --out ../data/lab04/report.csv

echo "Проверяем содержимое data/lab04/report.csv..."
head -n 10 ../data/lab04/report.csv

echo "Тесты и генерация отчетов завершены успешно."
