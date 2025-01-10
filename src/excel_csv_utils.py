import csv

import pandas as pd

PATH_TO_EXCEL = "C:/Users/Sator/PycharmProjects/PythonProject3/data/excel_file.xlsx"
PATH_TO_CSV = "C:/Users/Sator/PycharmProjects/PythonProject3/data/csv_file.csv"


def excel_transaction(path_file_excel: str) -> list:
    """Функция считывания операций из эксель файла"""
    list_operations_excel = []
    operations = pd.read_excel(path_file_excel)
    for index, row in operations.iterrows():
        if index != "Name":
            list_operations_excel.append({index: row})
    return list_operations_excel


def csv_transaction(path_file_csv: str) -> list:
    """Функция считывания операций из csv файла"""
    list_operations_csv = []
    with open(path_file_csv) as file:
        reader = csv.reader(file)
        for row in reader:
            list_operations_csv.append(row)
    return list_operations_csv


print(excel_transaction(PATH_TO_EXCEL))
print(csv_transaction(PATH_TO_CSV))
