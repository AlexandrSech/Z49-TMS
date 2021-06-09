"""Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
это порядковый номер строки в списке. Использовать генератор списков."""

a = 'abcdefghigklmnopqrstuvwxyz'

spis = [a[i] for i in range(5, 20)]
for el in range(len(spis)):
    spis[el] = str(el) + '-' + spis[el]
print(spis)