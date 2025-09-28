import pytest
from lab02.src.matrix import transpose, row_sums, col_sums


def test_transpose():
    assert transpose([[1, 2, 3]]) == [[1], [2], [3]]
    assert transpose([[1], [2], [3]]) == [[1, 2, 3]]
    assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    assert transpose([]) == []
    with pytest.raises(ValueError):
        transpose([[1, 2], [3]])


def test_row_sums():
    assert row_sums([[1, 2, 3], [4, 5, 6]]) == [6, 15]
    assert row_sums([[-1, 1], [10, -10]]) == [0, 0]
    assert row_sums([[0, 0], [0, 0]]) == [0, 0]
    with pytest.raises(ValueError):
        row_sums([[1, 2], [3]])


def test_col_sums():
    assert col_sums([[1, 2, 3], [4, 5, 6]]) == [5, 7, 9]
    assert col_sums([[-1, 1], [10, -10]]) == [9, -9]
    assert col_sums([[0, 0], [0, 0]]) == [0, 0]
    with pytest.raises(ValueError):
        col_sums([[1, 2], [3]])
