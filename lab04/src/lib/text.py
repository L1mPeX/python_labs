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
