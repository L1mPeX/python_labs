def transpose(matrix):
    if not matrix:
        return []
    length = len(matrix[0])
    if not all(len(row) == length for row in matrix):
        raise ValueError("Матрица должна быть прямоугольной")
    return [list(row) for row in zip(*matrix)]


def row_sums(matrix):
    if not matrix:
        return []
    length = len(matrix[0])
    if not all(len(row) == length for row in matrix):
        raise ValueError("Матрица должна быть прямоугольной")
    return [sum(row) for row in matrix]


def col_sums(matrix):
    if not matrix:
        return []
    length = len(matrix[0])
    if not all(len(row) == length for row in matrix):
        raise ValueError("Матрица должна быть прямоугольной")
    return [sum(col) for col in zip(*matrix)]
