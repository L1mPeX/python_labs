from typing import Tuple


def parse_participant(line: str) -> Tuple[str, str, int, bool]:
    """
    Разбирает строку участника вида:
    Фамилия Имя Возраст Формат_участия
    Возвращает кортеж (фамилия, имя, возраст, формат).
    """
    parts = line.strip().split()
    if len(parts) != 4:
        raise ValueError(f"Некорректный формат строки: {line}")

    last_name, first_name, age_str, format_str = parts

    if not age_str.isdigit():
        raise ValueError(f"Возраст должен быть целым числом: {age_str}")
    age = int(age_str)

    if format_str not in ("True", "False"):
        raise ValueError(f"Формат участия должен быть 'True' или 'False', а получено: {format_str}")
    is_fulltime = format_str == "True"

    return last_name, first_name, age, is_fulltime


def main() -> None:
    n_str = input().strip()
    if not n_str.isdigit():
        raise ValueError("Первое значение должно быть целым числом")
    n = int(n_str)

    fulltime_count = 0
    parttime_count = 0

    for _ in range(n):
        participant_line = input()
        _, _, _, is_fulltime = parse_participant(participant_line)
        if is_fulltime:
            fulltime_count += 1
        else:
            parttime_count += 1

    print(fulltime_count, parttime_count)


if __name__ == "__main__":
    main()
