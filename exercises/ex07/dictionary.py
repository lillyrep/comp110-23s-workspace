"""EX 07 - Dictionary Functions."""

__author__ = "730622763"


def invert(first_dict: dict[str, str]) -> dict[str, str]:
    """Inverts key and values."""
    result: dict[str, str] = {}
    for key in first_dict:
        val = first_dict[key]
        result[val] = key
    if key == key:
        raise ValueError("Key values must be unique.")
    return result


def favorite_color(color_list: dict[str, str]) -> str:
    """Returns color listed the most."""
    color_count: int = 0
    for color in color_list:
        if color in color_list:
            color_count[color] += 1
        else:
            color_count[count] = 0
    return max(color_list[color])


def count(count_list: list[str]) -> dict[str, int]:
    """Do this."""
    new_dict: dict[str, int] = {}
    for item in count_list:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    return new_dict