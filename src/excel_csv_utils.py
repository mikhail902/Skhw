import csv

import pandas as pd

PATH_TO_EXCEL = "C:/Users/Sator/PycharmProjects/PythonProject3/data/excel_file.xlsx"
PATH_TO_CSV = "C:/Users/Sator/PycharmProjects/PythonProject3/data/csv_file.csv"


def excel_transaction(file_path: str) -> list:
    """Функция считывающая строки из эксель файла и превращающая в список словарей из строк файла"""
    try:
        df = pd.read_excel(file_path)
        list_of_dicts = df.to_dict(orient="records")
        return list_of_dicts
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден по пути: {file_path}")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []


if __name__ == "__main__":
    result = excel_transaction(PATH_TO_EXCEL)
    if result:
        for dictionary in result:
            print(dictionary)
    else:
        print("Не удалось прочитать данные из Excel файла.")


def csv_to_list_of_dicts(file_path: str) -> list:
    """Функция считывающая строки из csv файла и превращающая в список словарей из строк файла"""
    try:
        list_of_dicts = []
        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                list_of_dicts.append(row)
        return list_of_dicts
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден по пути: {file_path}")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []


if __name__ == "__main__":
    result = csv_to_list_of_dicts(PATH_TO_CSV)
    if result:
        for dictionary in result:
            print(dictionary)
    else:
        print("Не удалось прочитать данные из CSV файла.")
