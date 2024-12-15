import os

import requests
from dotenv import load_dotenv

load_dotenv(".env")
API_KEY = os.getenv("API_KEY")


def conversion(dictionary: dict) -> any:
    """Функция конвертации в рубли"""
    try:
        url = "https://api.apilayer.com/exchangerates_data/convert"
        payload = {
            "amount": dictionary["operationAmount"]["amount"],
            "from": dictionary["operationAmount"]["currency"]["code"],
            "to": "RUB",
        }
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers, params=payload).json()
        return response["result"]
    except KeyError:
        return "Ошибка конвертации, закончился лимит запросов на перевод валюты"
