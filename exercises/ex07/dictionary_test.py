"""Unit Tests for EX 07."""

__author__ = "730622763"
from exercises.ex07.dictionary import invert, favorite_colors, count

def test_empty() -> None:
    """considered an edge case since not likely to give empty dict."""
    assert invert({}) == {}

def test_many() -> None:
    """considered a use case since multiple values in dict."""
    test_dict: dict[str, str] = {'a': 'z', 'b' : 'y', 'c': 'x'}
    assert invert(test_dict) == {'z': 'a', 'y': 'b', 'x': 'c'}

def test_value_same_as_key() -> None:
    """Likely to give same str as key and value."""
    test_dict: dict[str, str] = {'a': 'a', 'b' : 'y', 'c': 'x'}
    assert invert(test_dict) == {'a': 'a', 'y': 'b', 'x': 'c'}

def test_empty() -> None:
    """considered an edge case since not likely to give empty dict."""
    assert favorite_colors({}) == ""

def test_many() -> None:
    """considered a use case since multiple values in dict."""
    test_dict: dict[str, str] = {'a': 'green', 'b' : 'green', 'c': 'blue'}
    assert favorite_colors(test_dict) == "green"

def test_two_popular_colors() -> None:
    """likely to have two popular options."""
    test_dict: dict[str, str] = {'a': 'green', 'b' : 'green', 'c': 'blue', 'v': 'orange', 'r': 'blue'}
    assert favorite_colors(test_dict) == "green"

def test_empty() -> None:
    """considered an edge case since not likely to give empty dict."""
    assert count([]) == {}

def test_many() -> None:
    """considered a use case since multiple values in dict."""
    test_list: list[str] = [4, 3, 4, 2, 5, 4]
    assert count(test_list) == {'4': '3', '3': '1', '2': '1', '5': '1'}

def test_same_number() -> None:
    """user can input only same number in list."""
    test_list: list[str] = [4, 4, 4, 4, 4]
    assert count(test_list) == {'4': '5'}