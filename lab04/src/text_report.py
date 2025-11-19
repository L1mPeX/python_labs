import sys
import argparse
from collections import Counter
from lib.text import normalize, tokenize, count_freq, top_n
from io_txt_to_csv import read_text, write_csv

def frequencies_from_text(text: str) -> dict[str, int]:
    tokens = tokenize(normalize(text))
    return Counter(tokens)

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

def main():
    parser = argparse.ArgumentParser(description="Счётчик частот слов из текстового файла с выводом в CSV.")
    parser.add_argument("--in", dest="input_path", default="../data/input.txt",
                        help="Входной текстовый файл")
    parser.add_argument("--out", dest="output_path", default="../data/report.csv",
                        help="Путь для CSV отчёта")
    parser.add_argument("--encoding", default="utf-8",
                        help="Кодировка входного файла (по умолчанию utf-8)")
    args = parser.parse_args()

    try:
        text = read_text(args.input_path, encoding=args.encoding)
    except FileNotFoundError:
        print(f"Ошибка: файл {args.input_path} не найден.", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Ошибка: не удалось декодировать файл {args.input_path} с кодировкой {args.encoding}.", file=sys.stderr)
        sys.exit(1)

    freq = frequencies_from_text(text)
    sorted_freq = sorted_word_counts(freq)

    total_words = sum(freq.values())
    unique_words = len(freq)

    # Запись CSV с заголовком
    write_csv(sorted_freq, args.output_path, header=("word", "count"))

    # Вывод в консоль краткого отчёта, включая топ-5
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top_n(freq, 5):
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()
