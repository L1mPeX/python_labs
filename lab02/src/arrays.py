def min_max(arr):
    if not arr:
        raise ValueError("Массив пуст")
    return min(arr), max(arr)


def unique_sorted(arr):
    return sorted(set(arr))


def flatten(nested):
    if not all(isinstance(x, (list, tuple)) for x in nested):
        raise TypeError("Все элементы должны быть списками или кортежами")
    result = []
    for seq in nested:
        result.extend(seq)
    return result
