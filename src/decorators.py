import os

PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "data", "log.scripts.txt")


def log(filename=None):
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename is not None:
                    with open(PATH_TO_FILE, "a", encoding="utf-8") as file:
                        return file.write(f'Выполнена функция {func.__name__}, результат {result}.\n')
                else:
                    return result
            except Exception as error:
                if filename is not None:
                    with open(PATH_TO_FILE, "a", encoding="utf-8") as file:
                        return file.write("При выполнении функции произошла ошибка")
                else:
                    return "Функция выполнена с ошибкой"

        return wrapper

    return my_decorator


@log(filename="mylog.txt")
def my_function():
    pass


my_function(10, 20)
