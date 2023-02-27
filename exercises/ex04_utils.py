"""EX04 - Utils."""

__author__ = "730622763"

def all(int_list: list[int], int) -> bool:
    while len(str(int)) < len(int_list):
        if int_list == int:
            return True
        else:
            return False

def max(max_integers_list: list[int]) -> int:
    """Determines the max number in the list.""" 
    if len(max_integers_list) == 0:
        raise ValueError("max() arg is an empty List")
    max_integers_list_idx: int = 0 
    max_integer: int = int(max_integers_list[0])
    while max_integers_list_idx < len(max_integers_list):
        current_int: int = int(max_integers_list[max_integers_list_idx])
        if (current_int > max_integer):
                max_integer = current_int
        max_integers_list_idx += 1
    print(max_integer)

def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Determines if first list integers match second list integers at same index."""
    list_idx: int = 0
    while list_idx > len(first_list):
        if first_list[list_idx] == second_list[list_idx]:
            return True
        else:
            return False
    list_idx += 1
        