"""EX 05 - List Utility Functions."""

__author__ = "730622763"

def only_evens(int_list: list[int]) -> list[int]:
    """Returning only even ints in an int list."""
    int_list_num: int = 0
    even_list: list[int] = list()
    while int_list_num < len(int_list):
        if (int_list[int_list_num]) % 2 == 0:
            even_list.append((int_list[int_list_num]))
        int_list_num += 1
    return even_list

def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Adding second list to the first list."""
    new_list: list[int] = list()
    for x in first_list:
        new_list.append(x)
    for y in second_list:
        new_list.append(y) 
    return new_list

def sub(int_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Outputs specified index of list."""
    sub_list: list[int] = list()
    if len(int_list) == 0 or start_index >= len(int_list) or end_index <= 0:
        return []
    if start_index < 0:
        start_index = 0
    if end_index > len(int_list):
        end_index = len(int_list)
    while start_index < end_index:
        sub_list.append(int_list[start_index])
        start_index += 1                        
    return sub_list
    