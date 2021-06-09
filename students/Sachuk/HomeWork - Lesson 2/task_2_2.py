# Создать строку равную предпоследнему символу введенной строки.

s = input()
if len(s)>1:
    result = s[len(s)-2]
    print(result)
else:
    print('Length of a word is less then 2')