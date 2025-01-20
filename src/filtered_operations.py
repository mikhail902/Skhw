import re
from src.excel_csv_utils import *
from collections import Counter

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


def count_operations_by_category(operations: list, category_key_str: str) -> any:
    """Функция подсчета операций по категориям"""
    categories = [op[category_key_str] for op in operations if category_key_str in op]
    return Counter(categories)


category_key = "to"  # задаем категорию
default_list = csv_to_list_of_dicts(PATH_TO_CSV)
print(count_operations_by_category(default_list, category_key))
