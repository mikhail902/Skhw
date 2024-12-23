import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("C:/Users/Sator/PycharmProjects/PythonProject3/logs/masks_data.log", "a")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card: str) -> str:
    """Функция скрытия карты"""
    mask_card = ""
    for i in range(len(card)):
        if card[i].isdigit():
            if len(card[i:]) > 16:
                mask_card = "Неправильно ввели номер карты"
            else:
                mask_card = (
                    card[:i] + card[i : i + 4] + " " + card[i + 4 : i + 6] + 2 * "*" + " " + 4 * "*" + " " + card[-4:]
                )
            break
    logger.info("Функция get_mask_card_number выполнена успешно")
    return mask_card


def get_mask_account(mask_account_card: str) -> str:
    """Функция номера аккаунта"""
    logger.info("Функция get_mask_account выполнена успешно")
    return "Счет" + " " + 2 * "*" + mask_account_card[-4:]
