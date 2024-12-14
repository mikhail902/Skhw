import requests


def conversion(dictionary: dict):
    """Функция конвертации в рубли"""

    url = "https://api.apilayer.com/exchangerates_data/convert"
    payload = {
        "amount": dictionary['operationAmount']['amount'],
        "from": dictionary['operationAmount']['currency']['code'],
        "to": "RUB"
    }
    headers = {
        "apikey": "tP6pidXH3QMCPZmCOPfsyXE8CQxsvxMk"
    }
    response = requests.get(url, headers=headers, params=payload).json()

    return response['result']
