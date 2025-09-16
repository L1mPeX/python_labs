def restore_string(s: str) -> str:
    start_idx = None
    for i, ch in enumerate(s):
        if ch.isupper():
            start_idx = i
            break
    if start_idx is None:
        raise ValueError("Не найдена заглавная буква")

    second_idx = None
    for i, ch in enumerate(s[:-1]):
        if ch.isdigit():
            second_idx = i + 1
            break
    if second_idx is None:
        raise ValueError("Не найдена цифра для второго символа")

    step = second_idx - start_idx
    if step <= 0:
        raise ValueError("Некорректный шаг")

    result = []
    i = start_idx
    while i < len(s):
        result.append(s[i])
        if s[i] == '.':
            break
        i += step

    return "".join(result)


def main():
    s = input().strip()
    print(restore_string(s))


if __name__ == "__main__":
    main()
