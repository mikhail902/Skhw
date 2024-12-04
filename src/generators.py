def filter_by_currency(operations: list, currency="USD") -> iter:
    """Функция превращения списка транзакций в итератор"""
    try:
        return filter(lambda x: x["code"] == currency, operations)
    except StopIteration:
        print(f"Ошибка, слишком много значений запрошено {StopIteration}")


def transaction_descriptions(operations: list) -> iter:
    """Функция для вывода вида операции"""
    try:
        for i in operations:
            yield i["description"]
    except StopIteration:
        print(f"Ошибка, слишком много значений запрошено {StopIteration}")


def card_number_generator(start: int, stop: int) -> list:
    """Функция генерации списка номеров карт"""
    return ["{:016d}".format(i) for i in range(start, stop)]
