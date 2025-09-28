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
