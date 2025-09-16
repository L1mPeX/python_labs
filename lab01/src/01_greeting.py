from decimal import InvalidOperation
from typing import Optional


def is_valid_integer_string(input_string: str) -> bool:
    """Проверяет, является ли строка корректным целым числом (без пробелов, запятых и точек)"""
    cleaned = input_string.strip()
    if not cleaned:
        return False
    if cleaned.startswith('-'):
        cleaned = cleaned[1:]
    return cleaned.isdigit()


def parse_integer_string(number_string: str) -> Optional[int]:
    """Парсит строку в int, возвращает None при ошибке"""
    try:
        return int(number_string.strip())
    except (ValueError, InvalidOperation):
        return None


def get_valid_integer(prompt: str, min_value: int = 0, max_value: int = 150) -> int:
    """Получает и валидирует ввод целого числа с повторными попытками"""
    while True:
        try:
            user_input = input(prompt)

            if not is_valid_integer_string(user_input):
                raise ValueError("Возраст должен быть целым числом (без запятых и точек)")

            number = parse_integer_string(user_input)
            if number is None:
                raise ValueError("Не удалось преобразовать в число")

            if number < min_value:
                raise ValueError(f"Возраст не может быть меньше {min_value}")
            if number > max_value:
                raise ValueError(f"Возраст не может быть больше {max_value}")

            return number

        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}. Попробуйте ещё раз")


def get_valid_name(prompt: str) -> str:
    """Получает и валидирует имя (только буквы, минимум 1 символ)"""
    while True:
        name = input(prompt).strip()
        if not name:
            print("Ошибка: имя не может быть пустым")
            continue
        if any(ch.isdigit() for ch in name):
            print("Ошибка: имя не должно содержать цифры")
            continue
        return name


def main() -> None:
    name = get_valid_name("Имя: ")
    age = get_valid_integer("Возраст: ")
    print(f"Привет, {name}! Через год тебе будет {age + 1}.")


if __name__ == "__main__":
    main()
