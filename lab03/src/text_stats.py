import sys
from lib.text import normalize, tokenize, count_freq, top_n

def main():
    input_text = sys.stdin.read()
    norm_text = normalize(input_text)
    tokens = tokenize(norm_text)
    freq = count_freq(tokens)

    total_words = len(tokens)
    unique_words = len(freq)
    top5 = top_n(freq, 5)

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top5:
        print(f"{word}:{count}")

if __name__ == '__main__':
    main()
