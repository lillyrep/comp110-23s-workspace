"""EX 08 - Data Wrangling."""

__author__ = "730622763"

from csv import DictReader


DATA_DIRECTORY = "../../data"
DATA_FILE_PATH = f"{DATA_DIRECTORY}/nc_durham_2015_march_21_to_26.csv"

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table under a certain header e.g. high, low, etc."""
    result: list[str] = []
    # step through table
    for row in table:
        # save every value under key "header"
        result.append(row[header])
    return result
    

def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of table
    first_row: dict[str, str] = table[0]
    for key in first_row: 
        # for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result


def head(table: dict[str, list[str]], row_count: int) -> dict[str, list[str]]:
    return_dict: dict[str, list[str]] = {}
    row_count: n = 1
    for columns in table[row_count]:
        new_list: list[str] = []
        for n in columns:
            new_list.append(n[columns])
        return_dict[n] = head(columns, new_list)
    return return_dict

def select(first_table: dict[str, list[str]], first_list: list[str]) -> dict[str, list[str]]:
    returning_dict: dict[str, list[str]] = {}

def concat(one_table: dict[str, list[str]], two_table: dict[str, list[str]]) -> dict[str, list[str]]:
    the_return: dict[str, list[str]] = {}
    for columns in one_table:

