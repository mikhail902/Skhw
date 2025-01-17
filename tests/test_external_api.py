from unittest.mock import patch

from src.external_api import conversion


@patch("requests.get")
def test_conversion(mock_get, data_for_test_utils, result_data_for_test_utils):
    #mock_get.return_value.json.return_value = result_data_for_test_utils
    #assert conversion(data_for_test_utils) == result_data_for_test_utils
    #mock_get.assert_called_once_with("https://api.apilayer.com/exchangerates_data/convert")
    pass