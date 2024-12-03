import pytest

from src.masks import get_mask_card_number, get_mask_account
from src.processing import sort_by_date, filter_by_state
from src.widget import mask_account_card, get_date

not_sorted_by_date_1 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]
sorted_by_date_1 = [
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
]
not_sorted_by_date_2 = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]
sorted_by_date_2 = [
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
]


@pytest.mark.parametrize('value, expected',
                         [('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
                          ('Счет 7365410843013587', 'Счет 7365 41** **** 3587'),
                          ('', ''),
                          ('Счет 73654108430135874305', 'Неправильно ввели номер карты')])
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize('value, expected', [('Счет 7365410843013587', 'Счет **3587'), ])
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected


@pytest.mark.parametrize('value, expected', [('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
                                             ('', ''),
                                             ('Счет 73654108430135874305', 'Счет **4305')])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize('value, expected', [('2024-03-11T02:26:18.671407', '11.03.2024'),
                                             ('', ''),
                                             ('2024-03-11-32-54T02:26:18.671407', 'Неправильно введена дата')])
def test_get_date(value, expected):
    assert get_date(value) == expected


@pytest.mark.parametrize('value, expected',
                         [(not_sorted_by_date_1, sorted_by_date_1), (not_sorted_by_date_2, sorted_by_date_2), ('', [])])
def test_sort_by_date(value, expected):
    assert sort_by_date(value) == expected


@pytest.mark.parametrize('value, state, expected', [([{'id': 41428829, 'state': 'EXECUTED',
                                                       'date': '2019-07-03T18:35:29.512364'},
                                                      {'id': 939719570, 'state': 'CANCELED',
                                                       'date': '2018-06-30T02:08:58.425572'}], 'EXECUTED', [
                                                         {'id': 41428829, 'state': 'EXECUTED',
                                                          'date': '2019-07-03T18:35:29.512364'}]), ([], '', [])])
def test_filter_by_state(value, state, expected):
    assert filter_by_state(value, state) == expected
