import json
import logging

from src.external_api import conversion

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("C:/Users/Sator/PycharmProjects/PythonProject3/logs/utils_data.log", "a")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def dict_transactions(url: str) -> list:
    """Функция конвертации ссылки в список транкзаций"""
    try:
        with open(url, "r", encoding="utf-8") as f:
            data_list = json.load(f)
            logger.info("Список сконвертировался")
            return data_list
    except (FileNotFoundError, TypeError, json.JSONDecodeError) as e:
        logger.error(f"Ошибка чтения файла в функции dict_transactions, {e}")
        return []


def sum_transactions(transaction: list) -> float:
    """Функция суммирования транкзаций и перевод в рубли"""
    try:
        sum_ruble = 0
        for tr in transaction:
            tr_in_ruble = conversion(tr)
            float_tr_in_ruble = float(tr_in_ruble)
            sum_ruble += float_tr_in_ruble
        logging.info("Функция sum_transactions успешно выполнена")
        return sum_ruble
    except ValueError as e:
        logging.error(f"Ошибка в функции sum_transactions, {e}")
        return 0


file_path = "C:/Users/Sator/PycharmProjects/PythonProject3/data/operation.json"
print(dict_transactions(file_path))
