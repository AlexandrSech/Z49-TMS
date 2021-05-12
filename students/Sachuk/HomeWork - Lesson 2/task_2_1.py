# Создать строку равную третьему символу введенной строки.
s = input()
if len(s) > 2:
    result = s[2]
    print(result)
else:
    print('Length of a word is less then 3')
