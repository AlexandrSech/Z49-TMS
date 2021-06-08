'''
Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
это порядковый номер строки в списке. Использовать генератор списков.
'''

str_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six']
new_str_list = [f'{i} - {v}' for i, v in enumerate(str_list)]
print(new_str_list)