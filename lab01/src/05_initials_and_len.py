from typing import List


def get_valid_full_name(prompt: str) -> str:
    """Запрашивает ФИО и проверяет, что введено хотя бы два слова"""
    while True:
        full_name = input(prompt)
        if not full_name.strip():
            print("Ошибка: ввод не может быть пустым")
            continue

        parts: List[str] = full_name.split()
        if len(parts) < 2:
            print("Ошибка: требуется минимум два слова (Фамилия и Имя)")
            continue

        return full_name


def build_initials(parts: List[str]) -> str:
    """Формирует инициалы в верхнем регистре из списка слов"""
    initials = "".join(word[0].upper() for word in parts) + "."
    return initials


def main() -> None:
    full_name = get_valid_full_name("ФИО: ")
    trimmed = full_name.strip()
    length = len(trimmed)

    parts = trimmed.split()
    initials = build_initials(parts)

    print(f"Инициалы: {initials}")
    print(f"Длина (символов): {length}")


if __name__ == "__main__":
    main()
