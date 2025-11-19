#!/bin/bash
set -e

echo "Создаем директории для тестовых данных..."
mkdir -p ../data/samples
mkdir -p ../data/out

echo "Создаем пример JSON для теста json_to_csv..."
cat > ../data/samples/people.json << EOF
[
  {"name": "Alice", "age": "22", "city": "SPB"},
  {"name": "Bob", "age": "25", "city": "Moscow"}
]
EOF

echo "Создаем пример CSV для теста csv_to_json и csv_to_xlsx..."
cat > ../data/samples/people.csv << EOF
name,age,city
Alice,22,SPB
Bob,25,Moscow
EOF

echo "Тестируем json_to_csv..."
python3 -c "
from json_csv import json_to_csv
json_to_csv('../data/samples/people.json', '../data/out/people_from_json.csv')
"
if [[ ! -s ../data/out/people_from_json.csv ]]; then
  echo 'json_to_csv: Ошибка, файл не создан или пуст!'
  exit 1
fi

echo "Тестируем csv_to_json..."
python3 -c "
from json_csv import csv_to_json
csv_to_json('../data/samples/people.csv', '../data/out/people_from_csv.json')
"
if [[ ! -s ../data/out/people_from_csv.json ]]; then
  echo 'csv_to_json: Ошибка, файл не создан или пуст!'
  exit 1
fi

echo "Тестируем csv_to_xlsx..."
python3 -c "
from csv_xlsx import csv_to_xlsx
csv_to_xlsx('../data/samples/people.csv', '../data/out/people.xlsx')
"
if [[ ! -s ../data/out/people.xlsx ]]; then
  echo 'csv_to_xlsx: Ошибка, файл не создан или пуст!'
  exit 1
fi

echo "Все тесты ЛР5 пройдены успешно!"
