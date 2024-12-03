import pytest

from src.processing import filter_by_state, sort_by_date
from tests.conftest import not_sorted_by_date_1, not_sorted_by_date_2, sorted_by_date_1, sorted_by_date_2


@pytest.mark.parametrize(
    "value, expected", [(not_sorted_by_date_1, sorted_by_date_1), (not_sorted_by_date_2, sorted_by_date_2), ("", [])]
)
def test_sort_by_date(value, expected):
    assert sort_by_date(value) == expected


@pytest.mark.parametrize(
    "value, state, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
            ],
            "EXECUTED",
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
        ),
        ([], "", []),
    ],
)
def test_filter_by_state(value, state, expected):
    assert filter_by_state(value, state) == expected
