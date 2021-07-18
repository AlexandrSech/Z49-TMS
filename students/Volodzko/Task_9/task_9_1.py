"""
Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’,
где i это порядковый номер строки в списке. Использовать генератор списков.
"""

def power():
    list_lines = [
        "Черный Мерседес",
        "Синяй БМВ",
        "Зелёная Ауди"
    ]
    result = ["{} - {}".format(i, ii) for i, ii in enumerate(list_lines)]
    return result

print(power())