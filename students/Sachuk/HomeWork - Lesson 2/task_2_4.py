# Создать строку равную введенной строку без последних двух символов.

s = input()
if len(s) > 1:
    result = s[0:len(s)-2]
    print(result)
else:
    print('Length of a word is less then 2')