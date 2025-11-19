from lib.text import normalize, tokenize, count_freq, top_n

def test_normalize():
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"
    assert normalize("Hello\r\nWorld") == "hello world"
    assert normalize("  двойные   пробелы  ") == "двойные пробелы"

def test_tokenize():
    assert tokenize("привет мир") == ["привет", "мир"]
    assert tokenize("hello,world!!!") == ["hello", "world"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]
    assert tokenize("emoji 😀 не слово") == ["emoji", "не", "слово"]

def test_count_freq_and_top_n():
    tokens = ["a","b","a","c","b","a"]
    freq = count_freq(tokens)
    assert freq == {"a":3, "b":2, "c":1}
    assert top_n(freq, 2) == [("a",3), ("b",2)]

    tokens2 = ["bb","aa","bb","aa","cc"]
    freq2 = count_freq(tokens2)
    assert top_n(freq2, 2) == [("aa",2), ("bb",2)]

def run_all_tests():
    test_normalize()
    test_tokenize()
    test_count_freq_and_top_n()
    print("Все тесты пройдены успешно")

if __name__ == "__main__":
    run_all_tests()
