import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.mark.parametrize(
    "value",
    [
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
                "code": "USD",
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
                "code": "USD",
            },
        ]
    ],
)
def test_filter_by_currency(value):
    result = filter_by_currency(value)
    assert next(result) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
        "code": "USD",
    }
    assert next(result) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
        "code": "USD",
    }


@pytest.mark.parametrize(
    "value",
    [
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
                "code": "USD",
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
                "code": "USD",
            },
        ]
    ],
)
def test_transaction_descriptions(value):
    result = transaction_descriptions(value)
    assert next(result) == "Перевод организации"
    assert next(result) == "Перевод со счета на счет"


@pytest.mark.parametrize(
    "start, stop, result",
    [(1, 5, ["0000000000000001", "0000000000000002", "0000000000000003", "0000000000000004"]), (0, 0, [])],
)
def test_card_number_generator(start, stop, result):
    assert card_number_generator(start, stop) == result
