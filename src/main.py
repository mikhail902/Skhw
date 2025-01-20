from src.excel_csv_utils import csv_to_list_of_dicts, excel_transaction
from src.filtered_operations import search_of_operations
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import dict_transactions

PATH_TO_EXCEL = "C:/Users/Sator/PycharmProjects/PythonProject3/data/excel_file.xlsx"
PATH_TO_CSV = "C:/Users/Sator/PycharmProjects/PythonProject3/data/csv_file.csv"
PATH_TO_JSON = "C:/Users/Sator/PycharmProjects/PythonProject3/data/operation.json"

"""# inputting
card = input()
date = input()

print(mask_account_card(card))
print(get_date(date))"""


def main() -> any:
    """Основная логика проекта"""

    # Пользователь выбирает какой файл нужно обработать
    number = input(
        """Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.
        Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла\n"""
    )
    if number == 1:
        print("Для обработки выбран JSON-файл.")
        default_list = dict_transactions(PATH_TO_JSON)
    elif number == 2:
        print("Для обработки выбран CSV-файл.")
        default_list = csv_to_list_of_dicts(PATH_TO_CSV)
    else:
        print("Для обработки выбран XLSX-файл.")
        default_list = excel_transaction(PATH_TO_EXCEL)

    # По какому статусу фильтровать
    status = input(
        """Введите статус, по которому необходимо выполнить фильтрацию. 
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"""
    )
    if status != "":
        new_list_by_status = filter_by_state(default_list, status)
    else:
        new_list_by_status = default_list

    # Сортировка операций по дате
    sort_by_date_str = input("""Отсортировать операции по дате? Да/Нет\n""")
    if sort_by_date_str.lower() == "да":
        method_of_sort = input("Отсортировать по возрастанию или по убыванию?\n")
        if method_of_sort.lower() == "по возрастанию":
            method_of_sort_bool = True
            new_list_by_date = sort_by_date(new_list_by_status, method_of_sort_bool)
        else:
            method_of_sort_bool = False
            new_list_by_date = sort_by_date(new_list_by_status, method_of_sort_bool)
    else:
        new_list_by_date = new_list_by_status

    # обработка по рублевым операциям
    a = input("""Выводить только рублевые тразакции? Да/Нет\n""")
    if a == "да".lower():
        new_list_by_currency = filter_by_currency(new_list_by_date, "RUB")
    else:
        new_list_by_currency = new_list_by_date

    # обработка по определенному описанию
    b = input("""Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n""")
    if b.lower() == "да":
        user_str = input("Введите ваш текст для отборки\n")
        new_list_by_description = search_of_operations(new_list_by_currency, user_str)
    else:
        new_list_by_description = new_list_by_currency

    # Вывод
    print("Распечатываю итоговый список транзакций...")
    if len(new_list_by_description) > 0:
        print(f"Всего банковских операций в выборке: {len(new_list_by_description)}")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    return new_list_by_description


print(main())
