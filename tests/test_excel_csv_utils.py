from src.excel_csv_utils import excel_transaction, csv_to_list_of_dicts


def test_excel_transaction(str_for_excel_tests, result_for_tests_excel):
    assert excel_transaction(str_for_excel_tests) == result_for_tests_excel


def test_csv_to_list_of_dicts(str_for_csv_tests, result_for_tests_csv):
    assert csv_to_list_of_dicts(str_for_csv_tests) == result_for_tests_csv
