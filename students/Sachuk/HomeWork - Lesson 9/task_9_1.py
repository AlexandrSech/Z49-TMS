# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
# это порядковый номер строки в списке. Использовать генератор списков.

def gen(*args):
    d = {i : args[i] for i in range(len(args))}
    result = ''
    for key, value in d.items():
        result = result + str(key) + ' - ' + str(value) + '\n'
    return result

print(gen(123, 'qwerty', [1,'qwertt', 'q', {'a': 'b'}],))