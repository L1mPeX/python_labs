# Лабораторная работа № 3

## Тексты и частоты слов (словарь/множество)

text.py
```python
import re
from typing import List, Tuple, Dict

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    text = re.sub(r'[\t\r\n]+', ' ', text)
    text = re.sub(r' +', ' ', text).strip()
    return text

token_pattern = re.compile(r'\b\w+(?:-\w+)*\b', re.UNICODE)

def tokenize(text: str) -> List[str]:
    return token_pattern.findall(text)

def count_freq(tokens: List[str]) -> Dict[str, int]:
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq

def top_n(freq: Dict[str, int], n: int = 5) -> List[Tuple[str, int]]:
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]
```

text_stats.py
```python
import re
from typing import List, Tuple, Dict

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    text = re.sub(r'[\t\r\n]+', ' ', text)
    text = re.sub(r' +', ' ', text).strip()
    return text

token_pattern = re.compile(r'\b\w+(?:-\w+)*\b', re.UNICODE)

def tokenize(text: str) -> List[str]:
    return token_pattern.findall(text)

def count_freq(tokens: List[str]) -> Dict[str, int]:
    freq = {}
    for token in tokens:
        freq[token] = freq.get(token, 0) + 1
    return freq

def top_n(freq: Dict[str, int], n: int = 5) -> List[Tuple[str, int]]:
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]
```

Для тестов есть скрипт tests.py
```python
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
```

Скриншот вывода тестов:
![Скриншот 1](./materials/imgage.png)

## Лицензия <a name="license"></a>

[![License: CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
Проект доступен с открытым исходным кодом на условиях [Лицензии CC BY-NC-SA 4.0](./LICENSE).

_Авторские права 2025 Андрей Казарин_
