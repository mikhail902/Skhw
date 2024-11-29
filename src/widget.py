from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    """Маскирует номер карты или счета в строке"""

    if card.startswith("Счет"):
        mask_card = get_mask_account(card)
    else:
        mask_card = get_mask_card_number(card)

    return mask_card


def get_date(date: str) -> datetime.date:
    """Функция преобразованияя даты"""

    date_list = date.split("T")
    if len(date_list[0]) > 10:
        original_date = "Неправильно введена дата"
    elif len(date) == 0:
        original_date = ""
    else:
        date_str = date_list[0]
        date_object = datetime.strptime(date_str, "%Y-%m-%d")
        original_date = date_object.strftime("%d.%m.%Y")
    return original_date
