"""Unit tests for sum function """

from lessons.sum import sum

def test_empty() -> None:
    """considered an edge case."""
    assert sum([]) == 0.0

def test_one_element() -> None:
    """considered an edge case."""
    test_list: list[float] = [1.0]
    assert sum(test_list) == 1.0

def test_many() -> None:
    """considered a use case since multiple values in list."""
    test_list: list[float] = [1.0, 2.0, 3.0]
    assert sum(test_list) == 6.0

def test_many_with_negatives() -> None:
    """considered a use case."""
    test_list: list[float] = [1.0, -2.0, 1.0]
    assert sum(test_list) == 0
