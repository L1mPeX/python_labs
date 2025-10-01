# Лабораторная работа № 2

## Коллекции и матрицы (list/tuple/set/dict)

arrays.py
```python
def min_max(arr):
    if not arr:
        raise ValueError("Массив пуст")
    return min(arr), max(arr)


def unique_sorted(arr):
    return sorted(set(arr))


def flatten(nested):
    if not all(isinstance(x, (list, tuple)) for x in nested):
        raise TypeError("Все элементы должны быть списками или кортежами")
    result = []
    for seq in nested:
        result.extend(seq)
    return result
```

matrix.py
```python
def transpose(matrix):
    if not matrix:
        return []
    length = len(matrix[0])
    if not all(len(row) == length for row in matrix):
        raise ValueError("Матрица должна быть прямоугольной")
    return [list(row) for row in zip(*matrix)]


def row_sums(matrix):
    if not matrix:
        return []
    length = len(matrix[0])
    if not all(len(row) == length for row in matrix):
        raise ValueError("Матрица должна быть прямоугольной")
    return [sum(row) for row in matrix]


def col_sums(matrix):
    if not matrix:
        return []
    length = len(matrix[0])
    if not all(len(row) == length for row in matrix):
        raise ValueError("Матрица должна быть прямоугольной")
    return [sum(col) for col in zip(*matrix)]
```

tuples.py
```python
def format_record(record):
    if not isinstance(record, tuple) or len(record) != 3:
        raise TypeError("Ожидается кортеж из 3 элементов")

    name, group, gpa = record

    if not isinstance(name, str) or not name.strip():
        raise ValueError("Некорректное имя")
    if not isinstance(group, str) or not group.strip():
        raise ValueError("Некорректная группа")
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должен быть числом")

    parts = name.strip().split()
    surname = parts[0].capitalize()
    initials = "".join(p[0].upper() + "." for p in parts[1:])

    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"
```

Тесты запускаются автоматически по workflow:
![Скриншот 1](lab02/materials/img.png)

## Лицензия <a name="license"></a>

[![License: CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
Проект доступен с открытым исходным кодом на условиях [Лицензии CC BY-NC-SA 4.0](./LICENSE).

_Авторские права 2025 Андрей Казарин_
