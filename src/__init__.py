API_KEY = 'tP6pidXH3QMCPZmCOPfsyXE8CQxsvxMk'
url = "https://api.apilayer.com/exchangerates_data/convert"
payload = {
    "amount": "1200",
    "from": "EUR",
    "to": "RUB"
}
headers = {
    "apikey": "tP6pidXH3QMCPZmCOPfsyXE8CQxsvxMk"
}
response = requests.get(url, headers=headers, params=payload)
status_code = response.status_code
print(response.text)