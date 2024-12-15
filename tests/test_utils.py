from src.utils import dict_transactions


def test_dict_transactions(data_test_utils_dict):
    assert (
        dict_transactions("C:/Users/Sator/PycharmProjects/PythonProject3/data/for_test.json") == data_test_utils_dict
    )
    assert dict_transactions("") == []
