# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
# это порядковый номер строки в списке. Использовать генератор списков.

list_of_strings = ['my_string', 'new_string', 'cool_string']

new_list_of_strings = [f'{index} - {item}' for index, item in enumerate(list_of_strings)]

print(new_list_of_strings)