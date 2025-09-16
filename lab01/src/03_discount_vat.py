from decimal import Decimal, InvalidOperation
from typing import Optional


def is_valid_number_string(input_string: str) -> bool:
    """Проверяет, является ли строка корректным числом"""
    cleaned = input_string.strip().replace(',', '.')
    if not cleaned:
        return False
    if cleaned.startswith('-'):
        cleaned = cleaned[1:]
    if cleaned.count('.') > 1:
        return False
    if not cleaned.replace('.', '').isdigit():
        return False
    return True


def parse_number_string(number_string: str) -> Optional[Decimal]:
    """Парсит строку в Decimal, возвращает None при ошибке"""
    try:
        normalized = number_string.strip().replace(',', '.')
        return Decimal(normalized)
    except (InvalidOperation, ValueError):
        return None


def get_valid_decimal(prompt: str) -> Decimal:
    """Запрашивает вещественное число, пока не введут корректное"""
    while True:
        try:
            user_input = input(prompt)
            if not is_valid_number_string(user_input):
                raise ValueError("Некорректный формат числа (допустимы только цифры и десятичная точка/запятая)")
            number = parse_number_string(user_input)
            if number is None:
                raise ValueError("Не удалось преобразовать в число")
            if number < 0:
                raise ValueError("Число не может быть отрицательным")
            return number
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}. Попробуйте ещё раз")


def main() -> None:
    price = get_valid_decimal("Введите цену (₽): ")
    discount = get_valid_decimal("Введите скидку (%): ")
    vat = get_valid_decimal("Введите НДС (%): ")

    base = price * (Decimal('1') - discount / Decimal('100'))
    vat_amount = base * (vat / Decimal('100'))
    total = base + vat_amount

    print(f"База после скидки: {base:.2f} ₽")
    print(f"НДС:               {vat_amount:.2f} ₽")
    print(f"Итого к оплате:    {total:.2f} ₽")


if __name__ == "__main__":
    main()
