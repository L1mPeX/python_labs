from decimal import Decimal, InvalidOperation
from typing import Tuple, Optional


def is_valid_number_string(input_string: str) -> bool:
    """Проверяет, является ли строка корректным числом"""
    cleaned_string = input_string.strip()
    
    if not cleaned_string:
        return False
    
    if cleaned_string.startswith('-'):
        cleaned_string = cleaned_string[1:]
    
    cleaned_string = cleaned_string.replace(',', '.')
    
    if not cleaned_string.replace('.', '').isdigit():
        return False
    
    if cleaned_string.count('.') > 1:
        return False
    
    if cleaned_string.startswith('.') or cleaned_string.endswith('.'):
        return False
    
    return True


def parse_number_string(number_string: str) -> Optional[Decimal]:
    """Парсит строку в Decimal, возвращает None при ошибке"""
    try:
        normalized_string = number_string.strip().replace(',', '.')
        return Decimal(normalized_string)
    except (InvalidOperation, ValueError):
        return None


def get_valid_number(prompt: str) -> Decimal:
    """Получает и валидирует ввод числа с повторными попытками"""
    while True:
        try:
            user_input = input(prompt)
            
            if not is_valid_number_string(user_input):
                raise ValueError("Некорректный формат числа. Используйте формат '123.45' или '123,45'")
            
            number = parse_number_string(user_input)
            if number is None:
                raise ValueError("Не удалось преобразовать в число")
                
            return number
        
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}. Попробуйте еще раз")


def calculate_sum_and_avg(num1: Decimal, num2: Decimal) -> Tuple[Decimal, Decimal]:
    """Вычисляет сумму и среднее арифметическое двух чисел"""
    total = num1 + num2
    average = total / Decimal('2')
    return total, average


def format_result(total: Decimal, average: Decimal) -> str:
    """Форматирует результат для вывода с двумя знаками после запятой"""
    return f"sum={total:.2f}; avg={average:.2f}"


def main() -> None:    
    num1 = get_valid_number("a: ")
    num2 = get_valid_number("b: ")
    
    total, average = calculate_sum_and_avg(num1, num2)
    
    result = format_result(total, average)
    print(result)


if __name__ == "__main__":
    main()