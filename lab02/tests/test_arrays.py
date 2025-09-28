import pytest
from lab02.src.arrays import min_max, unique_sorted, flatten


def test_min_max():
    assert min_max([3, -1, 5, 5, 0]) == (-1, 5)
    assert min_max([42]) == (42, 42)
    assert min_max([-5, -2, -9]) == (-9, -2)
    assert min_max([1.5, 2, 2.0, -3.1]) == (-3.1, 2)
    with pytest.raises(ValueError):
        min_max([])


def test_unique_sorted():
    assert unique_sorted([3, 1, 2, 1, 3]) == [1, 2, 3]
    assert unique_sorted([]) == []
    assert unique_sorted([-1, -1, 0, 2, 2]) == [-1, 0, 2]
    assert unique_sorted([1.0, 1, 2.5, 2.5, 0]) == [0, 1.0, 2.5]


def test_flatten():
    assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten(([1, 2], (3, 4, 5))) == [1, 2, 3, 4, 5]
    assert flatten([[1], [], [2, 3]]) == [1, 2, 3]
    with pytest.raises(TypeError):
        flatten([[1, 2], "ab"])
