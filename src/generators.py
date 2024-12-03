def filter_by_currency(operations: list, currency="USD") -> iter:
    """Функция превращения списка транзакций в итератор"""
    usd_operations = []
    for i in operations:
        if i["code"] == currency:
            usd_operations.append(i)
    usd_operations_iter = iter(usd_operations)
    return usd_operations_iter


def transaction_descriptions(operations: list) -> iter:
    """Функция для вывода вида операции"""
    for i in operations:
        yield i["description"]


def card_number_generator(start: int, stop: int) -> str:
    """Функция генерации номеров карт"""
    for i in range(start, stop+1):
        card_number = i
        formatted_number = "{:016d}".format(card_number)
        print(formatted_number)

print(card_number_generator(1,3))
"""for card_number in card_number_generator(1, 5):
    print(card_number)"""

"""operation = [{"code": "USD", 3: 3, "description": 2}, {"description": 1, "code": "USD"}]
usd_transactions = filter_by_currency(operation, "USD")
for _ in range(len(operation)):
    print(next(usd_transactions))
"""
"""operation = [{1: 2, 3: 3, "description": 2},{"description":1}]
descriptions = transaction_descriptions(operation)
for _ in range(2):
    print(next(descriptions))
"""
