import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Счет 7365410843013587", "Счет 7365 41** **** 3587"),
        ("", ""),
        ("Счет 73654108430135874305", "Неправильно ввели номер карты"),
    ],
)
def test_get_mask_card_number_first(value, expected):
    assert get_mask_card_number(value) == expected


def test_get_mask_card_number_second(data_for_masks):
    assert get_mask_card_number(data_for_masks) == "Visa Platinum 7000 79** **** 6361"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Счет 7365410843013587", "Счет **3587"),
    ],
)
def test_get_mask_account_first(value, expected):
    assert get_mask_account(value) == expected


def test_get_mask_account_second(data_for_mask):
    assert get_mask_account(data_for_mask) == "Счет **8527"
