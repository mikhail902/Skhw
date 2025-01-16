import pytest

# conf for test_processing

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


@pytest.fixture
def data_for_masks():
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def data_for_mask():
    return "Счет 7365410843498527"


@pytest.fixture
def data_for_filter_by_currency():
    return [
        {
            "id": 939734789,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
            "code": "USD",
        },
    ]


@pytest.fixture
def data_test_utils_dict():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
    ]


@pytest.fixture
def data_for_test_utils():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def result_data_for_test_utils():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def result_for_tests_excel():
    return [{'id': 650703, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210, 'currency_name': 'Sol',
             'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
             'description': 'Перевод организации'},
            {'id': 3598919, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740,
             'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065',
             'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'},
            {'id': 593027, 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'amount': 30368,
             'currency_name': 'Shilling', 'currency_code': 'TZS', 'from': 'Visa 1959232722494097',
             'to': 'Visa 6804119550473710', 'description': 'Перевод с карты на карту'},
            {'id': 366176, 'state': 'EXECUTED', 'date': '2020-08-02T09:35:18Z', 'amount': 29482,
             'currency_name': 'Rupiah', 'currency_code': 'IDR', 'from': 'Discover 0325955596714937',
             'to': 'Visa 3820488829287420', 'description': 'Перевод с карты на карту'},
            {'id': 5380041, 'state': 'CANCELED', 'date': '2021-02-01T11:54:58Z', 'amount': 23789,
             'currency_name': 'Peso', 'currency_code': 'UYU', 'from': 0, 'to': 'Счет 23294994494356835683',
             'description': 'Открытие вклада'},
            {'id': 1962667, 'state': 'EXECUTED', 'date': '2023-10-22T09:43:32Z', 'amount': 18588,
             'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Mastercard 7286844946221431',
             'to': 'Счет 76145988629288763144', 'description': 'Перевод организации'},
            {'id': 5294458, 'state': 'EXECUTED', 'date': '2022-06-20T18:08:20Z', 'amount': 16836,
             'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': 'Visa 2759011965877198',
             'to': 'Счет 38287443300766991082', 'description': 'Перевод с карты на карту'},
            {'id': 5429839, 'state': 'EXECUTED', 'date': '2023-06-23T19:46:34Z', 'amount': 25261,
             'currency_name': 'Hryvnia', 'currency_code': 'UAH', 'from': 0, 'to': 'Счет 76768135089446747029',
             'description': 'Открытие вклада'},
            {'id': 3226899, 'state': 'EXECUTED', 'date': '2023-04-17T09:21:15Z', 'amount': 21680,
             'currency_name': 'Koruna', 'currency_code': 'CZK', 'from': 0, 'to': 'Счет 88329674734590848775',
             'description': 'Открытие вклада'}]


@pytest.fixture
def result_for_tests_csv():
    return [{
        'id;state;date;amount;currency_name;currency_code;from;to;description': '650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации'},
        {
            'id;state;date;amount;currency_name;currency_code;from;to;description': '3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту'},
        {
            'id;state;date;amount;currency_name;currency_code;from;to;description': '593027;CANCELED;2023-07-22T05:02:01Z;30368;Shilling;TZS;Visa 1959232722494097;Visa 6804119550473710;Перевод с карты на карту'},
        {
            'id;state;date;amount;currency_name;currency_code;from;to;description': '366176;EXECUTED;2020-08-02T09:35:18Z;29482;Rupiah;IDR;Discover 0325955596714937;Visa 3820488829287420;Перевод с карты на карту'},
        {
            'id;state;date;amount;currency_name;currency_code;from;to;description': '5380041;CANCELED;2021-02-01T11:54:58Z;23789;Peso;UYU;;Счет 23294994494356835683;Открытие вклада'},
        {
            'id;state;date;amount;currency_name;currency_code;from;to;description': '1962667;EXECUTED;2023-10-22T09:43:32Z;18588;Peso;COP;Mastercard 7286844946221431;Счет 76145988629288763144;Перевод организации'},
        {
            'id;state;date;amount;currency_name;currency_code;from;to;description': '5294458;EXECUTED;2022-06-20T18:08:20Z;16836;Yuan Renminbi;CNY;Visa 2759011965877198;Счет 38287443300766991082;Перевод с карты на карту'},
        {
            'id;state;date;amount;currency_name;currency_code;from;to;description': '5429839;EXECUTED;2023-06-23T19:46:34Z;25261;Hryvnia;UAH;;Счет 76768135089446747029;Открытие вклада'},
        {
            'id;state;date;amount;currency_name;currency_code;from;to;description': '3226899;EXECUTED;2023-04-17T09:21:15Z;21680;Koruna;CZK;;Счет 88329674734590848775;Открытие вклада'}]

@pytest.fixture
def str_for_excel_tests():
    return "C:/Users/Sator/PycharmProjects/PythonProject3/data/excel_file_for_tests.xlsx"

@pytest.fixture
def str_for_csv_tests():
    return "C:/Users/Sator/PycharmProjects/PythonProject3/data/csv_file_for_tests.csv"