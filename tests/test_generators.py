import pytest

from src.generators import filter_by_currency

@pytest.mark.parametrize
def test_filter_by_currency():
    assert