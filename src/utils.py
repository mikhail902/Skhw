import json

from external_api import conversion


def dict_transactions(url: str) -> list:
    """Функция конвертации ссылки в список транкзаций"""
    try:
        with open(url, 'a') as f:
            data_list = json.load(f)
            return data_list
    except (FileNotFoundError, TypeError, json.JSONDecodeError) as e:
        print(f'Ошибка чтения файла {e}')
        return []


def sum_transactions(transaction: list) -> float:
    """Функция суммирования транкзаций и перевод в рубли"""
    sum_ruble = 0
    for tr in transaction:
        tr_in_ruble = conversion(tr)
        float_tr_in_ruble = float(tr_in_ruble)
        sum_ruble += float_tr_in_ruble
    return sum_ruble


file_path = 'data/operations.json'
# dict_transactions(file_path)
