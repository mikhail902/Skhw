import re

PATH_TO_EXCEL = "C:/Users/Sator/PycharmProjects/PythonProject3/data/excel_file.xlsx"
PATH_TO_CSV = "C:/Users/Sator/PycharmProjects/PythonProject3/data/csv_file.csv"


def search_of_operations(operations: list, key: str) -> list:
    """ """
    new_list = []
    pattern = re.compile(key)
    for dict_number in operations:
        if pattern.search(str(dict_number["description"])):
            new_list.append(dict_number)
    return new_list
