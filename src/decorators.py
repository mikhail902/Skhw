import time
from functools import wraps


def log(filename=None) -> any:
    """Декоратор, который проверяет функцию на время работы, ошибки и правильный ответ"""

    def wrapper(function):
        @wraps(function)
        def inner(*args, **kwargs):
            try:
                time_1 = time.time()
                result = function(*args, **kwargs)
                time_2 = time.time()
                time_of_work = time_2 - time_1
                if filename is not None:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"""\nФункция успешно выполнена. Результат функции: {result}""")
                        file.write(f"""\nВремя работы: {time_of_work} секунд""")
                        return result
                else:
                    print(result)
                    return result
            except Exception as e:
                time_1 = time.time()
                result = function(*args, **kwargs)
                time_2 = time.time()
                time_of_work = str(time_2 - time_1) + result
                if file is not None:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(
                            f"""\nПри выполнении функции произошла ошибка {e}. Результат функции: {time_of_work}\n.
                             Входные параметры {args, " ", kwargs}"""
                        )
                return result

        return inner

    return wrapper


@log(filename="results_of_decorators.txt")
def log_first(x, y):
    return x + y


@log(filename=None)
def log_second(x, y):
    return x + y


log_first(1, 2)
log_second(4, 6)
