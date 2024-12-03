import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 7365410843013587", "Счет 7365 41** **** 3587"),
        ("", ""),
        ("Счет 73654108430135874305", "Неправильно ввели номер карты"),
    ],
)
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Счет 7365410843013587", "Счет **3587"),
    ],
)
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected
