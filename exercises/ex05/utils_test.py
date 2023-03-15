"""Unit Test for Utils."""

__author__ = "730622763"

from exercises.ex05.utils import only_evens, concat, sub

def test_empty() -> None:
    """considered an edge case."""
    assert only_evens([]) == []

def test_many() -> None:
    """considered a use case since multiple values in list."""
    test_list: list[int] = [1, 2, 4]
    assert only_evens(test_list) == [2, 4]

def test_with_negatives() -> None:
    """Likely to have a negative value in list."""
    test_list: list[int] = [-2, 7, 8]
    assert only_evens(test_list) == [-2, 8]

def test_first_empty() -> None:
      """Edge case."""
      first_test_list: list[int] = []
      second_list: list[int] = [3, 4, 6]
      assert concat(first_test_list, second_list) == [3, 4, 6]

def test_many() -> None:
    """If a list have more than one values so a use case."""
    first_list: list[int] = [1, 2, 4]
    second_list: list[int] = [1, 4, 7]
    assert concat(first_list, second_list) == [1, 2, 4, 1, 4, 7]