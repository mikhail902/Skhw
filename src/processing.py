def filter_by_state(dicts: list, state="EXECUTED") -> list:
    """Функция, которая отбирает принятые операции"""

    new_dicts = []
    for i in dicts:
        if str(i["state"]).lower() == state.lower():
            new_dicts.append(i)
    return new_dicts


def sort_by_date(date_list: list | str, method_of_sort=False) -> list:
    """Функция сортировки по дате"""

    if sort_by_date == "":
        sorted_date = []
    else:
        sorted_date = sorted(date_list, key=lambda data: data["date"], reverse=method_of_sort)
    return sorted_date
