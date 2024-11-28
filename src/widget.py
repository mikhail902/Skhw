from datetime import datetime

from masks import get_mask_account, get_mask_card_number


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
    date_str = date_list[0]
    date_object = datetime.strptime(date_str, "%Y-%m-%d")
    return date_object.strftime("%d.%m.%Y")
