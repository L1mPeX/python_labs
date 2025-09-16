from typing import Optional


def is_valid_integer_string(input_string: str) -> bool:
    """Проверяет, является ли строка корректным целым числом"""
    cleaned = input_string.strip()
    if not cleaned:
        return False
    if cleaned.startswith('-'):
        return False
    return cleaned.isdigit()


def parse_integer_string(number_string: str) -> Optional[int]:
    """Парсит строку в int, возвращает None при ошибке"""
    try:
        return int(number_string.strip())
    except ValueError:
        return None


def get_valid_minutes(prompt: str) -> int:
    """Получает и валидирует количество минут"""
    while True:
        user_input = input(prompt)
        if not is_valid_integer_string(user_input):
            print("Ошибка: нужно ввести целое неотрицательное число минут")
            continue

        minutes = parse_integer_string(user_input)
        if minutes is None:
            print("Ошибка: не удалось преобразовать в число")
            continue

        return minutes


def main() -> None:
    minutes = get_valid_minutes("Минуты: ")
    hours = minutes // 60
    mins = minutes % 60
    print(f"{hours}:{mins:02d}")


if __name__ == "__main__":
    main()
